import scipy.io
import pandas as pd

mat = scipy.io.loadmat('P01.mat')
print(mat["data"].shape)
#mat['data'] es una matriz de 3 dimensiones, 
#hay que convertirla en una de 2d para pasarla a dataframe
#df1 = pd.DataFrame(mat)
#print(df1.index)