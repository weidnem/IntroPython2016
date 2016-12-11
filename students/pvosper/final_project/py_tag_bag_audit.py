#!/usr/bin/env python

'''
Creates tag_bag_audit.csv, listing .patterns and .budget_sets from
.global_tag_bags

NOTES:
- While this will be run exclusively on Windows, I'm writing/testing this
    on a Mac, so paths are set for MacOS/Linux.
- Test content 'atlantis' does not contain a tag bag reference

@CHB: This is pretty deeply nested -- break into separate functions, maybe?
'''

import io

import os

import time

start = time.time()


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
    '''Returns list of relative file paths for tag bags from list of
        destinations'''
    l = []
    for dest_file in dest_list:
        with open(dest_file) as destination:
            lines_list = destination.readlines()
            for i in range(len(lines_list)):
                if 'FIELD global_tag_bag' in lines_list[i] is not False:
                    # Actual reference on following line within field
                    for j in range(4):
                        if 'FIELD m_referenced_tag_name' in \
                                lines_list[i + j] is not False:
                            l.append(extract_tag_name(lines_list[i + j]))
    return l


def tag_bag_content(tb_list):
    '''Returns list of content references within each tag bag from a list'''
    outfile = open('tag_bag_audit.csv', 'w')
    # Find referenced tags from bags in list
    for tag_bag in tb_list:
        with open(tag_bag) as f:
            for line in f:
                if line.find('.tft') >= 0:
                    tag_name = extract_tag_name(line)
                    write_list = [
                        base_file(tag_bag),
                        tag_bag,
                        base_file(tag_name),
                        tag_name]
                    write_string = (
                        ','.join(write_list) +
                        '\n').replace('\\\\', '\\').replace('"', '')
                    outfile.write(write_string)


def extract_tag_name(line_string):
    '''Returns referenced tag name with path given valid string
        (line from file), otherwise returns None'''
    if '"' in line_string is not False:
        tag_path = line_string[line_string.find('"'):-1]
        return tag_path.replace('\\\\', '\\').replace('"', '')
    else:
        return None


def base_file(file_name):
    '''Returns the base file name given valid path'''
    s = os.path.basename(file_name)
    return s[:s.find('.')]


end = time.time()


if __name__ == "__main__":

    dest_list = destinations_list('destinations')

    print(dest_list)

    tb_list = tag_bag_list(dest_list)

    print(tb_list)

    tag_bag_content(tb_list)

    print('\tFinished!\n\tElapsed time: {:.10f} seconds'.format(end - start))
