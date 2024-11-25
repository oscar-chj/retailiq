import pandas as pd
import numpy as np
import os

def load_data():
    # Load datasets
    sales_data = pd.read_csv('data/raw/train.csv', dtype={'StateHoliday': str})
    store_data = pd.read_csv('data/raw/store.csv')
    return sales_data, store_data


def merge_data(sales_data, store_data):
    # Merge sales data with store data
    data = pd.merge(sales_data, store_data, on='Store', how='left')
    return data

def clean_data(df):
    # Handle missing values
    df.fillna(0, inplace=True)
    # Convert date column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # Filter out records where the store was closed
    df = df[df['Open'] == 1]
    # Filter out records with zero sales
    df = df[df['Sales'] > 0]
    return df

def feature_engineering(df):
    # Extract date features
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Day'] = df['Date'].dt.day
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    # Encode categorical variables
    categorical_cols = ['StoreType', 'Assortment', 'StateHoliday']
    df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    return df

def save_processed_data(df, filename):
    # Create processed data directory if it doesn't exist
    if not os.path.exists('data/processed/'):
        os.makedirs('data/processed/')
    df.to_csv(f'data/processed/{filename}', index=False)

if __name__ == '__main__':
    sales_data, store_data = load_data()
    data = merge_data(sales_data, store_data)
    data = clean_data(data)
    data = feature_engineering(data)
    save_processed_data(data, 'sales_data_processed.csv')
