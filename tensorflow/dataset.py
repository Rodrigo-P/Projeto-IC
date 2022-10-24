# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import pandas
#import os

X = pandas.read_json("jsons\\Data_X.json", lines = True)
Y = pandas.read_json("jsons\\Data_Y.json", lines = True)


print(X.head())
print(Y.head())

X.hist(bins=50)
plt.show()

Y.hist()
plt.show()

# collsX = list(X.columns)

# for i in range(len(collsX)):
# 	collX = X.pop(collsX[i])

# 	X.to_json("tensorflow\\varRemoved\\X_" + collsX[i] + ".json")
# 	X.insert(i, collsX[i], collX)


# X.pop("jaccardCoef")
# collsX = list(X.columns)

# for i in range(len(collsX)):
# 	collX = X.pop(collsX[i])

# 	X.to_json("tensorflow\\jaccRemoved\\X_" + collsX[i] + ".json")
# 	X.insert(i, collsX[i], collX)