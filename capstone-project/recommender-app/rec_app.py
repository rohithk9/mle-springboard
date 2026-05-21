import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd
from openai import OpenAI
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)
app.logger.setLevel(logging.DEBUG)

@app.before_request
def log_request():
    app.logger.debug("Incoming request: %s %s", request.method, request.path)
    app.logger.debug("Headers: %s", dict(request.headers))
    app.logger.debug("JSON body: %s", request.get_json(silent=True))
    app.logger.debug("Raw body: %s", request.get_data(as_text=True))

@app.after_request
def log_response(response):
    app.logger.debug("Outgoing response: %s", response.status)
    app.logger.debug("Response headers: %s", dict(response.headers))
    app.logger.debug("Response data: %s", response.get_data(as_text=True))
    return response

@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.exception("Unhandled exception:")
    return jsonify({"error": str(e)}), 500

load_dotenv()

# Load model components
with open("beer_recommender_model.pkl", "rb") as f:
    model_data = pickle.load(f)

# vectorizer = model_data['vectorizer']
combined_similarity_df = model_data["combined_similarity_df"]
# desc_similarity_df = model_data['desc_similarity_df']
df = model_data["df"]

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# 2. Keep your recommendation logic as a core python function
def get_beer_recommendations(style: str, min_abv: float = 0.0) -> str:
    """Finds top 5 beer recommendations based on style and minimum ABV."""
    target_indices = df.index[
        df["Style"].str.contains(style, case=False, na=False)
    ].tolist()
    if not target_indices:
        return f"No direct style match found for '{style}'."

    # Process first match for simplicity in tool execution
    idx = target_indices[0]
    similar_beers = combined_similarity_df[idx].sort_values(ascending=False).head(20)

    recs = df.loc[similar_beers.index, ["Style", "Name", "ABV"]]
    filtered_recs = recs[recs["ABV"] >= min_abv].head(5)

    if filtered_recs.empty:
        return "No beers match that ABV threshold."

    return filtered_recs.to_string(index=False)


# 3. Define the tool definition for the LLM
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_beer_recommendations",
            "description": "Call this when the user explicitly requests beer recommendations and has provided a style (e.g., IPA, Stout, Lager).",
            "parameters": {
                "type": "object",
                "properties": {
                    "style": {
                        "type": "string",
                        "description": "The style of beer requested (e.g., 'Stout', 'IPA').",
                    },
                    "min_abv": {
                        "type": "number",
                        "description": "The minimum ABV filter if specified by the user, default is 0.0.",
                    },
                },
                "required": ["style"],
            },
        },
    }
]


@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    history = request.json.get("history", [])

    messages = [
        {
            "role": "system",
            "content": "You are an expert Cicerone (beer sommelier) AI Agent. Guide users to find the perfect beer. If they give a vague preference, suggest styles. If they state a style they like, use the 'get_beer_recommendations' tool to fetch results.",
        }
    ]

    # Append history and new message
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})

    # First LLM pass to see if it wants to use a tool
    response = client.chat.completions.create(
        model="gpt-4o-mini", messages=messages, tools=tools
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    # Check if the agent decided to call your ML model
    if tool_calls:
        # Append the assistant's tool call request to history (serialized to dict)
        messages.append(response_message.model_dump())

        for tool_call in tool_calls:
            if tool_call.function.name == "get_beer_recommendations":
                import json

                args = json.loads(tool_call.function.arguments)

                # Execute your local ML logic
                tool_output = get_beer_recommendations(
                    style=args.get("style"), min_abv=args.get("min_abv", 0.0)
                )

                # Append the tool execution results
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "name": "get_beer_recommendations",
                        "content": tool_output,
                    }
                )

                final_response = client.chat.completions.create(
                    model="gpt-4o-mini", messages=messages
                )

                # Convert any final message objects to clean dicts for the frontend
                messages.append(final_response.choices[0].message.model_dump())
                return jsonify(
                    {
                        "response": final_response.choices[0].message.content,
                        "history": messages,
                    }
                )

    # If no tool was called, append the standard text response (serialized to dict)
    messages.append(response_message.model_dump())
    return jsonify({"response": response_message.content, "history": messages})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
