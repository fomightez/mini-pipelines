#!/usr/bin/env python
# shepherds_chr_thru_plot_expression_across_chromosomes.py by Wayne Decatur
# ver 0.1
#
#*******************************************************************************
# USES Python 2.7 but should be convertable via 2to3, see https://docs.python.org/3.0/library/2to3.html
#
# PURPOSE: This script is meant to be an accessory script for working with
# `plot_expression_across_chromosomes.py` when you want to generate plots for
# each chromosome individually for several combinations of data in same 
# summary data file.
#
# There is a separate script, called 
# generate_reports_for_genome_and_all_chromosomes_various_samples, to take the
# output images and combine them for a summary report.
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
# python shepherds_chr_thru_plot_expression_across_chromosomes.py
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
list_of_chr_names = '''
I
II
III
IV
V
VI
VII
VIII
IX
X
XI
XII
XIII
XIV
XV
XVI
'''  # this is for yeast
columns_to_use_in_third_position_in_columns = ["4","6","8"]

mutant_strains_list = ["P6","delUPF1","P6delUPF1"] # provide in sequence order 
# that matches position in `columns_to_use_in_third_position_in_columns`; these 
# will be used in the labels for y-axis

name_for_output_directory= "manhattan_imgs"
file_name_prefix_for_data = "genes_mean_TPM_info_wihoutP6A"
file_name_prefix_to_use_for_renaming = file_name_prefix_for_data + "_across_chr"
file_name_tag_to_use_for_moving = "_across_chr_"



# info from the script `plot_expression_across_chromosomes.py `
suffix_for_saving_result_in_plot_script =  "_across_chr.png"

# Originally I had tested advancing color by index value as enumerating
# list_of_chrs; however, while it works for first few chromosomes, some quirks
# like the fact genome plot includes `MT` near middle and that `chr IX` gets 
# plotted out of order because starts with `I` means index value won't always 
# match. Dictionary below is to allow user to specify things so it will match:
color_advance_by_chr_dict = {
    "I": 0,
    "II": 1,
    "III": 2,
    "IV": 3,
    "IX": 4,
    "V": 6,
    "VI": 7,
    "VII": 8,
    "VIII": 9,
    "X": 10,
    "XI": 11,
    "XII": 12,
    "XIII": 13,
    "XIV": 14,
    "XV": 15,
    "XVI": 16
}

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




def generate_more_descriptive_name(file_name,third_pos):
    '''
    Takes an expected file namd and another sting to return a new name based on 
    the original name, but distinguished by the "third_pos" string

    Specific examples
    =================
    Calling function with
        ("genes_mean_TPM_info_wihoutP6A_across_chr.png", "4")
    returns
        "col_4_genes_mean_TPM_info_wihoutP6A_across_chr.png"


    or
    Calling function with
        ("genes_mean_TPM_info_wihoutP6A_across_chr_III.png", "4")
    returns
        "col_4_genes_mean_TPM_info_wihoutP6A_across_chr_III.png"
        
    '''
    name_prefix = "col_"
    main_part_of_name, file_extension = os.path.splitext(
    file_name) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    return name_prefix + third_pos + "_" + main_part_of_name + file_extension



