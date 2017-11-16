#!/usr/bin/env python
# -*- coding: utf-8 -*-


# shepherds_read_starts_at_start_of_origins_thru_to_plotting.py by Wayne Decatur
__author__ = "Wayne Decatur" #fomightez on GitHub
__version__ = "0.0.1"
__license__ = "MIT"


# ****WORKS "AS-IS" BY PASTING INTO A JUPYTER NOTEBOOK CELL WHEN 
# `plot_panel_bar_plots_with_fit.py` UPLOADED TO THE HOST SERVER.****
# (Uncomment the last line, i.e., `plt.show()` for plot to show up in the notebook.)

#*******************************************************************************
# USES Python 2.7 but should be convertable via 2to3, see https://docs.python.org/3.0/library/2to3.html
#
# PURPOSE: Work in progress script to shepherds read_starts at start of origins
# through to plotting using `plot_panel_bar_plots_with_fit.py`
#
#
#
#
#
# Dependencies beyond the mostly standard libraries/modules:
# `plot_panel_bar_plots_with_fit.py` needs to be in the same directory
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
#----------------------------------------------------
# python shepherds_read_starts_at_start_of_origins_thru_to_plotting.py
#-----------------------------------------------------
#
#
#*******************************************************************************
#


#*******************************************************************************
##################################
#  USER ADJUSTABLE VALUES        #

##################################
#
output_file_name = "stacked_plot_active_promoters_for_wt.png"

#starts_data parts
ori3_wt1_starts_per_position = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 5, 8, 16, 3, 10, 2, 16, 5, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 4, 3, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 1, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 2, 0, 2, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 5, 8, 1, 3, 1, 1, 0, 0, 0, 0, 1, 14, 16, 20, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0]
ori2_wt1_starts_per_position = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 3, 1, 11, 2, 0, 0, 0, 3, 4, 0, 0, 0, 5, 0, 2, 0, 1, 0, 2, 8, 67, 38, 26, 5, 0, 0, 8, 13, 39, 3, 32, 6, 46, 17,
            12, 1, 1, 1, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 6, 2, 1, 1, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 3, 0, 1, 0, 0, 0, 0, 0, 1, 2, 2, 0, 1, 0, 2, 2, 0, 0, 0, 0, 0, 1, 0, 3, 0, 1, 
            1, 42, 16, 4, 1, 0, 0, 0, 0, 0, 1, 0, 1, 2, 2, 0, 0, 2, 0, 0, 1, 0, 0, 2, 1, 1, 1, 1, 8, 1, 6, 1, 1, 25, 2, 9, 7, 2, 2, 1, 0, 0, 4, 44, 55, 93, 6, 9, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0]
ori5_wt1_starts_per_position = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 2, 0, 0, 1, 1, 4, 10, 16, 27, 9, 17, 1, 12, 6, 10, 5, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 4, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 2, 1, 0, 1, 2, 0, 0, 0, 4, 1, 2, 1, 0, 0, 0, 0, 4, 3, 1, 0, 2, 1, 0, 3, 1, 0, 0, 0,
            0, 1, 0, 1, 1, 0, 3, 0, 0, 2, 2, 0, 0, 0, 1, 3, 2, 1, 0, 0, 0, 8, 2, 0, 0, 0, 4, 1, 7, 0, 1, 0, 0, 9, 5, 1, 1, 0, 2, 0, 1, 9, 5, 2, 1, 0, 9, 0, 1, 0, 0, 0, 1, 1,
            0, 1, 1, 0, 2, 2, 0, 2, 1, 0, 1, 1, 2, 0, 4, 1, 1, 11, 1, 4, 6, 1, 1, 2, 1, 1, 1, 22, 21, 34, 4, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1]
ori3_wt2_starts_per_position = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 11, 4, 18, 1, 7, 2, 9, 3, 5, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 2, 1, 0, 9, 1, 2, 5, 0, 0, 0, 0, 0, 0, 9, 5, 22, 1, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
            0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
