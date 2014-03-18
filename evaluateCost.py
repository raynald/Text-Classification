import numpy as np;

def EvaluateCost(cityLabelPredict, countryLabelPredict, cityLabel, countryLabel):
    tmp = (cityLabelPredict != cityLabel);
    cityCost = np.sum(tmp, 0);
    tmp = (countryLabelPredict != countryLabel);
    countryCost = np.sum(tmp, 0) * 0.25;
    cost = cityCost + countryCost;
    return cost, cityCost, countryCost;

