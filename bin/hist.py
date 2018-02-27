from __future__ import division
# Graph Module
import numpy as np
import pandas as pd
import os 
import sys
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

intable = sys.argv[1]
Max = sys.argv[2]
Min  = sys.argv[3]
out = sys.argv[4]


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

table = pd.read_table(intable)
data = table["RNAlength"]
if max(data) < Max:
    Max=max(data)
else:
    Max=Max
    data=[min(i, Max) for i in  data]
p,fig = BasicHist(data=data,xmax=5000,xmin=0)#,Title=Title,yTitle=yTitle,xTitle=xTitle,color=Col)
fig.savefig(out+"_Length.PNG",dpi=100)
fig.savefig(out+"_Length.PDF")