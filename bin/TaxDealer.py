import pandas as pd
import sys
import os
import matplotlib.pyplot as plt
# personal library
import forTaxonomy
import BASICGraph
import TableDealer

tax      = sys.argv[1]
covs    = sys.argv[2]
pkms  = sys.argv[3]
smp    =  sys.argv[4]
out      = sys.argv[5]
Top      = sys.argv[6] # Not Yet ~ !


Levels  = ["Kingdom","Phylum","Class","Order","Family","Genus","Species"]
covlst   = covs.split(",")
smplst = smp.split(",")

if len(open(tax).read()) != 0 :
    # Average Depth
    AvgDepthAll,AvgDepthSet,AvgDepthlst = TableDealer.TableCombine(Anno=tax,vfilelist=covs,ColumNames=smp)
    AvgDepthSUM = TableDealer.TableGroupSUM(AvgDepthAll)
    AvgDepthTax,AvgDepthLst= TableDealer.TaxSplit(AvgDepthSUM)
    os.mkdir(out+"/AvgDepth/")
    AvgDepthTax.to_csv(out+"/AvgDepth/"+"AvgDepth.xls", sep='\t', encoding='utf-8',header=True,index=None)
    os.mkdir(out+"/AvgDepth/RelativeAbundance")
    for t in range(len(AvgDepthLst)):
        AvgDepthLst[t].to_csv(out+"/AvgDepth/"+Levels[t]+".xls", sep='\t', encoding='utf-8',header=True)
        AvgRelative = TableDealer.RelativeTable(AvgDepthTax).groupby(Levels[t]).sum()
        AvgRelative.to_csv(out+"/AvgDepth/RelativeAbundance/"+Levels[t]+".RelativeAbundance.xls", sep='\t', encoding='utf-8',header=True)
        fig = plt.figure()
        DominantCombine,DominantLst,fig = forTaxonomy.TaxAbundStack(DF=AvgRelative.sort_values(str(AvgRelative.columns[0]),ascending=False),labels=None,Dominant=0.05)
        fig.savefig(out+"/AvgDepth/RelativeAbundance/"+Levels[t]+"_StackBar.PNG",dpi=100)
        fig.savefig(out+"/AvgDepth/RelativeAbundance/"+Levels[t]+"_StackBar.PDF")
        plt.close("all")
        for s in range(len(smplst)):
            #Abundance [Pie]
            DF,p,fig = forTaxonomy.TaxPie(AvgDepthLst[t],values=int(s),labels=None)
            fig.savefig(out+"/AvgDepth/"+Levels[t]+"."+str(AvgDepthLst[t].columns[int(s)])+"_Pie.PNG",dpi=100)
            fig.savefig(out+"/AvgDepth/"+Levels[t]+"."+str(AvgDepthLst[t].columns[int(s)])+"_Pie.PDF")
            top,p,fig = forTaxonomy.TaxTOPBar(AvgDepthLst[t],values=int(s),labels=None,TOP=10) 
            fig.savefig(out+"/AvgDepth/"+Levels[t]+"."+str(AvgDepthLst[t].columns[int(s)])+"_Top10Bar.PNG",dpi=100)
            fig.savefig(out+"/AvgDepth/"+Levels[t]+"."+str(AvgDepthLst[t].columns[int(s)])+"_Top10Bar.PDF")
            plt.close("all")
    # FPKM
    FPKMAll,FPKMSet,FPKMlst = TableDealer.TableCombine(Anno=tax,vfilelist=pkms,ColumNames=smp,Values=7)
    FPKMSUM = TableDealer.TableGroupSUM(FPKMAll)
    FPKMTax,FPKMLst= TableDealer.TaxSplit(FPKMSUM)
    os.mkdir(out+"/FPKM/")
    FPKMTax.to_csv(out+"/FPKM/"+"FPKM.xls", sep='\t', encoding='utf-8',header=True,index=None)
    os.mkdir(out+"/FPKM/RelativeAbundance")
    for t in range(len(FPKMLst)):
        FPKMLst[t].to_csv(out+"/FPKM/"+Levels[t]+".xls", sep='\t', encoding='utf-8',header=True)
        FPKMRelative = TableDealer.RelativeTable(FPKMTax).groupby(Levels[t]).sum()
        FPKMRelative.to_csv(out+"/FPKM/RelativeAbundance/"+Levels[t]+".RelativeAbundance.xls", sep='\t', encoding='utf-8',header=True)
        fig = plt.figure()
        DominantCombine,DominantLst,fig = forTaxonomy.TaxAbundStack(DF=FPKMRelative.sort_values(str(FPKMRelative.columns[0]),ascending=False),labels=None,Dominant=0.05)
        fig.savefig(out+"/FPKM/RelativeAbundance/"+Levels[t]+"_StackBar.PNG",dpi=100)
        fig.savefig(out+"/FPKM/RelativeAbundance/"+Levels[t]+"_StackBar.PDF")
        plt.close("all")
        for s in range(len(smplst)):
            #Abundance [Pie]
            DF,p,fig = forTaxonomy.TaxPie(FPKMLst[t],values=int(s),labels=None)
            fig.savefig(out+"/FPKM/"+Levels[t]+"."+str(FPKMLst[t].columns[int(s)])+"_Pie.PNG",dpi=100)
            fig.savefig(out+"/FPKM/"+Levels[t]+"."+str(FPKMLst[t].columns[int(s)])+"_Pie.PDF")
            top,p,fig = forTaxonomy.TaxTOPBar(FPKMLst[t],values=int(s),labels=None,TOP=10) 
            fig.savefig(out+"/FPKM/"+Levels[t]+"."+str(FPKMLst[t].columns[int(s)])+"_Top10Bar.PNG",dpi=100)
            fig.savefig(out+"/FPKM/"+Levels[t]+"."+str(FPKMLst[t].columns[int(s)])+"_Top10Bar.PDF")
            plt.close("all")
    # RPKM
    RPKMAll,RPKMSet,RPKMlst = TableDealer.TableCombine(Anno=tax,vfilelist=pkms,ColumNames=smp,Values=5)
    RPKMSUM = TableDealer.TableGroupSUM(RPKMAll)
    RPKMTax,RPKMLst= TableDealer.TaxSplit(RPKMSUM)
    os.mkdir(out+"/RPKM/")
    RPKMTax.to_csv(out+"/RPKM/"+"RPKM.xls", sep='\t', encoding='utf-8',header=True,index=None)
    os.mkdir(out+"/RPKM/RelativeAbundance")
    for t in range(len(RPKMLst)):
        RPKMLst[t].to_csv(out+"/RPKM/"+Levels[t]+".xls", sep='\t', encoding='utf-8',header=True)
        RPKMRelative = TableDealer.RelativeTable(RPKMTax).groupby(Levels[t]).sum()
        RPKMRelative.to_csv(out+"/RPKM/RelativeAbundance/"+Levels[t]+".RelativeAbundance.xls", sep='\t', encoding='utf-8',header=True)
        # Relative Abundance Stack 
        fig = plt.figure()
        DominantCombine,DominantLst,fig = forTaxonomy.TaxAbundStack(DF=RPKMRelative.sort_values(str(RPKMRelative.columns[0]),ascending=False),labels=None,Dominant=0.05)
        fig.savefig(out+"/RPKM/RelativeAbundance/"+Levels[t]+"_StackBar.PNG",dpi=100)
        fig.savefig(out+"/RPKM/RelativeAbundance/"+Levels[t]+"_StackBar.PDF")
        plt.close("all")
        for s in range(len(smplst)):
            #Abundance [Pie]
            DF,p,fig = forTaxonomy.TaxPie(RPKMLst[t],values=int(s),labels=None)
            fig.savefig(out+"/RPKM/"+Levels[t]+"."+str(RPKMLst[t].columns[int(s)])+"_Pie.PNG",dpi=100)
            fig.savefig(out+"/RPKM/"+Levels[t]+"."+str(RPKMLst[t].columns[int(s)])+"_Pie.PDF")
            top,p,fig = forTaxonomy.TaxTOPBar(RPKMLst[t],values=int(s),labels=None,TOP=10) 
            fig.savefig(out+"/RPKM/"+Levels[t]+"."+str(RPKMLst[t].columns[int(s)])+"_Top10Bar.PNG",dpi=100)
            fig.savefig(out+"/RPKM/"+Levels[t]+"."+str(RPKMLst[t].columns[int(s)])+"_Top10Bar.PDF")
            plt.close("all")
    # Reads
    ReadAll,ReadSet,Readlst = TableDealer.TableCombine(Anno=tax,vfilelist=pkms,ColumNames=smp,Values=4)
    ReadSUM = TableDealer.TableGroupSUM(ReadAll)
    ReadTax,ReadLst= TableDealer.TaxSplit(ReadSUM)
    os.mkdir(out+"/Reads/")
    ReadTax.to_csv(out+"/Reads/"+"Reads.xls", sep='\t', encoding='utf-8',header=True,index=None)
    os.mkdir(out+"/Reads/RelativeAbundance")
    for t in range(len(ReadLst)):
        ReadLst[t].to_csv(out+"/Reads/"+Levels[t]+".xls", sep='\t', encoding='utf-8',header=True)
        ReadRelative = TableDealer.RelativeTable(ReadTax).groupby(Levels[t]).sum()
        ReadRelative.to_csv(out+"/Reads/RelativeAbundance/"+Levels[t]+".RelativeAbundance.xls", sep='\t', encoding='utf-8',header=True)
        # Relative Abundance Stack 
        fig = plt.figure()
        DominantCombine,DominantLst,fig = forTaxonomy.TaxAbundStack(DF=ReadRelative.sort_values(str(ReadRelative.columns[0]),ascending=False),labels=None,Dominant=0.05)
        fig.savefig(out+"/Reads/RelativeAbundance/"+Levels[t]+"_StackBar.PNG",dpi=100)
        fig.savefig(out+"/Reads/RelativeAbundance/"+Levels[t]+"_StackBar.PDF")
        plt.close("all")
        for s in range(len(smplst)):
            #Abundance [Pie]
            DF,p,fig = forTaxonomy.TaxPie(ReadLst[t],values=int(s),labels=None)
            fig.savefig(out+"/Reads/"+Levels[t]+"."+str(ReadLst[t].columns[int(s)])+"_Pie.PNG",dpi=100)
            fig.savefig(out+"/Reads/"+Levels[t]+"."+str(ReadLst[t].columns[int(s)])+"_Pie.PDF")
            top,p,fig = forTaxonomy.TaxTOPBar(ReadLst[t],values=int(s),labels=None,TOP=10) 
            fig.savefig(out+"/Reads/"+Levels[t]+"."+str(ReadLst[t].columns[int(s)])+"_Top10Bar.PNG",dpi=100)
            fig.savefig(out+"/Reads/"+Levels[t]+"."+str(ReadLst[t].columns[int(s)])+"_Top10Bar.PDF")
            plt.close("all")
else:
    open(prefix+".PNG","w")
    open(prefix+".xls","w")
