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


def main():
    """

    """
    # Connect to file.
    data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")

    clean(data)


if __name__ == '__main__':
    main()
