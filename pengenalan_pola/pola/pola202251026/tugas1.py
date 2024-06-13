from tkinter import*
import pandas as pd
import scipy
import seaborn as sns
import matplotlib.pyplot as plt

def tampilkan_grafik():
    df=pd.DataFrame({'hours': [1,2,3,4,5,6,7,8,9,10],'score':[78,79,84,80,81,89,95,90,83,89]})

    #membuat DataFrame
    print (df)

    #membuat regresi linier
    p=sns.regplot(data=df, x=df.hours, y=df.score)
    #plt.show()

    #menghitung berapa nilai regresnya
    slope, intercept,r, p, sterr=scipy.stats.linregress(x=p.get_lines()[0].get_xdata(),
                                                        y=p.get_lines()[0].get_ydata())

    #menampilkan grafik
    plt.text(2, 95, 'y=' +str(round(intercept,3))+'+'+str(round(slope,3))+'x')
    plt.title("Hours vs Scores")
    plt.show()
def pilihan_diubah(*args):
    if variable.get() == "Option 1":
        tampilkan_grafik()
        
root = Tk()
root.geometry("300x300")

OPTIONS = [
    "Option 1",
    "Option 2",
    "Option 3"]#etc

variable = StringVar()
variable.set(OPTIONS[0])#default value

variable.trace("w", pilihan_diubah)
w = OptionMenu(root, variable, *OPTIONS)
w.pack()

root.mainloop()