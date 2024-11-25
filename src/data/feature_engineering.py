import pandas as pd

def add_features(df):
    # Add holiday features
    df['is_holiday'] = df['date'].apply(lambda x: 1 if x in holidays else 0)
    # Add lag features
    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)
    # Add rolling mean features
    df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()
    return df

if __name__ == '__main__':
    sales_data = pd.read_csv('data/processed/sales_data_processed.csv')
    sales_data = add_features(sales_data)
    sales_data.dropna(inplace=True)
    sales_data.to_csv('data/processed/sales_data_features.csv', index=False)
