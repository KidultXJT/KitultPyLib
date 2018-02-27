#!usr/bin/python
# -*- coding:utf-8 -*-

## --------------------------------------------------------
## Author: Kidult
## Email : junting.xie@sagene.com.cn
## Date  : 2017-11-10
## --------------------------------------------------------
## Description: 
## Dealing the Fasta
## 

# module
import sys
import os
import re
# Data
import pandas as pd
import numpy as np
from collections import Counter
# KitultLib
import BASICGraph

## ------------------------------------------------------------------ Information ----------------------------------------------------------------------- ##

## GC ratio
def GC(seq):
    # Description:
    # Calculate GC ratio with a Sequence
    gc = (seq.upper().count("G") + seq.upper().count("C"))/len(seq)
    return gc

## A,T,C,G

## Length

## k-mer

## ------------------------------------------------------------------------------------------- Format Problem --------------------------------------------------------------------------------------------------- ##
def formatFA1(infa,                                   
                             rename=None):
                             # Description:
                             # Format \n to None And Rename // yinsijun
                             # BUT have memery Problem
                             open(str(infa.split('.fa')[0])+".format.fa",'w').write('>'+'\n>'.join(map(lambda a:'\n'.join(a),[[str(rename)+"_"+str(x),y[1].upper().replace('\n','')] for x,y in enumerate(map(lambda x:x.split('\n',1),open(infa).read().split('\n>')))]))+'\n')
            
def formatFA2(infa,                                   
                              rename=None):
                              # Description:
                              # Format \n to None And Rename, AND return Num of Sequence // gonghao
                              # Num
                              i = iter(zip(['']+['\n' for i in xrange(0,10000)], xrange(0,10000)))
                              return len([open(str(infa.split('.fa')[0])+".format.fa",'a').write(line.strip() if '>' != line[0] else '{0[0]}>{rename}_{0[1]}\n'.format(i.next(),rename=rename)) for f in [open(infa)] for line in f])
                    
def formatFA3(infa,                                   
                              rename=None):
                              # Description:
                              # Format \n to None And Rename, AND return Num of Sequence // yangliyan
                              # Rebuild a Class
                              class new(int):
                                    def __init__(self):
                                        self.count = 0
                                    def __repr__(self):
                                        return str(self.count)
                                    def __str__(self):
                                        return str(self.count)
                                    def up(self):
                                        self.count += 1
                                        return self.count
                              a = new()
                              return len([open(str(infa.split('.fa')[0])+".format.fa", 'a').write(i) for i in [line.strip() if line[0] != '>' else line.split('\t')[0].split('_')[0].replace('S1', 'S2') + '_' + str(a.up()) + '\n' if a.count==0 else '\n' + line.split('\t')[0].split('_')[0].replace('S1', 'S2') + '_' + str(a.up()) + '\n' for line in open(infa)]])

def formatFA4(infa,
                            # Description:
                            # Format \n to None And Rename, AND return Num of Sequence // xiejunting // FOR MetaG
                            rename=None,
                            out=None):
                            # Out Name
                            if out != None:
                                out = out
                            else:
                                out = str(infa.split('.fa')[0])+".format.fa"
                            # Rename or Not
                            if rename == None:
                                    i = iter(zip(['']+['\n' for i in xrange(0,100000000)], xrange(0,100000000)))
                                    return len([open(out,'a').write(line.strip() if '>' != line[0] else '{0[0]}{line}\n'.format(i.next(),line=line.strip())) for line in open(infa)])
                            else:
                                    i = iter(zip(['']+['\n' for i in xrange(0,100000000)], xrange(0,100000000)))
                                    return len([open(out,'a').write(line.strip() if '>' != line[0] else '{0[0]}>{rename}_{0[1]}\n'.format(i.next(),rename=rename)) for line in open(infa)])
                                
