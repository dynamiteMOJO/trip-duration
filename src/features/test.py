import pathlib
import sys
import joblib
import mlflow

import pandas as pd
from hyperopt import hp
from sklearn.model_selection import train_test_split
from hyperopt.pyll.base import scope
from sklearn.metrics import mean_squared_error
from hyperopt import hp, fmin, tpe, Trials, STATUS_OK, space_eval
from xgboost import XGBRegressor

curr_dir = pathlib.Path(__file__)
home_dir = curr_dir.parent.parent.parent

input_file = "/data/processed/"
data_path = home_dir.as_posix() + input_file
output_path = home_dir.as_posix() + "/models"
pathlib.Path(output_path).mkdir(parents=True, exist_ok=True)

TARGET = "trip_duration"

train_features = pd.read_csv(data_path + "/train.csv")
X = train_features.drop(TARGET, axis=1)
y = train_features[TARGET]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)
print(y_train.head(), y_test.head())