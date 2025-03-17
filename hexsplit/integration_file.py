# Copyright (C) 2025 Shreya Seshadri (shreya.seshadri@uconn.edu) and
# Mukul S. Bansal (mukul.bansal@uconn.edu).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see http://www.gnu.org/licenses/.


#import modules
import subprocess, argparse, os, sys, glob

def make_window_dirs(folder_name): 
    if not os.path.exists(folder_name): 
        os.mkdir(folder_name)
    else:
        print('A directory with the same name already exists. Please specify a new folder name and rerun')
        exit()

    # window directories
    if not os.path.exists(folder_name + os.path.sep + "windows"): 
        os.mkdir(folder_name + os.path.sep + "windows")
    
    if not os.path.exists(folder_name + os.path.sep + "windows" + os.path.sep + "setA"): 
        os.mkdir(folder_name + os.path.sep + "windows" + os.path.sep + "setA")

    if not os.path.exists(folder_name + os.path.sep + "windows" + os.path.sep + "setB"): 
        os.mkdir(folder_name + os.path.sep + "windows" + os.path.sep + "setB")

def make_rxmlgt_dirs(folder_name):
    #raxml gene tree directory
    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees")
    #Set A
    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA")
    
    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA" + os.path.sep + "window1"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA" + os.path.sep + "window1")

    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA" + os.path.sep + "window2"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA" + os.path.sep + "window2")

    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA" + os.path.sep + "window3"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setA" + os.path.sep + "window3")

    #Set B
    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB")

    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB" + os.path.sep + "window1"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB" + os.path.sep + "window1")

    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB" + os.path.sep + "window2"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB" + os.path.sep + "window2")

    if not os.path.exists(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB" + os.path.sep + "window3"): 
        os.mkdir(folder_name + os.path.sep + "raxmlgenetrees" + os.path.sep + "setB" + os.path.sep + "window3")

def make_rxmlbs_dirs(folder_name): 
    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees")

    #Set A
    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA")
    
    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA" + os.path.sep + "window1"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA" + os.path.sep + "window1")

    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA" + os.path.sep + "window2"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA" + os.path.sep + "window2")

    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA" + os.path.sep + "window3"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setA" + os.path.sep + "window3")

    #Set B
    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB")

    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB" + os.path.sep + "window1"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB" + os.path.sep + "window1")

    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB" + os.path.sep + "window2"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB" + os.path.sep + "window2")

    if not os.path.exists(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB" + os.path.sep + "window3"): 
        os.mkdir(folder_name + os.path.sep + "raxmlbstrees" + os.path.sep + "setB" + os.path.sep + "window3")
    

def create_windows(fasta_file, folder_name):
    #STEP 1: Go through fasta file and split into windows Set A and Set B
    
    python_exe = sys.executable
    #print(os.getcwd())

    #Set A
    setA_script = os.path.join('scripts', '01_SetA_splitFasta.py')
    setA_window_dir = os.path.join(folder_name, 'windows', 'setA')
    #create Set A windows
    if os.path.exists(folder_name + os.path.sep + "windows" + os.path.sep + "setA"): 
        subprocess.run([python_exe, setA_script, fasta_file, setA_window_dir], check=True)
    
    #Set B
    setB_script = os.path.join('scripts', '01_SetB_splitFasta.py')
    setB_window_dir = os.path.join(folder_name, 'windows', 'setB')
    #create Set B windows
    if os.path.exists(folder_name + os.path.sep + "windows" + os.path.sep + "setB"): 
        subprocess.run([python_exe, setB_script, fasta_file, setB_window_dir], check=True)

def create_rxml_genetrees(raxml_location, model, folder_name): 
    #Create Raxml Gene Trees
  
    model = model
    main_dir= os.getcwd()

    #Set A
    window_dir_setA = os.path.join(main_dir, folder_name, 'windows', 'setA')
    final_dir_setA = os.path.join(main_dir, folder_name, 'raxmlgenetrees', 'setA')
    setA_flag = True

    for w in glob.glob(f'{window_dir_setA}/window*'):
        #print(w)
        check_file_setA = subprocess.run(['ls', '-lh', w], capture_output=True, text=True)
        if check_file_setA.returncode == 0: 
            pass
        else: 
            print('Error {}: Cannot find file {}'.format(check_file_setA.returncode, w))
            setA_flag = False
            break
        absolute_w = os.path.abspath(w)
        window = os.path.basename(w)
        os.chdir(final_dir_setA + os.path.sep + window)
        #print("I am here:")
        #print(os.getcwd())

        run_rxmlgt_setA = subprocess.run([raxml_location,'-f', 'a','-p', '13579','-N', '9','-m', model,'-x', '12345','-s', absolute_w,'-n', window], capture_output=True, text=True)
        if run_rxmlgt_setA.returncode == 0: 
            pass
        else: 
            print('RAxML error: error code {} for {} set A'.format(run_rxmlgt_setA.returncode, window))
            print(run_rxmlgt_setA.stdout)
            setA_flag = False
            break
        os.chdir(main_dir)

    #Set B
    window_dir_setB = os.path.join(main_dir, folder_name, 'windows', 'setB')
    final_dir_setB = os.path.join(main_dir, folder_name, 'raxmlgenetrees', 'setB')
    setB_flag = True

    for w in glob.glob(f'{window_dir_setB}/window*'):
        check_file_setB = subprocess.run(['ls', '-lh', w], capture_output=True, text=True)
        if check_file_setB.returncode == 0: 
            pass
        else: 
            print('Error {}: Cannot find file {}'.format(check_file_setB.returncode, w))
            setB_flag = False
            break
        absolute_w = os.path.abspath(w)
        window = os.path.basename(w)
        os.chdir(final_dir_setB + os.path.sep + window)
        #print("I am here:")
        #print(os.getcwd())

        run_rxmlgt_setB = subprocess.run([raxml_location,'-f', 'a','-p', '13579','-N', '9','-m', model,'-x', '12345','-s', absolute_w,'-n', window], capture_output=True, text=True)
        if run_rxmlgt_setB.returncode == 0: 
            pass
        else: 
            print('RAxML error: error code {} for {} set B'.format(run_rxmlgt_setB.returncode, window))
            print(run_rxmlgt_setB.stdout)
            setB_flag = False
            break
        os.chdir(main_dir)

    if(setA_flag and setB_flag): 
        return(True)
    else: 
        return(False)

def create_rxml_bootstrap_trees(raxml_location, model, num_bootstrap, folder_name):
    #Create Raxml Bootstrap Trees
  
    model = model
    main_dir= os.getcwd()

    #Set A
    window_dir_setA = os.path.join(main_dir, folder_name, 'windows', 'setA')
    final_dir_setA = os.path.join(main_dir, folder_name, 'raxmlbstrees', 'setA')
    setA_flag = True

    for w in glob.glob(f'{window_dir_setA}/window*'):
       if w.endswith('.reduced'):
           pass
       else: 
        #print(w)
        check_file_setA = subprocess.run(['ls', '-lh', w], capture_output=True, text=True)
        if check_file_setA.returncode == 0: 
            pass
        else: 
            print('Error {}: Cannot find file {}'.format(check_file_setA.returncode, w))
            setA_flag = False
            break
        absolute_w = os.path.abspath(w)
        window = os.path.basename(w)
        os.chdir(final_dir_setA + os.path.sep + window)
        #print("I am here:")
        #print(os.getcwd())

        run_rxmlbs_setA = subprocess.run([raxml_location,'-b', '12345', '-p', '13579', '-#', str(num_bootstrap), '-m', model, '-s', absolute_w, '-n', window], capture_output=True, text=True)
        if run_rxmlbs_setA.returncode == 0: 
            pass
        else: 
            print('RAxML error: error code {} for {} set A'.format(run_rxmlbs_setA.returncode, window))
            print(run_rxmlbs_setA.stdout)
            setA_flag = False
            break
        
        bootstrap_file = 'RAxML_bootstrap.{}'.format(window)
        bootstrap_file_path = os.path.abspath(bootstrap_file)
        if os.path.exists(bootstrap_file_path): 
            pass
        else: 
            print('{} does not exist'.format(bootstrap_file_path))
            setA_flag = False
            break
        
        run_rxmlbs_split_setA = subprocess.run(['split', '-l', '1', bootstrap_file_path], capture_output=True, text=True)
        if run_rxmlbs_split_setA.returncode == 0: 
            pass
        else: 
            print('Split Error: {} for {} set A'.format(run_rxmlbs_split_setA.returncode, window))
            print(run_rxmlbs_split_setA.stdout)
            setA_flag = False
            break
        os.chdir(main_dir)

    #Set B
    window_dir_setB = os.path.join(main_dir, folder_name, 'windows', 'setB')
    final_dir_setB = os.path.join(main_dir, folder_name, 'raxmlbstrees', 'setB')
    setB_flag = True

    for w in glob.glob(f'{window_dir_setB}/window*'):
       if w.endswith('.reduced'):
           pass
       else: 
        #print(w)
        check_file_setB = subprocess.run(['ls', '-lh', w], capture_output=True, text=True)
        if check_file_setB.returncode == 0: 
            pass
        else: 
            print('Error {}: Cannot find file {}'.format(check_file_setB.returncode, w))
            setB_flag = False
            break
        absolute_w = os.path.abspath(w)
        window = os.path.basename(w)
        os.chdir(final_dir_setB + os.path.sep + window)
        #print("I am here:")
        #print(os.getcwd())

        run_rxmlbs_setB = subprocess.run([raxml_location,'-b', '12345', '-p', '13579', '-#', str(num_bootstrap), '-m', model, '-s', absolute_w, '-n', window], capture_output=True, text=True)
        if run_rxmlbs_setB.returncode == 0: 
            pass
        else: 
            print('RAxML error: error code {} for {} set B'.format(run_rxmlbs_setB.returncode, window))
            print(run_rxmlbs_setB.stdout)
            setB_flag = False
            break
        
        bootstrap_file = 'RAxML_bootstrap.{}'.format(window)
        bootstrap_file_path = os.path.abspath(bootstrap_file)
        if os.path.exists(bootstrap_file_path): 
            pass
        else: 
            print('{} does not exist'.format(bootstrap_file_path))
            setB_flag = False
            break
        
        run_rxmlbs_split_setB = subprocess.run(['split', '-l', '1', bootstrap_file_path], capture_output=True, text=True)
        if run_rxmlbs_split_setB.returncode == 0: 
            pass
        else: 
            print('Split Error: {} for {} set B'.format(run_rxmlbs_split_setB.returncode, window))
            print(run_rxmlbs_split_setB.stdout)
            setB_flag = False
            break
        os.chdir(main_dir)
        
    if (setA_flag and setB_flag) == True: 
        return True
    else: 
        return False

def hist_intersection_test(threshold, folder_name): 
    hist_int_filepath = 'scripts/04_adv_hist_intersection.py'
    hist_int_abs_filepath = os.path.abspath(hist_int_filepath)
    setA_bs_path = os.path.abspath(folder_name + os.path.sep + 'raxmlbstrees' + os.path.sep + 'setA')
    setB_bs_path = os.path.abspath(folder_name + os.path.sep + 'raxmlbstrees' + os.path.sep + 'setB')
    setA_gt_path = os.path.abspath(folder_name + os.path.sep + 'raxmlgenetrees' + os.path.sep + 'setA')
    setB_gt_path = os.path.abspath(folder_name + os.path.sep + 'raxmlgenetrees' + os.path.sep + 'setB')

    subprocess.run(['python3', hist_int_abs_filepath, '-thresh', str(threshold), '-setA_bs', setA_bs_path, '-setA_gt', setA_gt_path, '-setB_bs', setB_bs_path, '-setB_gt', setB_gt_path], check=True)   


if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument("-msa", "--multiple_sequence_alignment", type=str, required=True, help="Location of the file to be tested")
    parser.add_argument("-rxml_loc", "--raxml_location", type=str, required=False, help="Where RAxML (Sequential Version) is stored on your machine")
    parser.add_argument("-fn", "--folder_name", type=str, required=True, help="Name of folder containing all created files")
    parser.add_argument("-m", "--model", type=str, required=False, help="RAxML model to be used - default is GTRCAT", default='GTRCAT')
    parser.add_argument("-nbs", "--num_bootstrap", type=int, required=False, help="Number of bootstrap trees to be created - default is 100", default=100)
    parser.add_argument("-thresh", "--threshold", type=float, required=False, help="Threshold for histogram intersection test - default is 0.5", default=0.5)


    args = parser.parse_args()

    fasta_file=args.multiple_sequence_alignment
    raxml_location = args.raxml_location
    model = args.model
    num_bootstrap = args.num_bootstrap
    threshold = args.threshold
    folder_name = args.folder_name

    #Create Set A and Set B
    make_window_dirs(folder_name)
    create_windows(fasta_file, folder_name)

    #Create RAxML Gene Trees from Set A and Set B
    make_rxmlgt_dirs(folder_name)
    rxml_genetrees = create_rxml_genetrees(raxml_location, model, folder_name)
    if rxml_genetrees == True: 
        print('RAxML Gene Trees Successfully Created')
    else: 
        print("Error in generating RAxML Gene Trees - exiting process")
        exit()

    #Create RAxML Bootstrap Trees from Set A and Set B
    make_rxmlbs_dirs(folder_name)
    rxml_bootstraptrees = create_rxml_bootstrap_trees(raxml_location, model, num_bootstrap, folder_name)
    if rxml_bootstraptrees == True: 
        print('{} RAxML Bootstrap Trees Successfully Created'.format(num_bootstrap))
    else: 
        print('Error in generating RAxML Bootstrap Trees - exiting process')
        exit()

    #Run Histogram Intersection Test
    hist_intersection_test(threshold, folder_name)
