"""
Name: Paul Briant
Date: 12/11/16
Class: Introduction to Python
Assignment: Final Project

Description:
Code for Final Project
"""

import pandas
from datetime import datetime

# Connect to file.
data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")

# print(data.ix[datetime(2012, 8, 19)])

# Remove Date Values column
data = data.drop(["Date Value"], axis=1)
print(data)

# Determine what values are missing
# empty = data.apply(lambda col: pandas.isnull(col))
