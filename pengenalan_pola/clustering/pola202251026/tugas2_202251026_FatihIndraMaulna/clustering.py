import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt

# Ignore warning
import warnings
warnings.filterwarnings('ignore')

# Read data
data = pd.read_csv("clustering.csv")
X = data[["ApplicantIncome", "LoanAmount"]]

# Function to visualize data point (peminjam)
def peminjam():
    plt.scatter(X["ApplicantIncome"], X["LoanAmount"], c="blue")
    plt.xlabel("Applicant Income")
    plt.ylabel("Loan Amount (In Thousands)")
    plt.title("Borrower's Figure")
    plt.show()

# Function to visualize initial centroids (titik awal)
def titikAwal():
    K = 3  # Number of centroids
    Centroids = X.sample(n=K)
    plt.scatter(X["ApplicantIncome"], X["LoanAmount"], c="blue")
    plt.scatter(Centroids["ApplicantIncome"], Centroids["LoanAmount"], c="red")
    plt.xlabel("Applicant Income")
    plt.ylabel("Loan Amount (In Thousand)")
    plt.title("Initial Centroids")
    plt.show()

# Function to perform K-Means clustering and show result
def hasil():
    K = 3  # Number of centroids
    Centroids = X.sample(n=K)
    diff = 1
    j = 0

    while diff != 0:
        XD = X
        i = 1
        for index1, row_c in Centroids.iterrows():
            ED = []
            for index2, row_d in XD.iterrows():
                d1 = (row_c["ApplicantIncome"] - row_d["ApplicantIncome"])**2
                d2 = (row_c["LoanAmount"] - row_d["LoanAmount"])**2
                d = sqrt(d1 + d2)
                ED.append(d)
            X[i] = pd.Series(ED, name='d')
            i = i + 1

        C = []
        for index, row in X.iterrows():
            min_dist = row[1]
            pos = 1
            for i in range(K):
                if row[i + 1] < min_dist:
                    min_dist = row[i + 1]
                    pos = i + 1
            C.append(pos)
        X["Cluster"] = C
        Centroids_new = X.groupby(["Cluster"]).mean()[["LoanAmount", "ApplicantIncome"]]
        if j == 0:
            diff = 1
            j = j + 1
        else:
            diff = (Centroids_new['LoanAmount'] - Centroids['LoanAmount']).sum() + (Centroids_new['ApplicantIncome'] - Centroids['ApplicantIncome']).sum()
        Centroids = X.groupby(["Cluster"]).mean()[["LoanAmount", "ApplicantIncome"]]

    color = ['blue', 'green', 'cyan']
    for K in range(K):
        data = X[X["Cluster"] == K + 1]
        plt.scatter(data["ApplicantIncome"], data["LoanAmount"], c=color[K])
    plt.scatter(Centroids["ApplicantIncome"], Centroids["LoanAmount"], c='red')
    plt.xlabel('income')
    plt.ylabel('LoanAmount(In Thousands)')
    plt.title('Clustering Result (K = {})'.format(K))
    plt.show()

