#Let's start with importing necessary libraries
import pickle
# import numpy as np
import pandas as pd

class predObj:

    def predict_log(self, dict_pred):
        with open("model.pkl", 'rb') as f:
            model = pickle.load(f)
        data_df = pd.DataFrame(dict_pred,index=[1,])
        result = model.predict(data_df)

        return result



