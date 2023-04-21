import pandas as pd 
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Import
training_file_path = '/Users/josearnel/Documents/Coding_Den/Kaggle/Data Science/home-data-for-ml-course/train.csv'
test_file_path = '/Users/josearnel/Documents/Coding_Den/Kaggle/Data Science/home-data-for-ml-course/test.csv'
training_data = pd.read_csv(training_file_path)
test_data = pd.read_csv(test_file_path)
# print(training_data.describe())

train_y = training_data.SalePrice
val_y = training_data.SalePrice
# val_y = test_data.SalePrice

# train_y = train_y.loc[:1458]
val_y = train_y.loc[:1458]

# print(test_data.columns)
_features = ['LotArea', 'YearBuilt','YearRemodAdd','OverallQual', 'OverallCond', 'GrLivArea', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 
            'KitchenAbvGr','TotRmsAbvGrd', 'MiscVal']            
train_X = training_data[_features]
val_X = test_data[_features]
# print(X.describe())
# print(X.head())

# Define
rf_model = RandomForestRegressor(random_state=0)
# Fit
rf_model.fit(train_X,train_y)
# Predict
rf_predict = rf_model.predict(val_X)
# Evaluate 
rf_mae = mean_absolute_error(val_y,rf_predict)

output = pd.DataFrame({'Id': test_data.Id, 
                        'SalePrice': rf_predict})
print(output)
print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_mae))
print("Shape of train_X {}, val_X {}".format(train_X.shape, val_X.shape))
print("Shape of train_y {}, val_y {}".format(train_y.shape, val_y.shape))

print("Shape of train_y {}, val_y {}".format(train_y.shape, val_y.shape))
