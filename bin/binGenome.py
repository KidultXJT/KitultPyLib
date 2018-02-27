import pandas as pd
import sys
import os
# personal library
import forSum
import BASICGraph

mbmarker = sys.argv[1]
mbsum       = sys.argv[2]
prefix          = sys.argv[3]

if len(open(mbmarker).read()) != 0 :
    marker = pd.read_table(mbmarker,sep="\t")
    SUM = pd.read_table(mbsum,sep="\t")
    p,fig = BASICGraph.BasicScatter(X=marker["Unnamed: 0"],  # Contigs
                                                                    Y=marker["Total marker"], # Marker Gene
                                                                    Col=SUM["Abundance"],    # Coverage 
                                                                    Size=SUM["Genome size"]*0.0001, # Genome Size
                                                                    Title="",xTitle="Num of Conitgs",yTitle="Num of Marker Gene")
    fig.savefig(prefix+"_Bin.PNG",dpi=100)
    fig.savefig(prefix+"_Bin.PDF")
else:
    open(prefix+".PNG","w")