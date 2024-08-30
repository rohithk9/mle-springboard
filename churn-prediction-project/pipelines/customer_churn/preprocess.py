import os
import tempfile
import numpy as np
import pandas as pd
import datetime as dt

if __name__ == "__main__":
    
    base_dir = "/opt/ml/processing"
    #Read Data
    df = pd.read_csv(
        f"{base_dir}/input/storedata_total.csv"
    )
    # convert created column to datetime
    df["created"] = pd.to_datetime(df["created"], errors='coerce')
    #Convert firstorder and lastorder to datetime datatype
    df["firstorder"] = pd.to_datetime(df["firstorder"],errors='coerce')
    df["lastorder"] = pd.to_datetime(df["lastorder"],errors='coerce')
    #Drop Rows with Null Values
    df = df.dropna()
    #Create column which gives the days between the last order and the first order
    df['first_last_days_diff'] = (df['lastorder'] - df['firstorder']).dt.days
    #Create column which gives the days between the customer record was created and the first order
    df['created_first_days_diff'] = (df['created'] - df['firstorder']).dt.days
    #Drop columns
    df.drop(['custid', 'created','firstorder','lastorder'], axis=1, inplace=True)
    ## Apply one hot encoding on favday and city columns
    df = pd.get_dummies(df,prefix=['favday','city'],columns=['favday','city'])
    categorical_cols = ['favday_Friday', 'favday_Monday', 'favday_Saturday', 'favday_Sunday',
                        'favday_Thursday', 'favday_Tuesday', 'favday_Wednesday', 'city_BLR',
                        'city_BOM', 'city_DEL', 'city_MAA']
    df[categorical_cols] = df[categorical_cols].replace({True: 1, False: 0})

    # Split into train, validation and test datasets
    y = df.pop("retained").astype(int)
    X_pre = df
    y_pre = y.to_numpy().reshape(len(y), 1)
    X = np.concatenate((y_pre, X_pre), axis=1)
    np.random.shuffle(X)
    
    # Split in Train, Test and Validation Datasets
    train, validation, test = np.split(X, [int(.7*len(X)), int(.85*len(X))])
    train_rows = np.shape(train)[0]
    validation_rows = np.shape(validation)[0]
    
    test_rows = np.shape(test)[0]
    train = pd.DataFrame(train)
    test = pd.DataFrame(test)
    validation = pd.DataFrame(validation)
    
    # Convert the label column to integer
    train[0] = train[0].astype(int)
    test[0] = test[0].astype(int)
    validation[0] = validation[0].astype(int)
    
    # Save the Dataframes as csv files
    train.to_csv(f"{base_dir}/train/train.csv", header=False, index=False)
    validation.to_csv(f"{base_dir}/validation/validation.csv", header=False, index=False)
    test.to_csv(f"{base_dir}/test/test.csv", header=False, index=False)