import math
import re
import argparse
import os
import numpy as np
import sys
import glob 
import scipy.stats as st
import dendropy
from dendropy import Tree
from dendropy.calculate import treecompare
#import seaborn as sns
import matplotlib.pyplot as plt
plt.switch_backend('agg')

def return_intersection(hist_1, hist_2):
    #intsc=np.sum(np.minimum(x,y))
    minima = np.minimum(hist_1, hist_2)
    intersection = np.true_divide(np.sum(minima), np.sum(hist_2))
    return intersection

def calcRF(t1,t2):
    tns = dendropy.TaxonNamespace()
    tree1=Tree.get_from_path(str(t1),"newick",taxon_namespace=tns)
    tree2=Tree.get_from_path(str(t2),"newick",taxon_namespace=tns)
    tree1.encode_bipartitions()
    tree2.encode_bipartitions()
    return (treecompare.unweighted_robinson_foulds_distance(tree1, tree2))

def compareNeighbors(ml_trees_path):
    #RAxML Gene Trees used
    samplePath=ml_trees_path
    # r=root, d=directories, f = file                                                                                                                      
    # print(samplePath)                                                                                                                                    

    window1_tree=samplePath+"/window1/RAxML_bestTree.window1"
    window2_tree=samplePath+"/window2/RAxML_bestTree.window2"
    window3_tree=samplePath+"/window3/RAxML_bestTree.window3"
    w1w2=calcRF(window1_tree,window2_tree)
    w1w3=calcRF(window1_tree,window3_tree)
    w2w3=calcRF(window2_tree,window3_tree)
        
    return(w1w2, w1w3, w2w3)


def generateDistribution(threshold,sample,best_tree_rfs):
    #RAxML Bootstrap Trees Used
    #print('sample is: ' + str(sample))
    w1w2s=np.zeros((100))
    w1w3s=np.zeros((100))
    w2w3s=np.zeros((100))

    index=0

    for bootstrap in glob.glob(str(sample)+'/window1/x*'):
        filename=(os.path.basename(bootstrap)).split(".")[0]
        w2_tree=str(sample)+'/window2/'+filename
        w3_tree=str(sample)+'/window3/'+filename
        w1w2=calcRF(bootstrap,w2_tree)
        w1w3=calcRF(bootstrap,w3_tree)
        w2w3=calcRF(w2_tree,w3_tree)

        w1w2s[index]=w1w2
        w1w3s[index]=w1w3
        w2w3s[index]=w2w3

        index=index+1
       
    maximum=max(max(w1w2s),max(w1w3s),max(w2w3s))+1
    minimum=min(min(w1w2s),min(w1w3s),min(w2w3s))
    nbin=int(maximum-minimum)
    #print('number of bins', nbin)

    hist_w1w2s, b1 = np.histogram(w1w2s, bins=nbin, range=(minimum,maximum))
    hist_w1w3s, b2 = np.histogram(w1w3s, bins=nbin, range=(minimum,maximum))
    hist_w2w3s, b3 = np.histogram(w2w3s, bins=nbin, range=(minimum,maximum))

    
    print('Pairwise ML Tree RF scores -> w1w2: {}, w2w3: {}, w1w3: {}'.format(w1w2, w2w3, w1w2))
    #print(w1w2, w2w3, w1w2)
    '''
    print('average of w1w2 bootstraps', w1w2s.mean())
    print('average of w1w3 bootstraps', w1w3s.mean())
    print('average of w2w3 bootstraps', w2w3s.mean())

    print('standard dev of w1w2 bootstraps', np.std(w1w2s))
    print('standard dev of w1w3 bootstraps', np.std(w1w3s))
    print('standard dev of w2w3 bootstraps', np.std(w2w3s))
    
    print("w1w2, w1w3, w2w3")
    '''
    
    x=None

    # if max is w1w3 and min is w1w2
    if  best_tree_rfs.index(max(best_tree_rfs)) == 1 and best_tree_rfs.index(min(best_tree_rfs))==0:
        x=return_intersection(hist_w1w3s,hist_w1w2s)

    # if max is w1w3 and min is w2w3
    elif best_tree_rfs.index(max(best_tree_rfs)) == 1 and best_tree_rfs.index(min(best_tree_rfs))==2:
        x=return_intersection(hist_w1w3s,hist_w2w3s)

    # if max is w2w3 and min is w1w2
    elif  best_tree_rfs.index(max(best_tree_rfs)) == 2 and best_tree_rfs.index(min(best_tree_rfs))==0:
        x=return_intersection(hist_w1w2s,hist_w2w3s)

    # if max is w2w3 and min is w1w3
    elif best_tree_rfs.index(max(best_tree_rfs)) == 2 and best_tree_rfs.index(min(best_tree_rfs))==1:
        x=return_intersection(hist_w1w3s,hist_w2w3s)

    # if max is w1w2 and min is w1w3   
    elif best_tree_rfs.index(max(best_tree_rfs)) == 0 and best_tree_rfs.index(min(best_tree_rfs))==1:
        x=return_intersection(hist_w1w2s,hist_w1w3s)

    # if max is w1w2 and min is w2w3
    elif best_tree_rfs.index(max(best_tree_rfs)) == 0 and best_tree_rfs.index(min(best_tree_rfs))==2:
        x=return_intersection(hist_w2w3s,hist_w1w2s)

    if x!=None:
        if x < threshold:
            #print('sample ' + str(sample) + ' passed the statistical test with ' + str(x))
            return (1, str(x))
        else:
            #print('sample ' + str(sample) + ' failed the statistical test with ' + str(x))
            return (0, str(x))
    else:
        print('All rfs are equivalent for sample {} - not possible to distinguish'.format(str(sample)))
        return (0, None)

