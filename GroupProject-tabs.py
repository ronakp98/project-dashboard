import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Load CSV file from Datasets folder
df5 = pd.read_csv('../Datasets/duration-of-unemployment.csv')
df6 = pd.read_csv('../Datasets/15yUnemployment.csv')
df7 = pd.read_csv('../Datasets/US-UnemployedbyState.csv')
df8 = pd.read_csv('../Datasets/fatalwork-injuries.csv')
df9 = pd.read_csv('../Datasets/laborparticipationrate2.csv')
df10 = pd.read_csv('../Datasets/UnemploymentData.csv')
df11 = pd.read_csv('../Datasets/laborparticipationrate.csv')
df12 = pd.read_csv('../Datasets/unemploymentnumsbymonth.csv')
df13 = pd.read_csv('../Datasets/unemployedbyindustry.csv')
df14 = pd.read_csv('../Datasets/laborparticipationbygender.csv')

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Bar chart data
barchart_df = df7
barchart_df = barchart_df.sort_values(by=['State'], ascending=[True]).head(50)
data_barchart = [go.Bar(x=barchart_df['State'], y=barchart_df['Unemployment rate'])]

barchart_df2 = df13
barchart_df2 = barchart_df2.sort_values(by=['Industry and Class of Worker'], ascending=[True]).head(14)
data_barchart2 = [go.Bar(x=barchart_df2["Industry and Class of Worker"], y=barchart_df2['Number'])]

# Stack bar chart data
stackbarchart_df = df8.sort_values(by=['Total'], ascending=[False]).head(20)
trace1_stackbarchart = go.Bar(x=stackbarchart_df['Year'], y=stackbarchart_df['Self-employed'], name='Self-employed',
                              marker={'color': '#FFD700'})
trace2_stackbarchart = go.Bar(x=stackbarchart_df['Year'], y=stackbarchart_df['Wage and salary'], name='Wage and salary',
                              marker={'color': '#9EA0A1'})
data_stackbarchart = [trace1_stackbarchart, trace2_stackbarchart]

stackbarchart_df2 = df14.sort_values(by=['Total'], ascending=[False]).head(20)
trace3_stackbarchart = go.Bar(x=stackbarchart_df2['Year'], y=stackbarchart_df2['Men'], name='Men',
                              marker={'color': '#FFD700'})
trace4_stackbarchart = go.Bar(x=stackbarchart_df2['Year'], y=stackbarchart_df2['Women'], name='Women',
                              marker={'color': '#9EA0A1'})
data_stackbarchart2 = [trace3_stackbarchart, trace4_stackbarchart]

# Line Chart
line_df = df6
line_df['date'] = pd.to_datetime(line_df['date'])
data_linechart = [go.Scatter(x=line_df['date'], y=line_df['Percentage'], mode='lines', name='Max')]

line_df2 = df11
line_df2['date'] = pd.to_datetime(line_df2['date'])
data_linechart2 = [go.Scatter(x=line_df2['date'], y=line_df2['Rate'], mode='lines', name='Max')]

# Multi Line Chart
multiline_df = df5
multiline_df['date'] = pd.to_datetime(multiline_df['date'])
trace1 = go.Scatter(x=multiline_df['date'], y=multiline_df['Less than 5 weeks'], mode='lines', name='< 5 weeks')
trace2 = go.Scatter(x=multiline_df['date'], y=multiline_df['5-14 weeks'], mode='lines', name='5-14 weeks')
trace3 = go.Scatter(x=multiline_df['date'], y=multiline_df['15-26 weeks'], mode='lines', name='15-26 weeks')
trace4 = go.Scatter(x=multiline_df['date'], y=multiline_df['27 weeks and over'], mode='lines', name='> 26 weeks')
data_multiline = [trace1, trace2, trace3, trace4]

multiline_df2 = df10
multiline_df2['date'] = pd.to_datetime(multiline_df['date'])
trace1 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 16 & Up'], mode='lines',
                    name='16 & UP')
trace2 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 16-19'], mode='lines',
                    name='Ages 16-19')
trace3 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 20 & Up Men'], mode='lines',
                    name='20 & UP Men')
trace4 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 20 & Up Women'], mode='lines',
                    name='20 & UP Women')
trace5 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 16 & Up White'], mode='lines',
                    name='16 & UP White')
trace6 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 16 & African American'], mode='lines',
                    name='16 & UP African American')
trace7 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 16 & Asians'], mode='lines',
                    name='16 & UP Asians')
trace8 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 16 & Latino/Hispanic'], mode='lines',
                    name='16 & UP Latino/Hispanic')
trace9 = go.Scatter(x=multiline_df['date'],
                    y=multiline_df2['Unemployment Rate - 25 & Up Less than a high school diploma'], mode='lines',
                    name='> High School Diploma')
trace10 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 25 & Up No College'], mode='lines',
                     name='No College')
