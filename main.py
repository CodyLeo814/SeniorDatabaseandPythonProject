
from flask import Flask, render_template
# What effects the heart and heart attacks

# Setup
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sb
import pandas as pd
app = Flask(__name__)

data = pd.read_csv(r"C:\Users\codst\Downloads\heart.csv")

# shows the data
@app.route("/")
def head():
    return render_template("index.html")


# copy data so that the main data is not tampered with in case of a problem
df1 = data.copy()
# print data info
df1.info()
# remove duplicate
df1.drop_duplicates(inplace=True)  # dropping duplicated rows
df1.reset_index(drop=True, inplace=True)

# relabeling got assistance online
df1['exng'] = df1['exng'].map({1: 'yes', 0: 'no'})
df1['cp'] = df1['cp'].map({0: 'typical angina', 1: 'atypical angina', 2: 'non-anginal pain', 3: 'asymptomatic'})
df1['fbs'] = df1['fbs'].map({1: 'true', 0: 'false'})
df1['restecg'] = df1['restecg'].map(
    {0: 'normal', 1: 'having ST-T wave abnormality', 2: 'showing probable or definite left ventricular hypertrophy'})
df1['output'] = df1['output'].map({0: 'less chance of heart attack', 1: 'more chance of heart attack'})

# making the visuals

# correlation of the columns to each other in respect of probability of happening



@app.route("/correlations")
def Correlation():
    plt.figure(figsize=(15, 10))
    sb.heatmap(df1.corr(), annot=True, cmap='coolwarm')
    return f'<img src="data:image/png;base64,{plt.show()}"/>'
# note the warmer the color the more corolation the values effect each other


# making several web applications for each graph

# by age graph



@app.route("/age")
def Age():
    plt.figure(figsize=(10, 15))
    plt.title('Prevalence of Heart attack by age', fontsize=15)
    sb.histplot(x=df1['age'], hue=df1['output'])
    return f'<img src="data:image/png;base64,{plt.show()}"/>'

# max heart rate minigraph
@app.route("/maxheartrate")
def maxheartrate():
    plt.figure(figsize=(10, 15))
    plt.title('Prevalence of Heart attack by Maximum heart rate', fontsize=15)
    sb.histplot(x=df1['trtbps'], hue=df1['output'])
    return f'<img src="data:image/png;base64,{plt.show()}"/>'

# cholestoral minigraph
@app.route("/cholesterol")
def cholesterol():
    plt.figure(figsize=(10, 15))
    plt.title('Prevalence of Heart attack by cholestoral in mg/dl', fontsize=15)
    sb.histplot(x=df1['chol'], hue=df1['output'])
    return f'<img src="data:image/png;base64,{plt.show()}"/>'

# oldpeak minigraph
@app.route("/oldpeak")
def oldpeak():
    plt.figure(figsize=(10, 15))
    plt.title('Prevalence of Heart attack by old peak', fontsize=15)
    sb.histplot(x=df1['oldpeak'], hue=df1['output'])
    return f'<img src="data:image/png;base64,{plt.show()}"/>'

if __name__ == "__main__":
    app.run()
