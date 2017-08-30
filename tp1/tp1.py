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
con esto descartamos la hiptesis nula el clima no influye en la velocidad
de los atletas. tenemos que ver si las hiptesis de t_test se cumplen y vamo
"""

p = sp.stats.ttest_rel(df['tiempo_sol'], df['tiempo_lluvia'])

print(p)

#para ver si son normales
#lo es yohooo
norm_s = sp.stats.shapiro(df['tiempo_sol'])
norm_l = sp.stats.shapiro(df['tiempo_lluvia'])
norm_n = sp.stats.shapiro(df['tiempo_nublado'])

"""
print(norm_s)
print(norm_l)
print(norm_n)
"""
#no estariamos usando bien el f...
"""
var_sl = sp.stats.f.stats(df['tiempo_sol'], df['tiempo_lluvia'])
var_ln= sp.stats.f.stats(df['tiempo_nublado'], df['tiempo_lluvia'])
var_sn = sp.stats.f.stats(df['tiempo_sol'], df['tiempo_nublado'])

print(var_sl)
"""

"""
sobre la hipotesis 1 nosotros por el test p sabemos que no tienen
misma media, podemos decir que si por que la media de dias de sol
mas baja que en dias de lluvia y con eso concluir que la 1 es verdad.
es decir con P decimos que no son iguales, entonces tienen que ser distintas
como ms < ml podemos suponer que la hip 1 es verdaera.
"""


"""
Nos falta definir que cosas usar, para mi un tstudent tipo muestra independtiente
para ver cual es la prob de que lluvia y sol y nublado (tomados de dos9 tengan la
media... posta copairse del powerpoint(acordarse de chequear las hipotesis)


Tendriamos que releer los test de rank sum, mannwhitney u y wilcoxon, que serian
los que no estabamos cuando los explico...


y el de permutaciones, que permutamos?los tiempos en nublado sol y lluvia?

"""
