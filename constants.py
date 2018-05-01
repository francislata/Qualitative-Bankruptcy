####
####
#### Manages all common constants used throughout this project
####
####

RAW_DATA_PATH = 'data/raw_data.txt'
HEADERS = ['Industrial Risk', 'Management Risk', 'Financial Flexibility', 'Credibility', 'Competitiveness', 'Operating Risk', 'Class']
FEATURES = HEADERS[:len(HEADERS) - 1]
OPTIMAL_FEATURES = ['Financial Flexibility', 'Competitiveness']
TARGET = HEADERS[-1]
TEST_SIZE = 0.1
RANDOM_STATE = 42
