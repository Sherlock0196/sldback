#3 Libraries
from sklearn.naive_bayes import GaussianNB
import csv
import numpy as np
import pickle

def mach(arg,train):
    #LOADED CSV
    if(train):
        with open('merged.csv','rU') as f:
            xs=[list(map(int,line)) for line in csv.reader(f)]

        no_ld = []
        has_ld = []

        for var in xs:
            if (var[-1] == 0):
                del var[-1]
                no_ld.append(var)    
            else:
                del var[-1]
                has_ld.append(var)

        combined = has_ld + no_ld
        xses = np.array(combined)
        yses = ['LD'] * len(has_ld) +  ['NO LD'] * len(no_ld) 
        yses = np.array(yses)

    #---------TRAINING THE MODEL-----------
        clf = GaussianNB()
        clf.fit(xses, yses)
        with open('gaus.pkl', 'wb') as fid:
            pickle.dump(clf, fid) 
  
# load the model from disk
    with open('gaus.pkl', 'rb') as fid:
        clf2 = pickle.load(fid)
        
    result = clf2.predict(new_xs)
    print(result)

