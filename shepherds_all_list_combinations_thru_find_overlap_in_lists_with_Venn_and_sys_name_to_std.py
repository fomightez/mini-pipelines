#!/usr/bin/env python
# shepherds_all_list_combinations_thru_find_overlap_in_lists_with_Venn_and_sys_name_to_std.py by Wayne Decatur
# ver 0.1
#
#*******************************************************************************
# USES Python 2.7 but should be convertable via 2to3, see https://docs.python.org/3.0/library/2to3.html
#
# PURPOSE: This script is meant to be an accessory script for working with
# `find_overlap_in_lists_with_Venn.py` and a special version of
# `genes_in_list_with_SGD_Systematic_Name_to_standard_name.py`
# when you have several lists and want to find the
# overlap in all the combinations plus add information about yeast genes.
# For example, if you had five files of lists
# it will generate and run commands to `find_overlap_in_lists_with_Venn.py` to find overlap
# between all five files, between all combinations of four of the five files,
# all combincations of three of the five files, and in all combinations of pairs
#  of the files.
# The crux is of the script is that it takes the list of the files containing
# the list and steps through making lists of all the combinations starting with
# all the files and stepping down to all the possible pairs. It then uses this
# lists to generate the commands to run `find_overlap_in_lists_with_Venn.py` on all the
# combinations and handles making the resulting output files have meaningful
# names. THEN IT FIXES THE GENE NAMES TO HAVE STANDARD NAME ALONGSIDE THE
# SYSTEMATIC.
# It needs a special version of the file
# `genes_in_list_with_SGD_Systematic_Name_to_standard_name.py` that has been
# edited to produce as output the same file name it started with as input. (
# This is done just by changing the `generate_output_file_name(` function to
# just return the name it was called with. I just do this on my PythonAnywhere
# account in the directory where I am using this script.)
# `find_overlap_in_lists_with_Venn.py` and the special version of
# `genes_in_list_with_SGD_Systematic_Name_to_standard_name.py`needs to be placed
# in the directory along with this script.
# Note, aside from `find_overlap_in_lists_with_Venn.py` there is a related script for
# generating results of all the combinations of pairs of lists, called
# `find_overlap_in_list_pairs.py`. That script DOES NOT have the dependencies
# this one does, and so some may find it more convenient than this particular
# script.
# With the optional flag `--commands_only`, you can just output the commands
# needed to paste into the command line. This will allow you to bypass any
# dependencies needed to run the commands from withing script, and so may be
# more convenient. If you wanted the commands as a file you could just use a
# redirect like so
# `shepherds_all_list_combinations_thru_find_overlap_in_lists_and_sys_name_to_std.py list1.txt list2.txt list3.txt > commands.txt`.
# The  `find_overlap_in_lists_with_Venn.py`script also sends to the command line some
# information about the percent matching the shared list. You can easily
# redirect that information for every combination run to a file by adding
# `2>> info.log` to the call to this script. BE AWARE THAT as a by product,
# this will send the typical feedback seen to that log file.
#
#
# related script is: `shepherds_all_list_combinations_thru_find_overlap_in_lists.py`
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
# v.0.1. basic working version with the list files supplied via command line
#
#
#
# TO RUN:
# Example,
# Enter on the command line of your terminal, the line
#-----------------------------------
# python shepherds_all_list_combinations_thru_find_overlap_in_lists_with_Venn_and_sys_name_to_std.py list1.txt list2.txt list3.txt list4.txt list5.txt
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
# ?
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

def generate_more_descriptive_imagefile_name(provided_file_name):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file
    name.

    Specific example
    ================
    Calling function with
        ("file1_file2_file3_shared_items.txt")
    returns
        "file1_file2_file3_overlap_representation.png"
    '''
    # return already determined generate_more_descriptive_name() result where `_shared_items` and anything after it replaced with `_overlap_representation.png`
    return provided_file_name.rsplit("_shared_items", 1)[0] + '_overlap_representation.png'


def generate_output_file_name_function_from_overlap_script(first_file_name, list_files_to_analyze_list):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file
    name.

    Specific example
    ================
    Calling function with
        ("file1.txt")
    when `list_files_to_analyze_list` contains 3 file names
    returns
        "file1_and_3others_shared_items.txt"
    '''
    main_part_of_name, file_extension = os.path.splitext(
        first_file_name) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    if len(list_files_to_analyze_list) == 2:
        base_name_without_extension_for_second_file = os.path.splitext(
            os.path.basename(list_files_to_analyze_list[1]))[0]
        if '.' in first_file_name:  #I don't know if this is needed with the os.path.splitext method but I had it before so left it
            return main_part_of_name + "_and_"+ base_name_without_extension_for_second_file +"_shared_items" + file_extension
        else:
            return first_file_name + "_and_"+ base_name_without_extension_for_second_file +"_shared_items"
    else:
        if '.' in first_file_name:  #I don't know if this is needed with the os.path.splitext method but I had it before so left it
            return main_part_of_name + "_and_"+ str(len(
                list_files_to_analyze_list) - 1) +"others_shared_items" + file_extension
        else:
            return first_file_name + "_and_"+ str(len(
                list_files_to_analyze_list) - 1) +"others_shared_items"


