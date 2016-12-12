"""
Name: Paul Briant
Date: 12/11/16
Class: Introduction to Python
Assignment: Final Project

Description:
Tests for Final Project
"""

import clean_data as cd
import matplotlib.pyplot as plt
import pandas
import pytest


def get_data():
    """
    Retrieve data from csv file to test.
    """
    data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")
    return data


def test_mod_dates():
    """
    Ensure dates are modified in the year, month day numerical format.
    """
    data = get_data()
    data = data.drop(["Date Value"], axis=1)
    column_names = list(data.columns.values)
    data.columns = cd.rename_columns(column_names)
    date_list = cd.mod_dates(data)
    assert date_list[0:5] == ["2005-07-15", "2005-08-15", "2005-09-15",
                              "2005-10-15", "2005_11_15"]


def test_rename_columns():
    """
    Test whether rename_columns successfully renames each column.
    """
    data = get_data()
    data = data.drop(["Date Value"], axis=1)
    column_names = list(data.columns.values)
    column_list = cd.rename_columns(column_names)
    assert column_list[0:5] == ["Date", "90001", "90002", "90003", "90004"]


@pytest.mark.mpl_image_compare
def test_plot_zipcode():
    """
    Test zipcode based wateruse graphs.

    To Do: fix test that fails
    """
    data = get_data()
    cleaned = cd.clean(data)
    wateruse = cd.plot_zipcode(cleaned, "90012")
    return wateruse


def test_menu():
    """
    Test the generation of a text menu for the user interface.
    """
    choices = """

              Please select one of the following options:

              ************************************************************

              v - View visualizations for water use in a specific zipcode.
              s - View statistics for water use in  a specific zipcode.
              x - Exit program.

              ************************************************************

              """
    assert cd.menu() == choices
