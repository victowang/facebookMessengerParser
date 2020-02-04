import dash
import dash_core_components as dcc
import dash_html_components as html
import csv_to_data

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
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

if __name__ == '__main__':
    app.run_server(debug=True)