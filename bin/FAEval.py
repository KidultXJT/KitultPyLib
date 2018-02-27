import pandas as pd
import sys
import os
import FastAdeal

mixfa    = sys.argv[1]
smpfa   = sys.argv[2]
smpid   = sys.argv[3]

idlst = smpid.split(",")
falst = smpfa.split(",")

SUM = FastAdeal.makeSUM(mixfa,ColumnsName="Mix")[0] # Mix EvTable
for i in range(len(idlst)):
    EvTable,Lst = FastAdeal.makeSUM(falst[i],ColumnsName=idlst[i])
    SUM = SUM.join(EvTable)
SUM.to_csv("EvalAssembly.xls", sep='\t', encoding='utf-8',header=True,index=True)