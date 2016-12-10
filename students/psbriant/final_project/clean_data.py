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

# Change source to smaller file.
data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")

print(data["Date Text"].head())


first_date = data["Date Text"].values[0]
# print(first_date)

# datetime.strptime(first_date, "%Y-%m-%d")
# datetime(2012, 3, 10, 0, 0)

data.date = data.date.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
# print(data.date.head())
data.index = data.date
# print(data)

# print(data.ix[datetime(2012, 8, 19)])

# Remove date column
data = data.drop(["date"], axis=1)
# print(data.columns)

# Determine what values are missing
empty = data.apply(lambda col: pandas.isnull(col))
