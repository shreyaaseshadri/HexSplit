# HexSplit

## Overview and Description of Software

HexSplit implements a simple proof-of-concept approach to detecting the presence of partial gene transfer (PGT) (i.e., horizontal transfer of a fragment of a gene) in a given gene family. HexSplit takes as input a multiple sequence alignment for the gene family under consideration, creates 2 sets of roughly equal tri-partitioned windows (regular and offset), computes maximum likelihood (ML) trees and bootstrap replicates for each window, and compares these windows and sets through statistical analysis to determine if that gene family has been affected by significant partial gene transfer. HexSplit can be used to easily identify gene families whose gene trees may be impacted by the presence of significant partial gene transfer.

HexSplit builds upon the existing method [trippd](https://github.com/suz11001/Tripartition), which analyzes 3 windows to determine the presence of PGT. HexSplit improves upon the sensitivity of trippd, especially on gene famiilies affected by multiple PGTs and on gene families where PGT has impacted the middle portions of gene sequences. Further methodological details on HexSplit appear in the associated manuscript (see below for citation).


## Dependencies
- Python 3
  - DendroPy
  - Scipy
  - Numpy
- RAxML 8.2.11

## Usage

### Contents
HexSplit contains 
  1. Scripts - a directory containing 3 python files used to create the regular tripartition windows, the offset tripartition windows, and run the final histogram intersection test
  2. integration_file.py - a wrapper script. This is the file the user interacts with.

HexSplit will create new directories and sub-directories to store the tripartion and RAxML files and output the final result in the terminal. The user must specify the name of the main directory. An example is provided in the Example section of this document. 

### Input
The primary input for HexSplit is a multiple sequence alignment for the gene family being analyzed. We have provided 4 fasta files as examples of appropriate inputs. More information can be found in the Test Data section of this document. 

HexSplit also requires the location of RAxML on your machine. Please download and compile [RAxML](https://cme.h-its.org/exelixis/resource/download/NewManual.pdf) before using HexSplit. RAxML's github repo can be found [here](https://github.com/stamatak/standard-RAxML). Note: the current version of HexSplit assumes that the sequential version of RAxML is being used. However, the source code can be easily modified for use with multi-threaded versions of RAxML.  

Below is a list of parameters HexSplit supports. Please note the required parameters and pass in complete paths to files: 
  1. Multiple Sequence Alignment
  2. RAxML location
  3. Name of Directory/Folder to be created to store intermediate files

### Parameters
* -msa, --multiple_sequence_alignment : Path to the multiple sequence alignment file to be tested.
* -rxml_loc, --raxml_location : Path to where RAxML is stored on the user's local machine.
* -fn, --folder_name : User specified name to store created files (tripartitions, maximum likelihood and bootstrap trees).
* -m, --model : RAxML model to be used. Default: GTRCAT
* -nbs, --num_bootstrap : Number of bootstrap trees to be created. Default: 100
* -thresh, --threshold : Threshold used in histogram intersection test. Default: 0.5

### Test Data
We have provided 4 sample fasta files.
  1. noPGT_large.fa - No PGT, contains 229 gene sequences
  2. noPGT_short.fa - No PGT, contains 15 gene sequences (a subset of noPGT_large.fa)
  3. PGT_large.fa - PGT, contains 229 gene sequences
  4. PGT_short.fa - PGT, contains 9 gene sequences (a subset of PGT_large.fa)

These files were each tested with the GTRCAT model, 100 bootstrap trees, and a threshold value of 0.5 on a 2020 Macbook Pro M1. The short files ran in ~2 minutes while the larger files took between 2 and 4 hours to complete. The number of bootstraps plays a key role in runtime. 

### Running the Software
  1. Download HexSplit
  2. cd into the hexsplit directory (cd hexsplit-main, cd hexsplit)
  3. Ensure your multiple sequence alignment file is accessible
  4. Ensure dendropy is installed and RAxML executable is present
  5. Run wrapper script from the terminal - an example is provided below

### Example

#### Input: 
`python3 integration_file.py -msa /Users/shrey/Documents/test_files/noPGT_short.fa -rxml_loc /Users/shrey/standard-RAxML/raxmlHPC-AVX -fn noPGT_short -m GTRGAMMA -nbs 100 -thresh 0.5`

#### Sample Output: 
RAxML Gene Trees Successfully Created  
100 RAxML Bootstrap Trees Successfully Created

Regular windows 
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2  
Regular windows histogram intersection test result: 0.59

Offset windows 
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2  
Offset windows histogram intersection test result 0.83

PGT not detected

#### Interpreting the Output: 
RAxML Gene Trees Successfully Created (progress update for the user)  
100 RAxML Bootstrap Trees Successfully Created (progress update for the user)  

Regular windows (below information is for regular tripartition windows)  
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2 (pairwise RF scores between ML trees generated from the 3 partitions)  
Regular windows histogram intersection test result: 0.59 (result of the statistical analysis, a value less than the threshold indicates the presence of PGT)  

Offset windows (below information is for windows created with a 1/3 offset)  
Pairwise ML Tree RF scores -> w1w2: 2, w2w3: 2, w1w3: 2 (pairwise RF scores between ML trees generated from the 3 partitions)  
Offset windows histogram intersection test result 0.83 (result of the statistical analysis, a value less than the threshold indicates the presence of PGT)

PGT not detected (final result)

## Citing HexSplit

HexSplit can be cited as follows:

<i>HexSplit: An Improved Computational Approach for Detecting Partial Gene Transfer</i><br>
Shreya Seshadri, Sumaira Zaman, Mukul S. Bansal<br>
Under review
