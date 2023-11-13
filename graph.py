import plotly.express as px
import streamlit as st
import plotly.graph_objects as go
import numpy as np

tab1, tab2, tab3, tab4 = st.tabs(["P112D", "P113D", "P122D", "P123D"])
with tab1:
    st.header('P1.1 (2D case)')
    col1, col2, col3 = st.columns(3)
    with col1:
        x_v = st.number_input("x-coordinate for v", key='1')
        x_u = st.number_input("x-coordinate for u", key='2')
        t = st.slider("Parameter t", -10.0, 10.0, step=0.1, key='3')
    with col2:
        y_v = st.number_input("y-coordinate for v", key='4')
        y_u = st.number_input("y-coordinate for u", key='5')
    t_l = np.linspace(-10, 10, 100)
    x_w = x_v + t_l * x_u
    y_w = y_v + t_l * y_u
    fig112D = go.Figure(data=[go.Scatter(x=x_w, y=y_w, mode='lines+markers', name='points'),
                    go.Scatter(x=[x_v], y=[y_v], mode='markers', name='v'),
                    go.Scatter(x=[0,x_u], y=[0,y_u], mode='lines', name='u'),
                    go.Scatter(x=[x_v + t * x_u], y=[y_v + t * y_u], mode='markers', name='w')])
    st.plotly_chart(fig112D, use_container_width=True)

with tab2:
    st. header('P1.1 (3D case)')
    col1, col2, col3 = st.columns(3)
    with col1:
        x3_v = st.number_input("x-coordinate for v", key='6')
        x3_u = st.number_input("x-coordinate for u", key='7')
        t3 = st.slider("Parameter t", -10.0, 10.0, step=0.1, key='8')
    with col2:
        y3_v = st.number_input("y-coordinate for v", key='9')
        y3_u = st.number_input("y-coordinate for u", key='10')
    with col3:
        z3_v = st.number_input("z-coordinate for v", key='11')
        z3_u = st.number_input("z-coordinate for u", key='12')
    x3_w = x3_v + t_l * x3_u
    y3_w = y3_v + t_l * y3_u
    z3_w = z3_v + t_l * z3_u
    fig113D = go.Figure(data=[go.Scatter3d(x=x3_w, y=y3_w, z=z3_w, line=dict(color='darkblue', width=2)),
                            go.Scatter3d(x=[0,x3_u], y=[0,y3_u], z=[0,z3_u], line=dict(color='red', width=2)),
                            go.Scatter3d(x=[x3_v + t3 * x3_u], y=[y3_v + t3 * y3_u], z=[z3_v + t3 * z3_u], marker=dict(color='yellow'))])
    st.plotly_chart(fig113D, use_container_width=True)

with tab3:
    st. header('P1.2 (2D case)')
    col1, col2, col3 = st.columns(3)
    with col1:
        x_u = st.number_input("x-coordinate for u", key='13')
        x_v = st.number_input("x-coordinate for v", key='14')
        t = st.slider("Parameter t", -10.0, 10.0, step=0.1, key='15')
    with col2:
        y_u = st.number_input("y-coordinate for u", key='16')
        y_v = st.number_input("y-coordinate for v", key='17')
    x_w = t_l * x_u + (1-t_l) * x_v
    y_w = t_l * y_u + (1-t_l) * y_v

    fig122D = go.Figure(data=[
        go.Scatter(x=x_w, y=y_w, mode='lines+markers', name='line'),
        px.scatter(x=[x_v, x_u], y=[y_v, y_u], color_discrete_sequence=["black"]).data[0],
        go.Scatter(x=[(1-t) * x_v + t * x_u], y=[(1-t) * y_v + t * y_u], mode='markers', name='w')])
    st.plotly_chart(fig122D, use_container_width=True)

with tab4:
    st.header('P1.2 (3D case)')
    col1, col2, col3 = st.columns(3)
    with col1:
        x3_v = st.number_input("x-coordinate for v", key='18')
        x3_u = st.number_input("x-coordinate for u", key='19')
        t3 = st.slider("Parameter t", -10.0, 10.0, step=0.1, key='20')
    with col2:
        y3_v = st.number_input("y-coordinate for v", key='21')
        y3_u = st.number_input("y-coordinate for u", key='22')
    with col3:
        z3_v = st.number_input("z-coordinate for v", key='23')
        z3_u = st.number_input("z-coordinate for u", key='24')
    x3_w = (1-t_l) * x3_v + t_l * x3_u
    y3_w = (1-t_l) * y3_v + t_l * y3_u
    z3_w = (1-t_l) * z3_v + t_l * z3_u
    fig113D = go.Figure(data=[
        go.Scatter3d(x=x3_w, y=y3_w, z=z3_w, line=dict(color='darkblue', width=2)),
        go.Scatter3d(x=[x3_u, x3_v], y=[y3_u, y3_v], z=[z3_u, z3_v], line=dict(color='red', width=2)),
        go.Scatter3d(x=[(1-t3) * x3_v + t3 * x3_u], y=[(1-t3) * y3_v + t3 * y3_u], z=[(1-t3) * z3_v + t3 * z3_u], marker=dict(color='yellow'))])
    st.plotly_chart(fig113D, use_container_width=True)
