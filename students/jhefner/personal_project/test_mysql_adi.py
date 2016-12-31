#!./bin/python

"""
Tests for mysql_ADI.py
"""

import sys
import os
import argparse
import pymysql
from configparser import SafeConfigParser
import json
from mysql_ADI import connect_to_db

def test_connect_to_db():
    assert connect_to_db()


test_connect_to_db()
