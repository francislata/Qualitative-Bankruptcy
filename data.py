####
####
#### Manages loading and preprocessing of the raw data
####
####

import constants as C
import pandas as pd
from sklearn.model_selection import train_test_split

'''
Loads the raw data as a CSV file and returns a dataframe
'''
def load_raw_data():
	raw_data_df = pd.read_csv(C.RAW_DATA_PATH, names=C.HEADERS)

	return raw_data_df

'''
Preprocesses the data
'''
def preprocess_data(dataset, columns):
	for feature in C.FEATURES:
		dataset[feature] = dataset[feature].astype('category').cat.codes

	return dataset[columns], dataset[C.TARGET]

'''
Splits the data into training and test sets
'''
def split_data_to_training_and_test_sets(X, y):
	return train_test_split(X, y, test_size=C.TEST_SIZE, random_state=C.RANDOM_STATE)
