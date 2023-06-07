#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.figure_factory as ff
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd

import math
import random
from datetime import timedelta

import warnings
warnings.filterwarnings("ignore")


# In[2]:


import plotly.express as px


# In[12]:


import plotly as py
py.offline.init_notebook_mode(connected = True)


# In[9]:


import os

try:
    os.system("rm -rf Covid-19-Preprocessed-Dataset")
    
except:
    print('File does not exist')


# In[6]:


df =pd.read_csv('datacovid/preprocessed/covid_19_data_cleaned.csv',
               parse_dates=['Date'])


# In[11]:


df.head()


# In[13]:


import missingno as msno
msno.matrix(df)


# In[4]:


df['Province/State'] = df['Province/State'].fillna("")


# In[5]:


df


# In[2]:


country_daywise =pd.read_csv('datacovid/preprocessed/country_daywise.csv',
               parse_dates=['Date'])

countrywise =pd.read_csv('datacovid/preprocessed/countrywise.csv',
               )

daywise =pd.read_csv('datacovid/preprocessed/daywise.csv',
               parse_dates=['Date'])


# In[17]:


countrywise.head()


# In[18]:


country_daywise.head()


# In[19]:


daywise.head()


# In[20]:


df


# In[21]:


confirmed = df.groupby('Date').Confirmed.agg('sum').reset_index()


# In[22]:


confirmed


# In[23]:


recovered = df.groupby('Date').Recovered.agg('sum').reset_index()
recovered


# In[24]:


death = df.groupby('Date').Deaths.agg('sum').reset_index()
death


# In[25]:


df.isna().sum()


# In[26]:


df.info()


# In[27]:


df.query('Country == "US"')


# Scatter plot for Confirmed cases

# In[28]:


confirmed.head()


# In[29]:


fig = go.Figure()

fig.add_trace(go.Scatter(x = confirmed.Date, y = confirmed.Confirmed,mode= 'lines+markers', name = 'Confirmed Cases', line = dict(color = 'Orange'
                                                                                                                                  , width = 1)))

fig.add_trace(go.Scatter(x = recovered.Date, y = recovered.Recovered,mode= 'lines+markers', name = 'Recovered Cases', line = dict(color = 'Red',
                                                                                                                                  width =1)))


fig.add_trace(go.Scatter(x = death.Date, y = death.Deaths,mode= 'lines+markers', name = 'Death Cases', line = dict(color = 'Blue',
                                                                                                                                  width =1)))

fig.update_layout(title = 'Worldwide Covid cases', xaxis_tickfont_size =14, 
                 yaxis = dict(title = 'Number of cases'))
fig.show()


# Cases Timeplaps on worldmap

# In[30]:


df.info()


# In[31]:


df.Date = df.Date.astype(str
              )


# In[32]:


fig = px.density_mapbox(df, lat='Lat', lon= 'Long', hover_name = 'Country',
                       hover_data= ['Confirmed','Recovered','Deaths'],
                        animation_frame='Date',
                        color_continuous_scale='Portland',
                        radius=7,
                        zoom = 0,
                        height= 700
                       )

fig.update_layout(title = 'worldwide covid 19 cases with timelapse')

fig.update_layout(mapbox_style = 'open-street-map', mapbox_center_lon = 0)

fig.show()


# Total cases on ships

# In[33]:


df.Date = df.Date.astype(np.datetime64)


# In[ ]:


df.info()


# In[ ]:


ship_rows = df['Province/State'].str.contains('Grand Princess') | df['Province/State'].str.contains('Diamond Princess') | df['Country'].str.contains('Diamond Princess') | df.Country.str.contains('MS Zaandam')


# In[ ]:


df[ship_rows]


# In[ ]:


ship = df[ship_rows]


# In[ ]:


ship


# In[ ]:


df = df[~ship_rows]


# In[ ]:


df


# In[ ]:


ship_latest = ship[ship.Date == max(ship.Date)]


# In[ ]:


ship_latest


# In[ ]:


ship_latest.style.background_gradient(cmap = 'Pastel1_r')


# In[ ]:


get_ipython().system('pip install --upgrade pandas')


# Cases ovet time with area plot
# 

# In[ ]:


