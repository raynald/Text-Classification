import numpy as np;
import csv;
from sklearn import svm;

from evaluateCost import *;
from dictionary import *;

feature=[]
feature2=[]
feature3=[]
label=[]
for line in open('training.csv'):
    line = line.split(',')
    feature+=[line[0]]
    feature3+=[line[1]]
    feature2+=[line[2]]

for line in open('training50-0.5.txt','w'):
    line = line.split(',')
    label+=[line[0]]

v={}
for line in open("OutlierIndex-50-0.35"):
    x = int(line)
    v[x]=x

outFile = open('new_train.csv','w');
for i in range(0, 6108):
    outFile.write(feature[i]);
    outFile.write(',');
    tmp = v.get(i)
    if tmp==i:
        outFile.write(label[i]);
    else:
        outFile.write(feature3[i]);
    outFile.write(',');
    outFile.write(feature2[i]);
outFile.close();