def generate_output_file_name_function_from_plot_across_chr_script(file_name, suffix,limit_to_chrs):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file
    name.

    It also indicates in resulting file name name specific chromsomes or 
    scaffolds if plotting was limited to those.

    Specific examples
    =================
    Calling function with
        ("data1.txt", "_across_chr.png")
    returns
        "data1_across_chr.png"
    
    if `limit_to_chrs = ["II","IV"]`,
    Calling function with
        ("data1.txt", "_across_chr.png")
    returns
        "data1_across_chr_II_IV.png"
    '''
    main_part_of_name, file_extension = os.path.splitext(
        file_name) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    if limit_to_chrs:
        main_part_of_suffix, suffix_file_extension = os.path.splitext(
        suffix)
        suffix = main_part_of_suffix + "_" + "_".join(
            limit_to_chrs) + suffix_file_extension 
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
parser = argparse.ArgumentParser(prog='shepherds_chr_thru_plot_expression_across_chromosomes.py',description="shepherds_chr_thru_plot_expression_across_chromosomes.py \
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


# Start by using the block of list_of_chr_names to make lists_of_chr
# combinations greater than pairings.
list_of_chrs = [x.strip() for x in list_of_chr_names.split("\n")]
# When I did `--commands_only` option for another script, I was seeing some empty ones and so added
# the next line to filter out those
list_of_chrs  = [x for x in list_of_chrs if x] # current best way to do filter empty strings according to http://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings

# preparation for commands
prefix_for_renaming_command = "mv "

# Make a large set of commands for each combination of data:
# First block of commands will be for running `plot_expression_across_chromosomes.py` on \
# all and then each chromosome in chromosome list for current combination of data
# and then a couple of commands at end to rename the new files for all chrs 
# and move them to a directory.

prefix_for_py_script_command = "python plot_expression_across_chromosomes.py edited_genes.gtf " + file_name_prefix_for_data + ".tsv --columns 1,2,"

for indx, third_pos in enumerate(columns_to_use_in_third_position_in_columns):

    py_script_command = prefix_for_py_script_command + third_pos + " --smooth --exp_desig "+ mutant_strains_list[indx]

    '''
    above line based on:
    python plot_expression_across_chromosomes.py edited_genes.gtf genes_mean_TPM_info_wihoutP6A.tsv --columns 1,2,4 --chrs IV,VIII,XII --smooth
    but want all chromosomes first, and so leaving out `--chrs`
    '''

    if just_output_commands_only:
        print (py_script_command)
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

    # need rename and move result
    #previously made the directory given above as `name_for_output_directory`
    # Now for the renaming command, I'll need to determine what file name that
    # last command would produce and then use that to rename and move.
    file_name_expected = generate_output_file_name_function_from_plot_across_chr_script(
        file_name_prefix_for_data + ".tsv", 
        suffix_for_saving_result_in_plot_script, None)
    # print file_name_expected # FOR DEBUGGING
    better_name = generate_more_descriptive_name(file_name_expected,third_pos)
    renaming_command = (prefix_for_renaming_command
        + file_name_expected + ' ' +name_for_output_directory+ "/" +  better_name)
    #print (renaming_command) ## FOR DEBUGGING ONLY

    if just_output_commands_only:
        print (renaming_command)
    else:
        sys.stderr.write(
        'RENAMING FILE JUST MADE TO BE MORE DESCRIPTIVE AND MOVING:\n'
        + renaming_command + "\n")
        rename_file  = EasyProcess(renaming_command).call()




    # plot for each chromosome and rename and move those
    for chr in list_of_chrs:
        py_script_command = (prefix_for_py_script_command + third_pos + " -chr "
            + chr +" --smooth  --exp_desig "+ mutant_strains_list[indx] + 
            " --advance_color "+ str(color_advance_by_chr_dict [chr]) )
        if just_output_commands_only:
            print (py_script_command)
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

        # need rename and move result
        #previously made the directory given above as `name_for_output_directory`
        # Now for the renaming command, I'll need to determine what file name that
        # last command would produce and then use that to rename and move.
        file_name_expected = generate_output_file_name_function_from_plot_across_chr_script(
            file_name_prefix_for_data + ".tsv", 
            suffix_for_saving_result_in_plot_script, [chr])
        # print file_name_expected # FOR DEBUGGING
        better_name = generate_more_descriptive_name(
            file_name_expected,third_pos)
        # print(better_name)  # FOR DEBUGGING
        renaming_command = (prefix_for_renaming_command
            + file_name_expected + ' ' +name_for_output_directory+ "/" +  better_name)
        #print (renaming_command) ## FOR DEBUGGING ONLY

        if just_output_commands_only:
            print (renaming_command)
        else:
            sys.stderr.write(
            'RENAMING FILE JUST MADE TO BE MORE DESCRIPTIVE AND MOVING:\n'
            + renaming_command + "\n")
            rename_file  = EasyProcess(renaming_command).call()

#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************
