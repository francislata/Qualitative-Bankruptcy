import constants as C
import pandas as pd

'''
Loads the raw data as a CSV file and returns a dataframe
'''
def load_raw_data():
	raw_data_df = pd.read_csv(C.RAW_DATA_PATH, names=C.HEADERS)

	return raw_data_df
