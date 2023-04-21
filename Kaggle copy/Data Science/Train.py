import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error

housing_data = '/Users/josearnel/Documents/Coding_Den/Kaggle/Data Science/home-data-for-ml-course/train.csv'
test_file_path = '/Users/josearnel/Documents/Coding_Den/Kaggle/Data Science/home-data-for-ml-course/test.csv'
training_data = pd.read_csv(housing_data)
test_data = pd.read_csv(test_file_path)

y = training_data.SalePrice

features = ['LotArea', 'YearBuilt','YearRemodAdd','OverallQual', 'OverallCond', 'GrLivArea', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 
            'KitchenAbvGr','TotRmsAbvGrd', 'MiscVal'] 
X = training_data[features]
test_X = test_data[features]

test_X = test_data.loc[:364]

print(test_X.shape)

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Model
housing_model = DecisionTreeRegressor(random_state=1)
# Fit
housing_model.fit(train_X, train_y)
# Predict
housing_predict = housing_model.predict(val_X)
test_predict = housing_model.predict(test_X)
# Validate 
mae = mean_absolute_error(housing_predict, val_y)
mae2 = mean_absolute_error(test_predict, val_y)

print(val_X.shape)
print(val_y.shape)
print("MAE {}".format(mae))
# print("MAE {}".format(mae2))
