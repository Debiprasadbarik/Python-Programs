from pandas import read_csv
import numpy as np
from sklearn.preprocessing import Binarizer
path=r"iris.csv"
d=read_csv(path)
print(d.shape)
print(d.dtypes)
nd=d[['sepal.length','sepal.width','petal.length','petal.width']]
print(nd)
v=nd.values
dn=Binarizer(threshold=0.5).fit(v)
nv=dn.transform(v)
np.set_printoptions(precision=2)
print(nv)