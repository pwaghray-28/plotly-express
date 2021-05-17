import pandas as pd
import plotly.express as px
df = pd.read_csv("data.csv")
#figure = px.line(df,x = "2003",y = "Per capita", color = "Country")
#figure = px.bar(df,x = "Country", y = "InternetUsers")
figure = px.scatter(df, x = "Population", y = "Per capita", size = "Percentage", color = "Country" )
figure.show()