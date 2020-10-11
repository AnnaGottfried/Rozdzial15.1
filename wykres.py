import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

salaries = [
	("Mark", 1000),
	("John", 1500),
	("Daniel", 2300),
	("Greg", 5000)
]

names = list(map(lambda tup:tup[0], salaries))
salary_values = list(map(lambda tup:tup[1], salaries))

layout = {
	'title': 'Salaries with plotly'
}

fig = go.Figure(go.Bar(
            x=names,
            y=salary_values), layout)


app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter

'''
fig.show()

data = go.Scatter(x=names, y=salary_values)
layout = {
	'title': 'Salaries with plotly'
}
fig = go.Figure(data, layout)
fig.show()

'''