ori2_wt2_starts_per_position = [0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 1, 12, 1, 0, 1, 0, 5, 2, 2, 0, 0, 5, 1, 0, 0, 0, 0, 3, 5, 48, 30, 15, 3, 2, 3, 16, 14, 26, 4, 29, 5, 34, 9,
            5, 3, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 0, 4, 2, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 5,
            23, 9, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 0, 0, 1, 2, 0, 4, 0, 0, 2, 1, 1, 0, 4, 2, 1, 20, 1, 6, 11, 0, 1, 0, 0, 0, 0, 42, 43, 88, 3, 2, 1, 1, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
ori5_wt2_starts_per_position = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 5, 2, 0, 0, 0, 0, 0, 0, 1, 4, 10, 11, 24, 11, 18, 0, 20, 5, 7, 5, 0, 0, 1, 0, 0, 0, 1, 0, 4, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 5, 2, 0, 3, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2, 1, 0, 1, 0, 1, 3, 2, 0, 0, 3, 1, 0, 2, 1, 0, 1, 2,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 4, 1, 0, 0, 0, 1, 2, 2, 0, 0, 2, 0, 5, 4, 0, 2, 3, 2, 1, 1, 9, 1, 1, 2, 2, 4, 0, 0, 3, 0, 0, 1, 0,
            0, 0, 1, 1, 3, 0, 1, 1, 2, 0, 0, 1, 0, 0, 1, 0, 0, 16, 0, 7, 1, 0, 2, 0, 1, 0, 2, 15, 19, 46, 2, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ori3_wt3_starts_per_position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 3, 8, 8, 17, 4, 15, 2, 14, 8, 5, 1, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 2, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 3, 1, 0, 0, 0, 0, 0, 0,
            0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 4, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0,
            0, 0, 1, 2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 2, 0, 1, 9, 0, 1, 2, 0, 2, 0, 2, 0, 1, 9, 19, 34, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 3, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 1, 0]
ori2_wt3_starts_per_position = [0, 0, 0, 0, 0, 2, 3, 1, 0, 0, 1, 0, 9, 3, 0, 2, 1, 1, 1, 0, 2, 0, 4, 0, 1, 0, 1, 1, 2, 4, 55, 33, 23, 1, 2, 4, 13, 21, 29, 3, 46, 6, 32, 7,
            11, 4, 0, 0, 0, 4, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 2, 3, 1, 2, 0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 2, 0, 1, 0, 2, 1, 1, 0, 0, 0, 1, 2,
            35, 13, 2, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 3, 0, 1, 1, 2, 0, 2, 24, 1, 7, 5, 1, 0, 1, 3, 0, 3, 43, 44, 104, 4, 12, 1, 2, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
ori5_wt3_starts_per_position = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 1, 0, 1, 2, 11, 14, 38, 13, 27, 1, 22, 8, 14, 4, 2, 1, 0, 2, 0, 0, 0, 0, 1, 1, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 3, 2, 0, 4, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 
            0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 3, 1, 1, 2, 0, 0, 0, 1, 4, 5, 0, 0, 6, 0, 0, 2, 0, 0, 0, 
            0, 0, 1, 0, 1, 3, 2, 0, 0, 0, 0, 2, 3, 0, 1, 2, 1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 5, 2, 4, 0, 1, 0, 0, 6, 5, 1, 0, 0, 0, 1, 5, 13, 3, 1, 0, 0, 5, 1, 1, 2, 2, 1, 0,
            1, 0, 2, 1, 3, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 9, 0, 1, 19, 1, 9, 6, 0, 1, 1, 1, 0, 0, 23, 14, 62, 2, 2, 1, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0]
            
#starts_data_parts pieced together in order to match planned plot
wt_starts_data = [
                ori2_wt1_starts_per_position,
                ori2_wt2_starts_per_position,
                ori2_wt3_starts_per_position,
                ori3_wt1_starts_per_position,
                ori3_wt2_starts_per_position,
                ori3_wt3_starts_per_position,
                ori5_wt1_starts_per_position,
                ori5_wt2_starts_per_position,
                ori5_wt3_starts_per_position
                ]

distance_from_5prime_end_to_plot = 60  # set number of positions total to plot,
# starting from 5'end of promoter. First base at 5'end would be `1`, and so on.

