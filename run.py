####
####
#### Responsible for loading data as well as training and evaluating the model
####
####

import constants as C
from data import load_raw_data, preprocess_data, split_data_to_training_and_test_sets
from model import create_logistic_regression_model, create_SVM, calculate_accuracy

if __name__ == '__main__':
	# Loads the raw data
	dataset = load_raw_data()

	# Splits the data to training and test sets
	X, y = preprocess_data(dataset, C.FEATURES)
	X_train, X_test, y_train, y_test = split_data_to_training_and_test_sets(X, y)

	# Generate the LR model, train, and get the accuracy score
	lr_classifier = create_logistic_regression_model(X_train, y_train)
	accuracy = calculate_accuracy(lr_classifier, X_test, y_test)

	print()
	print('--------------')
	print('Accuracy of logistic regression model using all features:', accuracy)
	print('--------------')
	print()

	# Generate the SVC model, train, and get the accuracy score
	svm_classifier = create_SVM(X_train, y_train)
	accuracy = calculate_accuracy(svm_classifier, X_test, y_test)

	print()
	print('--------------')
	print('Accuracy of SVM model using all features:', accuracy)
	print('--------------')
	print()

	# Splits the data to training and test sets
	X, y = preprocess_data(dataset, C.OPTIMAL_FEATURES)
	X_train, X_test, y_train, y_test = split_data_to_training_and_test_sets(X, y)

	# Generate the LR model, train, and get the accuracy score
	lr_classifier = create_logistic_regression_model(X_train, y_train)
	accuracy = calculate_accuracy(lr_classifier, X_test, y_test)

	print()
	print('--------------')
	print('Accuracy of logistic regression model using selected features:', accuracy)
	print('--------------')
	print()

	# Generate the SVC model, train, and get the accuracy score
	svm_classifier = create_SVM(X_train, y_train)
	accuracy = calculate_accuracy(svm_classifier, X_test, y_test)

	print()
	print('--------------')
	print('Accuracy of SVM model using selected features:', accuracy)
	print('--------------')
	print()
