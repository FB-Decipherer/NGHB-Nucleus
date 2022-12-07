import os.path
import zipfile
from typing import List

# from typing import List
import filetype
import shutil
import datetime
from pathlib import Path
from zipfile import ZipFile

import csv
import pandas as pd

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# import  lib_programname
# path_to_program = lib_programname.get_path_executed_script()


project_name = 'NGHB-Nucleus'
project_prefix = 'NGHB-Nucleus'
"""# Derive Project Directories"""

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

"""# Set common file name for all output files"""

# the Output Filename used throughout is the concatenation of the Project Prefix with the
# current date and time (having the granularity of Minutes):

now = datetime.datetime.now()
output_filename = project_prefix + ' ' + now.strftime("%Y-%m-%d_%H-%M-%S")

"""# Copy two sample image files from input to a generic output directory"""

# sample target image file:
target_file_name = 'target.png'
target_file_path = targets_dir + target_file_name

if not os.path.exists(target_file_path):
    bp = target_file_path

if not filetype.is_image(target_file_path):
    bp = target_file_path
img1 = mpimg.imread(target_file_path)
# plt.imshow(img1)

output_path_1 = outputs_dir + 'Output' + '/' + target_file_name
outputs_arc_path1 = shutil.copyfile(target_file_path, output_path_1)  # transfer function

# --------------

# sample template image file:
template_file_name = 'template.png'
template_file_path = templates_dir + template_file_name

if not os.path.exists(template_file_path):
    bp = template_file_path

if not filetype.is_image(template_file_path):
    bp = template_file_path
img2 = mpimg.imread(template_file_path)
# plt.imshow(img2)

output_path_2 = outputs_dir + 'Output' + '/' + template_file_name
outputs_arc_path2 = shutil.copyfile(template_file_path, output_path_2)  # sample 'transfer function'

# --------------------
# Plot the two sample images side by side:
f, axarr = plt.subplots(1, 2)
axarr[0].imshow(img1)
axarr[1].imshow(img2)

# --------------------

# Create and display a FileChooser widget
#fc1 = FileChooser(templates_dir)

# display(fc1)
# -------------------

from os.path import basename


# Create the new archive:
def make_archive(archive_arc_path: object, file_paths: object) -> object:
    # writing files to a zipfile
    with ZipFile(archive_arc_path, 'w') as zip:
        # writing each file one by one
        for file in file_paths:
            zip.write(file, basename(file))

            zip.write(file)


#       zip.printdir()


def archive_signals_paths(fps):
    archive_file_paths: list[str] = []

    for fp in fps:
        tp = Path(fp)
        signal_arc_path = tp.parts[5] + '/' + tp.parts[6] + '/' + tp.parts[7] + '/' + tp.parts[8] + '/' + tp.name
        if not os.path.exists(signal_arc_path):
            bp = system_file_path
        archive_file_paths.append(signal_arc_path)
    return archive_file_paths


def archive_system_paths(fps):
    system_arc_path = ''
    archive_file_paths: list[str] = []

    for fp in fps:
        tp = Path(fp)
        system_arc_path = tp.parts[5] + '/' + tp.parts[6] + '/' + tp.name

    archive_file_paths.append(system_arc_path)
    return archive_file_paths


# system_file_path = '/Users/gorehambury/DataspellProjects/Prologue Decode/TC Prologue Decode/System/tc_prologue_decode_v1.py'

# if not os.path.exists(system_file_path):
#   bp = system_file_path

# system_file_paths_to_archive: list[str] = [system_file_path]
# archive_sys_paths = archive_system_paths(system_file_paths_to_archive)

# signal_file_paths_to_archive: list[str] = [target_file_path, template_file_path, outputs_arc_path1, outputs_arc_path2]
# archive_sig_paths = archive_signals_paths(signal_file_paths_to_archive)

# archive_file_paths = [system_file_path]

# archive_arc_path = archive_dir + output_filename + '.zip'
# make_archive(archive_arc_path,  archive_file_paths)


# Delete all but the last two files in selected directories:

def trim_previous_output_files(*trim_dirs):
    for trim_dir in trim_dirs:
        for filename in sorted(os.listdir(trim_dir))[:-2]:
            filename_rel_ath = os.path.join(trim_dir, filename)

            is_dir = os.path.isdir(filename_rel_ath)
            if not is_dir:
                os.remove(filename_rel_ath)
            else:
                print(filename_rel_ath)


# trim_previous_output_files(archive_dir, system_dir, od)


def zip_dir(dirpath, zippath):
    fzip = zipfile.ZipFile(zippath, 'w', zipfile.ZIP_DEFLATED)
    basedir = os.path.dirname(dirpath) + '/'
    for root, dirs, files in os.walk(dirpath):
        if os.path.basename(root)[0] == '.':
            continue  # skip hidden directories
        dirname = root.replace(basedir, '')
        for f in files:
            if f[-1] == '~' or (f[0] == '.' and f != '.htaccess'):
                # skip backup files and all hidden files except .htaccess
                continue
            fzip.write(root + '/' + f, dirname + '/' + f)
    fzip.close()


from git.repo import Repo

from git import Repo

#repo = Repo(os.getcwd())


it = 0
os.system("git add --all")
os.system("git commit -m 'sssss' ")



#it = 1

