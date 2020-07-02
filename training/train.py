from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
from sklearn import datasets
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


dataset = datasets.fetch_california_housing()
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.1)

model_parameters = {
    'n_estimators': 200,
    'max_depth': 3,
    'min_samples_split': 5,
    'learning_rate': 0.01,
    'loss': 'ls'
}

pipeline = Pipeline([
    ('scalar', StandardScaler()),
    ('regressor', GradientBoostingRegressor(**model_parameters))
])

pipeline.fit(X_train, y_train)

initial_type = [('float_input', FloatTensorType([None, 8]))]
onx = convert_sklearn(pipeline, initial_types=initial_type)
with open("artifacts/california_housing.onnx", "wb") as f:
    f.write(onx.SerializeToString())