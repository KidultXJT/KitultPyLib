from __future__ import division
# module
import sys
import os
import re
# Data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from collections import Counter

# Personal Lib
import BASICGraph
import forSum


def AnnoAbundTable(anno, # Columns 1 should be the Sequence ID(Unique)
                                           covs, # Columns 1 should be the Sequence ID(Unique) including all the anno Sequence ID(Unique)
                                           smp,
                                           values = "TPM",
                                           labels = "Name"
                  ):
    # Description
    # make AnnoAbundance Table
    # make Unassign Assign list
    Anno = pd.read_table(anno,sep="\t")
    Anno.columns = ["Name"]+list(Anno.columns[1:])
    covfilelst = covs.split(",")
    smplist = smp.split(",")
    samples = []
    assign = []
    unassign = []
    ALL = []
    T = []
    ANNO = Anno
    for i in range(len(covfilelst)):
        cov = covfilelst[i]
        c = pd.read_table(cov,sep="\t")
        c.columns = ["Name"]+list(c.columns[1:]) # column 1 should be the Sequence ID(Unique ID can match the covs Sequence ID)
        tpm = pd.DataFrame({"Name":c[str(labels)],str(smplist[i]):c[str(values)]}) # 414 == All input query
        tpm = tpm.loc[tpm[str(smplist[i])] > 0] # have this Gene in this Covfile 
        All = len(tpm.index)                                     # sample have Num of Gene
        ALL.append(All)
        samples.append(str(smplist[i]))
        #TPM = pd.merge(Anno,tpm,how="right",on="Name") 
        TPM = pd.concat([Anno, tpm], axis=1, join='outer') # CovFile have all the Sequence ID(Unique) - combine Anno and All samples Covfile Table
        a = pd.concat([ANNO, tpm], axis=1, join='inner')      # Anno only
        T.append(a)
        #a = Anno.join(tpm, on="Name", how='inner')
        assign.append(len(a.index))
        unassign.append((All - len(a.index)))
        Anno = TPM
        AssignLst = [ALL,assign,unassign,samples]
    return TPM,AssignLst

def AnnoAssignPie(anno, # Columns 1 should be the Sequence ID(Unique)
                                      covs, # Columns 1 should be the Sequence ID(Unique) including all the anno Sequence ID(Unique)
                                      smp,
                                      values = "TPM",
                                      labels = "Name",
                                      Groupby = "target"
                 ):
                # Description:
                # EzAnno
                # make Assign Unassign Result
                # make GeneAbundance Table
                # extract Groupby Target Table
                smplist = smp.split(",")
                TPM,AssignLst = AnnoAbundTable(anno=anno,covs =covs,smp=smp,values=values,labels=labels)
                tpmSUM = pd.DataFrame(TPM.groupby(Groupby).sum())  # target protein_id descriptions
                AStable = pd.DataFrame({"Samples":AssignLst[3],"All":AssignLst[0],"Assign":AssignLst[1],"Unassign":AssignLst[2]},columns=["Samples","All","Assign","Unassign"]).T
                AStable["Labels"] = AStable.index
                AStable.columns = AStable.loc["Samples"]
                AStable = pd.DataFrame(AStable.iloc[1:,:],columns=["Samples"]+smplist)
                astable = AStable.iloc[1:,:]
                graph = []
                for n in range(len(AStable.columns))[1:]:
                    p,fig = BASICGraph.BasicPie(astable,values=int(n),labels=0,Title="",yTitle=str(smplist[n-1]))
                    graph.append([p,fig])
                return TPM,tpmSUM,AStable,graph

def FunfreqHBar(anno, # Columns 1 should be the Sequence ID(Unique)
                                  covs, # Columns 1 should be the Sequence ID(Unique) including all the anno Sequence ID(Unique)
                                  smp,
                                  out = None,
                                  Key = "description",
                                  Title = "Function Frequency",
                                  xTitle = "Frequency",
                                  yTitle = "Function Description"
                 ):
                # Description:
                # EzAnno
                # make Frequency Result
                smplist = smp.split(",")
                TPM,AssignLst = AnnoAbundTable(anno=anno,covs =covs,smp=smp)
                graph = []
                freq = []
                for n in range(len(smplist)):
                    t = TPM.loc[TPM[str(smplist[n])] > 0]
                    if out != None:
                        df,p = forSum.freqHBar(data=t[str(Key)],out="./{smp}".format(smp=smplist[n]),Title=Title,xTitle=xTitle,yTitle=yTitle)
                    else:
                        df,p,fig = forSum.freqHBar(data=t[str(Key)],Title=Title,xTitle=xTitle,yTitle=yTitle)
                    graph.append([p,fig])
                    freq.append(df)
                return freq,graph
                
def FunAbundHBar(anno, # Columns 1 should be the Sequence ID(Unique)
                 covs, # Columns 1 should be the Sequence ID(Unique) including all the anno Sequence ID(Unique)
                 smp,
                 out = None,
                 Key = "description",
                 Title = "Function Abundance(TPM)",
                 xTitle = "TPM",
                 yTitle = "Function Description",
                 colorsets = "christmas"
                ):
                # Description:
                # EzAnno
                # make Abundance Result
                smplist = smp.split(",")
                TPM,AssignLst = AnnoAbundTable(anno=anno,covs =covs,smp=smp)
                graph = []
                Abund = []
                for n in range(len(smplist)):
                    t = TPM.loc[TPM[str(smplist[n])] > 0]
                    table = t.groupby(str(Key)).sum()
                    df = pd.DataFrame(table[str(smplist[n])])
                    df = pd.DataFrame({0:df.index,1:df.iloc[:,0]}).sort_values(by=int(1),ascending=True)
                    if out != None:
                        p,fig,color = BASICGraph.BasicHBar(df=df,Title=Title,yTitle=yTitle,xTitle=xTitle,colorsets=colorsets)
                    else:
                        p,fig,color = BASICGraph.BasicHBar(df=df,Title=Title,yTitle=yTitle,xTitle=xTitle,colorsets=colorsets)
                    graph.append([p,fig])
                    Abund.append([smplist[n],df])
                return TPM,Abund,graph