temp = df.groupby('Date')['Confirmed','Recovered','Deaths','Active'].agg('sum').reset_index()


# In[ ]:


temp =temp[temp.Date == max(temp.Date)].reset_index(drop = True)


# In[ ]:


temp


# In[ ]:


tm = temp.melt(id_vars = 'Date', value_vars= ['Active', 'Deaths','Recovered'])

act = '#ff0000'  # Define the color for 'Active'
rec = '#00ff00'  # Define the color for 'Recovered'
dth = '#0000ff'  # Define the color for 'Deaths'


fig = px.treemap(tm, 
                 path = ['variable'],
                 values = 'value',
                 height = 250,
                 width =800,
                 color_discrete_sequence=[act, rec, dth]
                )

fig.data[0].textinfo = 'label+text+value'
fig.show()


# In[ ]:


temp = df.groupby('Date')['Recovered','Deaths','Active'].agg('sum').reset_index()


# In[ ]:


temp = temp.melt(
    id_vars = 'Date',
    value_vars= ['Recovered','Deaths','Active'],
    var_name= 'Case',
    value_name='Count'
)

temp


# In[ ]:


fig = px.area(
    temp,
    x = 'Date',
    y= 'Count',
    color = 'Case',
    height = 600,
    title= 'Cases over time',
    color_discrete_sequence= [rec, dth, act]
)

fig.update_layout(xaxis_rangeslider_visible = True)
fig.show()


# Covid 19 cases on folium map

# In[34]:


temp = df[df.Date == max(df.Date)]
temp


# In[35]:


import folium


# In[36]:


m = folium.Map(
    location=[0,0],
    tiles = 'cartodbpositron', 
    min_zoom=1, max_zoom=4,
    zoom_start=1
)

for i in range(0, len(temp)):
    folium.Circle(location=[temp.iloc[i]['Lat'],temp.iloc[i]['Long']], color = 'crimson',
                  fill = 'crimson',
                  tooltip = '<li><bold> Country: '+str(temp.iloc[i]['Country']) + 
                            '<li><bold> Province: '+str(temp.iloc[i]['Province/State']) + 
                            '<li><bold> Confirmed: '+str(temp.iloc[i]['Confirmed']) + 
                            '<li><bold> Death: '+str(temp.iloc[i]['Deaths']) ,
                  radius = int(temp.iloc[i]['Confirmed'])**0.5).add_to(m)

                 
                
    
m    
    


# Confirmed cases with chloropeth maps

# In[37]:


get_ipython().system('pip install chloropleth')


# In[38]:


fig = px.choropleth(
    country_daywise,
    locations = 'Country',
    locationmode = 'country names',
    color = (country_daywise['Confirmed']),
    hover_name = 'Country',
    animation_frame= country_daywise.Date.dt.strftime('%Y-%m-%d'),
    title = 'Cases over time',
    color_continuous_scale= px.colors.sequential.Inferno
)

fig.update(layout_coloraxis_showscale = True)

fig.show()


# Deaths and Recoveries per 100 cases

# In[39]:


daywise.head()


# In[40]:


import plotly.express as px
from plotly.subplots import make_subplots

act = '#ff0000'  # Define the color for 'Confirmed'
dth = '#0000ff'  # Define the color for 'Deaths'

fig_c = px.bar(
    daywise,
    x='Date',
    y='Confirmed',
    color_discrete_sequence=[act]
)

fig_d = px.bar(
    daywise,
    x='Date',
    y='Deaths',
    color_discrete_sequence=[dth]
)

fig = make_subplots(rows=1, cols=2, shared_xaxes=False, horizontal_spacing=0.1,
                    subplot_titles=('Confirmed Cases', 'Deaths Cases'))

fig.add_trace(fig_c['data'][0], row=1, col=1)
fig.add_trace(fig_d['data'][0], row=1, col=2)

fig.update_layout(height = 400)

fig.show()


# Static colormap

# In[41]:


import plotly.express as px
import numpy as np
from plotly.subplots import make_subplots

act = '#ff0000'  # Define the color for 'Confirmed'
dth = '#0000ff'  # Define the color for 'Deaths'

