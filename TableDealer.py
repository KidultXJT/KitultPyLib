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

#def TableCombine0(Anno,      # With many "Description" Columns, Like Taxonomy Levels 1-7
#                 vfilelist,  # Split by ",". Samples Valuse Table with single or Multi Valuse Columns, Such As mapping Result Plus Reads, Average Depth, Or TPM and so on.
#                 ColumNames, # Split by "," Such be equal to vfilelist. vfilelist = "A.txt,B.txt,C.txt" || ColumNames = "A,B,C" or "Column1,Column2,Column3"
#                 aKey=0, # To Combine "two" Tables, Such As Sequence ID (Unique)
#                 vKey=0,
#                 Description=-1,   # Anno
#                 Values=0          # vfilelist
#                ):
#    # Description::
#    # Anno Can be Taxonomy Assign
#    # Anno Can be Function Annotation
#    # vfilelist Can be TPM result, Coverage result and So on.
#    # Combine File for Frequency Abundance Relative Abundance TPM result And so on.
#    Anno = pd.read_table(Anno,sep="\t",index_col=int(aKey),header=None)
#    Anno.rename(columns={Anno.columns[int(Description)]:"Description"},inplace=True)
#    anno = Anno
#    lst = [anno] # Including Anno Table Valuse Tables RawAll Table(with np.nan)
#    for n in range(len(ColumNames.split(","))):
#        v = pd.read_table(vfilelist.split(",")[n],sep="\t",index_col=int(vKey))
#        v.columns = list(v.columns[:-1]) + [str(ColumNames.split(",")[n])]
#        lst.append(len(v))
#        Anno = pd.concat([Anno,v], axis=1, join='outer')
#    lst.append(Anno)
#    All = Anno.iloc[:,1:].replace(np.nan,0).join(Anno["Description"])
#    Set = Anno.dropna()
#    return(All,Set,lst)

def TableCombine(Anno,      # With many "Description" Columns, Like Taxonomy Levels 1-7
                 vfilelist,  # Split by ",". Samples Valuse Table with single or Multi Valuse Columns, Such As mapping Result Plus Reads, Average Depth, Or TPM and so on.
                 ColumNames, # Split by "," Such be equal to vfilelist. vfilelist = "A.txt,B.txt,C.txt" || ColumNames = "A,B,C" or "Column1,Column2,Column3"
                 aKey=0, # To Combine "two" Tables, Such As Sequence ID (Unique)
                 aheader = None,
                 Values = 1,
                 vKey=0,
                 vheader = None,
                 Description=-1   # Anno
                ):
    # Description::
    # Anno Can be Taxonomy Assign
    # Anno Can be Function Annotation
    # vfilelist Can be TPM result, Coverage result and So on.
    # Combine File for Frequency Abundance Relative Abundance TPM result And so on.
    Anno = pd.read_table(Anno,sep="\t",index_col=int(aKey),header=None)
    Anno.rename(columns={Anno.columns[int(Description)]:"Description"},inplace=True)
    Anno["Key"] = Anno.index
    anno = Anno
    lst = [anno] # Including Anno Table Valuse Tables RawAll Table(with np.nan)
    for n in range(len(ColumNames.split(","))):
        v = pd.read_table(vfilelist.split(",")[n],sep="\t",index_col=int(vKey),comment="#")
        v.rename(columns=lambda x:x.replace(v.columns[int(Values)-1],str(ColumNames.split(",")[n])), inplace=True)
        v = pd.DataFrame(v[str(ColumNames.split(",")[n])])
        lst.append(v)
        v["Key"] = list(v.index)
        Anno = pd.merge(v,Anno, on="Key",how="left",left_index=True)
    del Anno["Key"]
    All = Anno
    Set = Anno.dropna()
    return(All,Set,lst)

def TableGroupSUM(table, # Can be Come from "TableCombine()"
                  Description=-1 # GroupBy
                ):
    # Description::
    # Group SUM
    SUM = table.groupby(str(table.columns[int(Description)])).sum()
    return(SUM)

