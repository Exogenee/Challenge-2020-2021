import pandas as pd 
from download import download
import matplotlib.pyplot as plt
import seaborn as sns

url = " https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
path_target = "La myriade de Totems de Montpellier.csv"
download(url, path_target, replace=True)

df_bicycle = pd.read_csv("La myriade de Totems de Montpellier.csv")
df_bicycleimport pandas as pd 
from download import download
import matplotlib.pyplot as plt
import seaborn as sns

url = " https://docs.google.com/spreadsheets/d/e/2PACX-1vQVtdpXMHB4g9h75a0jw8CsrqSuQmP5eMIB2adpKR5hkRggwMwzFy5kB-AIThodhVHNLxlZYm8fuoWj/pub?gid=2105854808&single=true&output=csv"
path_target = "La myriade de Totems de Montpellier.csv"
download(url, path_target, replace=True)

#Nous donne le type de valeur que l'on a dans chaque variable de notre dataset :
df_bicycle.dtypes

#Nous donne le nbr de float et int
df_bicycle.dtypes.value_counts()

df_bicycle.describe()


#modifictation des noms des colonnes : 
df_bicycle.columns

df_bicycle.columns=['Date', 'Heure', 'Total année', 'Total du jour', 'Unnamed', 'Remarque']
df_bicycle
df_bicycle.columns

#création d'une copie : 
bicycle = df_bicycle.copy()

#suppression des colonnes inutiles :
bicycle = bicycle.drop(columns = ['Unnamed'])
bicycle = bicycle.drop(columns = ['Remarque'])

for col in bicycle.select_dtypes('float'):
    plt.figure()
    sns.displot(bicycle[col])

#retire les éléments vides : (donc les éléments ou ya des NAN)
#bicycle = bicycle.dropna()

#je refais une copie de ma copie initiale modifiée :

# bicycle_2 = bicycle.copy()

#il faudrait retirer toutes les heures au dessus de 10h :
bicycle_2 = bicycle[(bicycle["Heure"] <= "10") & (bicycle_2["Heure"] >= "08")]
#bicycle_2 = bicycle_2[bicycle_2["Heure"] >= "08"]

#garder seulement les dernieres lignes chaque fois qu'on a 2 fois le meme jour 
bicycle_2 = bicycle_2.drop_duplicates(subset = ['Date'], keep = 'last')
bicycle_2

#on peut s'occuper de retirer tous les weekends et les jours féries 
#de nouveau une copie :
bicycle_3 = bicycle_2.copy()
bicycle_3.sort_index(1, ascending=True)
#te change le numéro de chacune de tes lignes
for i in range (len(bicycle_3)):
    bicycle_3.rename(index = {bicycle_3.index[i]:i}, inplace = True)
bicycle_3

bicycle_3.index[bicycle_3['Date'] == "05/01/2021"] #index te donne la ligne exacte à partir du 5 janvier 2021
bicycle_4 = bicycle_3.copy() #encore une copie
bicycle_4 = bicycle_3.iloc[122:] #va au dessus de toutes les lignes à partir de la 122(celle trouvée au dessus)

#te change le numéro de chacune de tes lignes

for i in range (len(bicycle_4)):
    bicycle_4.rename(index = {bicycle_4.index[i]:i}, inplace = True)
bicycle_4


bicycle_4.describe() #nous donne des informations (moyenne, écart type)

#quand j'aurais mon tableau avec les jours de la semaine, puor ne garder que les vendredis je peux faire ça 
bicycle_3[bicycle_3['Jour'] == 'Vendredi' ]
bicycle_3[bicycle_3['Heure'] == '08:30:00' ] #ça marche

#je ferai un describe

#conversion avec les jours semaine
import datetime

Date = df_bicycle['Date']
'Date' = datetime.datetime.strptime('Date', '%Y-%m-%d %H:%M:%S.%f')

date_time_obj = datetime.datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S.%f')

import locale
locale.setlocale(locale.LC_ALL,'')

from datetime import datetime, date, time

dt=date(2021,1,5)
str(dt)
dt.isoformat()
dt
df_bicycle.strftime('%A')



from datetime import date

#me donne tous les vendredis jusqu'au jour de la prédiction
Ven = pd.date_range(pd.Timestamp("2021-01-08"), periods=13, freq='7d')
Ven.strftime('%B %d, %Y, %r')


#Me donne seulement les dates du tableau bicycle_4
Date = bicycle_4['Date']
Date


time = pd.to_datetime(bicycle_4['Date'] ,format='%d/%m/%Y')

l = []
for i in range (bicycle_4.shape[0]):
    l.append(pd.to_datetime(bicycle_4.iloc[i,0]).weekday()) 

bicycle_4['Weekday'] = l
del bicycle_4 ['Total année']

bicycle_4 = bicycle_4[bicycle_4['Weekday'] != 6]
bicycle_4 = bicycle_4[bicycle_4['Weekday'] != 5]

for i in range (len(bicycle_4)):
    bicycle_4.rename(index = {bicycle_4.index[i]:i}, inplace = True)
bicycle_4

