"""
Name: Paul Briant
Date: 12/11/16
Class: Introduction to Python
Assignment: Final Project

Description:
This program allows the user to select a zipcode to see statistics and graphs
for monthly water use in the city of Los Angeles.

To Do:
Add code to check for null cells
Add try/except to verify input zipcode is in Los Angeles.
Add additional plotting functionality
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

    # Assign dates as the index
    data.index = mod_dates(data)
    return data


def mod_dates(data):
    """
    Take in partially cleaned csv file and reformat dates so they year, month,
    day in a numerical format.
    """
    data.Date = data.Date.apply(lambda d: datetime.strptime(d, "%b_"
                                "%Y").date().replace(day=15))
    return data.Date


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
    Provide a set of options for the user to select. Take in zero values and
    output the menu as a string.
    """
    choices = """

              Please select one of the following options:

              ************************************************************

              v - View visualizations for water use in a specific zipcode.
              s - View statistics for water use in  a specific zipcode.
              x - Exit program.

              ************************************************************

              """

    return choices


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
    Connect to csv file, clean data and initiate user expirience.
    """
    # Connect to file.
    data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")
    cleaned_data = clean(data)
    user_interface(cleaned_data)


if __name__ == '__main__':
    main()
