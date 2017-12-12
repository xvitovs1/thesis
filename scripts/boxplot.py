import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd
import plotly
import array
import sys
import operator

if(len(sys.argv) != 4):
    print('Usage: python instructions_count.py basic_file epta_file staged_file')
    exit(0)

basic = pd.read_csv(sys.argv[1], ' ')
epta = pd.read_csv(sys.argv[2], ' ')
staged = pd.read_csv(sys.argv[3], ' ')

basic['increase']=basic['afterI']/basic['beforeI']
epta['increase']=epta['afterI']/epta['beforeI']
staged['increase']=staged['afterI']/staged['beforeI']

trace0 = go.Box(
    x=basic['increase'],
    name='basic',

)
trace1 = go.Box(
    x=epta['increase'],
    name='ePTA',
    marker=dict(
        color='#FF851B'
    )
)
trace2 = go.Box(
    x=staged['increase'],
    name='staged',
    marker=dict(
        color='green'
    )
)
data = [trace0, trace1, trace2]
layout = go.Layout(
    xaxis=dict(
        title='Increase of the size of the code',
        zeroline=True,
        showline=True,
		range=[0.5, 3],
        titlefont=dict(
            color='black',
            size=14
        ),
        tickfont=dict(
            color='black',
            size=16
        ),

    ),yaxis=dict(
        zeroline=True,
        showline=True,
        titlefont=dict(
            color='black',
            size=14
        ),
        tickfont=dict(
            color='black',
            size=16
        ),

    ),
    boxmode='group',
    legend=dict(
        traceorder='reversed',
        font=dict(
            size=16,
			color='black'
        )
	)

)
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig)
