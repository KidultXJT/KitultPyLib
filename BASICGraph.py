from __future__ import division
# Graph Module
import numpy as np
import pandas as pd
from scipy import stats, integrate
# Graph
## matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.mlab as mlab
import matplotlib.path as path
from matplotlib import colors as mcolors  # Colors
from matplotlib.transforms import blended_transform_factory
## seaborn
import seaborn as sns
# OrderDict
from collections import OrderedDict

# Presonal Library
import colSet

## ------------------------------------------------------------------------- Basic Graph ------------------------------------------------------------------------------------ ##

## ---------------------------------------------- Distribution ---------------------------------------------- ##
## ====== Histogram ====== ##
## Length GC ...
def BasicHist(data,
                           width=1.5,
                           height=1,
                           xmin=0,                         # xlim and AddLineX 
                           xmax=1000,                 # xlim and AddLIneX
                           #ymax=0,                       # AddLiney
                           n=20,                             # bins    
                           alpha=0.7,
                           rwidth=0.7,
                           color="c",                    # colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
                           Title = "Histograms",
                           TitleSize=20,
                           xTitle="",
                           xTitleSize=15,
                           yTitle="",
                           yTitleSize=15,
                           theme="seaborn",    # Style label :: default,classic,bmh,dark_background,fivethirtyeight,ggplot,grayscale,seaborn,seaborn-bright,seaborn-colorblind,seaborn-dark,seaborn-dark-palette,seaborn-darkgrid,seaborn-deep,seaborn-muted,seaborn-notebook,seaborn-paper,seaborn-pastel,seaborn-poster,seaborn-talk,seaborn-ticks,seaborn-white,seaborn-whitegrid
                           #Linecolor="tomato",
                           #Linewidth=1,
                           #Linestyles='--',   # - line -- dotted -. and so on 
                           #AddLineX=0,     # Zero means None
                           #AddLineY=0
             ):
        with plt.style.context(theme):
            data=np.array(data)
            # Setting fig size
            (fig_width, fig_height) = plt.rcParams['figure.figsize']
            fig_size = [fig_width*width, fig_height*height]
            fig, ax    = plt.subplots(figsize=fig_size)#, squeeze=True)
            plt.subplots_adjust(bottom=0.15,left=0.15)
            # Axis
            ## Title
            ax.set_title(Title,fontsize=TitleSize)
            ax.set_ylabel(yTitle,fontsize=yTitleSize,color="dimgray")
            ax.set_xlabel(xTitle,fontsize=xTitleSize,color="dimgray")
            ax.grid(True) 
            ## axis
            plt.xlim([xmin,xmax])
            # Plot
            if xmax <= 1:
                xmax = 0.05
                xmin  = 0
            ax.hist(data, bins=abs(int(max(data)/(xmax-xmin)))*n, alpha=alpha,rwidth=rwidth,color=color)
            #plt.hlines(AddLineY,0,ymax,colors=Linecolor,linewidth=Linewidth,linestyles=Linestyles)
            #plt.hlines(AddLineX,xmin,xmax,colors=Linecolor,linewidth=Linewidth,linestyles=Linestyles)
        return ax,fig

    
def BasicBar(df,
                          width=1,
                          height=1.0,
                          alpha=0.8,
                          rwidth=0.5,
                          colorsets="metal",    # sci, free, sy, kidult
                          Title = "Bar Chart",
                          TitleSize=20,
                          xTitle="",
                          xTitleSize=15,
                          yTitle="",
                          yTitleSize=15,
                          theme="seaborn",
                          rotation=0,
                          yscale=None
             ):
        with plt.style.context(theme):
            # Setting fig size
            (fig_width, fig_height) = plt.rcParams['figure.figsize']
            fig_size = [fig_width*width, fig_height*height]
            fig, ax    = plt.subplots(figsize=fig_size)#, squeeze=True)
            fig.subplots_adjust(bottom=0.4)
            # Axis
            ## Title
            ax.set_title(Title,fontsize=TitleSize)
            ax.set_ylabel(yTitle,fontsize=yTitleSize,color="dimgray")
            ax.set_xlabel(xTitle,fontsize=xTitleSize,color="dimgray")
            ax.grid(True)
            # Plot
            plt.xticks(range(len(df.iloc[:,0])), df.iloc[:,0],rotation=rotation)
            if colorsets not in ["ocean","pantone","green","christmas","no1","no2","sci1","sci2","stone","ai","metal","bitch"]:
                colors = colorsets
                ax.bar(range(len(df.iloc[:,0])), df.iloc[:,1],# align='center',
                       alpha=alpha,width=rwidth,color=colors)
            else:
                bars = ax.bar(range(len(df.iloc[:,0])), df.iloc[:,1], #align='center', 
                              alpha=alpha,width=rwidth)
                colors = colSet.colSet10(name=colorsets)*100
                for i, bar in enumerate(bars):
                    bar.set_color(colors[i])
        return ax,fig,colors
    
