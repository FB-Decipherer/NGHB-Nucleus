import os.path
import zipfile
from typing import List

# from typing import   List
import filetype
import shutil
import datetime
from pathlib import Path
from zipfile import ZipFile

import csv
import pandas as pd

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

project_name = 'TC Prologue Decode'
project_prefix = 'TC-PD'
"""# Derive Project Directories xyz"""

system_dir = os.getcwd()
root_dir = str(Path(system_dir).parents[1]) + '/'
if not os.path.exists(root_dir):
    bp = root_dir

content_dir = root_dir + project_name + '/'
if not os.path.exists(content_dir):
    bp = content_dir

# Root Directory for project content:
# content_dir =  '/' + project_name + '/'

# Input File Directory paths (4 total):
signals_dir = content_dir + 'Signals/'
inputs_dir = signals_dir + 'Inputs/'
targets_dir = inputs_dir + 'Targets/'
templates_dir = inputs_dir + 'Templates/'

# Output File Directory paths (2 total):
outputs_dir = signals_dir + 'Outputs/'

# Archive File Directory paths (1 total):
archive_dir = content_dir + 'Archive/'

"""# Validate Project Directories"""

if not os.path.exists(system_dir):
    bp = system_dir

if not os.path.exists(targets_dir):
    bp = targets_dir

if not os.path.exists(templates_dir):
    bp = templates_dir

if not os.path.exists(outputs_dir):
    bp = outputs_dir

if not os.path.exists(archive_dir):
    bp = archive_dir
