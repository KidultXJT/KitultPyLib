import pandas as pd
import sys
import os
import FastAdeal

infa     = sys.argv[1]
outfa  = sys.argv[2]
prefix = sys.argv[3]

if len(open(infa).read()) != 0 :
    FastAdeal.formatFA(infa,out=outfa,rename=prefix)
    data,N50,p,fig = FastAdeal.faLength(outfa,Max=5000,out=prefix)
    data,p,fig = FastAdeal.faGCratio(outfa,out=prefix)
else:
    open(outfa,"w")
    open(prefix+".xls","w")
    open(prefix+".PNG","w")