def formatFA(infa,
             # Description:
             # Read All
             rename=None,
             out=None,
             slum=True
    ):
    # Out Name
    if out != None:
        out = out
    else:
        out = str(infa.split('.fa')[0])+".format.fa"
    if slum:# Rename or Not
        List = []
        if rename == None:
            for x,y in enumerate(map(lambda x:x.split('\n',1),open(infa).read().split('\n>'))):
                ID = y[0]
                seq = y[1].upper().replace("\n","")
                List.append([ID,seq])
            fa = (">"+"\n>".join(map(lambda a:"\n".join(a),List))+"\n")[1:]
        else:
            for x,y in enumerate(map(lambda x:x.split('\n',1),open(infa).read().split('\n>'))):
                ID = str(rename)+"_"+str(x)
                seq = y[1].upper().replace("\n","")
                List.append([ID,seq])
            fa =  ">"+"\n>".join(map(lambda a:"\n".join(a),List))+"\n"
    else:
        print "Not Ready ~"
    open(out,'a').write(fa)
    OutLst = [len(fa),fa]
    return OutLst
                            
## ---------------------------------------------------------------------  Distribution ------------------------------------------------------------------------------- ##
## --------------------------------------------------------------------- Length >>>>>>>>>>>>>>>>>>>>>>>>>>>>
def faLength(infa,
                           out=None,
                           Max=5000,
                           Min=1000,
                           Title="Length Distribution",
                           xTitle="Length(nt)",
                           yTitle="Counts",
                           Col="c"):
             # Description:
             # make a Length Summary to make a Distribution Graph // xiejunting
            # Length
            #data=sorted([int(len(y[1])) for x,y in enumerate(map(lambda x:x.split("\n",1),open(infa).read().split('\n>')))],reverse=False)# memory problem  \\ xiejunting 2017-11-24 
            data = sorted([int(len(line.strip())) for f in [open(infa)] for line in f if  ">" != line[0]]) # fix the memory Problem \\ xiejunting 2017-11-25
            # N50
            N50=data[list(np.cumsum(np.cumsum(data) > sum(data)/2)).index(1)]
            # Length Distribution
            df = pd.DataFrame(Counter(np.array(data)).items()).sort_values(by=[0])
            Data = data
            # Make Distribution Graph
            if max(data) < Max:
                Max=max(data)
            else:
                Max=Max
                data=[min(i, Max) for i in  data]
            p,fig = BASICGraph.BasicHist(data=data,xmax=Max,xmin=Min,Title=Title,yTitle=yTitle,xTitle=xTitle,color=Col)
            if out != None:
                # Make Distribution Table
                df.columns = ['Length(nt)','Counts']
                df.to_csv(out+"_Length", sep='\t', encoding='utf-8',header=True,index=None)
                ## SAVE PNG
                fig.savefig(out+"_Length.PNG",dpi=100)
            return Data,N50,p,fig
        
## ----------------------------------------------- GC Ratio >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>       
def faGCratio(infa,
                           out=None,
                           Title="GC Distribution",
                           xTitle="GC Ratio (%)",
                           yTitle="Counts"):
             # Description:
             # make a Length Summary to make a Distribution Graph // xiejunting
            # GC Ratio
            def GC(seq):
                    # Description:
                    # Calculate GC ratio with a Sequence
                    gc = (float(seq.upper().count("G") + seq.upper().count("C"))/len(seq))*100   # Pay attention , should be float  // xiejunting  2017-11-25 
                    return float(gc)
            data = [GC(line.strip()) for f in [open(infa)] for line in f if  ">" != line[0]]
            # Length Distribution
            df = pd.DataFrame(Counter(np.array(data)).items()).sort_values(by=[0])
            # Make Distribution Graph    
            p,fig = BASICGraph.BasicHist(data=data,xmax=max(data),xmin=min(data),n=100,rwidth=1,Title=Title,xTitle=xTitle,yTitle=yTitle,color="gold")
            if out != None:
                # Make Distribution Table
                df.columns = ['GC Ratio (%)','Counts']
                df.to_csv(out+"_GC", sep='\t', encoding='utf-8',header=True,index=None)
                ## SAVE PNG
                fig.savefig(out+"_GC.PNG",dpi=100)
            return data,p,fig

