#!/usr/bin/env python
# shepherds_many_lists_thru_identify_duplicates_in_a_list.py by Wayne Decatur
# ver 0.1
#
#*******************************************************************************
# USES Python 2.7 but should be convertable via 2to3, see https://docs.python.org/3.0/library/2to3.html
#
# PURPOSE: This script is meant to be an accessory script for working with
# `identify_duplicates_in_a_list.py` when you have several list in files and
# want to  find all instances of items in the lists that occur more than once.
#
#
#
#
#
#
# Dependencies beyond the mostly standard libraries/modules:
# EasyProcess which PythonAnywhere seems to have is layered on top of the subprocess module
#
#
#
# VERSION HISTORY:
# v.0.0.1. basic working version with the list of files hardcoded
# v.0.1. added ability to use an optional flag to just print out the pertinent
# commands to make it more universally useable without dependencies needed to
# actually run the produced commands from within the Python script
#
#
#
# TO RUN:
# Example,
# Enter on the command line of your terminal, the line
#-----------------------------------
# python shepherds_many_lists_thru_identify_duplicates_in_a_list.py
#-----------------------------------
#
#
#*******************************************************************************
#


#*******************************************************************************
##################################
#  USER ADJUSTABLE VALUES        #

##################################
##
#
lists_of_list_files_as_text_block = '''
snm1-5001_positive_gi_list.txt
snm1-5001_significant_positive_gi_list.txt
snm1-5001_significant_negative_gi_list.txt
snm1-5001_negative_gi_list.txt
snm1-5001_GI_profile_top_300.txt
snm1-172_negative_gi_list.txt
pop7-5001_negative_gi_list.txt
pop7-5001_significant_positive_gi_list.txt
pop7-5001_positive_gi_list.txt
pop7-5001_significant_negative_gi_list.txt
pop7-5001_GI_profile_top_300.txt
snm1-172_significant_positive_gi_list.txt
snm1-172_positive_gi_list.txt
snm1-172_significant_negative_gi_list.txt
snm1-172_GI_profile_top_300.txt
rmp1-ts_GI_profile_top_300.txt
rmp1-ts_significant_positive_gi_list.txt
rmp1-ts_positive_gi_list.txt
rmp1-ts_significant_negative_gi_list.txt
rmp1-ts_negative_gi_list.txt
pop3-5001_significant_positive_gi_list.txt
pop3-5001_positive_gi_list.txt
pop3-5001_negative_gi_list.txt
pop3-5001_significant_negative_gi_list.txt
pop3-5001_GI_profile_top_300.txt
pop1-5001_significant_positive_gi_list.txt
pop1-5001_positive_gi_list.txt
pop1-5001_significant_negative_gi_list.txt
pop1-5001_negative_gi_list.txt
pop1-5001_GI_profile_top_300.txt
''' #block was copied from finder on mac and pasted here
lists_of_list_files = []

directory_to_make = "redundancy_info"
file_name_tag_to_use_for_moving = "_redundant_alleles.txt"
#
#*******************************************************************************
#**********************END USER ADJUSTABLE VARIABLES****************************





















#*******************************************************************************
#*******************************************************************************
###DO NOT EDIT BELOW HERE - ENTER VALUES ABOVE###

import sys
import os
import argparse



###---------------------------HELPER FUNCTIONS---------------------------------###

def generate_more_descriptive_name(list_files_to_analyze_list):
    '''
    Takes a list as an argument and returns string for the name of the
    output file. The generated name is based on all the original file
    names in th elist.

    Specific example
    ================
    Calling function with
        ("file1.txt", "file2.txt", "file3.txt")
    returns
        "file1_file2_file3_shared_items.txt"
    '''
    name_suffix = "_shared_items.txt"
    list_of_file_names_without_extension = []
    for each_name in list_files_to_analyze_list:
        each_name_without_extension, _ =  os.path.splitext(each_name) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
        list_of_file_names_without_extension.append(each_name_without_extension)
    better_name_main_part = "_".join(list_of_file_names_without_extension)
    return better_name_main_part + name_suffix



suffix_for_saving_result = "_redundant_alleles.txt"

