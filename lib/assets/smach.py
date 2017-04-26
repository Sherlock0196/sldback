#3 Libraries
from sklearn import tree
import csv
import sys
import numpy as np

def mach(data,arg):
    #LOADED CSV
    #with open('merged.csv','rU') as f:
     #   xs=[list(map(int,line)) for line in csv.reader(f)]

    no_ld = []
    has_ld = []

    data = data.tolist()
    arg = arg.tolist()
    xs = data
    
    
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
    clf = tree.DecisionTreeClassifier()
    clf.fit(xses, yses)

    #----------PREDICTION----------------
    new_xs = arg
    #[[1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],[1,1,1,1,1,0,1,1,0,0,0,1,0,1,1,0],
     #       [1,1,0,0,0,0,0,1,1,0,1,0,1,0,0,0], [1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0]]
    #print clf.predict(new_xs)
    #print clf.score(xses,yses)
    #print clf.predict_proba(new_xs)

    return clf.predict(new_xs)

    #new_xs = [['1','1','0','1','0','1','1','1','0','1','1','1','0','1','0','1'], ['1','0','0','0','1','0','1','1','0','1','1','0','0','0','1','0']]

data = np.array(eval(sys.argv[1]))
arg = np.array(eval(sys.argv[2]))


print mach(data,arg)
