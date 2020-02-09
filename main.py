

import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('Demanda_2015.txt', sep="\t")
data.columns = ["Date", "Time", "Usage"]

data['Date'] = pd.to_datetime(data['Date'] + ' ' + data['Time'])
del data['Time']

data.plot(figsize=(200,10))

data.plot(x='Date', y='Usage')
plt.gcf().set_size_inches(100, 15)
#plt.savefig('graph_demanda1.png')



databases = []

for i in range(12):
  hey = data[pd.to_datetime(data['Date']).dt.month == i+1]
  hey.sort_values(by='Date')
  hey.columns = ["Date" + str(i+1), "Usage" + str(i+1)]
  hey.reset_index()
  print(hey.columns)
  print(hey)
  

hey.to_csv(r'pandas.txt', sep=' ')

datas = pd.concat(databases, ignore_index=True)




datas['Date12'].to_csv(r'pandas.txt', sep=' ')