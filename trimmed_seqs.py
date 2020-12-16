#args: input: ouput: path-to-trimmomatic.tar

## trimmomatic script
import os
import subprocess
import sys
import argparse

#argument parser
parser = argparse.ArgumentParser()
parser.add_argument("-in_files", help="Directory containing fastq files [Don't include '/']",
                   required=True)
parser.add_argument("-out_dir", help="Output directory [Don't include '/']",
                   required=True)
parser.add_argument("-trim", help="Path to trimmomatic.jar",
                   required=True)
args = parser.parse_args()

#parameters                                                                            
in_files = args.in_files
out_dir = args.out_dir
trim = args.trim
print("infiles: ", in_files)
print("output: ", out_dir)
print("trim location: ", trim)

#create output dir                                                                                    
print('Creating output: ', out_dir)
os.makedirs(out_dir)

#read in file list                                                                                    
file_list = os.listdir(in_files)
print('# files in : ', in_files)

#run trimmomatic on every file in list                                                                     
#path to trimmomatic
for seq in file_list:
    cmd = "java -jar {trim} SE -phred33 {in_files}/{seq} {out_dir}/{seq}.trimmed LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36".format(**locals())
    os.system(cmd)
    
print("Input files: {in_files}/{seq} trimmed to:  {out_dir} trim_{in_files}/{seq}".format(**locals()))
