import numpy as np;
import csv;
from sklearn import svm;

from evaluateCost import *;
from dictionary import *;


#########################generate score file#######################################


# load and transform city label
cityLabel = np.genfromtxt('training.csv', dtype = 'int32', delimiter = ',', usecols = 1);
numCityClass = np.unique(cityLabel).size;
cityDict = ConstructDict(np.unique(cityLabel), \
           np.linspace(0, numCityClass - 1, numCityClass) );
cityRevDict = ConstructDict(np.linspace(0, numCityClass - 1, \
              numCityClass), np.unique(cityLabel) );
cityLabel = GetDictValue(cityDict, np.copy(cityLabel) );


# load and transform country label
countryLabel = np.genfromtxt('training.csv', dtype = 'int32', \
               delimiter = ',', usecols = 2);
numCountryClass = np.unique(countryLabel).size;
countryDict = ConstructDict(np.unique(countryLabel), \
           np.linspace(0, numCountryClass - 1, numCountryClass) );
countryRevDict = ConstructDict(np.linspace(0, numCountryClass - 1, numCountryClass), \
                 np.unique(countryLabel) );
countryLabel = GetDictValue(countryDict, np.copy(countryLabel) );

# load feature
featCityTrain = np.genfromtxt('./feature/training2_06.vector', delimiter = ' ');

cValCity = 0.05;
        
cityModel = svm.LinearSVC(C = cValCity);
cityModel.fit(featCityTrain, cityLabel);
cityLabelScore = cityModel.decision_function(featCityTrain);
cityLabelPred = np.argmax(cityLabelScore, 1);
cityLabelPredOrig = GetDictValue(cityRevDict, np.copy(cityLabelPred) );
cityLabelOrig = GetDictValue(cityRevDict, np.copy(cityLabel) );

cityStr = np.genfromtxt('training.csv', dtype = str, delimiter = ',', usecols = 0);
testLabel = np.genfromtxt('training.csv', dtype = int, delimiter = ',', usecols = 1);

outFile = open('OutlierInfoAdd.txt','w');
for i in range(0, cityLabelPred.size):
    outFile.write(cityStr[i] );
    outFile.write(',');
    outFile.write(str(testLabel[i] ) );
    outFile.write(',');
    outFile.write(str(cityLabelOrig[i] ) );
    outFile.write(',');
    outFile.write(str(cityLabelPredOrig[i] ) );
    outFile.write(',');
    outFile.write(str(cityLabelScore[i, cityLabel[i] ] ) );
    outFile.write(',');
    outFile.write(str(cityLabelScore[i, cityLabelPred[i] ] ) );
    outFile.write('\n');
    
outFile.close();
print 'finished'


##############################generate outlier index###############################
outlierIndex = [];
clusterThresh = 10;
eliminateRatio = 0.4;
outlierIndexName = './outlier_index/OutlierIndex-' + str(clusterThresh) + '-' + str(eliminateRatio);

score = np.genfromtxt('./OutlierInfo.txt', delimiter = ',', usecols = 4);
labelPred = np.genfromtxt('./OutlierInfo.txt', delimiter = ',', usecols = 3);
label = np.genfromtxt('./OutlierInfo.txt', delimiter = ',', usecols = 2);

nCityClass = np.unique(label).size;
outlierId = np.zeros( (label.size), dtype = np.int);
for cityCode in np.unique(label):
    cityId = (label == cityCode);
    cityId = np.where(np.copy(cityId) == True);
    cityId = np.array(cityId);
    
    if cityId.size >= clusterThresh:
        tmpScore = score[cityId];
        tmpId = np.argsort(tmpScore);
        tmpId = np.array(tmpId);
        nOutlierTmp = int(np.round(cityId.size * eliminateRatio) );
        
        outlierIdTmp = tmpId[0, 0:nOutlierTmp];
        outlierId[cityId[0, outlierIdTmp] ] = True;

outlierId = np.where(np.copy(outlierId) == 1);
outlierId = np.array(outlierId);
outFile = open(outlierIndexName,'w');
for i in range(0, outlierId.size):
    print i 
    outFile.write(str(outlierId[0, i] ) );
    outFile.write('\n');
outFile.close();
