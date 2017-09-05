import scipy.io
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
m = scipy.io.loadmat('P01.mat')
mm = m['data']
elect = mm[:,44,:]
df = pd.DataFrame(elect)
plt.plot(np.linspace(-200, 1340, 201), df.mean())
plt.show()