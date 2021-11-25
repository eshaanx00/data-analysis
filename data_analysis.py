import plotly.express as px
import pandas

data = pandas.read_csv("data_analysis.csv")
d1 = data.groupby(["student_id","level"],as_index=False)["attempt"].mean()

fig = px.scatter(d1,x="student_id",y="level",size='attempt',color="attempt")
fig.show()