trace11 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 25 & Up Associates Degree'],
                     mode='lines', name='> Associates Degree')
trace12 = go.Scatter(x=multiline_df['date'], y=multiline_df2['Unemployment Rate - 25 & Up Bachelors Degree or Higher'],
                     mode='lines', name='Bachelors and UP')
data_multiline2 = [trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12]

# Bubble chart
new_df = df7.groupby(['State']).agg({'Unemployment rate': 'sum', 'Number of unemployed': 'sum'}).reset_index()
new_df = new_df.sort_values(by=['State'], ascending=[True]).head(50)

bubble_df = df13.groupby(['Industry and Class of Worker']).agg({'Rate': 'sum', 'Number': 'sum'}).reset_index()
bubble_df = bubble_df.sort_values(by=['Industry and Class of Worker'], ascending=[True]).head(14)

# Preparing data
data_bubblechart = [
    go.Scatter(x=new_df['Unemployment rate'],
               y=new_df['Number of unemployed'],
               text=new_df['State'],
               mode='markers',
               marker=dict(size=new_df['Unemployment rate'] * 10, color=new_df['Unemployment rate'], showscale=False))]

data_bubblechart2 = [
    go.Scatter(x=bubble_df['Rate'],
               y=bubble_df['Number'],
               text=bubble_df['Industry and Class of Worker'],
               mode='markers',
               marker=dict(size=bubble_df['Rate'] * 10, color=bubble_df['Rate'], showscale=False))]

# Heatmap
data_heatmap = [go.Heatmap(x=df9['Month'],
                           y=df9['Year'],
                           z=df9['Rate'].values.tolist(),
                           colorscale='Jet',
                           reversescale=True)]

data_heatmap2 = [go.Heatmap(x=df12['Month'],
                            y=df12['Year'],
                            z=df12['Number'].values.tolist(),
                            colorscale='Jet',
                            reversescale=True)]

# Comparison Tool.......................................................................................................
# Initialize figure
ct = go.Figure()
# Add Traces
ct.add_trace(
    go.Bar(x=barchart_df['State'], y=barchart_df['Unemployment rate'])
)

ct.add_trace(
    go.Bar(x=barchart_df2["Industry and Class of Worker"], y=barchart_df2['Number'])
)

ct.add_trace(
    go.Scatter(x=line_df['date'], y=line_df['Percentage'], mode='lines', name='Max')
)

ct.add_trace(
    go.Scatter(x=line_df2['date'], y=line_df2['Rate'], mode='lines', name='Max')
)

# Add Buttons
ct.update_layout(
    updatemenus=[
        dict(
            buttons=list([
                dict(label="None",
                     method="restyle",
                     args=[{"visible": [False, False, False, False]},
                           {"title": "No Chart Selected"}]),
                dict(label="Bar 1",
                     method="update",
                     args=[{"visible": [True, False, False, False]},
                           {"title": "Unemployment Rate By State"}]),
                dict(label="Bar 2",
                     method="update",
                     args=[{"visible": [False, True, False, False]},
                           {"title": "Unemployment Numbers by Industry"}]),
                dict(label="Line Chart",
                     method="update",
                     args=[{"visible": [False, False, True, False]},
                           {"title": "United States Unemployment Rates"}]),
                dict(label="Line Chart 2",
                     method="update",
                     args=[{"visible": [False, False, False, True]},
                           {"title": "United States Labor Participation"}]),
            ]),
        )
    ])
# .......................................................................................................................
app.layout = html.Div([

    html.H1(children='Python Dash',
            style={
                'textAlign': 'center',
                'color': '#ef3e18'
            }
            ),

    html.Div('Web dashboard for Data Visualization using Python', style={'textAlign': 'center'}),
    html.Hr(style={'color': '#7FDBFF'}),

    dcc.Tabs(id='tabs-example', value='tab-1', children=[
        dcc.Tab(label='Bar Charts', value='tab-1'),
        dcc.Tab(label='Stackbar Charts', value='tab-2'),
        dcc.Tab(label='Line Charts', value='tab-3'),
        dcc.Tab(label='Multi-line Charts', value='tab-4'),
        dcc.Tab(label='Bubble Charts', value='tab-5'),
        dcc.Tab(label='Heat Maps', value='tab-6'),
        dcc.Tab(label='Comparison Tool', value='tab-7'),
    ]),
    html.Div(id='tabs-example-content')
])


