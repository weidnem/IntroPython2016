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
data_columns = ["Date_Text", "Date_Value", "90001", "90002", "90003", "90004",
                "90005", "90006", "90007", "90008", "90010", "90011", "90012",
                "90013", "90014", "90015", "90016", "90017", "90018", "90019",
                "90020", "90021", "90022", "90023", "90024", "90025", "90026",
                "90027", "90028", "90029", "90031", "90032", "90033", "90034",
                "90035", "90036", "90037", "90038", "90039", "90041", "90042",
                "90043", "90044", "90045", "90046", "90047", "90048", "90049",
                "90056", "90057"]
# first_date = data..values[0]
# print(first_date)
