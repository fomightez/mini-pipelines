# mini-pipelines
**A collection of scripts that chain together other scripts by preparing and then processing/transforming the data. A.K.A `shepherding scripts`, `script uniters`, `utility scripts`, `parent scripts`, `shepherds`, `control scripts`, `chained scripts`, `linked scripts`,  `processors`, `conveyance scripts`, `scripted processing`, `mini-workflows`, `script managers`, `workflow faciliators`, `workflow aides`, `scripted workflows`, `scripted data handlers`, `daisy-chained scripts`, `connected scripts`, `multiple scripts chained together`.**&ast;  
  
The repository will probably be mainly Python scripts, but could include some shell/Bash ones too. The inaugral scripts that went into this repository were Python and used Python to control things at the command line level as well. In other words, from within Python I generated and executed commands to run as if on shell command line. 

As written, many of these rely on the `EasyProcess` module that is layered on the `subprocess` module and is found pre-installed at [PythonAnywhere](http://www.pythonanywhere.com). I suggest using them or edited versions there for the easiest experience.
  
&ast;In naming this repository, I based it on the responses of stevegt and Alastair Kerr as posted [here](https://www.biostars.org/p/17696/).

**Update: in some ways, recent work in Jupyter notebooks gluing together different scripts is reminiscent of some of what is accomplished in parts of these mini-pipelines, particularly mixing shell and python tasks, and is a useful alternative, see [here](https://github.com/fomightez/sequencework) and [here](https://github.com/fomightez/structureework) for links to just some nucleic acid analyses and structure/function analyses examples, respectively.**


**Update: Keep in mind that Python's `functools.partial()` may be useful when dealing with differing argument number needs at different points in such a pipeline, see [here](https://stackoverflow.com/a/15331967/8508004).**

---



**Description of each script**

* shepherds_all_list_combinations_thru_find_overlap_in_list.py 
  An accessory script for working with the script [find_overlap_in_lists.py](https://github.com/fomightez/text_mining) when you have several lists and want to find the overlap in all the combinations.
  
* shepherds_many_lists_thru_identify_duplicates_in_a_list.py  
  title speaks for now, until I fix this description
 
* shepherds_all_list_combinations_thru_find_overlap_in_lists_and_sys_name_to_std.py  
  title speaks for now, until I fix this description
  
* shehperds_all_list_combinations_thru_find_overlap_in_lists_with_Venn_and_sys_name_to_std.py  
  title speaks for now, until I fix this description
  
* shepherds_many_lists_thru_identify_duplicates_in_a_list_and_sys_name_to_std.py  
  title speaks for now, until I fix this description

* shepherds_chr_thru_plot_expression_across_chromosomes.py  
  Uses the script [plot_expression_across_chromosomes.py](https://github.com/fomightez/sequencework/tree/master/plot_expression_across_chromosomes) to analyze the entire yeast genome and then all chromosomes for several samples. Producing images of the plots for all those. The version of this script new relies on the columns in the summary data given the script to match samples provided in the `USER ADJUSTABLE VALUES ` for this script. There is an associated script, `generate_reports_for_genome_and_all_chromosomes_various_samples.py`, here that takes the produced images and makes a report.
  
 * generate_reports_for_genome_and_all_chromosomes_various_samples.py  
  Uses the output from the script, shepherds_chr_thru_plot_expression_across_chromosomes.py, to make a summary report as a pdf. I run this script on [PythonAnywhere](http://www.pythonanywhere.com), where they have the `ReportLab` module installed under Python 2.7.
  
 * shepherds_read_starts_at_start_of_origins_thru_to_plotting.py  
  **TBD fully; example here does last steps to produce plot.** Utilizes the `--export_data` option to run `plot_coverage_and_starts.py` in an automated manner and plot the starts in a subregion of the data using the script `plot_panel_bar_plots_with_fit.py`. An example of what it produces is shown [here](https://github.com/fomightez/general_scripted_plotting#plot_panel_bar_plots_with_fitpy) where the asscoiated script is described. The associated script `plot_panel_bar_plots_with_fit.py` is found [here](https://github.com/fomightez/general_scripted_plotting), as it is general and not specific to read data; it might be placed in the directory with `shepherds_read_starts_at_start_of_origins_thru_to_plotting.py  `.
  
  * extract_data_on_line_using_word_listONhardcodedFILESminiPIPELINE.py  
    Adaptation of [`extract_data_on_line_using_word_list.py` from my text-mining repo](https://github.com/fomightez/text_mining) to use two different word lists to extract two sets of data out of each of several data files as a mini-pipeline. Everything is hard-coded into the script as a quicker route to getting the data without regard to generalizing the script. (**Of course, that would be useful if I had time or more need for this later**; for now this script serves as a good guide to how a quicker route via a mini-pipeline can be achieved hard-coding file references.) The choice to hard-code the file paths in instead of providing them on the command line as a call also obviated the need to escape the spaces in the file paths since I had copied them from Finder on the Mac and had included those. (Note about adapting further: I had occasion to use this script with DESeq2-generated output, and I found changing the last conditional from `if any(word.lower() in line.lower().split() for word in list_of_words):` to `if any(word.lower() in line.lower().split('"') for word in list_of_words):` was necessary because DESeq2 has the gene names flanked by quotes.)



Tangentially Related
--------------------

Approaches even more "structured" than my mini-pipelines or MAKEFILES or Bash scripts, some REAL pipeline options I have seen for when I outgrow shell scripts and using subprocess/sh/pybash:

 * [snakemake](https://github.com/ctb/2019-snakemake-ucdavis/blob/master/tutorial.md) - even makes schematic directed acyclic graphs (DAG) of your workflow, see [here](https://snakemake.readthedocs.io/en/stable/tutorial/basics.html)  
 (also see [nbpipeline - Snakemake-like pipelines for Jupyter Notebooks, producing interactive pipeline reports](https://github.com/krassowski/nbpipeline))

 * Bioinformatics pipelineing option - NExtFlow and Common Workflow Language. See [here](https://twitter.com/pathogenomenick/status/931444079992373248) "This GUI is for connecting command line tools into workflows. It generates CWL workflow descriptions that are human readable, yes." and [here](https://twitter.com/biocrusoe/status/931447928513851394) and [here](https://twitter.com/biocrusoe/status/888703760679272450) for help and discussion.
 
 * [FlowCraft](https://flowcraft.readthedocs.io/en/latest/getting_started/overview.html) is an assembler of pipelines written in nextflow for analyses of genomic data. The premisse is simple: `Software are container blocks → Build your lego-like pipeline → Execute it (almost) anywhere.`
 
 * The Broad Institute's [Workflow Description Language( WDL) User Guide](https://software.broadinstitute.org/wdl/documentation/)
 
 * see [here](http://blog.booleanbiotech.com/nextflow-snakemake-reflow.html) for some comparison in 2019 of several of the above items.
 
 * Carpentries page on [Automation and Make](https://swcarpentry.github.io/make-novice/)
 >"Make is used to compile source code into executable programs or libraries, but Make can also be used to:  
run analysis scripts on raw data files to get data files that summarize the raw data;  
run visualization scripts on data files to produce plots; and to  
parse and combine text files and plots to create papers."
 
 * [Luigi](https://github.com/spotify/luigi)- Luigi is a Python (2.7, 3.3, 3.4, 3.5, 3.6) package that helps you build complex pipelines of batch jobs. It handles dependency resolution, workflow management, visualization, handling failures, command line integration, and much more. Looks like it is what Spotify uses.

* [Tibanna: open-source software for automated execution of bioinformatics pipelines on Amazon Web Services (AWS)](https://github.com/4dn-dcic/tibanna), article about it [here](https://www.ncbi.nlm.nih.gov/pubmed/31077294)
  
* [snakepipes](https://academic.oup.com/bioinformatics/advance-article/doi/10.1093/bioinformatics/btz436/5499080): facilitating flexible, scalable and integrative epigenomic analysis   (July 2019)
code https://github.com/maxplanck-ie/snakepipes  
docs https://snakepipes.readthedocs.io/en/latest/ 
>"Due to the rapidly increasing scale and diversity of epigenomic data, modular and scalable analysis workflows are of wide interest. Here we present snakePipes, a workflow package for processing and downstream analysis of data from common epigenomic assays: ChIP-seq, RNA-seq, Bisulfite-seq, ATAC-seq, Hi-C and single-cell RNA-seq. "

* [Bioinformatics Pipeline using JUDI: Just Do It](https://www.biorxiv.org/content/10.1101/611764v1) (July 2019)
>"We developed JUDI on top of a Python based WMS, DoIt, for a systematic handling of pipeline parameter settings based on the principles of DBMS that simplifies plug-and-play scripting. The effectiveness of JUDI is demonstrated in a pipeline for analyzing large scale HT-SELEX data for transcription factor and DNA binding where JUDI reduces scripting by a factor of five.
 