def BasicHBar(df,
                             width=.8,
                             height=1.4,
                             alpha=0.8,
                             rwidth=0.5,
                             colorsets="yellowgreen",    # sci, free, sy, kidult
                             Title = "Bar Chart",
                             TitleSize=20,
                             xTitle="",
                             xTitleSize=15,
                             yTitle="",
                             yTitleSize=15,
                             theme="seaborn",
                             xrotation=0,
                             yrotation=45,
                             yscale=None
             ):
        with plt.style.context(theme):
            # Setting fig size
            (fig_width, fig_height) = plt.rcParams['figure.figsize']
            fig_size = [fig_width*width, fig_height*height]
            fig, ax    = plt.subplots(figsize=fig_size)#, squeeze=True)
            #plt.subplots_adjust(bottom=0.15,left=0.15)
            fig.subplots_adjust(left=0.35,right=.9, wspace=0.25, hspace=0.25,bottom=0.13, top=0.91)
            # Axis
            ## Title
            ax.set_title(Title,fontsize=TitleSize)
            ax.set_ylabel(yTitle,fontsize=yTitleSize,color="dimgray")
            ax.set_xlabel(xTitle,fontsize=xTitleSize,color="dimgray")
            ax.grid(True)
            # Plot
            plt.yticks(range(len(df.iloc[:,0])), df.iloc[:,0],rotation=xrotation)
            plt.xticks(rotation = yrotation)
            if colorsets not in ["ocean","pantone","green","christmas","no1","no2","sci1","sci2","stone","ai","metal","bitch"]:
                colors = colorsets
                ax.barh(range(len(df.iloc[:,0])), df.iloc[:,1], align='center', alpha=alpha,color=colorsets)
            else:
                bars = ax.barh(range(len(df.iloc[:,0])), df.iloc[:,1], align='center', alpha=alpha)#,width=rwidth)
                colors = colSet.colSet10(name=colorsets)*100
                for i, bar in enumerate(bars):
                    bar.set_color(colors[i])
        return ax,fig,colors    

    
def BasicScatter(X,
                                 Y,
                                 Col,
                                 Size,
                                 width=1,
                                 height=1,
                                 alpha=0.5,
                                 ecolor="grey",
                                 cmap = "OrRd", # Accent,Blues,BrBG,BuGn,BuPu,CMRmap,Dark2,GnBu,Greens,Greys,OrRd,Oranges,PRGn,Paired,Pastel1,Pastel2,PiYG,PuBu,PuBuGn,PuOr,PuRd,Purples,RdBu,RdGy,RdPu,RdYlBu,RdYlGn,Reds,Set1,Set2,Set3,Spectral,Wistia,YlGn,YlGnBu,YlOrBr,YlOrRd,afmhot,autumn,binary,bone,brg,bwr,cool,coolwarm,copper,cubehelix,flag,gist_earth,gist_gray,gist_heat,gist_ncar,gist_rainbow,gist_stern,gist_yarg,gnuplot,gnuplot2,gray,hot,hsv,cefire,nferno,jet,agma,ako,nipy_spectral,ocean,pink,lasma,prism,rainbow,ocket,seismic,spring,summer,tab10,tab20,tab20b,tab20c,terrain,iridis,lag,winter
                                 Title = "Scatter Chart",
                                 TitleSize=20,
                                 xTitle="X",
                                 xTitleSize=15,
                                 yTitle="Y",
                                 yTitleSize=15,
                                theme="seaborn"
             ):
        with plt.style.context(theme):
            # Setting fig size
            (fig_width, fig_height) = plt.rcParams['figure.figsize']
            fig_size = [fig_width*width*0.7*0.9, fig_height*height*0.9]
            fig, ax    = plt.subplots(figsize=fig_size)#, squeeze=True)
            plt.subplots_adjust(bottom=0.15,left=0.15)
            # Axis
            ## Title
            ax.set_title(Title,fontsize=TitleSize)
            ax.set_ylabel(yTitle,fontsize=yTitleSize,color="dimgray")
            ax.set_xlabel(xTitle,fontsize=xTitleSize,color="dimgray")
            #ax.grid(True)
            ax.scatter(np.array(X),np.array(Y),c=np.array(Col),s=np.array(Size),edgecolors="grey",alpha=alpha,cmap=cmap)
        return ax,fig
    
