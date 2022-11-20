import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import streamlit as st
#import altair as alt
#import plotly.express as px
#st.set_page_config(page_title="website of output",
#page_icon=":bar_chart:",
#layout="wide")

# Read data form text file
with open('FrequencyClubsFests.txt', 'r') as f:
    data = f.readlines()
    i = len(data)
    j = 0
   

    x, y =  list(map(int, data[j].strip().split(' ')))
    j += 1
    clubs = []
    for i in range(x):
        clubs.append(list(map(int, data[j].strip().split())))
        j += 1
    x, y =  list(map(int, data[j].split(' ')))
    j+=1
    fests = []
    for i in range(x):
        fests.append(list(map(int, data[j].strip().split())))
        j += 1
values=[clubs[1][1],clubs[1][2],clubs[1][3],clubs[2][1],clubs[2][2],clubs[2][3],clubs[3][1],clubs[3][2],clubs[3][3]]
names=["c1e1", "c1e2", "c1e3", "c2e1", "c2e2", "c2e3", "c3e1", "c3e2", "c3e3"]

print(values)
print(names)

figure=plt.figure()
plt.bar(names,values,color='black',width=0.5)
plt.xlabel("Clubs and Events")
plt.ylabel("Frequency")
plt.title("Frequency of Clubs and Events")
plt.show()
#save the figure
figure.savefig('FrequencyClubevents.png')
val=[fests[1][1],fests[1][2],fests[1][3],fests[1][4],fests[1][5],fests[1][6],fests[1][7],fests[1][8],fests[1][9],fests[1][10],fests[1][11],fests[1][12],fests[2][1],fests[2][2],fests[2][3],fests[2][4],fests[2][5],fests[2][6],fests[2][7],fests[2][8],fests[2][9],fests[2][10],fests[2][11],fests[2][12],fests[2][13],fests[2][14],fests[2][15]]


nam=["f1e1", "f1e2", "f1e3", "f1e4", "f1e5", "f1e6", "f1e7", "f1e8", "f1e9", "f1e10", "f1e11", "f1e12", "f2e1", "f2e2", "f2e3", "f2e4", "f2e5", "f2e6", "f2e7", "f2e8", "f2e9", "f2e10", "f2e11", "f2e12", "f2e13", "f2e14", "f2e15"]
gigure=plt.figure()
plt.bar(nam,val,color='black',width=.2)
plt.xlabel("Clubs and Events")
plt.ylabel("Frequency")
plt.title("Frequency of Clubs and Events")
plt.show()
#save the figure
gigure.savefig('Frequencyfestevents.png')