def plot(w1w2s,w1w3s,w2w3s, nbin):

    plt.hist(w1w2s, bins=nbin, label='w1w2')
    plt.hist(w1w3s, bins=nbin, label='w1w3')
    plt.hist(w2w3s, bins=nbin, label='w2w3')
    plt.legend()
    plt.savefig('histogram.png')

def loopsample(threshold,bootstrap_path, ml_trees_path):
     x=compareNeighbors(ml_trees_path)
     result = generateDistribution(threshold,bootstrap_path,x)     

     '''
     result = 1 -> passed statistical test - PGT Detected
     result = 0 -> failed statistical test / not possible to distinguish - PGT not Detected
     '''  
     return result                                                                                                                                                            


if __name__ == "__main__":
    
     parser = argparse.ArgumentParser(
     prog='hist_intersection.py',
     usage='''python hist_intersection.py --thresh [required overlap for gene families ] --tri_bs_sample [gene sample file tri partitioned bootstrapped directory] --tri_ml_sample [name of tri partitioned raxml file for sample] --hex_bs_sample [gene sample file hex split bootstrapped directory] --hex_ml_sample [name of hex split raxml file for sample]''',
     description='''determine whether gene family has sub-gene transfer (presence/absence)''',
     epilog='''It requires numpy, dendropy, scipy libraries''')
     parser.add_argument('-thresh','--threshold', type=str, help='minimum overlap required between distributions', required=True)
     parser.add_argument('-setA_bs','--tri_bs_sample', type=str, help='path to tri partitioned bootstrap samples', required=True)
     parser.add_argument('-setA_gt','--tri_ml_sample', type=str, help='path to tri partitioned maximum likelihood trees', required=True)
     parser.add_argument('-setB_bs','--hex_bs_sample', type=str, help='path to hex split bootstrap sample', required=True)
     parser.add_argument('-setB_gt','--hex_ml_sample', type=str, help='path to hex split maximum likelihood trees', required=True)
     parser.add_argument('--plot', type=bool, help='plot the RF-score distribition between partitions', required=False)

     args=parser.parse_args()
     threshold=float(args.threshold)
     tri_ml_trees_path=args.tri_ml_sample
     tri_bootstrap_path=args.tri_bs_sample
     hex_ml_trees_path=args.hex_ml_sample
     hex_bootstrap_path=args.hex_bs_sample
     
     print()
     print('Regular windows ')
     setA_test = loopsample(threshold,tri_bootstrap_path, tri_ml_trees_path)
     setA_result = setA_test[0]
     setA_value = setA_test[1]
     print("Regular windows histogram intersection test result: {}".format(setA_value))

     print()
     print('Offset windows ')
     setB_test = loopsample(threshold, hex_bootstrap_path, hex_ml_trees_path)
     setB_result = setB_test[0]
     setB_value = setB_test[1]
     print("Offset windows histogram intersection test result {}".format(setB_value))
     
     print()
     if (setA_result == 1 or setB_result == 1):
        print("PGT detected")
     else: 
        print('PGT not detected')
     
