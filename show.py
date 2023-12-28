import plotly.graph_objects as go
from plotly.subplots import make_subplots

def showCharts(data):
    fig = make_subplots(rows=1, cols=1, shared_xaxes=True, vertical_spacing=0.05, row_heights=[1])
    fig.add_trace(go.Candlestick(x=data['date'],
                                 open=data['open'],
                                 high=data['high'],
                                 low=data['low'],
                                 close=data['close'],
                                 name='Price'), row=1, col=1)
    fig.update_layout(title='Graphics', xaxis_title='date', xaxis_rangeslider_visible=False, height=800)
    fig.show()
