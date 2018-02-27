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



def freqBar(data,
                        out=None,
                        colorsets="metal", # canbe not colSets
                        Title="",
                        xTitle="Types",
                        yTitle="Values"
           ):
             # Description:
             # make a frequency DataFrame and frequency Graph // xiejunting
            # Frequence DataFrame
            # Remove NaN
            df = pd.DataFrame(Counter(np.array(data)).items()).dropna(how='any')
            # Make Frequence Graph
            p,fig,color = BASICGraph.BasicBar(df=df,Title=Title,yTitle=yTitle,xTitle=xTitle,colorsets=colorsets)
            if out != None:
                # Make Frequence DataFrame
                df.columns = ['Types','Freq']
                df.to_csv(out+"_Freq", sep='\t', encoding='utf-8',header=True,index=None)
                ## SAVE PNG
                fig.savefig(out+"_Freq.PNG",dpi=100)
            return df,p,fig


def freqHBar(data,
                          out=None,
                          width = 0.8,
                          colorsets="greenyellow", # canbe not colSets
                          Title="",
                          xTitle="Types",
                          yTitle="Values"
            ):
            # Description:
            # make a frequency DataFrame and frequency Graph // xiejunting
            # Frequence DataFrame
            # Remove NaN
            df = pd.DataFrame(Counter(np.array(data)).items()).dropna(how='any').sort_values(by=int(1),ascending=False)
            # Make Frequence Graph
            p,fig,color = BASICGraph.BasicHBar(df=df,Title=Title,yTitle=yTitle,xTitle=xTitle,colorsets=colorsets,width=width)
            if out != None:
                # Make Frequence DataFrame
                df.columns = ['Types','Freq']
                df.to_csv(out+"_Freq", sep='\t', encoding='utf-8',header=True,index=None)
                ## SAVE PNG
                fig.savefig(out+"_Freq.PNG",dpi=100)
            return df,p,fig