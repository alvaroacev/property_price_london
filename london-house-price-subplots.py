from pandas import DataFrame, read_csv
import pandas as pd
import plotly.graph_objs as go

from plotly.subplots import make_subplots
import plotly.graph_objects as go1



file = r'./london-data/house_price_index_avg.csv'
df = pd.read_csv(file, delimiter = '	', parse_dates=['Period'])
bottom = df.tail(1)
period = str(bottom['Period'].values.tolist())

sales_file = r'./london-data/house_price_index_sales_volume.csv'
sales_df = pd.read_csv(sales_file, delimiter = '	', parse_dates=['Period'])
sales_bottom = sales_df.tail(1)
sales_period = str(sales_bottom['Period'].values.tolist())

earnings_file = r'./london-data/median-ratio-house-price-earnings-residence-based.csv'
earnings_df = pd.read_csv(earnings_file, delimiter = ',', parse_dates=['Period'])

fig = make_subplots(rows=2, cols=2, subplot_titles=(
	"Period " + period + ", Average House Price",
	"Average price evolution",
	"Period " + sales_period + ", Sales Volumes",
	"Ratio of median house price to median gross annual, 2002-2018"))
# fig.add_trace(go.Bar(x=['City of London'], y=bottom['City of London'], name='City of London'),row=1, col=1)
# fig.add_trace(go.Bar(x=['Camden'], y=bottom['Camden'], name='Camden'),row=1, col=1)
# fig.add_trace(go.Bar(x=['Greenwich'], y=bottom['Greenwich'], name='Greenwich'),row=1, col=1)
fig.add_trace(go.Bar(x=['Hackney'], y=bottom['Hackney'], name='Hackney'),row=1, col=1)
# fig.add_trace(go.Bar(x=['Hammersmith & Fulham'], y=bottom['Hammersmith & Fulham'], name='Hammersmith & Fulham'),row=1, col=1)
fig.add_trace(go.Bar(x=['Islington'], y=bottom['Islington'], name='Islington'),row=1, col=1)
# fig.add_trace(go.Bar(x=['Kensington & Chelsea'], y=bottom['Kensington & Chelsea'], name='Kensington & Chelsea'),row=1, col=1)
fig.add_trace(go.Bar(x=['Lambeth'], y=bottom['Lambeth'], name='Lambeth'),row=1, col=1)
fig.add_trace(go.Bar(x=['Lewisham'], y=bottom['Lewisham'], name='Lewisham'),row=1, col=1)
fig.add_trace(go.Bar(x=['Southwark'], y=bottom['Southwark'], name='Southwark'),row=1, col=1)
fig.add_trace(go.Bar(x=['Tower Hamlets'], y=bottom['Tower Hamlets'], name='Tower Hamlets'),row=1, col=1)
fig.add_trace(go.Bar(x=['Wandsworth'], y=bottom['Wandsworth'], name='Wandsworth'),row=1, col=1)
# fig.add_trace(go.Bar(x=['Westminster'], y=bottom['Westminster'], name='Westminster'),row=1, col=1)
## add scatter
# fig.add_trace(go.Scatter(x=df['Period'], y=df['City of London'], name='City of London'),row=1,col=2)
# fig.add_trace(go.Scatter(x=df['Period'], y=df['Camden'], name='Camden'),row=1,col=2)
# fig.add_trace(go.Scatter(x=df['Period'], y=df['Greenwich'], name='Greenwich'),row=1,col=2)
fig.add_trace(go.Scatter(x=df['Period'], y=df['Hackney'], name='Hackney'),row=1,col=2)
# fig.add_trace(go.Scatter(x=df['Period'], y=df['Hammersmith & Fulham'], name='Hammersmith & Fulham'),row=1,col=2)
fig.add_trace(go.Scatter(x=df['Period'], y=df['Islington'], name='Islington'),row=1,col=2)
# fig.add_trace(go.Scatter(x=df['Period'], y=df['Kensington & Chelsea'], name='Kensington & Chelsea'),row=1,col=2)
fig.add_trace(go.Scatter(x=df['Period'], y=df['Lambeth'], name='Lambeth'),row=1,col=2)
fig.add_trace(go.Scatter(x=df['Period'], y=df['Lewisham'], name='Lewisham'),row=1,col=2)
fig.add_trace(go.Scatter(x=df['Period'], y=df['Southwark'], name='Southwark'),row=1,col=2)
fig.add_trace(go.Scatter(x=df['Period'], y=df['Tower Hamlets'], name='Tower Hamlets'),row=1,col=2)
fig.add_trace(go.Scatter(x=df['Period'], y=df['Wandsworth'], name='Wandsworth'),row=1,col=2)
# fig.add_trace(go.Scatter(x=df['Period'], y=df['Westminster'], name='Westminster'),row=1,col=2)

