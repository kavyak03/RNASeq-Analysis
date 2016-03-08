# RNASeq-Analysis
Custom workflow for analysis of RNAseq data

This repository includes custom analysis workflow scripts to analyze RNA-sequencing data in support of the associated publication by Turkarslan et al.

#Workflow:
##analyzeRNAseq.py
1. Read quality control (FastQC)
2. Trimming and filtering (Trimmomatic)
3. Alignment to reference genome (STAR)
4. Counting reads per transcript (htseq-count)
5. Calculating FPKMs (Cufflinks)

rnaseqStats.R
1. read stats and quality metrics 
2. Read count normalizations
3. Visualizations