bar_width = 1/1.023

title_prefix = " " #  

title_suffix = "  "

plot_style = "default" #try also `seaborn, `ggplot`,`default`, `bmh` or 
# `grayscale`; see others illustrated at
#  https://matplotlib.org/examples/style_sheets/style_sheets_reference.html


my_data_labels=["WT rep1","WT rep2","WT rep3"]
my_label_and_bar_colors =[(1,0,0,0.99)] 
# Better list of `my_label_and_bar_colors` made by getting some good colors and 
# then pasting in the code below into tmpnb.org to get the basic list to print 
# out and then pasted the list in below and modified the alpha and more.
'''
# Good colors: #516aa0, #e99650 #7ab36f; 
# RGB versions: (81/255.0,106/255.0,160/255.0),(233/255.0,150/255.0,80/255.0),(122/255.0,179/255.0,111/255.0)
import itertools #use based on https://stackoverflow.com/questions/34007106/how-do-you-create-a-list-of-repeated-tuples-in-python
n = 3
basic_list_of_RGBA = list(itertools.repeat((81/255.0,106/255.0,160/255.0,0.95), n)) + list(itertools.repeat((233/255.0,150/255.0,80/255.0,0.95), n)) + list(itertools.repeat((122/255.0,179/255.0,111/255.0,0.95), n))
basic_list_of_RGBA
'''
'''
# Another possible set of colors: (this one adapted from 3j9vBIOLstate3withOPM like found beyond option 1opaque with another gray SURFACE fancy.png)
# Good colors: settingsbluepurple: [0.286274509804, 0.254901960784, 0.439215686275], deepblue: (0.25, 0.25, 0.64999997615814209),settingsdarkpurpleblue: [0.254901960784, 0.258823529412, 0.439215686275], settingsblue: [0.549019607843, 0.56862745098, 0.937254901961] (`deepblue` is one of Pymol's default colors)
# for three: want settingsdarkpurpleblue, deepblue, settingsblue
import itertools #use based on https://stackoverflow.com/questions/34007106/how-do-you-create-a-list-of-repeated-tuples-in-python
n = 3
basic_list_of_RGBA = list(itertools.repeat((0.254901960784, 0.258823529412, 0.439215686275, 0.95), n)) + list(itertools.repeat((0.25, 0.25, 0.64999997615814209, 0.95), n)) + list(itertools.repeat((0.549019607843, 0.56862745098, 0.937254901961, 0.95), n))
basic_list_of_RGBA
'''

#Option 2
my_label_and_bar_colors = [
                        (0.3176470588235294, 0.41568627450980394, 0.6274509803921569, 0.95),
                        (0.3176470588235294, 0.41568627450980394, 0.6274509803921569, 0.95),
                        (0.3176470588235294, 0.41568627450980394, 0.6274509803921569, 0.95),
                        (0.9137254901960784, 0.5882352941176471, 0.3137254901960784, 0.95),
                        (0.9137254901960784, 0.5882352941176471, 0.3137254901960784, 0.95),
                        (0.9137254901960784, 0.5882352941176471, 0.3137254901960784, 0.95),
                        (0.47843137254901963, 0.7019607843137254, 0.43529411764705883, 0.95),
                        (0.47843137254901963, 0.7019607843137254, 0.43529411764705883, 0.95),
                        (0.47843137254901963, 0.7019607843137254, 0.43529411764705883, 0.95)
                        ]
#Option 1
my_label_and_bar_colors = [
                        (0.254901960784, 0.258823529412, 0.439215686275, 0.95),
                        (0.254901960784, 0.258823529412, 0.439215686275, 0.95),
                        (0.254901960784, 0.258823529412, 0.439215686275, 0.95),
                        (0.25, 0.25, 0.6499999761581421, 0.95),
                        (0.25, 0.25, 0.6499999761581421, 0.95),
                        (0.25, 0.25, 0.6499999761581421, 0.95),
                        (0.549019607843, 0.56862745098, 0.937254901961, 0.99),
                        (0.549019607843, 0.56862745098, 0.937254901961, 0.99),
                        (0.549019607843, 0.56862745098, 0.937254901961, 0.99),
                        ]