### Bars for sales volumes during last period recorded
# fig.add_trace(go.Bar(x=['City of London'], y=sales_bottom['City of London'], name='City of London'),row=2,col=1)
# fig.add_trace(go.Bar(x=['Camden'], y=sales_bottom['Camden'], name='Camden'),row=2,col=1)
# fig.add_trace(go.Bar(x=['Greenwich'], y=sales_bottom['Greenwich'], name='Greenwich'),row=2,col=1)
fig.add_trace(go.Bar(x=['Hackney'], y=sales_bottom['Hackney'], name='Hackney'),row=2,col=1)
# fig.add_trace(go.Bar(x=['Hammersmith & Fulham'], y=sales_bottom['Hammersmith & Fulham'], name='Hammersmith & Fulham'),row=2,col=1)
fig.add_trace(go.Bar(x=['Islington'], y=sales_bottom['Islington'], name='Islington'),row=2,col=1)
# fig.add_trace(go.Bar(x=['Kensington & Chelsea'], y=sales_bottom['Kensington & Chelsea'], name='Kensington & Chelsea'),row=2,col=1)
fig.add_trace(go.Bar(x=['Lambeth'], y=sales_bottom['Lambeth'], name='Lambeth'),row=2,col=1)
fig.add_trace(go.Bar(x=['Lewisham'], y=sales_bottom['Lewisham'], name='Lewisham'),row=2,col=1)
fig.add_trace(go.Bar(x=['Southwark'], y=sales_bottom['Southwark'], name='Southwark'),row=2,col=1)
fig.add_trace(go.Bar(x=['Tower Hamlets'], y=sales_bottom['Tower Hamlets'], name='Tower Hamlets'),row=2,col=1)
fig.add_trace(go.Bar(x=['Wandsworth'], y=sales_bottom['Wandsworth'], name='Wandsworth'),row=2,col=1)
# fig.add_trace(go.Bar(x=['Westminster'], y=sales_bottom['Westminster'], name='Westminster'),row=2,col=1)

### Earning graph
#fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['City of London'], name='City of London'),row=2,col=2)
#fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Camden'], name='Camden'),row=2,col=2)
#fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Greenwich'], name='Greenwich'),row=2,col=2)
fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Hackney'], name='Hackney'),row=2,col=2)
#fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Hammersmith & Fulham'], name='Hammersmith & Fulham'),row=2,col=2)
fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Islington'], name='Islington'),row=2,col=2)
#fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Kensington & Chelsea'], name='Kensington & Chelsea'),row=2,col=2)
fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Lambeth'], name='Lambeth'),row=2,col=2)
fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Lewisham'], name='Lewisham'),row=2,col=2)
fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Southwark'], name='Southwark'),row=2,col=2)
fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Tower Hamlets'], name='Tower Hamlets'),row=2,col=2)
fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Wandsworth'], name='Wandsworth'),row=2,col=2)
#fig.add_trace(go.Scatter(x=earnings_df['Period'], y=earnings_df['Westminster'], name='Westminster'),row=2,col=2)



#fig.show()

# fig1 = make_subplots(rows=1, cols=2)

# fig1.add_trace(go.Bar(x=['City of London'], y=bottom['City of London'], name='City of London'),row=1, col=1)
# fig1.add_trace(go.Bar(x=['Camden'], y=bottom['Camden'], name='Camden'),row=1, col=1)
# fig.add_trace(go.Scatter(x=df['Period'], y=df['City of London'], name='City of London'),row=1,col=2)
# fig.add_trace(go.Scatter(x=df['Period'], y=df['Camden'], name='Camden'),row=1,col=2)
fig.show()
