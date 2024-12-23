import subprocess
import os 
import sys

def stc_test():
    #cd to asm files
    os.chdir('asm_files')
    #assemble the file
    subprocess.run(['nasm', '-f', 'bin', 'stc.asm', '-o', 'stc.com'])