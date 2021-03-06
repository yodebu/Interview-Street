#!/usr/bin/env python

import Header
from Header import *

##-----------------------------------------------------
def Prev_File_Instance_Del():
  if os.path.isfile('screenout'):
    os.unlink('screenout')
  #if os.path.isfile('outfile'):
    #os.unlink('outfile')      
  #if os.path.isfile('outtree'):
    #os.unlink('outtree')        

#-----------------------------------------
''' validating mutation and crossover rates for boundary conditions '''
def ValidateRate(inp_val):
  if (inp_val > 1.0):
    inp_val = 1.0
  elif (inp_val < 0.05):
    inp_val = 0.05
  return inp_val

#-----------------------------------------
""" this function evaluates the fitness metric according to the least square estimate """
def EvaluateLS(orig_inp_dist_mat, number_of_taxa, curr_tree):
  if (DEBUG_LEVEL > 2):
    print 'list of taxa; ', curr_tree.infer_taxa().labels()
  # generate distance matrix of the current tree
  pdm_curr_tree = treecalc.PatristicDistanceMatrix(curr_tree)
  # obtain the least square error between the estimated distance matrix and the original one
  ls_error_est = 0
  curr_tree_taxa_set = curr_tree.infer_taxa()
  if (DEBUG_LEVEL > 0):
    if (number_of_taxa != len(curr_tree_taxa_set)):
      print 'EvaluateLS: length of current tree taxa set DIFFERS from the no of taxa ===>>> '
      print 'number_of_taxa: ', number_of_taxa
      print 'len(curr_tree_taxa_set): ', len(curr_tree_taxa_set)
      print 'error'
  for i in range(number_of_taxa - 1):
    t1 = curr_tree_taxa_set[i]
    for j in range(i+1, number_of_taxa):
      t2 = curr_tree_taxa_set[j]
      idx_i_orig_distmat = LIST_OF_TAXON_NAMES.index(t1.label)
      idx_j_orig_distmat = LIST_OF_TAXON_NAMES.index(t2.label)
      #print 't1: ', t1.label, 'idx: ', idx_i_orig_distmat, 't2: ', t2.label, 'idx: ', idx_j_orig_distmat
      ls_error_est = ls_error_est + pow((pdm_curr_tree(t1, t2) - orig_inp_dist_mat[idx_i_orig_distmat][idx_j_orig_distmat]), 2)
  
  return ls_error_est

##-----------------------------------------
#""" this function finds the maximum fitness tree from a given set of trees
#the fitness is computed by minimizing least square estimate 
#so minimizing the least square is equivalent to max fitness """
#def FindMaxFitnessTreeStr(orig_inp_dist_mat, no_of_taxa, inp_tree_str_list, no_of_trees):
  #for tc in range(no_of_trees):
    #curr_tree_str = inp_tree_str_list[tc]
    #curr_tree = dendropy.Tree(stream=StringIO(curr_tree_str), schema="newick")
    #curr_tree_LS_score = EvaluateLS(orig_inp_dist_mat, no_of_taxa, curr_tree)
    #if (tc == 0):
      #max_fitness_idx = tc
      #max_fitness_val = curr_tree_LS_score
      #max_fitness_tree_str = curr_tree_str
    #else:
      #if (curr_tree_LS_score < max_fitness_val):
	## since less least square estimate equals to more fitness
	#max_fitness_idx = tc
	#max_fitness_val = curr_tree_LS_score
	#max_fitness_tree_str = curr_tree_str
  
  #return max_fitness_idx, max_fitness_val, max_fitness_tree_str

#------------------------------------
''' this function computes the average value of input distance matrix
basically sum of n(n-1) / 2 elements of the distance matrix is averaged and returned '''
def Compute_Avg_Dist_Mat(input_dist_mat):
  # numpy shape function determines the size of input array
  avg_val = 0
  no_of_taxa = (numpy.shape(input_dist_mat))[0]
  for i in range(no_of_taxa - 1):
    for j in range(i+1, no_of_taxa):
      avg_val = avg_val + input_dist_mat[i][j]
  # compute the average value
  avg_val = (avg_val * 1.0) / ((no_of_taxa * (no_of_taxa - 1)) / 2)
  return avg_val
  
##-----------------------------------------------------
''' this function reads the distance matrix
from an input file '''
def ParseDistanceMatFromFile(inp_filename):
  # open file
  fp = open(inp_filename, 'r')
  lines = fp.readlines()
  # read the first line 
  lines[0].strip()
  number_of_taxa = int(lines[0])
  if (DEBUG_LEVEL > 2):
    print 'number_of_taxa: ', number_of_taxa
  DistMat = numpy.empty(number_of_taxa*number_of_taxa, float, 'C')
  if (DEBUG_LEVEL > 1):
    print 'first init: DistMat shape: ', DistMat.shape
  
  # this element counts the number of elements of the array
  currloc = 0
  
  for lc in range(1, len(lines)):
    lines[lc].strip()
    ''' employ string split method to derive the values
    1st value contains the taxon name
    2nd value onwards contain the distance values '''
    #print lines[lc]
    list_str = str.split(lines[lc], None)
    #print list_str
    #print len(list_str)
    for i in range(len(list_str)):
      if re.search('[A-Za-z]', str(list_str[i])):
	LIST_OF_TAXON_NAMES.append(str(list_str[i]))
      else:
	# this is a string of only numbers - so append in the distance matrix
	DistMat[currloc] = float(list_str[i])
	currloc = currloc + 1

  # close the file
  fp.close()
  if (DEBUG_LEVEL > 2):
    print 'no of elements inserted in the matrix: ', currloc
  
  # reshape the distance matrix
  OrigDistMat = numpy.reshape(DistMat, (number_of_taxa, number_of_taxa), order='C')
  if (DEBUG_LEVEL > 2):
    print 'after reshape: OrigDistMat shape: ', OrigDistMat.shape
  
  return OrigDistMat, number_of_taxa
  
##-----------------------------------------------------
''' this function writes a derived distance matrix to an output file specified
the file is written in the Phylip format, for using it with their standard functions 
Note --- the file is written as per lower triangular matrix convention '''
def WriteDistMat(InpDistMat, number_of_taxa, outfilename):
  fp = open(outfilename, 'w')
  taxa_str = '   ' + str(number_of_taxa)
  fp.write(taxa_str)
  for i in range(number_of_taxa):
    fp.write('\n')
    temp_str = str(LIST_OF_TAXON_NAMES[i])
    for spc in range(10 - (len(temp_str))):
      temp_str = temp_str + ' '
    fp.write(temp_str)
    # this line of j loop ensures that the matrix is a lower triangular matrix
    if (i > 0):
      for j in range(i):		#number_of_taxa
	if (j > 0):
	  fp.write('\t')
	fp.write(str(InpDistMat[i][j]))
  fp.close()

##-----------------------------------------------------
''' this function creates the automated batch file required to execute the NEIGHBOR routine 
parameters: neighbor_batch_filename - batch file containing the sequence of instructions for NJ method execution
inp_dist_mat_filename - file containing the input distance matrix which will be processed to produe the NJ output '''
def CreateNEIGHBORBatchFile(neighbor_batch_filename, inp_dist_mat_filename):
  fp = open(neighbor_batch_filename, 'w')
  fp.write(inp_dist_mat_filename)
  fp.write('\n')
  # input is a lower triangular matrix
  fp.write('L')
  fp.write('\n')        
  fp.write('Y')
  fp.write('\n')  
  fp.close()
  