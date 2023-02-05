import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor

boston = datasets.load_boston()
features = pd.DataFrame(boston.data,columns=boston.feature_names)
targets = boston.target

x_train,x_test,y_train,y_test = train_test_split(features,targets,test_size=0.33,random_state=42)

## Normal model build without any tuning
reg = RandomForestRegressor()
reg.fit(x_train, y_train)

reg_pred = reg.predict(x_test)
# r2_score(y_test,reg_pred)

# pickling of model
# import pickle 
# pickle.dump(reg,open('model.pkl','wb'))

'''fr checking if unpickling happens in correct manner'''
# model_file1 = pickle.load(open('model.pkl','rb'))
# print(model_file1.predict(x_test))