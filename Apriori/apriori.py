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

# Training Apriori on the dataset
from apyori import apriori
# For min_support, we want to consider only those products that are significant in terms of how frequently they are picked up by the customer. Hence, we will consider products that are bought atleast 3 times a day. This means that they are bought atleast 21 times a week. Hence, min_support equals = 21/7500
# We want a high Lift, which means a strong association. Hence, we will set it to a min_value of 3
rules = apriori(transactions, min_support = 0.003,min_confidence = 0.2,min_lift = 3,min_length = 2)

# Visualizing the results
results = list(rules)
