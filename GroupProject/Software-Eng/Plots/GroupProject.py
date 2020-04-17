import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df1 = pd.read_csv('../Datasets/CoronavirusTotal.csv')
df2 = pd.read_csv('../Datasets/CoronaTimeSeries.csv')
df3 = pd.read_csv('../Datasets/Olympic2016Rio.csv')
df4 = pd.read_csv('../Datasets/Weather2014-15.csv')
df5 = pd.read_csv('../Datasets/duration-of-unemployment.csv')
df6 = pd.read_csv('../Datasets/15yUnemployment.csv')
df7 = pd.read_csv('../Datasets/US-UnemployedbyState.csv')
df8 = pd.read_csv('../Datasets/fatalwork-injuries.csv')
df9 = pd.read_csv('../Datasets/laborparticipationrate2.csv')

app = dash.Dash()

# Bar chart data
barchart_df = df7
barchart_df = barchart_df.sort_values(by=['State'], ascending=[True]).head(50)
data_barchart = [go.Bar(x=barchart_df['State'], y=barchart_df['Unemployment rate'])]

# Stack bar chart data
stackbarchart_df = df8.groupby(['Year']).agg({'Self-employed': 'sum', 'Wage and salary': 'sum'})
stackbarchart_df = df8.sort_values(by=['Total'], ascending=[False]).head(20)
trace1_stackbarchart = go.Bar(x=stackbarchart_df['Year'], y=stackbarchart_df['Self-employed'], name='Self-employed',
marker={'color': '#FFD700'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['Year'], y=stackbarchart_df['Wage and salary'], name='Wage and salary',
marker={'color': '#9EA0A1'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart]

# Line Chart
line_df = df6
line_df['date'] = pd.to_datetime(line_df['date'])
data_linechart = [go.Scatter(x=line_df['date'], y=line_df['Percentage'], mode='lines', name='Max')]

# Multi Line Chart
multiline_df = df5
multiline_df['date'] = pd.to_datetime(multiline_df['date'])
trace1 = go.Scatter(x=multiline_df['date'], y=multiline_df['Less than 5 weeks'], mode='lines', name='< 5 weeks')
trace2 = go.Scatter(x=multiline_df['date'], y=multiline_df['5-14 weeks'], mode='lines', name='5-14 weeks')
trace3 = go.Scatter(x=multiline_df['date'], y=multiline_df['15-26 weeks'], mode='lines', name='15-26 weeks')
trace4 = go.Scatter(x=multiline_df['date'], y=multiline_df['27 weeks and over'], mode='lines', name='> 26 weeks')
data_multiline = [trace1, trace2, trace3, trace4]

# Bubble chart
new_df = df7.groupby(['State']).agg({'Unemployment rate': 'sum', 'Number of unemployed': 'sum'}).reset_index()
new_df = new_df.sort_values(by=['State'], ascending=[True]).head(50)
# Preparing data
data_bubblechart = [
    go.Scatter(x=new_df['Unemployment rate'],
               y=new_df['Number of unemployed'],
               text=new_df['State'],
               mode='markers',
               marker=dict(size=new_df['Unemployment rate'] * 10,color=new_df['Unemployment rate'], showscale=False))]

# Heatmap
data_heatmap = [go.Heatmap(x=df9['Month'],
                   y=df9['Year'],
                   z=df9['Rate'].values.tolist(),
                   colorscale='Jet',
                   reversescale=True)]

# Layout
app.layout = html.Div(children=[
    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),
    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bar chart', style={'color': '#df1e56'}),
    html.Div('This bar chart represents the Unemployment Rate by each State.'),
    dcc.Graph(id='graph2',
              figure={
                  'data': data_barchart,
                  'layout': go.Layout(title='Unemployment Rate By State', xaxis_title="State",
                                      yaxis_title="Unemployment Rate")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Stack bar chart', style={'color': '#df1e56'}),
    html.Div(
        'This stack bar chart represent the fatal work injuries for Self-employed / Wage and salary employees from 2014 to 2018.'),
    dcc.Graph(id='graph3',
              figure={
                  'data': data_stackbarchart,
                  'layout': go.Layout(title='Fatal Work Injuries', xaxis_title="Year",
                    yaxis_title="Number of Injuries", barmode='stack')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Line chart', style={'color': '#df1e56'}),
    html.Div('This line chart represent the unemployment rate of the United States over a 15 year period.'),
    dcc.Graph(id='graph4',
              figure={
                  'data': data_linechart,
                  'layout': go.Layout(title='United States Unemployment Rates', xaxis_title="Month / Year",
                                      yaxis_title="Unemployment Rate")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Multi Line chart', style={'color': '#df1e56'}),
    html.Div(
        'This line chart represent the the different lengths of unemployment over the course of 20 years'),
    dcc.Graph(id='graph5',
              figure={
                  'data': data_multiline,
                  'layout': go.Layout(title="Duration of Unemployment", xaxis_title="Date",
                                      yaxis_title="Unemployed Individuals")
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Bubble chart', style={'color': '#df1e56'}),
html.Div(
        'This bubble chart represent the unemployment rate by state and number of unemployed'),
    dcc.Graph(id='graph6',
              figure={
                  'data': data_bubblechart,
                  'layout': go.Layout(title='US Unemployment Rate',
                                      xaxis={'title': 'Unemployment Rate'}, yaxis={'title': 'Number of unemployed'},
                                      hovermode='closest')
              }
              ),
    html.Hr(style={'color': '#7FDBFF'}),
    html.H3('Heat map', style={'color': '#df1e56'}),
    html.Div(
        'This heat map represent the labor participation rate in the US by month since 2010.'),
    dcc.Graph(id='graph7',
              figure={
                  'data': data_heatmap,
                  'layout': go.Layout(title='Labor participation rate by Month since 2010',
                                      xaxis={'title': 'Month'}, yaxis={'title': 'Year'})
              }
              )
])



def update_figure(selected_continent):
    filtered_df = df1[df1['Continent'] == selected_continent]

    filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    new_df = filtered_df.groupby(['Country'])['Confirmed'].sum().reset_index()
    new_df = new_df.sort_values(by=['Confirmed'], ascending=[False]).head(20)
    data_interactive_barchart = [go.Bar(x=new_df['Country'], y=new_df['Confirmed'])]
    return {'data': data_interactive_barchart, 'layout': go.Layout(title='Corona Virus Confirmed Cases in '+selected_continent,
                                                                   xaxis={'title': 'Country'},
                                                                   yaxis={'title': 'Number of confirmed cases'})}


if __name__ == '__main__':
    app.run_server()
