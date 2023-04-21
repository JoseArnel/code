# 1.How Models Work


# _________________________
# 2.Basic Data Exploration
import pandas as pd

# save filepath to variable for easier access
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# read the data and store data in DataFrame tilted melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
melbourne_data.describe()

# EXCERCISE
import pandas as pd

# Path of file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
# Fill in the line below to read the file into a varaible home_data
home_data = pd.read_csv(iowa_file_path)
home_data.describe()

# What is the average lot size (rounded to nearest integer)?
avg_lot_size = 10517
# As of today, how old is the newest home (current year - the date in which it was built)
newest_home_age = 12


# ____________________________________
# 3.Your First Machine Learning Model
import pandas as pd

melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path) 
melbourne_data.columns

Index(['Suburb', 'Address', 'Rooms', 'Type', 'Price', 'Method', 'SellerG',
       'Date', 'Distance', 'Postcode', 'Bedroom2', 'Bathroom', 'Car',
       'Landsize', 'BuildingArea', 'YearBuilt', 'CouncilArea', 'Lattitude',
       'Longtitude', 'Regionname', 'Propertycount'],
      dtype='object')

# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.  
# Your Iowa data doesn't have missing values in the columns you use. 
# So we will take the simplest option for now, and drop houses from our data. 
# Don't worry about this much for now, though the code is:

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

X = melbourne_data[melbourne_features]
X.describe()
X.head()

# BUILDING YOUR MODEL
# Define: What type of model will it be? Decision Tree? Other Model
# Fit: Capture patterns from provided data. This is the heart of mdeling
# Predict: To predict
# Evaluate: Determine how accurate model's predictions are

from sklearn.tree import DecisionTreeRegressor

# Define model. Specify a number for random_state to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

# Making predictions for the following 5 houses:
#    Rooms  Bathroom  Landsize  Lattitude  Longtitude
# 1      2       1.0     156.0   -37.8079    144.9934
# 2      3       2.0     134.0   -37.8093    144.9944
# 4      4       1.0     120.0   -37.8072    144.9941
# 6      3       2.0     245.0   -37.8024    144.9993
# 7      2       1.0     256.0   -37.8060    144.9954
# The predictions are
# [1035000. 1465000. 1600000. 1876000. 1636000.]

# EXCERCISE
# Code you have previously used to load data
import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'
home_data = pd.read_csv(iowa_file_path)

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex3 import *

import panadas as pd

print(home_data.columns)

y = home_data.SalePrice

feature_names = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# select data
X = home_data[feature_names]
print(X)
print(X.head)

from sklearn.tree import DecisionTreeRegressor
# specify the model
# for reproducibility, set random_state
iowa_model = DecisionTreeRegressor(random_state = 1)

# fit model
iowa_model.fit(X,y)

predictions = iowa_model.predict(X)

y = home_data.SalePrice
print(y.head())

predictions = iowa_model.predict(X.head)
print(predictions)


# __________________
# 4.Model Validation
# Mean Absolute Error
# error = actual-predicted
from sklearn.metrics import mean_absolute_error

predicted_home_prices = melbourne_model.predict(X)
mean_absolute_error(y, predicted_home_prices)

# Validation data: exclude some data from modeling-building, to test accuracy
from sklearn.model_selection import train_test_split

# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 0)
# define model
melbourne_model = DecisionTreeRegressor()
# fit model
melbourne_model.fit(train_X, train_y)

# EXCERCISE
# split data
from sklearn.model_selection import train_test_split
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state = 1)
 
# specify, fit model
from sklearn.tree import DecisionTreeRegressor

# specify 
iowa_model DecisionTreeRegressor(random_state = 1)

# fit
iowa_model.fit(train_X, train_y)

# make prediction with validation data
val_predictions = iowa_model.predict(val_X)

# calulate MAE in validation data
from sklearn.metrics import mean_absolute_error

val_mae = mean_absolute_error(val_predictions, val_y)
print(val_mae)


# ______________________________
# 5.Underfitting and Overfitting 

# overfitting: model matches training data almost perfectly but does poorly in validation and other new data
# underfitting: model fails to capture important distionstions and patterns in the data

# overfitting: capturing spurious patterns that won't recur in the future, leading to less accurate predictions, 
# underfitting: failing to capture relevant patterns, again leading to less accurate predictions 

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
        model = DecisionTreeRegressor(max_leaf_nodes = max_leaf_nodes, random_state=0)
        model.fit(train_X, train_y)
        pred_val = model.predict(val_X)
        mae = mean_absolute_error(val_y, pred_val)
        return(mae)

# compare MAE with differing max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d \t\t Mean Absolute Error: %d" % (max_leaf_nodes, my_mae))

# Max leaf nodes: 5  		 Mean Absolute Error:  347380
# Max leaf nodes: 50  		 Mean Absolute Error:  258171
# Max leaf nodes: 500  		 Mean Absolute Error:  243495
# Max leaf nodes: 5000  		 Mean Absolute Error:  254983

# EXCERCISE
def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

candidate_max_leaf_nodes = [5, 25, 50, 100, 250, 500]
# # Write loop to find the ideal tree size from candidate_max_leaf_nodes
# lst = []
# for max_leaf_nodes in candidate_max_leaf_nodes:
#     curr = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
#     lst.append(curr)
# lst = sorted(lst)
# print(lst[0])

# store the best value of max_leaf_nodes (it will be either 5, 25, 50, 100, 250 or 500)
# best_tree_size = lst[round(len(lst)/2)+1]
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
print(scores)
best_tree_size = min(scores, key=scores.get)
print(best_tree_size)

# fit model using all data
final_model = DecisionTreeRegressor(max_leaf_nodes = 100, random_state = 1)
final_model.fit(X, y)


# ________________
# 6.Random Forests

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

forest_model =  RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))

# EXCERCISE
# Code you have previously used to load data
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)
# Create target object and call it y
y = home_data.SalePrice
# Create X
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Specify Model
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit Model
iowa_model.fit(train_X, train_y)

# Make validation predictions and calculate mean absolute error
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

# Using best value for max_leaf_nodes
iowa_model = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
iowa_model.fit(train_X, train_y)
val_predictions = iowa_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for best value of max_leaf_nodes: {:,.0f}".format(val_mae))

# use random forest
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))
print("Validation MAE for Random Forest Model: {}".format(melb_preds))

# _______________________________
# 7.Machine Learning Competitions
# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex7 import *

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

features = ['LotArea', 'YearBuilt','YearRemodAdd','OverallQual', 'OverallCond', 'GrLivArea', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 
            'KitchenAbvGr','TotRmsAbvGrd', 'MiscVal']

'MSSubClass'
'LotArea'
'OverallQual'
'OverallCond'
'YearBuilt'
'YearRemodAdd'
'1stFlrSF'
'2ndFlrSF'
'LowQualFinSF'
'GrLivArea'
'FullBath'
'HalfBath'
'BedroomAbvGr'
'KitchenAbvGr'
'TotRmsAbvGrd'
'Fireplaces'
'WoodDeckSF'
'OpenPorchSF'
'EnclosedPorch'
'3SsnPorch'
'ScreenPorch'
'PoolArea'
'MiscVal'
'MoSold'
'YrSold'


#/Users/josearnel/opt/anaconda3/bin:/Users/josearnel/opt/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/josearnel/opt/anaconda3/bin
#/home/xxx/bin:/usr/local/bin:/home/xxx/bin:/home/xxx/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin


# type pip
#pip not found

#pip 21.3.1 from /Users/josearnel/Library/Python/3.8/lib/python/site-packages/pip (python 3.8)