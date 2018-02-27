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

# KitultLib
import BASICGraph
import TableDealer
        
def TaxPie(DF,
           Title="",
           xTitle="",
           yTitle="",
           Col="christmas",
           theme="seaborn",
           values=1,
           labels=0,
           nlab=3
          ):
    #Description:
    # Table look like Normal Matrix
    if labels == None:
        DF = pd.DataFrame({"Taxonomy":list(DF.index),"Values":DF.iloc[:,values]},columns=["Taxonomy","Values"])
    else:
        #DF = DF.rename(columns={DF.columns[int(labels)]:"Taxonomy"},inplace=True)
        DF = pd.DataFrame({"Taxonomy":DF.iloc[:,int(labels)],"Values":DF.iloc[:,int(values)]},columns=["Taxonomy","Values"])
    DF = DF.sort_values(by="Values",ascending=False)
    DF["Taxonomy"] = DF["Taxonomy"].replace("","Unassign")
    if len(DF["Taxonomy"]) >= int(nlab):
        Labels = list(DF["Taxonomy"][:int(nlab)])+list(np.repeat([""], [len(DF["Taxonomy"])-int(nlab)], axis=0)) # Labels, Display in Pie Graph
    else:
            Labels = DF["Taxonomy"]
    Labels = map(lambda x:[x,''][x=='Unassign'],Labels)# without 'Unassign' Label
    T = pd.DataFrame({"Taxonomy": Labels,"Values": DF["Values"]})
    p,fig = BASICGraph.BasicPie(T,Title=Title,xTitle=xTitle,yTitle=yTitle,colors=Col,theme=theme)
    return DF,p,fig
          
def TaxTOPBar(DF,
              Title="",
              xTitle="",
              yTitle="",
              Col="r",
              theme="seaborn",
              values=0,
              labels=None, # Means INDEX is the Labels Columns
              TOP=3
             ):
    # Description:
    # Make (Top) Bar Graph
    if labels == None:
        DF = pd.DataFrame({"Taxonomy":list(DF.index),"Values":DF[DF.columns[values]]},columns=["Taxonomy","Values"])
    else:
        DF.rename(columns={DF.columns[int(labels)]:"Taxonomy"},inplace=True)
        DF = pd.DataFrame({"Taxonomy":DF["Taxonomy"],"Values":DF[DF.columns[values]]},columns=["Taxonomy","Values"])
    DF = DF.sort_values(by="Values",ascending=False)
    DF["Taxonomy"] = DF["Taxonomy"].replace("","Unassign")
    if len(DF["Taxonomy"]) > int(TOP):
        top = DF.iloc[0:int(TOP),:]
    else:
        top = DF
    p,fig,color = BASICGraph.BasicBar(top,theme=theme,colorsets=Col,rotation=90,Title=Title,xTitle=xTitle,yTitle=yTitle)
    return top,p,fig

def TaxAbundStack(DF,
                  Title="",
                  xTitle="",
                  yTitle="",
                  Col="christmas",
                  theme="seaborn",
                  valueColumnsFrom = 0,
                  labels=None,  # Means INDEX is the Labels Columns
                  TOP=10,
                  Dominant=0.001
                 ):
    # Description:
    # Make Stack Bar Graph
    DominantCombine,Lst = TableDealer.DominantTable(DF,Dominant=Dominant) # Make Dominant Table
    if labels == None:
        TAX = pd.DataFrame({"Taxonomy":DominantCombine.index})
        TAX.index = DominantCombine.index
    else:
        TAX = pd.DataFrame({"Taxonomy":DominantCombine.iloc[:,int(labels)]})
    VAR = pd.DataFrame(DominantCombine.iloc[:,int(valueColumnsFrom):])
    DominantCombine=pd.concat([TAX,VAR],axis=1)
    del DominantCombine["Taxonomy"]
    DominantCombine["rowSUM"] = DominantCombine.T.sum()
    DominantCombine = DominantCombine.sort_values(by="rowSUM",ascending=False) # Sort by RowSum
    del DominantCombine["rowSUM"]
    DominantCombine = DominantCombine.rename(index={"": 'UnAssign'})
    #if len(DominantCombine.index) > int(TOP):
    #    top = DominantCombine.iloc[0:int(TOP),:]
    #else:
    #    top = DominantCombine
    #ReIndex = list(DominantCombine.index).remove("UnAssign") + ["UnAssign"]
    #ReIndex = list(DominantCombine.index).remove("Others") + ["Others"]
    #DominantCombine.reindex(ReIndex)
    p,fig,colors = BASICGraph.BasicStackBar(DominantCombine,Title=Title,xTitle=xTitle,yTitle=yTitle,theme=theme)
    return DominantCombine,Lst,fig



