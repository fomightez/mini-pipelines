# mini-pipelines
**A collection of scripts that chain together other scripts by preparing and then processing/transforming the data. A.K.A `sheperding scripts`, `script uniters`, `utility scripts`, `parent scripts`, `shepards`, `control scripts`, `chained scripts`, `linked scripts`,  `processors`, `conveyance scripts`, `scripted processing`, `mini-workflows`, `script managers`, `workflow faciliators`, `workflow aides`, `scripted workflows`, `scripted data handlers`, `daisy-chained scripts`, `connected scripts`, `multiple scripts chained together`.**&ast;  
  
The repository will probably be mainly Python scripts, but could include some shell/Bash ones too. The inaugral scripts that went into this repository were Python and used Python to control things at the command line level as well. In other words, from within Python I generated and executed commands to run as if on shell command line. 
  
&ast;In naming this repository, I based it on the responses of stevegt and Alastair Kerr as posted [here](https://www.biostars.org/p/17696/).


---



**Description of each script**

* sheperds_chr_thru_plot_expression_across_chromosomes.py  
  Uses the script [plot_expression_across_chromosomes.py](https://github.com/fomightez/sequencework/tree/master/plot_expression_across_chromosomes) to analyze the entire yeast genome and then all chromosomes for several samples. Producing images of the plots for all those. The version of this script new relies on the columns in the summary data given the script to match samples provided in the `USER ADJUSTABLE VALUES ` for this script. There is an associated script, generate_reports_for_genome_and_all_chromosomes_various_samples.py, here that takes the produced images and makes a report.
  
 * generate_reports_for_genome_and_all_chromosomes_various_samples.py  
  Uses the output from the script, sheperds_chr_thru_plot_expression_across_chromosomes.py, to make a summary report as a pdf. I run this script on PythonAnywhere, where they have the `ReportLab` module installed under Python 2.7.
