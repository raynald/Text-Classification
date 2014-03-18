
import numpy as np;
import csv;
from sklearn import svm;

from evaluateCost import *;
from dictionary import *;
from utility import *;

# load and transform city label
cityLabel = np.genfromtxt('training.csv', dtype = 'int32', delimiter = ',', usecols = 1);
numCityClass = np.unique(cityLabel).size;
cityDict = ConstructDict(np.unique(cityLabel), \
           np.linspace(0, numCityClass - 1, numCityClass) );
cityLabel = GetDictValue(cityDict, np.copy(cityLabel) );


# load and transform country label
countryLabel = np.genfromtxt('training.csv', dtype = 'int32', \
               delimiter = ',', usecols = 2);
numCountryClass = np.unique(countryLabel).size;
countryDict = ConstructDict(np.unique(countryLabel), \
           np.linspace(0, numCountryClass - 1, numCountryClass) );
countryLabel = GetDictValue(countryDict, np.copy(countryLabel) );

# load feature
feat = np.genfromtxt('./feature/training2_06.vector', delimiter = ' ');
outlierId = np.genfromtxt('./outlier_index/OutlierIndex-10-0.2',dtype = np.int);
isOutlier = np.zeros( (feat.shape[0] ) );
isOutlier[outlierId] = 1;

nFold = 10;
nSample = cityLabel.size;
nCountry = np.unique(countryLabel).size;
res = nSample % nFold;
countryLabel = countryLabel[0:(nSample - res) ];
cityLabel = cityLabel[0:(nSample - res) ];
feat = feat[0:(nSample - res), :];
isOutlier = isOutlier[0:(nSample - res) ];

nSample = cityLabel.size;
idx = np.random.permutation(countryLabel.size);
isOutlier = isOutlier[idx];

idx = np.reshape(idx, (nFold, nSample/nFold) );
isOutlier = np.reshape(isOutlier, (nFold, nSample/nFold) );

for cValCity in np.logspace(-2, 1, 12):
    cost = 0;
    cityCost = 0;
    countryCost = 0;    
    for i in np.linspace(0, nFold - 1, nFold):
        idxTrain = np.delete(idx, i, 0);
        isOutlierTrain = np.delete(isOutlier, i, 0);
        idxTrain = np.ravel(idxTrain);
        isOutlierTrain = np.ravel(isOutlierTrain);
        isOutlierTrain = np.bool_(isOutlierTrain);
        idxTest = idx[i, :];
        idxTest = np.ravel(idxTest);
        dataTrain = feat[idxTrain, :];
        
        #eliminate        
        dataTrain = np.delete(dataTrain, \
                    np.array(np.where(isOutlierTrain == True) ), 0);
        
        dataTest = feat[idxTest, :];
        cityLabelTrain = cityLabel[idxTrain];
        cityLabelTrain = np.delete(cityLabelTrain, np.array(np.where(isOutlierTrain == True) ), 0);
        cityLabelTest = cityLabel[idxTest];
        countryLabelTrain = countryLabel[idxTrain];
        countryLabelTrain = np.delete(countryLabelTrain, np.array(np.where(isOutlierTrain == True) ), 0);
        countryLabelTest = countryLabel[idxTest];
        
        
        # train city model
        cityModel = svm.LinearSVC(C = cValCity);
        cityModel.fit(dataTrain, cityLabelTrain);
        
        # prediction
        countryLabelPred = countryLabelTest;  
        cityLabelPred = cityModel.decision_function(dataTest);
        cityLabelPred = np.argmax(cityLabelPred, 1);
        
        #cost calculation
        (costTmp, cityCostTmp, countryCostTmp) = EvaluateCost(cityLabelPred, countryLabelPred, cityLabelTest, countryLabelTest);
        cost = cost + costTmp;
        cityCost = cityCost + cityCostTmp;
        countryCost = countryCost + countryCostTmp;
    print 'cValCity ', cValCity    
    print cost, cityCost, countryCost





