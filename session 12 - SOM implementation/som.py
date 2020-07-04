# -*- coding: utf-8 -*-

#Self Organizing Map

##Install MiniSom Package
"""

!pip install MiniSom

"""### Importing the libraries"""

import numpy as np
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Credit_Card_Applications.csv')
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, -1].values

"""## Feature Scaling"""

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
X = sc.fit_transform(X)

"""##Training the SOM"""

from minisom import MiniSom
som = MiniSom(x=10, y=10, input_len= 15, sigma= 1.0, learning_rate = 0.5)
som.random_weights_init(X)
som.train_random(data = X, num_iteration = 100)

"""##Visualizing the results"""
"""#
bone() - uses a bare bone canvas
som.distance_map is the way of finfing the mean and then using the neuron distance
colorbar() helps you identify the class using color
markers is used to mark 0 and 1 , color is to color the 0 and 1
we are coloring and marking them depending upon y variable to compare it with the SOM formed and identify the defaults
"""#description of logic"""
from pylab import bone, pcolor, colorbar, plot, show
bone()
pcolor(som.distance_map().T)
colorbar()
markers = ['o', 's']
colors = ['r', 'g']
for i, x in enumerate(X):
    w = som.winner(x)
    plot(w[0] + 0.5,
         w[1] + 0.5,
         markers[y[i]],
         markeredgecolor = colors[y[i]],
         markerfacecolor = 'None',
         markersize = 10,
         markeredgewidth = 2)
show()

"""## Finding the frauds"""

"""#explaination"""
mappings = som.win_map(X)
frauds = np.concatenate((mappings[(2,1)], mappings[(8,3)]), axis = 0)
frauds = sc.inverse_transform(frauds)

"""##Printing the Fraunch Clients"""

print('Fraud Customer IDs')
for i in frauds[:, 0]:
  print(int(i))