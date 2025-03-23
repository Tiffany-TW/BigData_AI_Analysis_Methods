#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 14:40:03 2024

@author: twl
"""

import pandas as pd
import seaborn as sns

# Read file
df = pd.read_csv("/Users/twl/Documents/BigData_AI/Automobile_data.csv")


# Data cleaning
df = df.dropna()
for colname in df.columns:
    df = df[df[colname] != "?"]
df.price = df.price.astype("float64")
sns.set(font_scale=0.8)
sns.violinplot(data=df, x="make", y="price")

# Compute mutual information
X = df.copy()
y = X.pop("price") # X does not contain the target "price" and y contains the only feature "price"

# Label encoding for categroricals
for colname in X.select_dtypes("object"):
    X[colname], _ = X[colname].factorize()
    
# All discrete features shaould now have integer dtypes (double check this before using MI!)
discrete_features = X.dtypes == int

from sklearn.feature_selection import mutual_info_regression
import matplotlib.pyplot as plt
import numpy as np

def make_mi_scores(X, y, discrete_features):
    mi_scores = mutual_info_regression(X, y, discrete_features=discrete_features)
    mi_scores = pd.Series(mi_scores, name="MI Scores", index=X.columns)
    mi_scores = mi_scores.sort_values(ascending=False)
    return mi_scores

mi_scores = make_mi_scores(X, y, discrete_features)

def plot_mi_scores(scores):
    scores = scores.sort_values(ascending=True)
    width = np.arange(len(scores))
    ticks = list(scores.index)
    plt.barh(width, scores, color="#5DAC81")
    plt.yticks(width, ticks)
    plt.title("Mutual Information Scores")
   
plot_mi_scores(mi_scores)
