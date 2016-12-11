"""
Name: Paul Briant
Date: 12/11/16
Class: Introduction to Python
Assignment: Final Project

Description:
Code for Final Project
"""

import pandas
import matplotlib.pyplot as plt
from datetime import datetime, date


def clean(data):
    """
    Take in data and return cleaned version.
    """
    # Remove Date Values column
    data = data.drop(["Date Value"], axis=1)

    column_names = list(data.columns.values)
    data.columns = rename_columns(column_names)

    # Modify date format
    data.Date = data.Date.apply(lambda d: datetime.strptime(d, "%b_"
                                "%Y").date().replace(day=15))

    # Assign dates as the index
    # data.index = data.Date
    return data


def rename_columns(names):
    """
    Renames the date column and adds all columns into a list so they can be
    accessed by dot notation.
    """
    columns_list = []
    for name in names:
        if name == "Date Text":
            columns_list.append("Date")
        else:
            columns_list.append(name)
    return columns_list


def find_low_water_use(data):
    """

    """
    under100 = data[(data["90012"] <= 100) & (data["90013"] <= 100)]
    print(under100)
    under25 = data[(data["90012"] <= 25) & (data["90013"] <= 25)]
    print(under25)


def plot_zipcode(data, zipcode):
    """
    Plot water use data for a specified zipcode
    """
    # data["90012"].plot(kind="bar", rot=10)
    plt.plot(data[zipcode])
    plt.show()


def main():
    """

    """
    # Connect to file.
    data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")

    cleaned_data = clean(data)
    # find_low_water_use(cleaned_data)
    # plot_zipcode(cleaned_data, "90012")
    # cleaned_data["90012"].plot(kind="bar", rot=10)
    # cleaned_data["90012"].hist()
    # plt.plot(cleaned_data["90012"])
    # plt.plot([1, 2, 3, 4])


if __name__ == '__main__':
    main()
