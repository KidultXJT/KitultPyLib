import pandas as pd
import sys
import os
# personal library
import forSum
import BASICGraph

cov            = sys.argv[1]
covflt        = sys.argv[2]
prefix        = sys.argv[3]

if len(open(cov).read()) != 0 :
    t = pd.read_table(cov,sep="\t")
    # Gene GC Ratio : Before
    gc = t["Read_GC"]
    p,fig = BASICGraph.BasicHist(data=gc,xmax=max(gc),xmin=min(gc),n=10,rwidth=1,color="khaki",alpha=0.5,xTitle = "GC Ratio (%)",yTitle = "Frequency",Title="(Before) GC Ratio Distribution")
    fig.savefig(prefix+"_GC.PNG",dpi=100)
    # Avg Fold : Before
    avg = t["Avg_fold"]
    p,fig = BASICGraph.BasicHist(data=avg,xmax=20,xmin=0,n=200,rwidth=1,color="palevioletred",alpha=0.5,xTitle= "Average Depth",yTitle = "Frequency", Title = "(Before) Average Depth Distribution")
    fig.savefig(prefix+"_AvgDepth.PNG",dpi=100)
    # Coverage FILTER
    save = t.loc[t['Avg_fold'] > int(covflt)]
    save.to_csv(prefix+".CovFlt.xls", sep='\t', encoding='utf-8',header=True,index=None) # For filter Reads
    # Gene GC Ratio : Filter
    gc = save["Read_GC"]
    p,fig = BASICGraph.BasicHist(data=gc,xmax=max(gc),xmin=min(gc),n=10,rwidth=1,color="khaki",xTitle = "GC Ratio (%)",yTitle = "Frequency",Title="(Filtered by Depth) GC Ratio Distribution")
    fig.savefig(prefix+".CovFlt_GC.PNG",dpi=100)
    # Avg Fold : Filter
    avg = save["Avg_fold"]
    p,fig = BASICGraph.BasicHist(data=avg,xmax=20,xmin=0,n=200,rwidth=1,color="palevioletred",xTitle= "Average Depth",yTitle = "Frequency", Title = "(Filtered by Depth) Average Depth Distribution")
    fig.savefig(prefix+".CovFlt_AvgDepth.PNG",dpi=100)
else:
    open(prefix+".xls","w")
    open(prefix+".PNG","w")