def generate_image_file_name_from_venn_script(first_file_name, list_files_to_analyze_list):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file
    name.

    Specific example
    ================
    Calling function with
        ("file1.txt")
    when `list_files_to_analyze_list` contains 3 file names
    returns
        "file1_and_3others_overlap_representation.png"
    '''
    data_file_name_generator_result = generate_output_file_name_function_from_overlap_script(
        first_file_name, list_files_to_analyze_list)
    # return data_file_name_generator_result where `_shared_items` and anything after it replaced with `_overlap_representation.png`
    return data_file_name_generator_result.rsplit("_shared_items", 1)[0] + '_overlap_representation.png'



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
parser = argparse.ArgumentParser(prog='shepherds_all_list_combinations_thru_find_overlap_in_lists_and_sys_name_to_std.py',description="shepherds_all_list_combinations_thru_find_overlap_in_lists_and_sys_name_to_std.py \
    is meant to be an accessory script for working with \
    `find_overlap_in_lists_with_Venn.py` when you have several lists and want to find the \
    overlap in all the combinations. It was originally \
    intended to be used for lists \
    of genes, but works on any lists. **** Script by Wayne Decatur   \
    (fomightez @ github) ***")
parser.add_argument("Files", help="Names of files containing lists to compare. AT LEAST ONE REQUIRED.", nargs="+")
# see http://stackoverflow.com/questions/13219910/argparse-get-undefined-number-of-arguments
# for how last line allows any number of files to be used.
parser.add_argument("-c", "--commands_only",help=
    "add this flag to just have the commands that would need to be run sent to \
    standard out. You can then just paste them into the command line yourself. \
    This optional flag is meant to allow those who don't have EasyProcess (a \
    variation of the subprocess module) still use this script as it eliminates \
    the need for that non-standard dependency.",
    action="store_true")
#I would also like trigger help to display if no arguments provided because need at least one input file
if len(sys.argv)==1:    #from http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
list_files_to_analyze_list = args.Files
just_output_commands_only = args.commands_only

if not just_output_commands_only:
    from easyprocess import EasyProcess


###-----------------Actual Main portion of script---------------------------###

# Warn if only one file provided
if len(list_files_to_analyze_list) == 1:
    sys.stderr.write( "\n***WARNING***. Hard to check for overlap between lists, when given only one list.\nForget to add others? By default overlap equals provided list...ta da\n")

# Starting with the list of files to analyze, make lists of all the
# combinations greater than pairings.
all_combinations_list = []
for number_of_items_to_combine in reversed(range(2,len(list_files_to_analyze_list) + 1) ):
    all_combinations_list = combinations(
        number_of_items_to_combine, list_files_to_analyze_list,
        all_combinations_list)
# print all_combinations_list           # FOR DEBUGGING
# print str(len(all_combinations_list)) # FOR DEBUGGING

# Make three commands using each of the combinations:
# One command will be for running `find_overlap_in_lists_with_Venn.py` and
# one command will be for running `genes_in_list_with_SGD_Systematic_Name_to_standard_name.py` and
# one command will be for renaming the file produced by the previous command to
# something unique and more descriptive because otherwise previous results
# easy to clobber since script `find_overlap_in_lists_with_Venn.py` produces names like
# "file1_and_3others_shared_items.txt", and so any combination of four would
# match that and also it is hard to know what is included in such a result.


prefix_for_script_command = "python find_overlap_in_lists_with_Venn.py "
prefix_for_second_script_command = "python genes_in_list_with_SGD_Systematic_Name_to_standard_name.py --both_orf_std "
prefix_for_renaming_command = "mv "

for each_list_of_files in all_combinations_list :

    # For the command to run `find_overlap_in_lists_with_Venn.py` I'll need a string of
    # the each_list_of_files with each separated by a space
    string_of_filenames_for_py_command = " ".join(each_list_of_files)
    script_command = prefix_for_script_command + string_of_filenames_for_py_command

    # Now for the renaming command, I'll need to determine what file name that
    # last command would produce and then be ready for feeding to to the script
    # to add standard name along with systematic name and then in case of more
    # than two file to ake a better new name. EXCEPT FOR
    # CASE OF PAIRS SINCE PROGRAM ALREADY MAKES DESCRIPTIVE NAME FOR PAIRS.
    file_name_expected = generate_output_file_name_function_from_overlap_script(
        each_list_of_files[0], each_list_of_files)
    image_file_name_expected = generate_image_file_name_from_venn_script(
        each_list_of_files[0], each_list_of_files)
    # print file_name_expected # FOR DEBUGGING
    better_name = generate_more_descriptive_name(each_list_of_files)
    better_imagefile_name = generate_more_descriptive_imagefile_name(better_name)
    second_script_command = (prefix_for_second_script_command
        + file_name_expected)
    renaming_command = (prefix_for_renaming_command
        + file_name_expected + ' ' +  better_name)
    renaming_imagefile_command = (prefix_for_renaming_command
        + image_file_name_expected + ' ' +  better_imagefile_name)

    if just_output_commands_only:
        print (script_command + '\n')
        print (second_script_command + '\n')
        if len(each_list_of_files) > 2:
            print(renaming_command + '\n') #note that without running the
            # script, I cannot be sure if a file made or not and so producing
            # file handling call assuming something worked. No harm, no foul if
            # there was such no file produced.

            # Don't need to deal with image file renaming unless 3 or 4 lists
            # because for 2 it is already descriptive enough, and won't make an
            # image for those with more than four lists.
            if len(each_list_of_files) < 5:
                print(renaming_imagefile_command + '\n') #note that without running the
                # script, I cannot be sure if a file made or not and so producing
                # file handling call assuming something worked. No harm, no foul if
                # there was such no file produced.

    else:
        sys.stderr.write(
            '\nRUNNING SCRIPT:\n' + script_command)
        # Now to run the command
        ## ORIGINALLY HAD NEXT LINE WHEN JUST WANTED COMMAND TO RUN WITH NO FEEDBACK
        '''
        command_to_run = EasyProcess(
        'python find_overlap_in_lists.py '
        + string_of_filenames_for_py_command ).call() '''
        command_run_handler = EasyProcess(script_command).call().stderr
        # give some feedback and how running
        sys.stderr.write( command_run_handler + "\n")


        # The above command may have not produced output so need to verify that
        # it exists
        # And if it does exist need to first add standard gene name alongside
        # systematic, and then also in case of where more than two lists
        # involved rename output to be more descriptive.
        if os.path.isfile(file_name_expected):
            sys.stderr.write(
                '\nRUNNING SCRIPT TO ADD STANDARD GENE NAME:\n'
                + second_script_command)
            # Now to run the command
            second_command_run_handler = EasyProcess(
                second_script_command).call().stderr
            # give some feedback and how running
            sys.stderr.write( second_command_run_handler + "\n")
            # now handle renammg, if need be
            if len(each_list_of_files) > 2:
                sys.stderr.write(
                'RENAMING FILE JUST MADE TO BE MORE DESCRIPTIVE:\n'
                + renaming_command + "\n")
                # print better_name # FOR DEBUGGING
                rename_file_handler = EasyProcess(renaming_command).call()
                # Don't need to deal with image file renaming unless 3 or 4 lists
                # because for 2 it is already descriptive enough, and won't make an
                # image for those with more than four lists.
                if len(each_list_of_files) < 5:
                    sys.stderr.write(
                    'RENAMING IMAGE FILE JUST MADE TO BE MORE DESCRIPTIVE:\n'
                    + renaming_imagefile_command  + "\n")
                    # print better_imagefile_name # FOR DEBUGGING
                    rename_imagefile_handler = EasyProcess(
                        renaming_imagefile_command ).call()
                    print(renaming_imagefile_command + '\n') # for debugging








#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************