my_bar_alphas = [0.45]
my_label_alphas = [0.9,0.9,0.9,0.9,0.9,0.9,1.0,1.0,1.0]
shared_x_label = "distance from end"
shared_y_label = "Count"
first_set_of_data_at_bottom = True
lines_around_bars = False
group_label_subplots = [3,6,9] # list of numbers indicating for which subplots to 
# place labels for grouped subsets. Enter these as normal values, for instance 
#`1` for the first subplot and `3` for the third, etc.. The order of the list
# does not really matter as long as the corresponding text to be used for the
# subplot is in the same order in `group_label_subplots_str`.

group_label_subplots_str = ["GRP1","GRP2","GRP3"] #the text for the group labels
# specified by `group_label_subplots`. This needs to have the same 
# number of elements as `group_label_subplots` and match the order provided in
# `group_label_subplots`.

# To match Option 2
group_label_color_list =  [
                        (0.3176470588235294, 0.41568627450980394, 0.6274509803921569, 1.0),
                        (0.9137254901960784, 0.5882352941176471, 0.3137254901960784, 1.0),
                        (0.47843137254901963, 0.7019607843137254, 0.43529411764705883, 1.0),
                        ] 
# To match Option 1
group_label_color_list =  [
                        (0.254901960784, 0.258823529412, 0.439215686275, 1.0),
                        (0.25, 0.25, 0.6499999761581421, 1.0),
                        (0.549019607843, 0.56862745098, 0.937254901961, 1.0),
                        ] 
group_label_y_posns = [25.0,8.0,25.0]  #list of coordinate numbers for postioning
# in the y dimension text for group labels; list gets cycled if not at least  
# same size as `group_label_subplots`. Had to be added as a list and not a  
# single value because with real data I was seeing some group labels a little 
# different relative the x-axis, probably due to the x-axes being slightly 
# different.

group_label_fontsize = 15.0

curve_fit_or_smoother = "kr"  # options so far are 'gd' for 'Gaussian 
# distribution', 'ma' for 'moving average', 'sgf' for 'Savitzky Golay Filtering', 
# 'lowess', or 'kr' for 'kernel regression'. Or `None`, without quotes





#
#*******************************************************************************
#**********************END USER ADJUSTABLE VARIABLES****************************





























#*******************************************************************************
#*******************************************************************************
###DO NOT EDIT BELOW HERE - ENTER VALUES ABOVE###

import sys
import os
import argparse
import logging
import numpy as np
# USE NEXT TWO LINES IF NOT USING PYTHONANYWHERE, for when using a Jupyter notebooks, for example
import matplotlib
from matplotlib import pyplot as plt
'''# USE NEXT THREE LINES WHEN RUNNING ON PYTHONANYWHERE
import matplotlib # in order to use `matplotlib.use('Agg')`, need this first, see source of next line
matplotlib.use('Agg') # Force matplotlib to not use any Xwindows backend for running on PythonAnywhere. # from https://stackoverflow.com/questions/2801882/generating-a-png-with-matplotlib-when-display-is-undefined after searched error I was getting after upgrading matplolib in my Pythonanywhere account
import matplotlib.pyplot as plt'''

#DEBUG CONTROL
#comment line below to turn off debug print statements
#logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

###---------------------------HELPER FUNCTIONS---------------------------------###


def generate_output_file_name(file_name, suffix):
    '''
    Takes a file name as an argument and returns string for the name of the
    output file. The generated name is based on the original file
    name.

    It also notes in name specific chromsomes or scaffolds if plotting was 
    limited to those.

    Specific example
    ================
    Calling function with
        ("data1.txt", "_plot.png")
    returns
        "data1_plot.png"
    '''
    main_part_of_name, file_extension = os.path.splitext(
        file_name) #from http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
    if large_size:
        suffix =  suffix .replace(".png", "LARGE.png")
    return main_part_of_name + suffix




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
parser = argparse.ArgumentParser(prog='shepherds_read_starts_at_start_of_origins_thru_to_plotting.py',
    description="shepherds_read_starts_at_start_of_origins_thru_to_plotting.py \
    **** Script by Wayne Decatur   \
    (fomightez @ github) ***")

