import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image


st.header('FSCT Data Dashboard')
st.header('Represent and analyse Forest data dynamically')
st.markdown('This webb app is an example of how data can be presented in a user responsive dashboard. The data shown corresponds'
            ' to a forest plot in Carboneras (Soria, Spain) ')

tree_data= pd.read_csv(r'tree_data.csv')

st.markdown('*Data from FSCT*')
st.dataframe(tree_data)


st.header('Plot tree data : Volume vs Height')
st.subheader(' This graph plots the tree data obtained from FSCT alogrithm.')

st.markdown('**Filter your data by tree Id**')
# add slider for selecting the tree
# Add a slider to the sidebar:
tree_id_slider = st.slider(
    'Select a tree ID',
    0, 21, (5, 15)
)

# the tree_id_slider_returns a tuple
# generate a list wiht all teh valeus to populate the graph
list = [x for x in range(tree_id_slider[0],tree_id_slider[1]+1)]

# create a scatter plot with all the trees per plot representing volume vs height
scatter_plot = px.scatter(tree_data[tree_data['TreeId'].isin(list)],
                y="Height",
                x="Volume_1",
                color="CCI_at_BH",
                size='DBH',
                hover_data=['TreeId'])

st.plotly_chart(scatter_plot, use_container_width=True)



lat = tree_data['y_tree_base']
lon = tree_data ['x_tree_base']

# lon_lat = zip(lon,lat)

st.header('Add your data to a Map')
st.subheader('Info')

st.markdown('The locations shown were randomly generated in an area clsoe to the real plot location.'
            ' The coordinates exported by this FSCT run were in a local CRS. This map represents coordinates in WGS84 CRS.'
            )

map_data = pd.DataFrame(
    np.random.randn(21, 2) / [500, 500] + [41.737, -2.586],
    #lon_lat,
    columns=['lat', 'lon'])

st.map(map_data)

#  load images
adm = Image.open(r'admarco.png')
fbs = Image.open(r'fbezares.png')
jc = Image.open(r'jc.png')
dh = Image.open(r'dhernandez.png')
sm = Image.open(r'smorcuende.jfif')

## add Elements to the sidebar

# add header title to teh side bar
sidebar_title = st.sidebar.title('The SRURAL Team')

st.sidebar.header('Antonio de Marco | Chief')


st.sidebar.image(adm, caption='Antonio de Marco')
st.sidebar.markdown('Strength: Coordination skills')
st.sidebar.markdown('Weakness: Atilano')

st.sidebar.header('Sergio Morcuende | Docker Master ')

st.sidebar.image(sm, caption='Sergio Morcuende')
st.sidebar.markdown('Strength: Linux')
st.sidebar.markdown('Weakness: Windows')
st.sidebar.markdown('')

st.sidebar.header('Fernando Bezares | GIS Geek')
st.sidebar.image(fbs, caption='Fernando Bezares')
st.sidebar.markdown('Strength: Puns')
st.sidebar.markdown('Weakness: Hairdressers over 40')
st.sidebar.markdown('')

st.sidebar.header('JC | Data Scientist')
st.sidebar.image(jc, caption='JC')
st.sidebar.markdown('Strength: Furry Porn')
st.sidebar.markdown('Weakness: Installing CUDA | Piluca')
st.sidebar.markdown('')

st.sidebar.header('Daniel Hernandez | Android Developer')
st.sidebar.image(dh, caption='Daniel Hernández')
st.sidebar.markdown('Strength: Massive energy')
st.sidebar.markdown('Weakness: BootCV')





# Add a selectbox to the sidebar:
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )
#
# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )



#'''
#chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
#
#
#x = st.slider('x')  # 👈 this is a widget
#st.write(x, 'squared is', x * x)
#
#st.line_chart(chart_data)
#
#'''

#'''
#dataframe = pd.DataFrame(
#    np.random.randn(10, 20),
#    columns=('col %d' % i for i in range(20)))
#
#st.dataframe(dataframe.style.highlight_max(axis=0))
#'''
# print tree base coords in the map
