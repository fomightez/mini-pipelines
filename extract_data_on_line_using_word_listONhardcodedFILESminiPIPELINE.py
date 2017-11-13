#!/usr/bin/env python
# ADAPTED FROM extract_data_on_line_using_word_list.py by Wayne Decatur
# ver 0.1
#
#*******************************************************************************
# USES Python 2.7 but should be convertable via 2to3, see https://docs.python.org/3.0/library/2to3.html
#
# PURPOSE: ADAPTED FROM extract_data_on_line_using_word_list.py  to take two lists of gene names, combine them, and get data from 10 hardcoded files
# Hardcoding of the file nameas within the script, instead of running them from
# the shell was chosen so I didn't have to escape the file names with spaces.
#
#
#
#
#
# Dependencies beyond the mostly standard/built-in libraries/modules:
# None
#
#
#
# VERSION HISTORY:
# v.0.1. basic working version
#
#
#
#
#
# TO RUN:
# Example,
# Enter on the command line of your terminal, the line
#-----------------------------------
# python extract_data_on_line_using_word_listONhardcodedFILESminiPIPELINE.py
#-----------------------------------
#
#
#*******************************************************************************
#


#*******************************************************************************
##################################
#  USER ADJUSTABLE VALUES        #

##################################
#
#
gene_list_files = ["high_mfi_as_systematic.tsv","low_mfi_as_systematic.tsv"]


data_file_paths =[
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of Shafi 2016 RNA-Seq data with Salmon/totalPLUSori_mapped_salmon_output/toriWT_Rep2.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of Shafi 2016 RNA-Seq data with Salmon/totalPLUSori_mapped_salmon_output/toriWT_Rep3.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of Shafi 2016 RNA-Seq data with Salmon/totalPLUSori_mapped_salmon_output/toriMT_Rep2.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of Shafi 2016 RNA-Seq data with Salmon/totalPLUSori_mapped_salmon_output/toriMT_Rep3.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of April 2017 RNA-Seq data/mito_analysis/totalPLUSori_mapped_salmon_output/toriWT1.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of April 2017 RNA-Seq data/mito_analysis/totalPLUSori_mapped_salmon_output/toriWT2.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of April 2017 RNA-Seq data/mito_analysis/totalPLUSori_mapped_salmon_output/toriWT3.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of April 2017 RNA-Seq data/mito_analysis/totalPLUSori_mapped_salmon_output/toriMT1.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of April 2017 RNA-Seq data/mito_analysis/totalPLUSori_mapped_salmon_output/toriMT2.quant/quant.sf",
                "/Users/Wayne/Dropbox/impt informatics for lab work/high throughput NGS items/Analysis of April 2017 RNA-Seq data/mito_analysis/totalPLUSori_mapped_salmon_output/toriMT3.quant/quant.sf",
                ]

file_suffixes_for_save =[
                "totalWTREP2",
                "totalWTREP3",
                "totalMTREP2",
                "totalMTREP3",
                "mitoWT1",
                "mitoWT2",
                "mitoWT3",
                "mitoMT1",
                "mitoMT2",
                "mitoMT3",
                ]
#
#*******************************************************************************
#**********************END USER ADJUSTABLE VARIABLES****************************





















#*******************************************************************************
#*******************************************************************************
###DO NOT EDIT BELOW HERE - ENTER VALUES ABOVE###

import sys
import os
import argparse
import string


###---------------------------HELPER FUNCTIONS---------------------------------###


def generate_output_file_name(list_file_name,mid_suffix):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file name.

    Specific example
    ================
    Calling function with
        ("data_file.txt")
    returns
        "data_file_extracted.txt"
    '''
    main_part_of_name, file_extension = os.path.splitext(
        list_file_name,) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    return main_part_of_name[:8]+"_" + mid_suffix+ "_extracted.txt"


def generate_output_file(provided_text, list_file, indx):
    '''
    function takes text and saves it as a text file
    using the index provided to match suffix
    '''
    name_of_file_to_save = generate_output_file_name(list_file,file_suffixes_for_save[indx])
    data_file_stream = open(name_of_file_to_save , "w")
    data_file_stream.write(provided_text.rstrip('\r\n')) #rstrip to remove trailing newline
    # from http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python
    data_file_stream.close()
    sys.stderr.write( "\nExtracted lines ({0} total) saved as '{1}'.\n".format(len(provided_text.rstrip('\r\n').split('\n')), name_of_file_to_save))

def list2text(a_list):
    '''
    a function that takes a lists and makes a string where each item in list
    is on a new line
    '''
    return "\n".join(a_list)

###--------------------------END OF HELPER FUNCTIONS---------------------------###
###--------------------------END OF HELPER FUNCTIONS---------------------------###













'''
#*******************************************************************************
###-----------------for parsing command line arguments-----------------------###
parser = argparse.ArgumentParser(prog='extract_data_on_line_using_word_list.py',description="extract_data_on_line_using_word_list.py \
    takes two files. One file will be used as a list of words or names. That \
    list will be used to examine line by line the `data file` and lines \
    containing words/names from the list will be kept and placed in a resulting \
    file. It was originally intended to be used for lists of gene identifiers, \
    but works with any words or names, etc. **** Script by Wayne Decatur   \
    (fomightez @ github) ***")
