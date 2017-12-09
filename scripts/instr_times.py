import pandas as pd
import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import array
import sys
import operator

if(len(sys.argv) != 4):
    print('Usage: python instructions_count.py basic_file epta_file staged_file')
    exit(0)

basic = pd.read_csv(sys.argv[1], ' ')
epta = pd.read_csv(sys.argv[2], ' ')
staged = pd.read_csv(sys.argv[3], ' ')

avgBasic = basic['instr_time'].sum() / basic['instr_time'].count()
avgEpta = epta['instr_time'].sum() / basic['instr_time'].count()
avgStaged = staged['instr_time'].sum() / basic['instr_time'].count()


print('Average instrumentation times:')

print 'basic approach: {0}'.format(avgBasic)
print 'pta: {0}'.format(avgEpta)
print 'staged: {0}'.format(avgStaged)

benchmarks = array.array('i',(i for i in range(1,390)))

trace1 = go.Scatter(
    x=benchmarks,
    y=basic.sort_values(by=['instr_time'])['instr_time'].apply(lambda x: x*1000),
    mode='lines',
    name="'basic'",
    hoverinfo='name',
    line=dict(
        shape='linear'
    )
)
trace2 = go.Scatter(
    x=benchmarks,
    y=epta.sort_values(by=['instr_time'])['instr_time'].apply(lambda x: x*1000),
    mode='lines',
    name="'ePTA'",
    text=["tweak line smoothness<br>with 'smoothing' in line object"],
    hoverinfo='text+name',
    line=dict(
        shape='linear'
    )
)
trace3 = go.Scatter(
    x=benchmarks,
    y=staged.sort_values(by=['instr_time'])['instr_time'].apply(lambda x: x*1000),
    mode='lines',
    name="'staged'",
    hoverinfo='name',
    line=dict(
        shape='linear'
    )
)
data = [trace1, trace2, trace3]
layout = dict(
   xaxis=dict(
        title='The n-th fastest benchmark.',
        titlefont=dict(
            color='black'
        ),
        tickfont=dict(
            color='black'
        )
   ),
   yaxis=dict(
        title='The time of instrumentation in ms.',
        titlefont=dict(
            color='black'
        ),
        tickfont=dict(
            color='black'
        )
   ),
   legend=dict(
        traceorder='reversed',
        font=dict(
            size=16,
			color='black'
        )
	)
)
fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='instr_times')
