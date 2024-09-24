from flask import Flask, request, jsonify
from flask_cors import CORS 
import pickle
import pandas as pd
from tabulate import tabulate

app = Flask(__name__)
CORS(app)

start_idx = 0

# Load model components
with open('beer_recommender_model.pkl', 'rb') as f:
    model_data = pickle.load(f)

vectorizer = model_data['vectorizer']
combined_similarity_df = model_data['combined_similarity_df']
desc_similarity_df = model_data['desc_similarity_df']
df = model_data['df']

def content_based_recs(style, abv=None, refresh=False):
    global start_idx
    # Get similar styles of beers
    target_indices = df.index[df['Style'].str.contains(style, case=False, na=False)].tolist()
    num_recs = 5

    beer_recommendations = pd.DataFrame()

    # If refresh is True, show next set of recommendations
    if refresh:
        start_idx += num_recs
    else:
        start_idx = 0  # Reset the index when not refreshing

    # Get similar beers based on the description similarity
    for idx in target_indices:
        similar_beers = combined_similarity_df[idx].sort_values(ascending=False)
        
        top_recs = similar_beers.head(20)
        
        beer_recommendations = df.loc[top_recs.index, ['Style', 'Name', 'ABV']]
        beer_recommendations['similarity_score'] = top_recs.values
        
        if abv is not None:
            if not isinstance(abv, (int, float)):
                print(f"{abv} is not a valid number")
                abv = 0

    beer_recommendation_filt = beer_recommendations.loc[df['ABV'] >= abv]    
    # Slice the DataFrame based on the start index and number of recommendations to show
    current_beer_recs = beer_recommendation_filt.iloc[start_idx:start_idx + num_recs, :]
    if current_beer_recs.empty:
        return {
            'message': 'No recommendations found. Try a different style or ABV.'
        }
        
    return {
        'beer_recommendations': current_beer_recs.to_dict(orient='records'),
    }
    
@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json
    style = user_input.get('style')
    abv = user_input.get('abv')
    refresh = user_input.get('refresh', False)
    
    # Get recommendations
    recommendations = content_based_recs(style, abv, refresh)
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
