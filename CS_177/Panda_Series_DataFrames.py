"""import pandas as pd
import numpy as np
s1=pd.Series([1,34,56,'st',13])

s2=pd.Series([100,None,2003,np.nan])

s=pd.Series({0:1000,'a':2000,'b':303,"c":203})

d=pd.DataFrame({"A":s1,"B":s2,"C":s})
print(d)
d.rename(columns={'C':'Center'},inplace=True)
d1=d.dropna()
print(d)
print(d.info())
print()
print(d1)
print(d.fillna('LLL'))
print(d.dropna(subset=['A','B']))"""

import pandas as pd
import numpy as np

def load_and_clean(filename):
    f=pd.read_csv(filename)
    f['danger_level']=f['danger_level'].fillna(0)
    f=f.dropna()
    return f


df=load_and_clean("sample.csv")
print(df)
    
