import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error
import joblib

def evaluate_model():
    df = pd.read_csv('data/processed/sales_data_features.csv')
    X = df.drop(['sales', 'date'], axis=1)
    y = df['sales']
    model = joblib.load('models/random_forest_model.pkl')
    y_pred = model.predict(X)
    print('MAE:', mean_absolute_error(y, y_pred))
    print('RMSE:', mean_squared_error(y, y_pred, squared=False))

if __name__ == '__main__':
    evaluate_model()