#parser.add_argument("tsv_file", help="Name of file containing the tab-separated data from the command `samtools depth -a -r <chrom><start>-<end> INPUT.bam > output.coverage`. REQUIRED.", type=argparse.FileType('r'), metavar="COVERAGE")
#parser.add_argument("-rev", "--reverse_orientation", help="Plot left to right to correspond to 5'-> 3' direction on reverse strand.",action="store_true")
'''
parser.add_argument('-lim', '--limit', action='store', type=int, metavar="INT",
    help="**FOR ADVANCED USE.*** Allows for controlling the upper end of scale \
    for y-axis. Should only be needed when extremes of values in one plot might\
    not match a plot for a related but different sample. Put the upper limit\
    integer after the flag, such as `--limit 82`.") '''
# parser.add_argument("-exp_d", "--export_data", help="Export the data as CSV printed to the console as stdout; use a redirect in a shell command to send the output to a file. If the `--reverse_orientation` option is utilized when the script is called then the data is exported as of the complementary strand 5'-end is the starting point. This is a utility feature added to enable easily passing the data mined by this script onto related scripts. This overrides the plotting action, i.e, in this mode no plot will be made, despite the name of the script.",action="store_true")

'''
#I would also like trigger help to display if no arguments provided because need at least one input file
if len(sys.argv)==1:    #from http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()
tsv_file = args.tsv_file
reverse_orientation = args.reverse_orientation
limit = args.limit
export_data = args.export_data
'''







###-----------------Actual Main portion of script---------------------------###

# process data to make ready for plotting.
# Subset based on number of positions starting at 5'-end of promoter to plot &
# add the x-axis values for each set of data so there is an x and y set for each 
# subplot.
data = []
for each_ydata in wt_starts_data:
    data.append(
        [list(range(1,distance_from_5prime_end_to_plot+1)),each_ydata[0:distance_from_5prime_end_to_plot]])
    # the `+1` in the range function on the above line enables the distance 
    # along x-axis to start at 1 but have the proper number of positions 
    # since the `stop` setting for Python's range enables generating numbers up  
    # to, but not including the `stop` number.



import plot_panel_bar_plots_with_fit as plt_panel_bar



## MAKE PLOT ####

fig, axes = plt_panel_bar.plot_data(
    data,
    labels=my_data_labels,
    colors=my_label_and_bar_colors, 
    bar_alphas=my_bar_alphas,
    label_alphas=my_label_alphas,
    shared_x_label=shared_x_label,
    shared_y_label=shared_y_label,
    group_label_subplots = group_label_subplots,
    group_label_subplots_str = group_label_subplots_str,
    group_label_color_list = group_label_color_list,
    group_label_y_posns = group_label_y_posns,
    group_label_fontsize=group_label_fontsize,
    curve_fit_or_smoother = curve_fit_or_smoother,
    )

### END OF PLOT MAKING #####


# save data and give feedback
#output_file_name = generate_output_file_name(tsv_file.name, suffix_for_saving_result)
sys.stderr.write("\n\nPlot image saved to: {}\n".format(output_file_name))
plt.savefig(output_file_name) 
# plt.savefig(output_file_name[:-4]+"LARGE.png", dpi = (1600))  # IF NEED LARGE. Based on http://scipy-cookbook.readthedocs.io/items/Matplotlib_AdjustingImageSize.html
# plt.savefig(output_file_name[:-4]+".pdf", orientation='landscape') # UNFORTUNATELY DOES NOT PRODUCE VECTOR GRAPHICS, unlike ReportLab's pdf output; USE SVG for that and the make PDF later.
#plt.savefig(output_file_name[:-4]+".svg", orientation='landscape') # FOR VECTOR GRAPHICS; useful if merging into Adobe Illustrator. Based on https://neuroscience.telenczuk.pl/?p=331 ; I think ReportLab also outputs SVG?


plt.show() # <=== Use that when placed in a Jupyter notebook







#*******************************************************************************
###-***********************END MAIN PORTION OF SCRIPT***********************-###
#*******************************************************************************
