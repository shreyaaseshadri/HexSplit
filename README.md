# hexsplit

## Overview and Description of Software

Hexsplit is an implementation of a simple proof-of-concept approach to detecting the presence of partial gene transfer (PGT) (i.e., horizontal transfer of a fragment of a gene) in a given gene family. hexsplit takes as input a multiple sequence alignment for the gene family under consideration, creates 2 sets of roughly equal tri-partitioned windows (regular and offset), computes maximum likelihood (ML) trees and bootstrap replicates for each window, and compares these windows and sets through statistical analysis to determine if that gene family has been affected by significant partial gene transfer. hexsplit can be used to easily identify gene families whose gene trees may have been impacted by the presence of significant partial gene transfer.

## Dependencies
- Python 3
  - DendroPy
  - Scipy
  - Numpy
- RAxML 8.2.11 (Sequential Version)

## Usage

### Contents
hexsplit contains 
  1. Scripts - a directory containing 3 python files used to create the regular tripartition windows, the offset tripartition windows, and run the final histogram intersection test
  2. integration_file.py - a wrapper script. This is the file the user interacts with.

hexsplit will create new directories and sub-directories to store the tripartion and RAxML files and output the final result in the terminal. The user must specify the name of the main directory. An example is provided in the Example section of this document. 

### Input
hexsplit is designed to take in a gene family multiple sequence alignment as input. We have provided 4 fasta files as examples of appropriate inputs. More information can be found in the Provided Testing Samples of this document. 

hexsplit requires the location of RAxML on your machine. Please download RAxML before downloading hexsplit. More information on downloading and compiling RAxML can be found here: https://cme.h-its.org/exelixis/resource/download/NewManual.pdf . RAxML's github repo can be found here: https://github.com/stamatak/standard-RAxML . Note: hexsplit is designed for the sequential version of RAxML. 

Below is a list of parameters hexsplit supports. Please note the required parameters and pass in complete paths to files: 
  1. Multiple Sequence Alignment
  2. RAxML location
  3. Name of Main Directory/Folder to be created

### Parameters
* -msa, --multiple_sequence_alignment : Path to the multiple sequence alignment file to be tested.
* -rxml_loc, --raxml_location : Path to where RAxML is stored on the user's local machine.
* -fn, --folder_name : User specified name to store created files (tripartitions, maximum likelihood and bootstrap trees).
* -m, --model : RAxML model to be used. Default: GTRCAT
* -nbs, --num_bootstrap : Number of bootstrap trees to be created. Default: 10
* -thresh, --threshold : Threshold used in histogram intersection test. Default: 0.5

### Provided Testing Samples
We have provided 4 sample fasta files.
  1. noPGT_large.fa - No PGT, contains 229 gene sequences
  2. noPGT_short.fa - No PGT, contains 15 gene sequences (a subset of noPGT_large.fa)
  3. PGT_large.fa - PGT, contains 229 gene sequences
  4. PGT_short.fa - PGT, contains 9 gene sequences (a subset of PGT_large.fa)

These files were each tested with the GTRCAT model, 100 bootstrap trees, and a threshold value of 0.5 on a 2020 Macbook Pro M1. The short files ran in ~2 minutes while the larger files took between 2 and 4 hours to complete. The number of bootstraps plays a key role in runtime. 

### Running Software
  1. Download the zip
  2. cd into the hexsplit directory (cd hexsplit)
  3. Ensure your multiple sequence alignment is accessible
  4. Run wrapper script from the terminal - an example is provided below

#### Example

##### Input: 
python3 integration_file.py -msa /Users/shrey/Documents/test_files/noPGT_short.fa -rxml_loc /Users/shrey/standard-RAxML/raxmlHPC-AVX -fn noPGT_short -m GTRGAMMA -nbs 100 -thresh 0.5

##### Output: 
RAxML Gene Trees Successfully Created
100 RAxML Bootstrap Trees Successfully Created

Regular windows 
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2
Regular windows histogram intersection test result: 0.59

Offset windows 
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2
Offset windows histogram intersection test result 0.83

PGT not detected

##### Meaning: 
RAxML Gene Trees Successfully Created - update for the user
100 RAxML Bootstrap Trees Successfully Created - update for the user

Regular windows - below information is for regular tripartition windows
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2 - pairwise RF scores between ML trees generated from the 3 partitions \n
Regular windows histogram intersection test result: 0.59 - result of the statistical analysis, a value less than the threshold indicates the presence of PGT

Offset windows - below information is for tripartition windows created with an offset
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2 - pairwise RF scores between ML trees generated from the 3 partitions
Offset windows histogram intersection test result 0.83 - result of the statistical analysis, a value less than the threshold indicates the presence of PGT

PGT not detected - final result

