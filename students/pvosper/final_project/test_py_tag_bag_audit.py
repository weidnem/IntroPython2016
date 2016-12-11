#!/usr/bin/env python

'''
Testing for tag bag audit methods

$ToDo
    -
'''

import io

from py_tag_bag_audit import destinations_list, tag_bag_list, tag_bag_content, extract_tag_name

# Uses test files in destinations directory

def test_destinations_list():
    l = destinations_list('destinations')
    assert l[0] == 'destinations/atlantis/atlantis.grognok_destination.tft'
    assert l[1] == 'destinations/new_york/new_york.grognok_destination.tft'

def test_tag_bag_list():
    l = tag_bag_list(['destinations/new_york/new_york.grognok_destination.tft'])
    assert l[0] == 'destinations/new_york/new_york.destination_global_tag_bag.tft'

def test_tag_bag_content():
    tag_bag_content(['destinations/new_york/new_york.destination_global_tag_bag.tft'])
#     print(outfile.readline)
    assert False

def test_extract_tag_name():
    s = '                                                                FIELD m_referenced_tag_name               "destinations/new_york/new_york.destination_global_tag_bag.tft"'
    t = extract_tag_name(s)
    assert t == 'destinations/new_york/new_york.destination_global_tag_bag.tft'