parser.add_argument("list_file", help="Name of file containing list or words \
    or names to look for in lines of data file. REQUIRED.", type=argparse.FileType('r'), metavar="ListFile")
parser.add_argument("data_file", help="Name of file containing lines to scan \
    for the presence of the provided list of words or names. Only those lines \
    with those words or names will be kept for the outout file. REQUIRED.", type=argparse.FileType('r'), metavar="DataFile")
parser.add_argument("-l", "--lines",help=
    "add this flag to force individual lines to be used to read the words_list \
    and make the list to be compared to lines in the data file. This enables \
    the use of two-word names with punctuation, like `Mr. Smith`, or even phrases.",
    action="store_true")
parser.add_argument("-d", "--data_substring_suffices",help=
    "add this flag to allow substrings from the data lines to match contents\
    of the words_list. For example, when this flag is active `me` in the\
    words_list would allow for matches to lines containing the word `some`.",
    action="store_true")
parser.add_argument("-s", "--sensitive",help=
    "add this flag to force comparison of items to be case-sensitive (NOT \
    recommended). Default (recommended) is to make the comparisons independent \
    of character case in order make matching more robust, and not miss matches \
    when case use is inconsistent among the sources.",
    action="store_true")
#I would also like trigger help to display if no arguments provided because need at least one input file
if len(sys.argv)==1:    #from http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
list_file = args.list_file
data_file = args.data_file
use_lines = args.lines
case_sensitive = args.sensitive
data_substring_suffices = args.data_substring_suffices
'''
use_lines = False
case_sensitive = False
data_substring_suffices = False


###-----------------Actual Main portion of script---------------------------###


for each_list_file in gene_list_files:

    # Go through list file making a list of the words
    list_of_words=[]
    with open(each_list_file) as input_file_stream:
        for line in input_file_stream:
            line = line.strip() # don't want line endings so I can easily
            # work with later, hence the use of `.strip()`
            if use_lines:
                line_words = [line]
            else:
                line_words = [word.strip(string.punctuation) for word in line.split()] #tries
                # to address removing punctuation at end but not contractions in middle, 
                # based on Colonel Panic's answer at http://stackoverflow.com/questions/18135967/creating-a-list-of-every-word-from-a-text-file-without-spaces-punctuation
                # print(string.punctuation) yields `!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~`
            list_of_words.extend(line_words)






    # Warn about case issue.  
    if case_sensitive:
        sys.stderr.write( "\n***NOTICE***. Be aware using `--sensitive` option may result in missing matches if case use inconsistent in lists. ***NOTICE***\n")

    # Now go through each data file in `data_file_paths`, keeping lines that contain 
    # members of list_of_words and save each separately.

    for indx,file_path in enumerate(data_file_paths):
        lines_kept_list = []
        with open(file_path) as data_file:
            for line in data_file:
                line = line.strip() # don't want line endings so I can easily
                # work with later, hence the use of `.strip()`
                # Handle differently if `case_sensitive` option activated
                if case_sensitive:
                    if data_substring_suffices:
                        if any(word in line for word in list_of_words):
                            lines_kept_list.append(line)
                            # based on Lauritz V. Thaulow's answer at http://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python
                    else:
                        if any(word in line.split() for word in list_of_words):
                            lines_kept_list.append(line)
                            # based on Lauritz V. Thaulow's answer at http://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python
                else:
                    if data_substring_suffices:
                        if any(word.lower() in line.lower() for word in list_of_words):
                            lines_kept_list.append(line)
                        # expanded from Lauritz V. Thaulow's answer at http://stackoverflow.com/questions/6531482/how-to-check-if-a-string-contains-an-element-from-a-list-in-python
                    else:
                        if any(word.lower() in line.lower().split() for word in list_of_words):
                            lines_kept_list.append(line)


         
        # Save results and give feedback
        text_to_save = list2text(lines_kept_list)
        generate_output_file(text_to_save, each_list_file, indx)


 

#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************
