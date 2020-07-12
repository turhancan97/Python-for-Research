#Getting Started with Pandas

import pandas as pd
x = pd.Series([6,3,8,6])
print(x)

x = pd.Series([6,3,8,6], index=["q","w","e","r"])
print(x)

age = {"Ali":30,"Veli":25,"Can":40}
x = pd.Series(age)
print(x)

data = {"Name":["Tim","Ali"],
        "Age":[25,30],
        "ZIP":["35410","35400"]}
x = pd.DataFrame(data)
print(x)
x["Name"]

# Loading and Inspecting Data
import numpy as np
whisky = pd.read_csv("whiskies.txt")
whisky["Region"] = pd.read_csv("regions.txt")
whisky.head()
whisky.iloc[0:10]
whisky.iloc[5:10,0:5]
whisky.columns
flavors = whisky.iloc[:,2:14]
flavors

# Exploring Correlations

corr_flavors = pd.DataFrame.corr(flavors)
print(corr_flavors)

import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
plt.pcolor(corr_flavors)
plt.colorbar()

corr_whisky = pd.DataFrame.corr(flavors.transpose())
plt.figure(figsize=(10,10))
plt.pcolor(corr_whisky)
plt.colorbar()

# Clustering Whiskies By Flavor Profile

from sklearn.cluster.bicluster import SpectralCoclustering
model = SpectralCoclustering(n_clusters=6,random_state=0)
model.fit(corr_whisky)
np.sum(model.rows_,axis=1)
np.sum(model.rows_,axis=0)
model.row_labels_

#Comparing Correlation Matrices
whisky["Group"] = pd.Series(model.row_labels_,index=whisky.index)
whisky = whisky.ix[np.argsort(model.row_labels_)]
whisky = whisky.reset_index(drop=True)
correlations = pd.DataFrame.corr(whisky.iloc[:,2:14].transpose())
correlations = np.array(correlations)
plt.figure(figsize=(14,7))
plt.subplot(121)
plt.pcolor(corr_whisky)
plt.title("Original")
plt.axis("tight")
plt.subplot(122)
plt.pcolor(correlations)
plt.title("Rearranged")
plt.axis("tight")

import pandas as pd
data = pd.Series([1,2,3,4])
data = data.ix[[3,0,1,2]]
data[0]

import pandas as pd
data = pd.Series([1,2,3,4])
data = data.ix[[3,0,1,2]]
data = data.reset_index(drop=True)
data[0]
