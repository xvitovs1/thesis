import pandas as pd
import plotly.plotly as py
import plotly
import plotly.graph_objs as go

import sys

if(len(sys.argv) != 4):
    print('Usage: python instructions_count.py basic_file epta_file staged_file')
    exit(0)

basic = pd.read_csv(sys.argv[1], ' ')
epta = pd.read_csv(sys.argv[2], ' ')
staged = pd.read_csv(sys.argv[3], ' ')

beforeBasic = basic['beforeI'].sum()
afterBasic = basic['afterI'].sum()
pBasic = (afterBasic - beforeBasic) / (beforeBasic/100)

beforeEpta = epta['beforeI'].sum()
afterEpta = epta['afterI'].sum()
pEpta = (afterEpta - beforeEpta) / (beforeEpta/100)

beforeStaged = staged['beforeI'].sum()
afterStaged = staged['afterI'].sum()
pStaged = (afterStaged - beforeStaged) / (beforeStaged/100)

layout = go.Layout(
	xaxis=dict(
        titlefont=dict(
            color='black',
            size=14
        ),
        tickfont=dict(
            color='black',
            size = 14
        )
   ),
   yaxis=dict(
        titlefont=dict(
            color='black',
            size=14
        ),
        tickfont=dict(
            color='black',
            size=14
        )
   )
)

data = [go.Bar(
            x=['basic', 'ePTA', 'staged'],
            y=[pBasic, pEpta, pStaged],
    )]

fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='basic_bar')
