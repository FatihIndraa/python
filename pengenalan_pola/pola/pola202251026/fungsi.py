import pandas as pd
import scipy
import seaborn as sns
import matplotlib.pyplot as plt

def tampilkan_grafik():
    df=pd.DataFrame({'hours': [1,2,3,4,5,6,7,8,9,10],'score':[78,79,84,80,81,89,95,90,83,89]})

    #view DataFrame
    print (df)

    #create regplot
    p=sns.regplot(data=df, x=df.hours, y=df.score)
    #plt.show()

    #calculate slope and intercept of regression equation
    slope, intercept,r, p, sterr=scipy.stats.linregress(x=p.get_lines()[0].get_xdata(),
                                                        y=p.get_lines()[0].get_ydata())

    #display slope and intercept of regression equation
    #print(intercept, slope)
    #add regression equation to plot

    plt.text(2, 95, 'y=' +str(round(intercept,3))+'+'+str(round(slope,3))+'x')
    plt.title("Hours vs Scores")
    plt.show()
