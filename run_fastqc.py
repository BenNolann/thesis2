#different version of the same thing

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
args = parser.parse_args()

#parameters                                                                            
in_files = args.in_files
out_dir = args.out_dir
print("infiles: ", in_files)
print("output: ", out_dir)

#create output dir
print('Creating output: ', out_dir)
html_dir = os.path.join(out_dir, "html/")
zip_dir = os.path.join(out_dir, "zip/")
os.makedirs(out_dir)
os.makedirs(html_dir)
os.makedirs(zip_dir)


#read in file list                                                                             
file_list = os.listdir(in_files)
print('# files in : {in_files}'.format(**locals()))

#run fastqc on every file in list                                                              
for seq in file_list:
    cmd = "fastqc {in_files}/{seq}".format(**locals())
    print(cmd)
    os.system(cmd)


#move result files to output dir
cmd2 = "mv {in_files}/*.html {html_dir} | mv {in_files}/*.zip {zip_dir}".format(**locals())
print(cmd2)
os.system(cmd2)

print('Done.')
print('Output files can be found in {out_dir}'.format(**locals()))
