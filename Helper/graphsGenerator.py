import plotly
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

colors = {
    'background': '#111111',
    'text': '#006a71'}

df = pd.read_csv("C:\\Users\\omkar\\Desktop\\Python_Projects\\FAANG\\loggingInfo.csv", header=0)

perDayCount = df.groupby(["EndDate"], as_index=False)["Duration"].count()
perDayCount.rename(columns={'Duration': 'Count'}, inplace=True)

# # pie-chart
minRange, maxRange = perDayCount['EndDate'].min(), perDayCount['EndDate'].max()
pieChart = px.bar(perDayCount, y='Count', x='EndDate', text='Count',
                  hover_data=['Count'], color='Count',
                  labels={'Count': 'Count'}, color_continuous_scale=px.colors.sequential.Viridis)
pieChart.update_traces(texttemplate='%{text:.2s}', textposition='outside')
pieChart.update_layout(uniformtext_minsize=8, uniformtext_mode='hide', yaxis=dict(range=[minRange, maxRange]))

# pieChart = px.pie(perDayCount, values='Count', names='EndDate',
#                   title='Total Count Per Day',
#                   hover_data=['Count'], labels={'Count': 'Count'})
# pieChart.update_traces(textposition='inside', textinfo='percent+label')


# pie-chart-dificulties
difficultCount = df.groupby(["Difficult"], as_index=False)["Duration"].count()
difficultCount.rename(columns={'Duration': 'Count'}, inplace=True)

pieChartDifficult = px.pie(difficultCount, values='Count', names='Difficult',
                           title='Difficult Count',
                           hover_data=['Count'], labels={'Count': 'Count'})
pieChartDifficult.update_traces(textposition='inside', textinfo='percent+label')

# pieChart.update_layout(paper_bgcolor="#1b262c", font={'color': "#ffffdd", 'family': "Arial"})
# pieChart.write_html("pieChart.html")

# time series chart
# totalhours = df
# totalhours['DateTime'] = totalhours['EndDate'] + ' ' + totalhours['EndTime']
# print(totalhours)
totalhours = df.groupby(["EndDate"], as_index=False)["Duration"].sum()


TimeSeries = px.scatter(totalhours, x='EndDate', y='Duration', title='Total Time Series', range_x=[minRange, maxRange])
TimeSeries.update_xaxes(
    rangeslider_visible=True,
    showticklabels=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# TimeSeries.update_layout(paper_bgcolor="#1b262c", font={'color': "#ffffdd", 'family': "Arial"})
# TimeSeries.write_html("TotalTimeSeries.html")

# bar chart
BarGraph = px.bar(df, y='Duration', x='Name', text='Duration',
                  hover_data=['Duration'], color='Duration',
                  labels={'Duration': 'Duration'}, color_continuous_scale=px.colors.sequential.Viridis)
BarGraph.update_traces(texttemplate='%{text:.2s}', textposition='outside')
BarGraph.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
BarGraph.update_xaxes(showticklabels=False)
# BarGraph.update_layout(paper_bgcolor=colors['background'])

# BarGraph.update_layout(paper_bgcolor="#1b262c", font={'color': "#ffffdd", 'family': "Arial"})
# BarGraph.write_html("BarGraphs.html")

# Gauge  chart
data = df
filter = data["EndDate"] != " None"
data.where(filter, inplace=True)

GaugeGraph = go.Figure(go.Indicator(
    mode="gauge+number+delta",
    value=data['Duration'].count(),
    domain={'x': [0, 1], 'y': [0, 1]},
    title={'text': "Total Completed", 'font': {'size': 24}},
    delta={'reference': 200, 'increasing': {'color': "RebeccaPurple"}},
    gauge={
        'axis': {'range': [None, 200], 'tickwidth': 1, 'tickcolor': "#ffffdd"},
        'bar': {'color': "#fa1616"},
        'bgcolor': "white",
        'borderwidth': 2,
        'bordercolor': "gray",
        'steps': [
            {'range': [0, 50], 'color': '#d3de32'},
            {'range': [50, 100], 'color': '#cbeaed'},
            {'range': [100, 150], 'color': '#ffffdd'},
            {'range': [150, 200], 'color': '#006a71'}],
        'threshold': {
            'line': {'color': "red", 'width': 4},
            'thickness': 0.75,
            'value': 150}}))

# GaugeGraph.update_layout(paper_bgcolor="#1b262c", font={'color': "#ffffdd", 'family': "Arial"})
# GaugeGraph.write_html("GaugeGraphs.html")

# hori bar graph

TagCount = df.groupby(["Tag"], as_index=False)["Duration"].count()
TagCount.rename(columns={'Duration': 'Count'}, inplace=True)

# print(TagCount)

# TagCountFig = go.Figure(go.Bar(
#     x=TagCount['Count'],
#     y=TagCount['Tag'],
#     orientation='h'))

# TagCountFig = px.bar(TagCount, x='Count', y='Tag', orientation='h', color='Tag')


TagCountFig = px.bar(TagCount, y='Tag', x='Count', orientation='h', text='Count',
                     hover_data=['Count'], color='Tag',
                     labels={'Duration': 'Count'})
TagCountFig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
TagCountFig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')

# TagCountFig.show()
#-----------------------------------
import dash
import dash_core_components as dcc
import dash_html_components as html
# import plotly.express as px
# import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.Div([


        html.Div([
            html.H1('FAANG', style={
                'textAlign': 'center',
                'color': colors['text'],
            }),
        ], className="twelve columns"),


        html.Div([
            html.H3('Over All Progress', style={
                'textAlign': 'center',
                'color': colors['text'],
            }),
            dcc.Graph(id='g1', figure=TimeSeries)
        ], className="twelve columns"),

        html.Div([
            # html.H3('Completed Till Now', style={
            #     'textAlign': 'center',
            #     'color': colors['text'],
            # }),
            dcc.Graph(id='g3', figure=GaugeGraph)
        ], className="four columns"),

        html.Div([
            html.H3('Time Taken To Solve', style={
                'textAlign': 'center',
                'color': colors['text'],
            }),
            dcc.Graph(id='g4', figure=BarGraph)
        ], className="seven columns"),

        html.Div([
            html.H3('Count Per Day', style={
                'textAlign': 'center',
                'color': colors['text'],
            }),
            dcc.Graph(id='g2', figure=pieChart)
        ], className="five columns"),

        html.Div([
            html.H3('Difficulties Count', style={
                'textAlign': 'center',
                'color': colors['text'],
            }),
            dcc.Graph(id='g6', figure=pieChartDifficult)
        ], className="five columns"),


        html.Div([
            html.H3('Tags Based Completion', style={
                'textAlign': 'center',
                'color': colors['text'],
            }),
            dcc.Graph(id='g5', figure=TagCountFig)
        ], className="twelve columns"),
        # html.Div([
        #     html.H3('Column 6'),
        #     dcc.Graph(id='g6', figure=pieChart)
        # ], className="twelve columns")
    ], className="five row"),
])


if __name__ == '__main__':
    app.run_server(debug=False)
