####
####
#### Creates, trains, and evaluates the performance of the model
####
####

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC

'''
Creates a logistic regression model
'''
def create_logistic_regression_model(X_train, y_train, C=1.0):
	lr = LogisticRegression(C=C, class_weight='balanced')
	lr.fit(X_train, y_train.values.ravel())

	return lr

'''
Creates a support vector machine model
'''
def create_SVM(X_train, y_train, C=1.0):
	svc = SVC(C=C)
	svc.fit(X_train, y_train.values.ravel())

	return svc

'''
Calculates the classifier's accuracy
'''
def calculate_accuracy(classifier, X_test, y_test):
	predictions = classifier.predict(X_test)

	return accuracy_score(y_test, predictions)
