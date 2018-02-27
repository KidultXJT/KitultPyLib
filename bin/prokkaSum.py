import pandas as pd
import sys
import os
# personal library
import forSum
import FastAdeal
import BASICGraph

tsv     = sys.argv[1]
ffn     = sys.argv[2]
faa     = sys.argv[3]
gff     = sys.argv[4]
tbl      = sys.argv[5]
prefix = sys.argv[6]

if len(open(tsv).read()) != 0 :
    # tsv FORMAT && Sum GeneTypes
    # Fregment Types
    t = pd.read_table(tsv,sep="\t")
    t = t.loc[t['ftype'] != "ftype",:]
    data = t['ftype']
    TypesDF,p,Typesfig = forSum.freqBar(data=data,Title="Gene Prediction",xTitle="Gene Types",yTitle="Frequnecy",out=prefix+".GeneTypes")
    t.to_csv(prefix+".TSV", sep='\t', encoding='utf-8',header=True,index=None,float_format='%.2f')
    # HypotheticalProtein Ratio
    t = t.loc[t["ftype"] == "CDS",:]
    hp = t.loc[t["gene"] == "hypothetical protein",:]
    HypotheticalProtein = round(len(hp.index)/len(t.index),2)
    NotHyPro = round(1-HypotheticalProtein,2)
    All = HypotheticalProtein+NotHyPro
    DF = pd.DataFrame({"CDSTypes":["Hypothetical Protein","Not Hypothetical Protein"],"Values":[len(hp.index),len(t.index)-len(hp.index)]},columns=["CDSTypes","Values"])
    DF.to_csv(prefix+"_CDSTypes", sep='\t', encoding='utf-8',header=True,index=None,float_format='%.2f')
    p,fig = BASICGraph.BasicPie(df=DF,Title="CDS Types")
    fig.savefig(prefix+"_CDSTypes.PNG",dpi=100)
    # faa fna FORMAT && Length Distribution
    FastAdeal.formatFA(infa=ffn,out=prefix+".fna")
    FastAdeal.formatFA(infa=faa,out=prefix+".faa")
    data,N50,p,fig = FastAdeal.faLength(infa=prefix+".fna",Max=2000,Min=0,Col="lightskyblue",out=prefix+"FNA")
    data,N50,p,fig = FastAdeal.faLength(infa=prefix+".faa",Max=1000,Min=0,Col="tomato",out=prefix+"FAA")
    # gtf FORMAT && SUM
    os.system("cp {gff} {GFF}".format(gff=gff,GFF=prefix+".GFF"))
    # tbl FORMAT && SUM
    l = []
    Contigs = []
    Gene = []
    for line in open(tbl,"r").readlines():
        if line[0] == ">":
            l.append(line.rstrip()[9:])
        else:
            if line.strip().startswith("locus_tag"):
                Contigs.append(l[-1])
                Gene.append(line.strip()[10:])
    ContigsGene = pd.DataFrame({"Key":Contigs,"Gene":Gene})
    ContigsGene.to_csv(prefix+".TBL", sep='\t', encoding='utf-8',header=True,index=None,float_format='%.2f')
    #os.system("cp {CDSratio} {TBL}".format(CDSratio=prefix+"_CDSRatio",TBL=prefix+".TBL"))
else:
    open(prefix+".fna","w")
    open(prefix+".faa","w")
    open(prefix+".TSV","w")
    open(prefix+".PNG","w")
    open(prefix+".GFF","w")
