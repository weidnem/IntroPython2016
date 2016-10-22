# Charles Robison
# 2016.10.21
# Dictionary and Set Lab

#!/usr/bin/env python
import os

cwd = os.getcwd()

# write a program which prints the full path to all files
# in the current directory, one per line
for item in os.listdir(cwd):
    print(cwd + "/" + item)



# write a program which copies a file from a source, to a
# destination (without using shutil, or the OS copy command)
