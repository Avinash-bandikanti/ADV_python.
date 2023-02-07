import pandas as pd
import numpy as np
class Readcsv():
    def create_df(self,path):
        self.path=path
        self.df=pd.DataFrame(self.path)
        self.df['Total']=self.df.iloc[1:,]