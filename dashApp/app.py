import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import csv_to_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div(children=[
    html.H1(children='Display data from facebookMessengerParser'),
    html.Div(children='''made with Python Dash'''),

    dcc.Graph(
        style={'height': '700px'},
        id='sent-reactions-graph',
        figure={
            'data': csv_to_data.sent("data/csv/sentReactions.csv"),
            'layout': { 'title': 'Sent reactions' },
        }
    ),
    dcc.Graph(
        style={'height': '700px'},
        id='received-reactions-graph',
        figure={
            'data': csv_to_data.received("data/csv/receivedReactions.csv"),
            'layout': {'title': 'Received reactions'},
        }
    ),
]
)

radio_charts = csv_to_data.sent_radar_charts("data/csv/sentReactions.csv")
for radio_chart_dict in radio_charts[:]:
    fig = go.Figure(
        data=go.Scatterpolar(
            r=radio_chart_dict['r'],
            theta=radio_chart_dict['theta'],
            fill='toself',
        ),
    )
    fig.update_layout(
        title=radio_chart_dict['name'],
    )
    fig.show()

app.layout = layout

if __name__ == '__main__':
    app.run_server(debug=True)