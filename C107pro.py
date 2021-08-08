import pandas as pd
import csv
import plotly.express as px

file = pd.read_csv('data2.csv')
students = file.loc[file["student_id"]=="TRL_mda"]
students.groupby(["level"])["attempt"]

fig1 = px.scatter(x =["Level 1","Level 2","Level 3","Level 4"],
 y =students.groupby("level")["attempt"].mean(),
)
fig1.show()