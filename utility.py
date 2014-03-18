import numpy as np;

def GenAddCityFeat(countryConf, numCountry):
    for i in range(0, countryConf.shape[0] ):
        maxAbs = np.amax(np.absolute(countryConf[i, :] ) );
        countryConf[i, :] = countryConf[i, :] / maxAbs;
    return countryConf;