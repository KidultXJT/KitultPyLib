from __future__ import division
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

def colSet10(name="sci1"):
    # Description:
    # about 10 for a set
    #  random
    if name == "kidult":
        c = ["lightskyblue","lightcoral","gray","lightgreen"]
    if name == "ocean":
        c = ["#013882","#2EC7D5","#00A6DF","#9EC9E3","#016973","#017DCD","#74B4E0","#00ABC9","#009CA4"]
    if name == "pantone":
        c = ["#27B1BE","#F7931E","#E84A5F","#99BC5D","#FACC2E","#016973","#6566A9","#364F6B","#029E7E","#A51E37"]
    if name == "green":
        c = ["#9BDF46","#006837","#68C170","#2E9F82","#5A9E7C","#124C2F","#D9E021","#C5D200","#25A55F","#22B573"]
    if name == "christmas":
        c = ["#CD3131","#A0DBDB","#305973","#56A7A7","#06C1B6","#6A0000","#B17D58","#4A2C2C","#AB1212","#00293F"]
    if name == "no1":
        c = ["#4E1184","#65589C","#FF4D96","#E84A5F","#0E1555","#544D7E","#D4145A","#932B77","#FF847C","#2A363B"]
    if name == "no2":
        c = ["#42B2C7","#C2D93B","#66BD9F","#79C38A","#2FADDC","#D4DF26","#9DCE63","#53B8B4","#8BC977","#B1D44D"]
    if name == "sci1":
        c = ["#008694","#85925C","#C65B96","#546DA6","#E87E00","#7C509D","#A85169","#0071BA","#52B5A8","#6AC0E5"]
    if name == "sci2":
        c = ["#729A97","#90969D","#624C9A","#003F84","#6C9BD2","#C3A1CA","#8B8DC5","#0084B4","#696B68","#527586"]
    if name == "stone":
        c = ["#729A97","#90969D","#839FAD","#5D7750","#696B68","#775050","#C9C8BD","#9E9D95","#696B68","#527586"]
    if name == "ai":
        c = ["#527586","#90969D","#003F84","#0084B4","#6C9BD2","#C9C8BD","#00696F","#729A97","#6C9BD2","#839FAD"]
    if name == "metal":
        c = ["#CB9B0C","#5F5E5D","#5F6D68","#8B938F","#FBCF00","#F0CC7E","#7A7A7A","#9CA3AA","#617F74","#33604A"]
    if name == "bitch":
        c = ["#CDB1BA","#F7CF83","#BDAA94","#DFD0BA","#89507B","#00B3D6","#54BFC6","#9C856A","#EFA39F","#8DD0D5"]
    return c

#def colSetRandom(Set=[1:10]
#                ):
#                ## Description
#                ## Random ~~ Bravo ~~
#            colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
#            c = [[c for c in colors][s] for s in Set]
#            return c
