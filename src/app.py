import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# load dataset
try:
    df = pd.read_csv('D:/urban mobility/data/processed/uk_accidents_2016.csv')
except FileNotFoundError:
    print("Error: The file 'uk_accidents_2016.csv' was not found.")
    print("Please make sure the file path is correct and the preprocessing script has been run.")
    exit()

# data preparation and visualization
if len(df) > 50000:
    df_sample = df.sample(n=50000, random_state=42)
else:
    df_sample = df

df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M', errors='coerce').dt.hour
df.dropna(subset=['Hour'], inplace=True)
df['Hour'] = df['Hour'].astype(int)

# plotly visualizations
fig_map = px.scatter_map(
    df_sample,
    lat="Latitude",
    lon="Longitude",
    color="Accident_Severity",
    color_discrete_map={
        "Slight": "#2a9d8f",
        "Serious": "#f4a261",
        "Fatal": "#e76f51"
    },
    zoom=5,
    height=600,
    title="Accident Hotspots in the UK (2016)",
    hover_name="Accident_Index",
    hover_data=["Road_Type", "Weather_Conditions", "Speed_limit"]
)
fig_map.update_layout(mapbox_style="open-street-map")
fig_map.update_layout(margin={"r":0,"t":40,"l":0,"b":0})

weather_counts = df['Weather_Conditions'].value_counts().nlargest(10)
fig_weather = px.bar(
    weather_counts,
    x=weather_counts.index,
    y=weather_counts.values,
    title="Top 10 Weather Conditions During Accidents",
    labels={'x': 'Weather Condition', 'y': 'Number of Accidents'}
)
fig_weather.update_traces(marker_color='#2a9d8f')

hourly_counts = df.groupby('Hour')['Accident_Index'].count().reset_index()
hourly_counts.rename(columns={'Accident_Index': 'Accident_Count'}, inplace=True)
fig_hourly = px.bar(
    hourly_counts,
    x='Hour',
    y='Accident_Count',
    title='Accidents by Hour of the Day',
    labels={'Hour': 'Hour of Day (24h)', 'Accident_Count': 'Number of Accidents'}
)
fig_hourly.update_traces(marker_color='#f4a261')
fig_hourly.update_layout(xaxis = dict(tickmode = 'linear', dtick = 1))

road_type_counts = df['Road_Type'].value_counts().nlargest(5)
fig_road_type = px.pie(
    road_type_counts,
    names=road_type_counts.index,
    values=road_type_counts.values,
    title="Accident Distribution by Road Type",
    hole=.3
)

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div(style={'backgroundColor': '#f9f9f9', 'fontFamily': 'sans-serif'}, children=[
    # Header
    html.Div(
        style={'backgroundColor': '#2c3e50', 'padding': '20px', 'color': 'white', 'textAlign': 'center'},
        children=[
            html.H1('Urban Mobility & Traffic Accident Insights', style={'margin': '0', 'fontSize': '2.5em'}),
            html.H2('United Kingdom - 2016', style={'margin': '0', 'fontWeight': 'normal', 'fontSize': '1.5em'})
        ]
    ),

    # Main Content Area
    html.Div(style={'padding': '20px'}, children=[
        # Map
        html.Div(
            style={'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'borderRadius': '5px', 'backgroundColor': 'white', 'padding': '10px'},
            children=[
                 dcc.Graph(id='accident-map', figure=fig_map)
            ]
        ),

        # Two-column layout for charts
        html.Div(style={'display': 'flex', 'marginTop': '20px', 'gap': '20px'}, children=[
            # Left Column
            html.Div(
                style={'width': '50%', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'borderRadius': '5px', 'backgroundColor': 'white', 'padding': '20px'},
                children=[
                    dcc.Graph(id='weather-chart', figure=fig_weather)
                ]
            ),
            # Right Column
            html.Div(
                style={'width': '50%', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'borderRadius': '5px', 'backgroundColor': 'white', 'padding': '20px'},
                children=[
                     dcc.Graph(id='road-type-chart', figure=fig_road_type)
                ]
            ),
        ]),
        
        # Full-width chart for hourly data
        html.Div(
            style={'marginTop': '20px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.2)', 'borderRadius': '5px', 'backgroundColor': 'white', 'padding': '20px'},
            children=[
                dcc.Graph(id='hourly-chart', figure=fig_hourly)
            ]
        ),
    ])
])

# run the app
if __name__ == '__main__':
    app.run(debug=True)