#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 22:19:50 2019
@author: serdarturkaslan
Collects counts from htseqcount output as input for DESeq2
"""
import glob, sys, os
import pandas as pd

counts_dir = '/Volumes/omics4tb2/Collaborations/Vulcan/data/181203_K00235_0152_BHWNJ7BBXX_CBASS84_RNASeq/all_htseqcounts'

count_files = glob.glob('%s/*_htseqcounts.txt' %(counts_dir))

count_matrix = '%s/htseq_counts_matrix.txt' %(counts_dir)


count_df = pd.DataFrame()
count_df = pd.read_csv(count_files[0], sep='\t', index_col=0, header=0)
samples = []
for count_file in count_files[0:3]:
    
    sample = count_file.split('/')[-1]
    samples.append(sample)
    
    myfile = pd.read_csv(count_file, sep='\t', index_col=0, header=None)
    count_df = pd.concat([count_df, myfile], axis=1, ignore_index=False)

count_df.columns = [samples]

count_df.to_csv(count_matrix, sep='\t')