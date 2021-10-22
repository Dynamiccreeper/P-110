import pandas as pd
import plotly.figure_factory as ff
import statistics
import random

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()

population_mean=statistics.mean(data)
print("Population mean:-", population_mean)
std_deviation= statistics.stdev(data)
print("Population std dev:-", std_deviation)

def sample_data_points(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,(len(data)-1))
        value=data[random_index]    
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
def showfig(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["temp"],show_hist=False)
    fig.show()

def setup():
    meanlist=[]
    for i in range(0,100):
        mean_of_samples=sample_data_points(30)
        meanlist.append(mean_of_samples)

    sample_mean=statistics.mean(meanlist)
    print("Mean of all samples:-", sample_mean)
    std_dev= statistics.stdev(meanlist)
    print("Std dev of samples:-", std_dev)
    showfig(meanlist)

setup()