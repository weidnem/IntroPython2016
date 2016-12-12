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


def test_clean():
    """

    """


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


def test_user_interface():
    """
    Tests user interface.
    """