def generate_output_file_name_function_from_duplicate_fiding_script(
    file_name, suffix):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file
    name.

    Specific example
    ================
    Calling function with
        ("file1.txt", "_redudant_alleles.txt")
    returns
        "file1_redudant_alleles.txt"
    '''
    main_part_of_name, file_extension = os.path.splitext(
        file_name) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    return main_part_of_name + suffix



def list2text(a_list):
    '''
    a function that takes a lists and makes a string where each item in list
    is on a new line
    '''
    return "\n".join(a_list)


def combinations(n, list, combos=[]):
    '''
    takes a integer and a list

    function from https://gist.github.com/dougwt/1969743
    this code from "combinations.py"
    '''
    # initialize combos during the first pass through
    if combos is None:
        combos = []

    if len(list) == n:
        # when list has been dwindeled down to size n
        # check to see if the combo has already been found
        # if not, add it to our list
        if combos.count(list) == 0:
            combos.append(list)
            combos.sort()
        return combos
    else:
        # for each item in our list, make a recursive
        # call to find all possible combos of it and
        # the remaining items
        for i in range(len(list)):
            refined_list = list[:i] + list[i+1:]
            combos = combinations(n, refined_list, combos)
        return combos


###--------------------------END OF HELPER FUNCTIONS---------------------------###
###--------------------------END OF HELPER FUNCTIONS---------------------------###














#*******************************************************************************
###-----------------for parsing command line arguments-----------------------###
parser = argparse.ArgumentParser(prog='shepherds_all_list_combinations_thru_find_overlap_in_list.py',description="shepherds_all_list_combinations_thru_find_overlap_in_list.py \
    blah blah blah \
    **** Script by Wayne Decatur   \
    (fomightez @ github) ***")
'''
parser.add_argument("Files", help="Names of files containing lists to compare. AT LEAST ONE REQUIRED.", nargs="+")
# see http://stackoverflow.com/questions/13219910/argparse-get-undefined-number-of-arguments
# for how last line allows any number of files to be used.
'''
parser.add_argument("-c", "--commands_only",help=
    "add this flag to just have the commands that would need to be run sent to \
    standard out. You can then just paste them into the command line yourself. \
    This optional flag is meant to allow those who don't have EasyProcess (a \
    variation of the subprocess module) still use this script as it eliminates \
    the need for that non-standard dependency.",
    action="store_true")

'''
#I would also like trigger help to display if no arguments provided because need at least one input file
if len(sys.argv)==1:    #from http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    parser.print_help()
    sys.exit(1)
'''
args = parser.parse_args()
just_output_commands_only = args.commands_only


if not just_output_commands_only:
    from easyprocess import EasyProcess


###-----------------Actual Main portion of script---------------------------###


# Start by using the block of file names pasted to make lists_of_list_files
# combinations greater than pairings.
lists_of_list_files = [x.strip() for x in lists_of_list_files_as_text_block.split("\n")]
# When I did `--commands_only` option, I was seeing some empty ones and so added
# the next line to filter out those
lists_of_list_files = [x for x in lists_of_list_files if x] # current best way to do filter empty strings according to http://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings

# Make two-ish commands :
# One command will be for running `identify_duplicates_in_a_list.py` on each list
# and then a couple of commands at end to make a directory and copy all the
# files from earliery running to it based on the tag in the name.

prefix_for_py_script_command = "python identify_duplicates_in_a_list.py "

for list_file in lists_of_list_files:

    py_script_command = prefix_for_py_script_command + list_file
    if just_output_commands_only:
        print (py_script_command + '\n')
    else:
        sys.stderr.write(
            '\nRUNNING PYHON SCRIPT:\n' + py_script_command)
        # Now to run the command
        ## ORIGINALLY HAD NEXT LINE WHEN JUST WANTED COMMAND TO RUN WITH NO FEEDBACK
        '''
        command_to_run = EasyProcess(
        'python find_overlap_in_lists.py '
        + string_of_filenames_for_py_command ).call() '''
        command_run_handler = EasyProcess(py_script_command).call().stderr
        # give some feedback and how running
        sys.stderr.write( command_run_handler + "\n")


# Now for the moving command, first I need to make a directory to move
# created files into.
mkdir_command = "mkdir " + directory_to_make
prefix_for_moving_command = "mv "

move_command = (
    prefix_for_moving_command + "*" +
    file_name_tag_to_use_for_moving + " " + directory_to_make)
#turns out you
# cannot use wild-card with subprocess/easyprocess and you cannot add the solution
# zmo uses at http://stackoverflow.com/questions/21804935/how-to-use-the-mv-command-in-python-with-subprocess
# because it seems according to Easyprocess documentation, you are constrained to
# `shell=False` . BUT CAN STILL USE THE MOVE COMMAND WITH '*' commands_only output (see next.)

if just_output_commands_only:
    print (mkdir_command + '\n' + move_command) #even though cannot use wild-card
    # from within this script to move files, okay to output as command because
    # it will work for user to paste into command line
else:
    sys.stderr.write(
        '\nMOVING NEWLY CREATED FILES TO A DIRECTORY:\n' +
        mkdir_command + '\n' + move_command + '\n')


    # Now to run the commands
    mkdir_handler = EasyProcess(mkdir_command ).call().stderr
    # give some feedback and how running
    sys.stderr.write(mkdir_handler + "\n")
    # see ABOVE for why this below won't work since wildcard use is not possibe
    '''
    move_handler = EasyProcess(move_command ).call().stderr
    # give some feedback and how running
    sys.stderr.write(move_handler + "\n")
    '''
    # so do move with python
    # based on Peter Vlaar's example at
    # http://stackoverflow.com/questions/8858008/how-to-move-a-file-in-python
    import shutil
    #import os #already imported
    dir_path = os.path.dirname(os.path.realpath(__file__)) # from http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
    #print dir_path #for debugging
    source = os.listdir(dir_path) #current directory as list
    #print source # for debugging
    destination = dir_path+"/"+ directory_to_make +"/"
    #print destination # for debugging
    for each_file_name in source:
        if each_file_name.endswith(file_name_tag_to_use_for_moving):
            shutil.move(dir_path+"/"+ each_file_name,destination+ each_file_name)
    sys.stderr.write("(Did actual move in Python but that command is equivalent and\nwill work on command line; wildcard '*' not allowed with EasyProcess, it seems,\nwhich is way I went another route.)\n")

#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************
