#!/bin/env python3
#-* coding = UTF-8 *-
import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='This script is using to update data.')
parser.add_argument('-i','--input',required=True,help='Path of input')
parser.add_argument('-o','--output',required=True,help='dir to output')
args = parser.parse_args()
for root,dirs,files in os.walk(args.input):
    for file in files:
        out_root = root.replace(args.input,args.output,1) # replace gate name to output
        if not os.path.exists(out_root): # mkdir -p out_root
            os.makedirs(out_root)
        path = os.path.join(root,file) # the input file path
        mtime = os.stat(path).st_mtime # the input file modify time
        o_path = os.path.join(out_root,file) # the output file path
        if os.path.exists(o_path):
            o_mtime = os.stat(o_path).st_mtime # the output file modify time
            if mtime > o_mtime: # check the modify time
                shutil.copy(path,o_path) # catch the newer
        else:
            shutil.copy(path,o_path)
