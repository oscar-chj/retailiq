import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    df = pd.read_csv('data/processed/sales_data_features.csv')
    X = df.drop(['sales', 'date'], axis=1)
    y = df['sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [None, 10, 20],
    }
    grid_search = GridSearchCV(RandomForestRegressor(random_state=42), param_grid, cv=3, scoring='neg_mean_absolute_error')
    grid_search.fit(X_train, y_train)
    best_model = grid_search.best_estimator_
    joblib.dump(best_model, 'models/best_random_forest_model.pkl')
    joblib.dump(model, 'models/random_forest_model.pkl')
    y_pred = model.predict(X_test)
    print('MAE:', mean_absolute_error(y_test, y_pred))
    print('RMSE:', mean_squared_error(y_test, y_pred, squared=False))

if __name__ == '__main__':
    train_model()
