# hexsplit

**Author:** *Shreya Seshadri*

## Overview

## Description of the Software

Hexsplit is an implementation of a simple proof-of-concept approach to detecting the presence of partial gene transfer (PGT) (i.e., horizontal transfer of a fragment of a gene) in a given gene family. hexsplit takes as input a multiple sequence alignment for the gene family under consideration, creates 2 sets of roughly equal tri-partitioned windows (regular and offset), computes ML trees and bootstrap replicates for each window, and compares these windows and sets to determine if that gene family has been affected by significant partial gene transfer. hexsplit can be used to easily identify gene families whose gene trees may have been impacted by the presence of significant partial gene transfer.

## Dependencies
Python 3
  - DendroPy
  - Scipy
  - Numpy
- RAxML 8.2.11 PThreads enabled

## Usage
hexsplit contains a directory named scripts and a wrapper file names integration_file.py. The scripts directory contains 3 python files used to create the regular and offset tri-parition windows sets and to execute the histogram intersection test. To run hexsplit, the user only needs to interact and run integration_file.py. 

An example of running integration_file.py may look like:
python integration_file.py -ff /path/to/sequence_alignment_file -rxml_loc /path/to/raxmlHPC-PTHREADS -fn name_of_folder_to_be_created -nbs 3 -nthds 6

Running integration_file.py will create a new directory (with a user given name) to store all created files including windows, ML trees, and bootstrap trees. 

### Parameters
* -msa, --multiple_sequence_alignment : Path to the multiple sequence alignment file to be tested.
* -rxml_loc, --raxml_location : Path to where RAxML Pthreads is stored on the user's local machine.
* -fn, --folder_name : User specified name to store created files (windows, ML and bootstrap trees).
* -m, --model : RAxML model to be used. Default: GTRCAT
* -nbs, --num_bootstrap : Number of bootstrap trees to be created. Default: 10
* -thresh, --threshold : Threshold used in histogram intersection test. Default: 0.5
* -nthds, --num_pthreads : Number of threads to be used. Default: 2
