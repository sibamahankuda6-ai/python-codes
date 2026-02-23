# write the python program to content of a directory using the os module.
import os

# Take directory path from user
path = '/python'

# Check if the directory exists
if os.path.exists(path):
    print("Contents of the directory:")
    for item in os.listdir(path):
        print(item)
else:
    print("Directory does not exist")
