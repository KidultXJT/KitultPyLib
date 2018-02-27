import pandas as pd
import sys
import os
# personal library
import forSum
import BASICGraph
import FastAdeal

covflt     = sys.argv[1]  # prokka_CovFlt.xls
unifa      = sys.argv[2]  # prokka.uniflt.fna
prefix     = sys.argv[3]

if len(open(covflt).read()) != 0 :
    c = pd.read_table(covflt,sep="\t")
    IDlst = []
    for line in open(unifa,"r"):
        line = line.rstrip()
        if line[0] == ">":
            line = line[1:]
            infos = line.split(" ")
            ID = infos[0]
            IDlst.append(ID)
    unifltDF = pd.DataFrame(IDlst)
    t = unifltDF.join(c)
    t.to_csv(prefix+".UniFlt.xls",header=None,index=None,sep="\t")
    os.system("fish_in_winter.pl -bf table -ff fasta --bcolumn 1 --fcolumn 1 -gene {prefix}.UniFlt.xls {prefix}.covflt.faa > {prefix}.uniflt.faa".format(prefix = prefix))
    # Unique FILTER
    # Gene GC Ratio : Filter
    gc = t["Read_GC"]
    p,fig = BASICGraph.BasicHist(data=gc,xmax=max(gc),xmin=min(gc),n=10,rwidth=1,alpha = 0.9, color="khaki",xTitle = "GC Ratio (%)",yTitle = "Frequency",Title="(Filtered by Unique) GC Ratio Distribution")
    fig.savefig(prefix+".UniFlt_GC.PNG",dpi=100)
    # Avg Fold : Filter
    avg = t["Avg_fold"]
    p,fig = BASICGraph.BasicHist(data=avg,xmax=20,xmin=2,n=200,rwidth=1,alpha=0.9,color="palevioletred",xTitle= "Average Depth",yTitle = "Frequency", Title = "(Filtered by Unique) Average Depth Distribution")
    fig.savefig(prefix+".UniFlt_AvgDepth.PNG",dpi=100)
    data,N50,p,fig = FastAdeal.faLength(infa=unifa.replace("uni","cov"),Max=2000,Min=0,Col="lightskyblue",out=prefix+".FNA")
    data,N50,p,fig = FastAdeal.faLength(infa=prefix+".covflt.faa",Max=1000,Min=0,Col="tomato",out=prefix+".FAA")
    data,N50,p,fig = FastAdeal.faLength(infa=unifa,Max=2000,Min=0,Col="lightskyblue",out=prefix+".FNA")
    data,N50,p,fig = FastAdeal.faLength(infa=prefix+".uniflt.faa",Max=1000,Min=0,Col="tomato",out=prefix+".FAA")
else:
    open(prefix+".xls","w")
    open(prefix+".PNG","w")