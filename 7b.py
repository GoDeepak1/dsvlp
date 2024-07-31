#import libraries
import plotly.express as px
#define data
df = px.data.gapminder().query("year==2007")
fig = px.scatter_geo(df, locations="iso_alpha", size="pop", hover_name="country", projection="natural earth", title='World Map - Deepak USN: 1BI21CS179')
#show the plot
fig.show()
