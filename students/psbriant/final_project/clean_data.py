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


def clean(data):
    """
    Take in data and return cleaned version.
    """
    # Remove Date Values column
    data = data.drop(["Date Value"], axis=1)

    # Determine what values are missing
    # empty = data.apply(lambda col: pandas.isnull(col))

    return data


def find_low_water_use(data):
    """

    """
    under100 = data[(data["90012"] <= 100) & (data["90013"] <= 100)]
    print(under100)
    under25 = data[(data["90012"] <= 25) & (data["90013"] <= 25)]
    print(under25)


def main():
    """

    """
    # Connect to file.
    data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")

    cleaned_data = clean(data)
    find_low_water_use(cleaned_data)


if __name__ == '__main__':
    main()