def faNratio(infa,
                         out=None,
                         Title="Ratio Distribution",
                         xTitle="Ratio (%)",
                         yTitle="Counts",
                         NT = "A" # Canbe A T C G
            ):
             # Description:
             # make a Length Summary to make a Distribution Graph // xiejunting
            # GC Ratio
            def N(seq,
                        N = "A"):
                    # Description:
                    # Calculate N(A/T/C/G) ratio with a Sequence
                    n = (float(seq.upper().count(N))/len(seq))*100   # Pay attention , should be float  // xiejunting  2017-11-25 
                    return float(n)
            data = [N(line.strip(),N=NT) for f in [open(infa)] for line in f if  ">" != line[0]]
            # Length Distribution
            df = pd.DataFrame(Counter(np.array(data)).items()).sort_values(by=[0])
            # Make Distribution Graph    
            p,fig = BASICGraph.BasicHist(data=data,xmax=max(data),xmin=min(data),n=100,rwidth=1,Title=NT+Title,xTitle=NT+xTitle,yTitle=yTitle,color="gray")
            if out != None:
                # Make Distribution Table
                df.columns = ['{N} Ratio (%)'.format(N=NT),'Counts']
                df.to_csv(out+"_{N}".format(N=NT), sep='\t', encoding='utf-8',header=True,index=None)
                ## SAVE PNG
                fig.savefig(out+"_{N}.PNG".format(N=N),dpi=100)
            return data,p,fig

## ------------------------------------------------------------------- Reverse && Compliment ------------------------------------------------------------------------ ##

             
## ------------------------------------------------------------------- FNA to FAA -------------------------------------------------------------- ##
            
            
## ------------------------------------------------------------------- Extract Sequence ------------------------------------------------------------------------ ##

## By Sequence ID

## By Max Length

## By GC Ratio

## By sort sequence MATCH


############################## Evaluation ###################################
def makeSUM(infa,
                             Max=5000, # for Length
                             Min=1000,   # for Length
                             out=None,
                             ColumnsName = "-"
           ):
    # Description :
    # Make Summary Table
    EvLst = []
    GCData,GCp,GCfig =faGCratio(infa=infa,out=out)
    LengthData,N50,Lengthp,Lengthfig = faLength(infa=infa,out=out,Max=5000)
    # Make Length Summary
    NumCounts = len(LengthData)
    EvLst.append(NumCounts)
    MinLength = min(LengthData)
    EvLst.append(MinLength)
    MaxLength = max(LengthData)
    EvLst.append(MaxLength)
    MeanLength = np.mean(LengthData)
    EvLst.append(MeanLength)
    MedianLength = np.median(LengthData)
    EvLst.append(MedianLength)
    EvLst.append(N50)
    Base = pd.DataFrame(LengthData).sum()[0]
    EvLst.append(Base)
    # Make GC Summary
    MinGC = min(GCData)
    EvLst.append(MinGC)
    MaxGC = max(GCData)
    EvLst.append(MaxGC)
    MeanGC = np.mean(GCData)
    EvLst.append(MeanGC)
    MedianGC = np.median(GCData)
    EvLst.append(MedianGC) 
    EvTable = pd.DataFrame(EvLst)
    EvTable[0] = EvTable[0].map(lambda  x:("%.2f")%x)
    EvTable.index = ["NumCounts","Min Length (bp)","Max Length (bp)","Mean Length (bp)","Median Length (bp)","N50 (bp)","Basas","Min GC (%)","Max GC (%)","Mean GC (%)","Median GC (%)"]
    EvTable.columns = [str(ColumnsName)]
    Lst = [LengthData,N50,Lengthp,Lengthfig,GCData,GCp,GCfig]
    return EvTable,Lst