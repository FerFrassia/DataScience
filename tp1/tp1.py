import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('tiempos.txt', sep=' ')

sol = sns.tsplot(time=df['Atleta'], data=df['tiempo_sol'], interpolate=False, color="blue")

nublado = sns.tsplot(time=df['Atleta'], data=df['tiempo_nublado'], interpolate=False, color="red")

lluvia = sns.tsplot(time=df['Atleta'], data=df['tiempo_lluvia'], interpolate=False, color="green")

sns.plt.legend([sol, nublado, lluvia], labels=["sol","nublado","lluvia"])

sns.plt.show()
"""
esta seria la fase de limpiar.
dropee el ateta que tenia el dato, pero queria dropear solo ese dato feo...
podemos asumir que se paso mal y el tiempo es 18.9 o poner el promedio, va que se yo
"""

df.drop(df[df.tiempo_lluvia > 180.0].index, inplace=True)

sol = sns.tsplot(time=df['Atleta'], data=df['tiempo_sol'], interpolate=False, color="blue")

nublado = sns.tsplot(time=df['Atleta'], data=df['tiempo_nublado'], interpolate=False, color="red")

lluvia = sns.tsplot(time=df['Atleta'], data=df['tiempo_lluvia'], interpolate=False, color="green")

sns.plt.legend([sol, nublado, lluvia], labels=["sol","nublado","lluvia"])

sns.plt.show()


"""
Nos falta definir que cosas usar, para mi un tstudent tipo muestra independtiente
para ver cual es la prob de que lluvia y sol y nublado (tomados de dos9 tengan la
media... posta copairse del powerpoint(acordarse de chequear las hipotesis)


Tendriamos que releer los test de rank sum, mannwhitney u y wilcoxon, que serian
los que no estabamos cuando los explico...


y el de permutaciones, que permutamos?los tiempos en nublado sol y lluvia?

"""
