#%%
import pandas as pd 
from download import download
import matplotlib.pyplot as plt
import seaborn as sns
from download import download
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option('display.max_row', 68)
#%%
df_bicycle = pd.read_csv("La myriade de Totems de Montpellier.csv")
url = " https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
path_target = "La myriade de Totems de Montpellier.csv"
download(url, path_target, replace=True)
#%%
df_bicycle.columns=['Date', 'Heure', 'Total année', 'Total du jour', 'Unnamed', 'Remarque']
df_bicycle.columns
#%%
bicycle = df_bicycle.copy()
del bicycle['Total année']
bicycle = bicycle.drop(columns = ['Unnamed'])
bicycle = bicycle.drop(columns = ['Remarque'])
# %%
bicycle_2 = bicycle.copy()
bicycle_2 = bicycle[(bicycle["Heure"] <= "10") & (bicycle_2["Heure"] >= "08")]
bicycle_2 = bicycle_2.drop_duplicates(subset = ['Date'], keep = 'last')
bicycle_2
#%%
bicycle_3 = bicycle_2.copy()
#%%
for i in range (len(bicycle_3)):
    bicycle_3.rename(index = {bicycle_3.index[i]:i}, inplace = True)
bicycle_3

#%%
bicycle_3.index[bicycle_3['Date'] == "28/10/2020"] #donne la ligne exacte à compter du 28 octobre 2020
#%%
bicycle_4 = bicycle_3.copy() 
bicycle_4 = bicycle_3.iloc[106:] #prend les valeurs trouvée au dessus de la ligne 106(celle trouvée au dessus)

#%% 
for i in range (len(bicycle_4)):
    bicycle_4.rename(index = {bicycle_4.index[i]:i}, inplace = True)
bicycle_4

#%%
time = pd.to_datetime(bicycle_4['Date'] ,format='%d/%m/%Y')

bicycle_4['Date'] = time
l = []
for i in range (bicycle_4.shape[0]):
    l.append(pd.to_datetime(bicycle_4.iloc[i,0]).weekday()) 
#%%
bicycle_4['Jour'] = l #noté de Lundi = 0 à Dimanche =6
bicycle_4 = bicycle_4[(bicycle_4['Jour'] != 6) & (bicycle_4['Jour'] != 5)] #retrait de tous les weekends 
#%%
bicycle_4 = bicycle_4[(bicycle_4['Heure'] >= "08:31")]
for i in range (len(bicycle_4)):
    bicycle_4.rename(index = {bicycle_4.index[i]:i}, inplace = True)
#%%
bicycle_4 = bicycle_4.drop([7,8]) 
#%%
for i in range (len(bicycle_4)):
    bicycle_4.rename(index = {bicycle_4.index[i]:i}, inplace = True)
bicycle_4
#%%
bicycle_4['Total du jour'].mean()
#%%
bicycle_4['Total du jour'].median()



#####
# Etude des vendredis
# #utile pour la régression linéaire
# j = []
# for i in range (1,len(bicycle_4)+1):
#     j.append(bicycle_4.iloc[:i,2].sum())
# bicycle_4['Total'] = j
# # %%
# bicycle_5 = bicycle_4.copy()
# bicycle_5 = bicycle_4[(bicycle_4["Heure"] <= "09:37") & (bicycle_5["Heure"] >= "08:30")]
# for i in range (len(bicycle_5)):
#     bicycle_5.rename(index = {bicycle_5.index[i]:i}, inplace = True)
# bicycle_5
# #%%
# bicycle_5_vendredi = bicycle_5[bicycle_4['Jour'] == 4]
# for i in range (len(bicycle_5)):
#     bicycle_5.rename(index = {bicycle_5.index[i]:i}, inplace = True)
# bicycle_5
# bicycle_5['Total du jour'].mean()
# bicycle_5['Total du jour'].median()
# bicycle_5_vendredi['Total du jour'].mean()
# bicycle_5_vendredi['Total du jour'].median()




#####
#REGRESSION LINEAIRE

# import numpy as np 
# from sklearn.datasets import make_regression
# import matplotlib.pyplot as plt 

# # %%
# x = np.arange(start = 0, stop = 33)
# y = bicycle_4['Total']
# x, y = make_regression(n_samples = bicycle_5.shape[0], n_features = 1, noise = 10)
# plt.scatter(x,y) 
# # %%
# print(x.shape)
# y= y.reshape(y.shape[0],1)
# print(y.shape)
# # %%
# X = np.hstack((x,np.ones(x.shape)))
# X
# # %%
# theta = np.random.randn(2,1) # de cette dim car on fait 
# #une régression f(x)=ax +b
# theta
# # %%
# def model(X,theta):
#     return X.dot(theta)
# # %%
# plt.scatter(x,y)
# plt.plot(x,model(X,theta), c ='r')
# # %%
# def cout(X,y,theta):
#     m = len(y)
#     return 1/(2*m) * np.sum((model(X,theta) - y)**2)
# cout(X,y,theta)
# # %%
# def grad(X,y,theta):
#     m = len(y)
#     return 1/m * X.T.dot(model(X,theta) - y)
# # %%
# def gradient_descent(X,y,theta,learning_rate, n_iterations):

#     for i in range(0,n_iterations):
#         theta = theta - learning_rate * grad(X,y,theta)
#     return theta
# # %%
# theta_final = gradient_descent((X), y, theta, learning_rate = 0.01, n_iterations = 1000)
# # %%
# prediction = model(X,theta_final)
# plt.scatter(x,y)
# plt.plot(x,prediction,c='r')
