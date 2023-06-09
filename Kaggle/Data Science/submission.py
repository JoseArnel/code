# Set up filepaths
import os
if not os.path.exists("../input/train.csv"):
    os.symlink("../input/home-data-for-ml-course/train.csv", "../input/train.csv")  
    os.symlink("../input/home-data-for-ml-course/test.csv", "../input/test.csv") 

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# load data
iowa_file_path = ".../input/train.csv"
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice

# Create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

#select columns and preview data
X = home_data[features]
X.head()

# split into validation
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# define Random Forest
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predicts(val_X)
rf_mae = mean_absolute_error(val_predictions, val_y)

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))



# train model for competition
# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_on_full_data =  RandomForestRegressor(random_state=1)

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X,y)

# path to file you will use for predictions
test_data_path = '../input/test.csv'

# read test data file using pandas
test_data = pd.read_csv(test_data_path)


# create test_X which comes from test_data but includes only the columns you used for prediction.
# The list of columns is stored in a variable called features
test_X = test_data[features]

# make predictions which we will submit. 
test_preds = test_data.predict(test_X)

output = pd.DataFrame({'Id': test_data.Id, 
                        'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)