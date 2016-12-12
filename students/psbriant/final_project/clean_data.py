"""
Name: Paul Briant
Date: 12/11/16
Class: Introduction to Python
Assignment: Final Project

Description:
Code for Final Project

To Do:
Add user interface
Add code to check for null cells
Remove or improve functionality of find_low_water_use
Add additional plotting functionality
Finish tests
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
    data.index = data.Date
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


def plot_zipcode(data, zipcode):
    """
    Plot water use data for a specified zipcode
    """
    plt.plot(data[zipcode])
    plt.show()


def menu():
    """

    """
    print("""

          Please select one of the following options:

          ************************************************************

          v - View visualizations for water use in a specific zipcode.
          s - View statistics for water use in  a specific zipcode.
          x - Exit program.

          ************************************************************

          """)


def user_interface(cleaned_data):
    """
    Allows user to view visualizations and statistics for different Los Angeles
    Zip codes.
    """
    print("""

          ************************************

          Welcome to the visualization program
          for Los Angeles Zipcode water use.

          ************************************

          """)
    while True:
        response = input(menu())
        if response.lower() == "v":
            zipcode = input("Please enter a zipcode to visualize ")
            # plot water use for zipcode
            plot_zipcode(cleaned_data, zipcode)
        elif response.lower() == "s":
            # prompt for zipcode
            # print stats for zipcode
            print("")
        elif response.lower() == "x":
            print("Thank you for using this program")
            return False
        else:
            print("Please select an option from the following menu:")


def main():
    """

    """
    # Connect to file.
    data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")
    cleaned_data = clean(data)
    user_interface(cleaned_data)


if __name__ == '__main__':
    main()
