import pandas as pd
import numpy as np,
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_process(url_or_path_to_csv_file):

    df1 =(pd.read_csv(url_or_path_to_csv_file,sep =',')
         .drop(['education'],axis=1,inplace=True)
         .rename(columns={'male':'Sex'},inplace=True)
         .dropna(axis=0,inplace=True)
        )
    df2= (df
          .loc[lambda x: x['totChol']<600]
          .loc[lambda x: x['sysBP']< 295]
         )
    return df2

def cor_checking(dataframe):
    cor=dataframe.corr()
    plt.figure(figsize=(20,10))
    hmap=sns.heatmap(cor,xticklabels=cor.columns,yticklabels=cor.columns,annot=True)
    plt.title("Correlation among all the Variables of the Dataset", size=20)
    return hmap

def dist_plot_numeric(dataframe):
    numerical_val = ['cigsPerDay', 'BPMeds', 'totChol', 'sysBP', 'diaBP', 'BMI', 'heartRate', 'glucose']
    for i in numerical_val:
        sns.distplot(dataframe[i])
        plt.title('{} Distribution'.format(i), fontsize=20)
        plt.show()

def age_vs_totChol_plot(dataframe):
    sns.boxplot(x="age",y="totChol",data=dataframe)
    plt.title("Distribution of age with respect to total cholestrol level", size=14)
    fig_size = plt.rcParams["figure.figsize"]
    fig_size[0] = 8
    fig_size[1] = 10
    plt.rcParams["figure.figsize"] = fig_size
    plt.show()
    
    
def bmi_BP_glucose (dataframe):
    g1 = df.groupby("BMI").glucose.mean()
    g2 = df.groupby("BMI").sysBP.mean()
    g3 = df.groupby("BMI").diaBP.mean()

    plt.figure(figsize=(25,10))
    sns.lineplot(data=g1, label="glucose level")
    sns.lineplot(data=g2, label="systolic blood pressure")
    sns.lineplot(data=g3, label="diastolic blood pressure")
    plt.title("Graph showing glucose level, systolic and diastolic blood pressure based on BMI (body mass index).", size=20)
    plt.xlabel("BMI", size=20)
    plt.ylabel("count", size=20)
    plt.xticks(size=10)
    plt.yticks(size=10)