@app.callback(Output('tabs-example-content', 'children'),
              [Input('tabs-example', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('This bar chart represents the Unemployment Rate by each State.', style={'textAlign': 'center'}),
            dcc.Graph(id='graph2',
                      figure={
                          'data': data_barchart,
                          'layout': go.Layout(title='Unemployment Rate By State', xaxis_title="State",
                                              yaxis_title="Unemployment Rate")
                      }
                      ),
            html.Hr(style={'color': '#7FDBFF'}),

            html.H3('This bar chart represents the Unemployment Numbers \nby each industry and class of worker.',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='graph11',
                      style={
                          'height': 800
                      },
                      figure={
                          'data': data_barchart2,
                          'layout': go.Layout(title='Unemployment Numbers by Industry', xaxis_title="Industry",
                                              yaxis_title="Unemployment Number in Thousands",
                                              margin=dict(b=370), xaxis=dict(tickangle=90))
                      }
                      )
        ])

    elif tab == 'tab-2':
        return html.Div([
            html.H3(
                'This stack bar chart represent the fatal work injuries for Self-employed / Wage and salary employees from 2014 to 2018.',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph3',
                      figure={
                          'data': data_stackbarchart,
                          'layout': go.Layout(title='Fatal Work Injuries', xaxis_title="Year",
                                              yaxis_title="Number of Injuries", barmode='stack')
                      }
                      ),

            html.Hr(style={'color': '#7FDBFF'}),

            html.H3(
                'This stack bar chart represent the Unemployment rate for Men and Women over four decades\nand predicitons for the future decade',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph13',
                      figure={
                          'data': data_stackbarchart2,
                          'layout': go.Layout(title='Unemployment Rate by Decades', xaxis_title="Year",
                                              yaxis_title="Unemployment Rate", barmode='stack')
                      }
                      )
        ])

    elif tab == 'tab-3':
        return html.Div([
            html.H3('This line chart represent the unemployment rate of the United States over a 15 year period.',
                    style={'textAlign': 'center'}),
            dcc.Graph(id='graph4',
                      figure={
                          'data': data_linechart,
                          'layout': go.Layout(title='United States Unemployment Rates', xaxis_title="Month / Year",
                                              yaxis_title="Unemployment Rate")
                      }
                      ),

            html.Hr(style={'color': '#7FDBFF'}),

            html.H3(
                'This line chart represent the labor participation rate of the United States over a 10 year period.',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph9',
                      figure={
                          'data': data_linechart2,
                          'layout': go.Layout(title='United States Labor Participation', xaxis_title="Month / Year",
                                              yaxis_title="Labor Participation Rate")
                      }
                      )

        ])

    elif tab == 'tab-4':
        return html.Div([
            html.H3(
                'This line chart represents the different lengths of unemployment over the course of 20 years',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph5',
                      figure={
                          'data': data_multiline,
                          'layout': go.Layout(title="Duration of Unemployment", xaxis_title="Date",
                                              yaxis_title="Unemployed Individuals")
                      }
                      ),

            html.Hr(style={'color': '#7FDBFF'}),

            html.H3(
                'This line chart represents the demographic of unemployment over the course of 20 years',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph8',
                      figure={
                          'data': data_multiline2,
                          'layout': go.Layout(title="Unemployment Statistics", xaxis_title="Date",
                                              yaxis_title="Unemployment Rate")
                      }
                      )
        ])

    elif tab == 'tab-5':
        return html.Div([
            html.H3(
                'This bubble chart represent the unemployment rate by state and number of unemployed',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph6',
                      figure={
                          'data': data_bubblechart,
                          'layout': go.Layout(title='US Unemployment Rate',
                                              xaxis={'title': 'Unemployment Rate'},
                                              yaxis={'title': 'Number of unemployed'},
                                              hovermode='closest')
                      }
                      ),

            html.Hr(style={'color': '#7FDBFF'}),

            html.H3(
                'This bubble chart represent the unemployment rate by industry and number of unemployed',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph12',
                      figure={
                          'data': data_bubblechart2,
                          'layout': go.Layout(title='US Unemployment Rate by Industry',
                                              xaxis={'title': 'Unemployment Rate'},
                                              yaxis={'title': 'Number of Unemployed'},
                                              hovermode='closest')
                      }
                      )
        ])

    elif tab == 'tab-6':
        return html.Div([
            html.H3(
                'This heat map represent the labor participation rate in the US by month since 2010.',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph7',
                      figure={
                          'data': data_heatmap,
                          'layout': go.Layout(title='Labor participation rate by Month since 2010',
                                              xaxis={'title': 'Month'}, yaxis={'title': 'Year'})
                      }
                      ),

            html.Hr(style={'color': '#7FDBFF'}),

            html.H3(
                'This heat map represent the unemployment number in the US by month since 2010.',
                style={'textAlign': 'center'}),
            dcc.Graph(id='graph10',
                      figure={
                          'data': data_heatmap2,
                          'layout': go.Layout(title='Umemployment numbers by Month in thousands',
                                              xaxis={'title': 'Month'}, yaxis={'title': 'Year'})
                      }
                      )
        ])

    elif tab == 'tab-7':
        return html.Div([
            html.H3(
                'This is a tool that lets you select from multiple graphs for comparison purposes',
                style={'textAlign': 'center'}),

            dcc.Graph(figure=ct),
            dcc.Graph(figure=ct)
        ])


if __name__ == '__main__':
    app.run_server()
