import random as rd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as st
import pandas as pd

data = pd.read_csv("medium_data.csv")

population_mean = st.mean(data)

def random_set_of_mean(counter) :
    dataset = []
    for i in range(0,counter) :
        rand_index = rd.randint(0,len(data)-1)
        value = data[rand_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(mean_list) :
    df = mean_list

def setup():
    mean_list = []
    for i in range(0,100) :
        set_of_mean = random_set_of_mean(30)
        mean_list.append(set_of_mean)
    show_fig(mean_list)



