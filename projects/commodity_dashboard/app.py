# base imports
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px

# import utils function
from utils.load_clean_data import load_and_clean_data

# load the clean data
df = load_and_clean_data()
# get unique contracts
contracts = df['contract_id'].unique()

# initialize the app
app = dash.Dash(__name__)
app.title = "WTI Oil Futures Dashboard"

# app layout
app.layout = html.Div([
    # header title
    html.H1("WTI Oil Futures Dashboard", style={'textAlign': 'center'}),

    # dropdown for contract selection
    dcc.Dropdown(
        id='contract-dropdown',
        options=[{'label': contract, 'value': contract} for contract in contracts],
        value=contracts[0],  # default value
    ),

    # close price graph
    dcc.Graph(id='close-price-chart'),
])

# Callback
@app.callback(
    Output('close-price-chart', 'figure'),
    Input('contract-dropdown', 'value')  # single input
)
def update_chart(selected_contract):
    # subset the dataframe based on selected contract
    contract_df = df[df['contract_id'] == selected_contract]
    
    # generate the line chart
    fig = px.line(contract_df, x='date', y='close', title=f'{selected_contract} Close Price')
    # show line and markers
    fig.update_traces(mode='lines+markers')
    
    return fig

# run the app
if __name__ == '__main__':
    app.run(debug=True)
