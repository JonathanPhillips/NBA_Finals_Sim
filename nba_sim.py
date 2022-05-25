import pandas as pd 
import random as rnd
import numpy as np 
import matplotlib.pyplot as plt

gdf = pd.read_csv('stats_nba_com-teamgamelogs-2021_22-regular_season.csv')

def gameSim():
    GSWScore = (rnd.gauss(gswmeanpts,gswsdpts)+ rnd.gauss(miameanopp,miasdopp))/2
    MIAScore = (rnd.gauss(miameanpts,miadpts)+ rnd.gauss(gswmeanopp,gswsdopp))/2
    if int(round(GSWScore)) > int(round(MIAScore)):
        return 1
    elif int(round(GSWScore)) < int(round(MIAScore)):
        return -1
    else: return 0

def gamesSim(ns):
    gamesout = []
    team1win = 0
    team2win = 0
    tie = 0
    for i in range(ns):
        gm = gameSim()
        gamesout.append(gm)
        if gm == 1:
            team1win +=1 
        elif gm == -1:
            team2win +=1
        else: tie +=1 
    print('GSW Win ', team1win/(team1win+team2win+tie),'%')
    print('MIA Win ', team2win/(team1win+team2win+tie),'%')
    print('Tie ', tie/(team1win+team2win+tie), '%')
    return gamesout

gamesSim(100000)
