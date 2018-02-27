import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
# personal library
import forTaxonomy
import BASICGraph
import TableDealer

tbl       = sys.argv[1]
tpms  = sys.argv[2]
smps  = sys.argv[3]
prefix = sys.argv[4]

# For Tax2Gene ~ But Now Contigs to Gene Only
# TPM
TPMAll,TPMSet,TPMlst = TableDealer.TableCombine(Anno=tbl,vfilelist=tpms,ColumNames=smps,Values=3) 
TPMAll.index.names = ['CongtigsID']
TPMAll.to_csv("Gene.TPM.xls", sep='\t', encoding='utf-8',header=True)
# Reads
ReadsAll,ReadsSet,Readslst = TableDealer.TableCombine(Anno=tbl,vfilelist=tpms,ColumNames=smps,Values=4) 
ReadsAll.index.names = ['CongtigsID']
ReadsAll.to_csv("Gene.Reads.xls", sep='\t', encoding='utf-8',header=True)

