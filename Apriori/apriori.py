"""
@author: arjun
"""
# *********************************************************************************************************************
# AIM: Optimizing the sales in a grocery store using Apriori algorithm
# *********************************************************************************************************************
# Importing libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)

# Converting the dataset in to lists(input for apriori model)
transactions = []
for i in range(0,len(dataset)):
    currentItem = dataset.iloc[i,:].values
    currentTransaction = []
    for j in range(0,len(currentItem)):
        currentTransaction.append(str(currentItem[j]))
    transactions.append(currentTransaction)

