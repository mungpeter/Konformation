#!/usr/bin/env python3

###################
#
#  Peter M.U. Ung @ MSSM/Yale
#
#  v1  20.03.29
#
#  convert PDB files with unnatural/modified residues ususally on
#  SER/THR/TYR/HIS/LYS/CYS to the unmodified common form so that
#  BioPython can handle to PDB correctly
#
###################
import sys
import os,re

from tqdm import tqdm
from x_pdb_modif_resid import ReplacePDBModifiedAA

def main( list_file ):

  with open(list_file, 'r') as fi:
    pdb_list = [l.rstrip() for l in fi if l.rstrip is not False]

  count = 0
  for pdb in tqdm(pdb_list):
    ReplacePDBModifiedAA( pdb, 'temp.'+pdb )
    if os.path.isfile('temp.'+pdb):
      os.system('mv temp.{0} {0}'.format(pdb))
      count += 1

  print('\033[31m\n> converted:\033[0m {0}\n'.format(count))

##########################
if __name__ == '__main__':
  main( sys.argv[1] )