def FrequencyTable(table,# Can be Come from "TaxSplit()" or "TableCombine()" And So On
                   Description=0 # Extract
                ):
    # Description::
    # Extract Description Column 
    # Counter Frequence
    table = pd.DataFrame(table)
    if Description == None:
        table[-1] = table.index
        description=table[table.columns[int(-1)]]
    else:
        description= table[table.columns[int(Description)]]
    Freq = pd.DataFrame(Counter(np.array(description)).items()).sort_values(by=int(1),ascending=False)
    return(Freq)

def TaxSplit(table,# with Taxonomy Column like k__|p__|c__|o__|f__|g__|s__
             taxColumn=None, # TaxColumn is the table index or int(num) == table.iloc[:,int(num)]
             bc="d__,p__,c__,o__,f__,g__,s__",
             sep="|",
             levels="0,1,2,3,4,5,6" # Level 1 to Level 7
            ):
    # Description::
    # For Taxonomy Columns Split
    # 1. Make Split Taxonomy Columns
    # 2. Make GroupBy Levels Tables
    bclst = bc.split(",")
    if taxColumn == None:
        table[-1] = table.index
        tax=table[table.columns[int(-1)]]
        values=table.drop(-1,axis=1)
    else:
        tax=table[table.columns[int(taxColumn)]]
        values=pd.DataFrame(table.drop(table.columns[int(taxColumn)]),axis=1)
    values.index = list(range(len(values.index)))
    Tax = pd.DataFrame({"Kingdom" : tax.apply(lambda x:('').join(filter(lambda y:y.startswith(bclst[0]),x.split(str(sep)))).replace(bclst[0],"")),
                        "Phylum": tax.apply(lambda x:('').join(filter(lambda y:y.startswith(bclst[1]),x.split(str(sep)))).replace(bclst[1],"")),
                        "Class": tax.apply(lambda x:('').join(filter(lambda y:y.startswith(bclst[2]),x.split(str(sep)))).replace(bclst[2],"")),
                        "Order": tax.apply(lambda x:('').join(filter(lambda y:y.startswith(bclst[3]),x.split(str(sep)))).replace(bclst[3],"")),
                        "Family": tax.apply(lambda x:('').join(filter(lambda y:y.startswith(bclst[4]),x.split(str(sep)))).replace(bclst[4],"")),
                        "Genus": tax.apply(lambda x:('').join(filter(lambda y:y.startswith(bclst[5]),x.split(str(sep)))).replace(bclst[5],"")),
                        "Species": tax.apply(lambda x:('').join(filter(lambda y:y.startswith(bclst[6]),x.split(str(sep)))).replace(bclst[6],""))},
                       columns = ["Kingdom","Phylum","Class","Order","Family","Genus","Species"])
    Tax.index = list(range(len(Tax.index)))
    Tax = Tax.join(values)
    levels = levels.split(",")
    Lst = []
    for l in range(len(levels)):
        Lst.append(Tax.groupby(str(Tax.columns[l])).sum())       
    return(Tax,Lst)

def RelativeTable(table, # Can be GroupSUM() TaxSplit() ... result
                  valueColumnsFrom = 7
              ):
            # Description:
            # Make Relative Table
            for C in table.columns[int(valueColumnsFrom):]:
                    table[C] = table[C] / table[C].sum()
            Relative = table
            return Relative
        
def DominantTable(table, # Can be GroupSUM() ... result # Index was the Description
                  Dominant = 0.01
            ):
            # Description:
            # Make Dominant Table
            Lindex = []
            for C in table.columns:
                    Lindex.extend(list(table.index[table[str(C)]/sum(table[str(C)]) >= Dominant]))
            Lindex = list(set(Lindex))
            Dominant = table.ix[Lindex,:]
            Others = table.drop(Lindex)
            Lst = [Dominant,Others]
            #Dominant.append(Others.sum(), ignore_index=True)
            Dominant.loc["Others"]  = Others.sum()
            DominantCombine = Dominant
            return DominantCombine,Lst
        
 