fig_c = px.choropleth(
    countrywise,
    locations='Country',
    locationmode='country names',
    color=np.log(countrywise['Confirmed']),
    hover_name='Country',
    hover_data=['Confirmed']
)

fig_d = px.choropleth(
    countrywise,
    locations='Country',
    locationmode='country names',
    color=np.log(countrywise['Deaths']),
    hover_name='Country',
    hover_data=['Deaths']
)

fig = make_subplots(rows=1, cols=2, shared_xaxes=False, horizontal_spacing=0.1,
                    subplot_titles=('Confirmed Cases', 'Deaths Cases'),
                   specs=[[{'type':'choropleth'},{'type':'choropleth'}]])

fig.add_trace(fig_c['data'][0], row=1, col=1)
fig.add_trace(fig_d['data'][0], row=1, col=2)

fig.show()


# Deaths per 100 cases

# In[42]:


import plotly.express as px
from plotly.subplots import make_subplots

dth = '#0000ff'  # Define the color for 'Deaths'
rec = '#00ff00'  # Define the color for 'Recovered'

fig1 = px.line(
    daywise,
    x='Date',
    y='Deaths / 100 Cases',
    color_discrete_sequence=[dth]
)

fig2 = px.line(
    daywise,
    x='Date',
    y='Recovered / 100 Cases',
    color_discrete_sequence=[rec]
)

fig3 = px.line(
    daywise,
    x='Date',
    y='Deaths / 100 Recovered',
    color_discrete_sequence=[rec]
)

fig = make_subplots(rows=1, cols=3, subplot_titles=('Deaths / 100 Cases', 'Recovered / 100 Cases', 'Deaths / 100 Recovered'))

fig.add_trace(fig1['data'][0], row=1, col=1)
fig.add_trace(fig2['data'][0], row=1, col=2)
fig.add_trace(fig3['data'][0], row=1, col=3)

fig.update_layout(width =900)

fig.show()


# New cases and No of countries`

# In[43]:


import plotly.express as px
from plotly.subplots import make_subplots

act = '#ff0000'  # Define the color for 'Confirmed'
dth = '#0000ff'  # Define the color for 'Deaths'

fig_c = px.bar(
    daywise,
    x='Date',
    y='Confirmed',
    color_discrete_sequence=[act]
)

fig_d = px.bar(
    daywise,
    x='Date',
    y='No. of Countries',
    color_discrete_sequence=[dth]
)

fig = make_subplots(rows=1, cols=2, subplot_titles=('No of new cases per day', 'No of Countries '))

fig.add_trace(fig_c['data'][0], row=1, col=1)
fig.add_trace(fig_d['data'][0], row=1, col=2)

fig.update_layout(showlegend=False)  # Remove legend from the subplot

fig.show()


# In[44]:


daywise.columns


# Top 15 country case analysis

# In[45]:


import plotly.express as px
from plotly.subplots import make_subplots

top = 15
act = '#ff0000'  # Define the color for 'Confirmed'
dth = '#0000ff'  # Define the color for 'Deaths'
rec = '#00ff00'  # Define the color for 'Recovered'

fig_c = px.bar(
    countrywise.sort_values('Confirmed').tail(top),
    x='Confirmed',
    y='Country',
    text='Confirmed',
    orientation='h',
    color_discrete_sequence=[act]
)

fig_d = px.bar(
    countrywise.sort_values('Deaths').tail(top),
    x='Deaths',
    y='Country',
    text='Deaths',
    orientation='h',
    color_discrete_sequence=[dth]
)

fig_a = px.bar(
    countrywise.sort_values('Active').tail(top),
    x='Active',
    y='Country',
    text='Active',
    orientation='h',
    color_discrete_sequence=[act]
)

fig_r = px.bar(
    countrywise.sort_values('Recovered').tail(top),
    x='Recovered',
    y='Country',
    text='Recovered',
    orientation='h',
    color_discrete_sequence=[rec]
)

fig = make_subplots(rows=2, cols=2, subplot_titles=('Confirmed Cases', 'Deaths Cases', 'Active Cases', 'Recovered Cases'))

fig.add_trace(fig_c['data'][0], row=1, col=1)
fig.add_trace(fig_d['data'][0], row=1, col=2)
fig.add_trace(fig_a['data'][0], row=2, col=1)
fig.add_trace(fig_r['data'][0], row=2, col=2)

