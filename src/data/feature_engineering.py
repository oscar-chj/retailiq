import pandas as pd
import holidays

# Define the holidays (in Malaysia, for now)
country_holidays = holidays.Malaysia(years=range(2010, 2023))

def add_features(df):
    # Ensure 'date' column is in datetime format
    df['date'] = pd.to_datetime(df['date'])

    # Add holiday features
    df['is_holiday'] = df['date'].apply(lambda x: 1 if x in country_holidays else 0)

    # Add lag features
    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)

    # Add rolling mean features
    df['rolling_mean_7'] = df['sales'].rolling(window=7).mean()
    return df

if __name__ == '__main__':
    sales_data = pd.read_csv('data/processed/sales_data_processed.csv')

    # Ensure 'date' column is in datetime format
    sales_data['date'] = pd.to_datetime(sales_data['date'])

    sales_data = add_features(sales_data)
    sales_data.dropna(inplace=True)
    sales_data.to_csv('data/processed/sales_data_features.csv', index=False)
