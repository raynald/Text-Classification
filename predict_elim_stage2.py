import numpy as np;
import csv;
from sklearn import svm;

from evaluateCost import *;
from dictionary import *;

# load and transform city label
cityLabel = np.genfromtxt('new_train.csv', dtype = 'int32', delimiter = ',', usecols = 1);
numCityClass = np.unique(cityLabel).size;
cityDict = ConstructDict(np.unique(cityLabel), \
           np.linspace(0, numCityClass - 1, numCityClass) );
cityRevDict = ConstructDict(np.linspace(0, numCityClass - 1, \
              numCityClass), np.unique(cityLabel) );
cityLabel = GetDictValue(cityDict, np.copy(cityLabel) );


# load and transform country label
countryLabel = np.genfromtxt('new_train.csv', dtype = 'int32', \
               delimiter = ',', usecols = 2);
numCountryClass = np.unique(countryLabel).size;
countryDict = ConstructDict(np.unique(countryLabel), \
           np.linspace(0, numCountryClass - 1, numCountryClass) );
countryRevDict = ConstructDict(np.linspace(0, numCountryClass - 1, numCountryClass), \
                 np.unique(countryLabel) );
countryLabel = GetDictValue(countryDict, np.copy(countryLabel) );


# load feature
featCityTrain = np.genfromtxt('training0.2-0.6.vector', delimiter = ' ');
featCityValid = np.genfromtxt('validation0.2-0.6.vector', delimiter = ' ');
featCountryTrain = np.genfromtxt('training0.1-0.6.vector', delimiter = ' ');
featCountryValid = np.genfromtxt('validation0.1-0.6.vector', delimiter = ' ');

cValCity = 0.06;
cValCountry = 0.05;


cityModel = svm.LinearSVC(C = cValCity);
cityModel.fit(featCityTrain, cityLabel);
cityLabelPred = cityModel.decision_function(featCityValid);
cityLabelPred = np.argmax(cityLabelPred, 1);
cityLabelPred = GetDictValue(cityRevDict, np.copy(cityLabelPred) );



countryModel = svm.LinearSVC(C = cValCountry);
countryModel.fit(featCountryTrain, countryLabel);
countryLabelPred = countryModel.decision_function(featCountryValid);
countryLabelPred = np.argmax(countryLabelPred, 1);
countryLabelPred = GetDictValue(countryRevDict, np.copy(countryLabelPred) );

feature=[]
ind=0
for line in open('training.csv'):
    line = line.split('\n')
    feature+=[line[0]]
    ind=ind+1

outFile = open('predict_validation.txt','w');
for i in range(0, countryLabelPred.size):
    outFile.write(str(cityLabelPred[i] ) );
    outFile.write(',');
    outFile.write(str(countryLabelPred[i] ) );
    outFile.write('\n');

outFile.close();

