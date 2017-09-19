import scipy.io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal
import seaborn as sns

# m = scipy.io.loadmat('P01.mat')
# mm = m['data']
# elect = mm[:,44,:]
# df = pd.DataFrame(elect)

Index= ['aaa', 'bbb', 'ccc', 'ddd', 'eee']
Cols = ['A', 'B', 'C', 'D']
df = pd.DataFrame(abs(np.random.randn(5, 4)), index=Index, columns=Cols)

plt.pcolor(df)
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()

# plt.plot(np.linspace(-200, 1340, 201), df.mean())
# plt.show()