def BasicPie(df,
                         labels=0,
                         values=1,
                         width=1.5,
                         height=1,
                         colors = "christmas",
                         Title = "Pie Chart",
                         TitleSize=20,
                         xTitle="",
                         xTitleSize=15,
                         yTitle="",
                         yTitleSize=15,
                         theme="default"
             ):
        with plt.style.context(theme):
            # Setting fig size
            (fig_width, fig_height) = plt.rcParams['figure.figsize']
            fig_size = [fig_width*width, fig_height*height]
            fig, ax    = plt.subplots(figsize=fig_size)
            plt.subplots_adjust(bottom=0.15,left=0.15)
            # Axis
            ## Title
            ax.set_title(Title,fontsize=TitleSize)
            ax.set_ylabel(yTitle,fontsize=yTitleSize,color="dimgray")
            ax.set_xlabel(xTitle,fontsize=xTitleSize,color="dimgray")
            #ax.grid(True)
            ax.pie(df.iloc[:,values], labels=df.iloc[:,labels],startangle=90,colors=colSet.colSet10(name=colors))
            ax.axis('equal')
        return ax,fig
    
    
def BasicStackBar(df,
                                     width=1.4,
                                     height=.8,
                                     bwidth=.6,
                                     alpha=0.8,
                                     Title = "StackBar Chart",
                                     TitleSize=20,
                                     xTitle="",
                                     xTitleSize=15,
                                     yTitle="",
                                     yTitleSize=15,
                                     theme="seaborn"
             ):
        with plt.style.context(theme):
            
            Samples = df.columns
            Labels = df.index
            data = np.vstack([[df.iloc[s,i] for i in range(len(df.columns))] for s in range(len(df.index))])
            index =  range(len(df.iloc[0,:]))
            # make Colors Set
            c = []
            for n in ["christmas"]:
                c = c+colSet.colSet10(name=n)
            c = c*100
            # output Size
            (fig_width, fig_height) = plt.rcParams['figure.figsize']
            fig_size = [fig_width*width, fig_height*height]
            fig, ax    = plt.subplots(figsize=fig_size)
            fig.subplots_adjust(left=0.35,right=1.0, wspace=0.25, hspace=0.25,bottom=0.13, top=0.91)
            l = []
            for i in range(data.shape[0]):
                p = ax.bar(index, data[i], width=bwidth, color = c[i],bottom = np.sum(data[:i], axis = 0),alpha=alpha)
                l.append(p)
                ax.set_title(Title,fontsize=TitleSize)
                ax.set_ylabel(yTitle,fontsize=yTitleSize,color="dimgray")
                ax.set_xlabel(xTitle,fontsize=xTitleSize,color="dimgray")
                plt.xticks(index,Samples,rotation=30)
            fig.legend(([i for i in l]),(Labels),loc='upper right',bbox_to_anchor=(.2,0.85),ncol=1,shadow=False,fancybox=False,fontsize=8)
        return ax,fig,c