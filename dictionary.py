import numpy as np;
# construct dictionary
def ConstructDict(keyArray, valueArray):    
    numKey = keyArray.size;
    i = 0;
    keyDict = dict();
    keyDict.setdefault(-1);
    for key in keyArray:
        keyDict[key] = valueArray[i];
        i = i + 1;
    return keyDict;

# find match from dictionary
def GetDictValue(keyDict, keyArray):
    numKey = keyArray.size;
    valueArray = np.ones(numKey, dtype = np.int) * -1;
    tmp = 0;
    for key in keyArray:
        valueArray[tmp] = keyDict.get(key);
        tmp = tmp + 1;
    return valueArray;
        