fig.update_layout(showlegend=True)  # Remove legend from the subplot

fig.show()


# In[46]:


countrywise.Confirmed.nlargest(15)


# In[63]:


import plotly.express as px
from plotly.subplots import make_subplots

top = 15
act = '#ff0000'  # Define the color for 'Confirmed'
dth = '#0000ff'  # Define the color for 'Deaths'
rec = '#00ff00'  # Define the color for 'Recovered'

fig_c = px.bar(
    countrywise.sort_values('Confirmed').tail(top),
    x='Confirmed',
    y='Country',
    text='Confirmed',
    orientation='h',
    color_discrete_sequence=[act]
)

fig_d = px.bar(
    countrywise.sort_values('Deaths').tail(top),
    x='Deaths',
    y='Country',
    text='Deaths',
    orientation='h',
    color_discrete_sequence=[dth]
)

fig_a = px.bar(
    countrywise.sort_values('Active').tail(top),
    x='Active',
    y='Country',
    text='Active',
    orientation='h',
    color_discrete_sequence=[act]
)

fig_r = px.bar(
    countrywise.sort_values('Recovered').tail(top),
    x='Recovered',
    y='Country',
    text='Recovered',
    orientation='h',
    color_discrete_sequence=[rec]
)

fig_dc = px.bar(
    countrywise.sort_values('Deaths / 100 Cases').tail(top),
    x='Deaths / 100 Cases',
    y='Country',
    text='Deaths / 100 Cases',
    orientation='h',
    color_discrete_sequence=['#f84351']
)

fig_rc = px.bar(
    countrywise.sort_values('Recovered / 100 Cases').tail(top),
    x='Recovered / 100 Cases',
    y='Country',
    text='Recovered / 100 Cases',
    orientation='h',
    color_discrete_sequence=['#f84352']
)

fig = make_subplots(
    rows=2, cols=3, subplot_titles=(
        'Confirmed Cases', 'Deaths Cases', 'Active Cases', 
        'Recovered Cases', 'Death per 100 Cases', 'Recovered per 100 Cases'
    ), shared_xaxes = False, shared_yaxes = False,
    horizontal_spacing=.2,
    vertical_spacing=.5
    
)

fig.add_trace(fig_c['data'][0], row=1, col=1)
fig.add_trace(fig_d['data'][0], row=1, col=2)
fig.add_trace(fig_a['data'][0], row=1, col=3)
fig.add_trace(fig_r['data'][0], row=2, col=1)
fig.add_trace(fig_dc['data'][0], row=2, col=2)
fig.add_trace(fig_rc['data'][0], row=2, col=3)

fig.update_layout(showlegend=False)  # Remove legend from the subplot

fig.update_layout(height = 2000)
plt.tight_layout()
fig.show()


# In[48]:


countrywise.columns


# In[52]:


countrywise['Deaths / 100 Cases']


# In[64]:


conda install -c plotly plotly-orca ==1.2.1 psutil requests


# In[65]:


if not os.path.exists('images'):
    os.mkdir('images')


# In[69]:


fig.write_image('images/fig.png')


# In[68]:


pip install -U kaleido


# Scatter plot for deaths vs confirmed cases

# In[81]:



top = 15
fig = px.scatter(
    countrywise.sort_values('Deaths', ascending=False).head(top),
    x = 'Confirmed',
    y = 'Deaths',
    color = 'Country',
    size = 'Confirmed',
    height = 700,
    text = 'Country',
    log_x = True,
    log_y = True,
    title= 'Deaths vs Confirmed Cases'
)

fig.update_traces(textposition = 'top center')
fig.update_layout(showlegend = False)
fig.update_layout(xaxis_rangeslider_visible = True)
fig.show()


# In[70]:


countrywise.sort_values('Deaths', ascending=False).iloc[:15,:]


# Line plot

# In[108]:


fig = px.line(
    country_daywise,
    x='Date',
    y = 'Confirmed',
    color = 'Country',
    height = 600,
    width= 600,
    title = 'Confirmed',
    color_discrete_sequence=px.colors.cyclical.mygbm
)

