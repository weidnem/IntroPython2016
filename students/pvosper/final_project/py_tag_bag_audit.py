#!/usr/bin/env python

'''
Creates tag_bag_audit.csv, listing .patterns and .budget_sets from .global_tag_bags
Also creates common_budget_set_audit.csv, listing all .patterns from common budget sets
<source file name>, <source file w/relative path>, <referenced tag file name>, <referenced tag file file w/relative path>

NOTE: While this will be run exclusively on Windows, I'm writing/testing this
on a Mac, so paths are set for MacOS/Linux.

$ToDo:
    @CHB: This is pretty deeply nested -- break into separate functions, maybe?
    replace 'find' with 'in'
    fn for splitting name & path
    generator expression -> no intermediate array is produced
    for x in (y for y in items if y > 10):
    Iterating over Document Object Model (DOM)
    Windows vs MacOS/Linux file paths
    PEP8
'''

import io

import os

import time

start = time.clock()

def destinations_list(fpath):
    # In use, fpath should default to  = 'content\\world'
    '''Returns list of relative file paths for valid destinations'''
    l = []
    for destination_dir in os.scandir(fpath):
        # Filter out MacOS/Linux hidden files
        if not destination_dir.name.startswith('.'):
            for file in os.scandir(destination_dir.path):
                if file.name.endswith('.grognok_destination.tft'):
                    l.append('{}/{}'.format(destination_dir.path, file.name))
    return l

def tag_bag_list(dest_list):
    '''Returns list of relative file paths for tag bags from list of destinations'''
    l = []
    for dest_file in dest_list:
        with open(dest_file) as destination:
            lines_list = destination.readlines()
            for i in range(len(lines_list)):
                # if lines_list[i].find('FIELD global_tag_bag') >= 0:
                if 'FIELD global_tag_bag' in lines_list[i] != False:
                    # Actual reference on following line within field
                    for j in range(4):
                        if 'FIELD m_referenced_tag_name' in lines_list[i + j] != False:
                        # if lines_list[i + j].find('FIELD m_referenced_tag_name') >= 0:
                            l.append(extract_tag_name(lines_list[i + j]))
                            # There's only one global_tag_bag entry per destination so we should stop here
                            # break
    return l

def tag_bag_content(tb_list):
    '''Returns list of content references within each tag bag from a list'''
    outfile = open('tag_bag_audit.csv','w')
    # Find referenced tags from bags in list
    for tag_bag in tb_list:
        with open(tag_bag) as f:
            for line in f:
                if line.find('.tft') >= 0:
                    tag_name = extract_tag_name(line)
                    write_list = [tag_bag, tag_name]
                    write_string = (','.join(write_list) + '\n').replace('\\\\', '\\').replace('"', '')
                    # What happens when files with the same name are in differently named directories?
                    outfile.write(write_string)
  
def extract_tag_name(line_string):
    '''Returns referenced tag name with path given valid string (line from file), otherwise returns None'''
    # if line_string.find('"') >= 0:
    if '"' in line_string != False:
        tag_path = line_string[line_string.find('"'):-1]
        return tag_path.replace('\\\\', '\\').replace('"', '')
    else:
        return None
        
def source_files():
    '''Returns the source file name given valid path'''
    pass

end = time.clock()
                
if __name__ == "__main__":

    dest_list = destinations_list('destinations')

    print(dest_list)
    
    tb_list = tag_bag_list(dest_list)
        
    print(tb_list)
    
    tag_bag_content(tb_list)
    
    print('\tFinished!\n\tElapsed time: {:.2f} seconds'.format(end - start))