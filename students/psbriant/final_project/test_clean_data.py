"""
Name: Paul Briant
Date: 12/11/16
Class: Introduction to Python
Assignment: Final Project

Description:
Tests for Final Project
"""

import clean_data as cd
import pandas
import io

def get_data():
    """

    """
    data = pandas.read_csv("data/Residential_Water_Usage_Zip_Code_on_Top.csv")
    return data

def test_clean():
    """

    """


def test_rename_columns():
    """

    """
    data = get_data()
    data = data.drop(["Date Value"], axis=1)
    column_names = list(data.columns.values)
    column_list = cd.rename_columns(column_names)
    assert column_list[0:5] == ["Date", "90001", "90002", "90003", "90004"]


def test_find_low_water_use():
    """

    """


def test_plot_zipcode():
    """

    """