fig.show()


fig = px.line(
    country_daywise,
    x='Date',
    y = 'Deaths',
    color = 'Country',
    height = 600,
    width= 600,
    title = 'Deaths',
    color_discrete_sequence=px.colors.cyclical.mygbm
)

fig.show()

fig = px.line(
    country_daywise,
    x='Date',
    y = 'Recovered',
    color = 'Country',
    height = 600,
    width= 600,
    title = 'Recovered',
    color_discrete_sequence=px.colors.cyclical.mygbm
)

fig.show()



# Growth Rate after 100 cases

# In[3]:


get_100 = country_daywise[country_daywise.Confirmed > 100]
get_100 = get_100.Country.unique()


# In[4]:


get_100


# In[7]:


temp = df[df['Country'].isin(get_100)]
temp = temp.groupby(['Country','Date']).Confirmed.sum().reset_index()
temp = temp[temp.Confirmed > 100]
temp


# In[8]:


min_date = temp.groupby('Country').Date.min().reset_index()
min_date.columns = ['Country', 'Min Date']
min_date['Min Date']


# In[9]:


from_100th_case = pd.merge(temp, min_date , on = 'Country')
from_100th_case['N days'] = (from_100th_case['Date'] - from_100th_case['Min Date']).dt.days
# from_100th_case


# In[10]:


from_100th_case


# In[14]:


import plotly.express as px


fig = px.line(
    from_100th_case,
    x = 'N days',
    y = 'Confirmed',
    color = 'Country',
    title = 'N days from 100 case'
)
fig.show()


# First and Last case Report

# In[41]:


first_date = df[df.Confirmed > 0]
first_date = first_date.groupby(['Country']).Date.agg('min').reset_index()


# In[42]:


first_date


# In[116]:


last_date = df.groupby(['Country', 'Date'])[['Confirmed', 'Deaths', 'Recovered']]
last_date = last_date.sum().diff().reset_index()

mask = (last_date.Country != last_date.Country.shift(1))
mask

last_date.loc[mask, 'Confirmed'] = np.nan
last_date.loc[mask, 'Deaths'] = np.nan
last_date.loc[mask, 'Recovered'] = np.nan
last_date.sample(10)


# In[117]:


last_date = last_date[last_date.Confirmed > 0]
last_date= last_date.groupby('Country').Date.agg('max').reset_index()
last_date


# In[121]:


first_last = pd.concat([first_date, last_date['Date']],
                       axis =1
                      )


# In[122]:


first_last.columns


# In[123]:


first_last.drop


# In[105]:


first_date.Date


# In[113]:





# In[125]:


first_last = pd.merge(first_date, last_date[['Country', 'Date']], on='Country')
                   


# In[127]:


first_last = first_last.rename(columns={'Date_x': 'Min', 'Date_y': 'Max'})


# In[128]:


first_last


# In[130]:


first_last['N days'] = first_last['Max'] - first_last['Min']


# In[131]:


first_last


# Covid 19 vs other epidemics

# In[142]:


epidemics = pd.DataFrame({
    'epidemic': ['Covid-19','SARS','EBOLA','MERS','H1N1'],
    'Start_year': [2019,2002,2013,2012,2009],
    'End_Year': [2020,2004,2016,2020,2010],
    'confirmed': [full_latest.Confirmed.sum(),1111,111002,2519,656565],
    'deaths': [full_latest.Deaths.sum(),813,11323,866,19654]
} )


# In[143]:


epidemics


# In[144]:


epidemics['Mortality'] = (epidemics.deaths / epidemics.confirmed) * 100


# In[145]:


epidemics


# In[149]:


temp = epidemics.melt(
    id_vars = 'epidemic',
    value_vars= ['confirmed', 'deaths', 'Mortality'],
    var_name = 'Case',
    value_name = 'value'
)


# In[150]:


temp


# In[151]:


fig = px.bar(
    temp, 
    x= 'epidemic',
    y = 'value',
    color = 'epidemic',
    text = 'value',
    facet_col='Case',
    color_discrete_sequence= px.colors.qualitative.Bold
)

fig.update_traces(textposition = 'outside')

fig.show()


# In[ ]:




