#!/usr/bin/env python


# generate_reports_for_genome_and_all_chromosomes_various_samples.py by Wayne Decatur



#*******************************************************************************
# USES Python 2.7 but should be convertable via 2to3, see https://docs.python.org/3.0/library/2to3.html
# However, currently ReportLab isn't listed as being installed for Python 3 at
# PythonAnywhere.
#
# PURPOSE: Combines images in a report for different samples with plots for
# genome and individual chromosomes. Meant to work with output from script
# `sheperds_chr_thru_plot_expression_across_chromosomes.py`
#
#
#
#
#
# Dependencies beyond the mostly standard libraries/modules:
# ReportLab
#
#
#
# VERSION HISTORY:
# v.0.1. basic working version
#
#
#
# TO RUN:
# Example,
# Enter on the command line of your terminal, the line
#-----------------------------------
# python generate_reports_for_genome_and_all_chromosomes_various_samples.py
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
suffix_for_saving_result = "_manhattan_plots.pdf"


samples_involved = ["P6", "delUPF1", "P6delUPF1"] #must match the order each set of files handled

image_dir = "manhattan_imgs"


list_of_P6_files_names = '''
col_4_genes_mean_TPM_info_wihoutP6A_across_chr.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_I.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_II.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_III.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_IV.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_IX.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_V.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_VI.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_VII.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_VIII.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_X.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_XI.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_XII.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_XIII.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_XIV.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_XV.png
col_4_genes_mean_TPM_info_wihoutP6A_across_chr_XVI.png
'''  #pasted from bash `ls-1` command


list_of_delUPF1_files_names = '''
col_6_genes_mean_TPM_info_wihoutP6A_across_chr.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_I.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_II.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_III.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_IV.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_IX.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_V.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_VI.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_VII.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_VIII.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_X.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_XI.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_XII.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_XIII.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_XIV.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_XV.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_XVI.png
'''  #pasted from bash `ls-1` command or made by find and replace on `list_of_P6_files_names`

list_of_P6delUPF1_files_names = '''
col_8_genes_mean_TPM_info_wihoutP6A_across_chr.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_I.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_II.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_III.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_IV.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_IX.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_V.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_VI.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_VII.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_VIII.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_X.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_XI.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_XII.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_XIII.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_XIV.png
col_6_genes_mean_TPM_info_wihoutP6A_across_chr_XV.png
col_8_genes_mean_TPM_info_wihoutP6A_across_chr_XVI.png
'''  #pasted from bash `ls-1` command or made by find and replace on `list_of_P6_files_names`


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


def generate_output_file_name(sample, suffix):
    '''
    Takes a sample as an argument and returns string for the name of the
    output file based on the sample name.


    Specific example
    ================
    Calling function with
        ("S95", "_manhattan_plots.pdf")
    returns
        "S95_manhattan_plots.pdf"
    '''
    return sample + suffix




def list2text(a_list):
    '''
    a function that takes a lists and makes a string where each item in list
    is on a new line
    '''
    return "\n".join(a_list)

###--------------------------END OF HELPER FUNCTIONS---------------------------###
###--------------------------END OF HELPER FUNCTIONS---------------------------###














#*******************************************************************************
###-----------------for parsing command line arguments-----------------------###
parser = argparse.ArgumentParser(prog='generate_reports_for_genome_and_all_chromosomes_various_samples.py ',
    description="generate_reports_for_genome_and_all_chromosomes_various_samples.py blah blah blah.        \
    **** Script by Wayne Decatur   \
    (fomightez @ github) ***")

#parser.add_argument("List", help="Name of file containing the list to check over for redundants. REQUIRED.", type=argparse.FileType('r'), metavar="FILE")

#I would also like trigger help to display if no arguments provided
if len(sys.argv)==1:    #from http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()













###-----------------Actual Main portion of script---------------------------###

# Start by using the block of file names to make list_of_P6_files
list_of_P6_files = [x.strip() for x in list_of_P6_files_names.split("\n")]
# When I did `--commands_only` option for another script, I was seeing some empty ones and so added
# the next line to filter out those. Plus prepend directory to file name.
list_of_P6_files = [image_dir + "/"+ x for x in list_of_P6_files if x] # current best way to do filter empty strings according to http://stackoverflow.com/questions/3845423/remove-empty-strings-from-a-list-of-strings

#same for other samples
list_of_delUPF1_files = [x.strip() for x in list_of_delUPF1_files_names.split("\n")]
list_of_delUPF1_files = [image_dir + "/"+ x for x in list_of_delUPF1_files if x] 

list_of_P6delUPF1_files = [x.strip() for x in list_of_P6delUPF1_files_names.split("\n")]
list_of_P6delUPF1_files = [image_dir + "/"+ x for x in list_of_P6delUPF1_files if x] 


sample_files_list = [list_of_P6_files, list_of_delUPF1_files , list_of_P6delUPF1_files]

for index,sample in enumerate(samples_involved):

    # make report with two images per page in ReportLab
    output_file_name = generate_output_file_name(sample, suffix_for_saving_result)
    c = canvas.Canvas(output_file_name)

    for page_number,f in enumerate(sample_files_list[index]):
        if page_number == 0:
            continue
        c.translate(inch*0.5,inch*0.75)
        c.drawString(0,0,"Page "+str(page_number))
        c.setFillColorRGB(1,1,1) # fill canvas white
        c.drawImage(f, 0,12,533,367)
        c.translate(0,inch*5.5)
        c.drawImage(sample_files_list[index][0], 0,0,533,367)
        c.showPage() #trigger next canvas commands to concern a new page


    # save data and give feedback
    c.save()
    sys.stderr.write("\n\nOutput file named '" + output_file_name +"' created.\n")




#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************
