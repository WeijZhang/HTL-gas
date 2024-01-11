# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 12:17:46 2023

@author: A
"""
#%%
import streamlit as st
import pandas as pd
from joblib import load
import numpy as np

# 请确保model.pkl的路径与实际路径相匹配
MODEL_PATH = 'model.pkl'
# 载入预先训练好的模型
model = load(MODEL_PATH)

# 定义一个函数来处理输入并进行预测
def predict_properties(input_features):
    C1 = input_features['CCC'] 
    H1 = input_features['HHH'] 
    N1= input_features['NNN'] 
    O1 = input_features['OOO'] 
    ash1 = input_features['ash'] 
    SC1 = input_features['Solid_content']
    T1 = input_features['Temperature']
    P1 = input_features['Pressure'] 
    RT1 = input_features['Residence_time']
    # 4. 合并输入特征并转换为 NumPy 数组
    x=np.array([[C1,H1,N1,O1,ash1,SC1,T1,P1,RT1]])
    #x=np.array(x).reshape(-1,9)
    # 5. 使用模型进行预测
    prediction = model.predict(x)
    return prediction
#%%
# 使用 CSS 来自定义 Streamlit 应用的样式
st.markdown(f"""
    <style>
    html, body {{
        font-family: 'Times New Roman', Times, serif;
    }}
    [class*="st-"] {{
        font-family: 'Times New Roman', Times, serif;
    }}
    h1 {{
        font-size: 27px; /* 设置表头字体大小 */
    }}
    .reportview-container {{
        background-color: #ADD8E6; /* 修改为浅蓝色背景 */
    }}
    .sidebar .sidebar-content {{
        background-color: #456789; /* 侧边栏颜色 */
    }}
    </style>
    """, unsafe_allow_html=True)

#%%
st.markdown('<h1 class="big-font">Prediction of gaseous compositions producted from liquefaction of biomass</h1>', unsafe_allow_html=True)


# 输入字段布局
col1, col2= st.columns(2)
with col1:
    st.markdown(f'<div class="st-bc">', unsafe_allow_html=True)
    st.markdown('**Elementary compositions**')
    C1 = st.number_input('C (wt.%)', min_value=0.0, value=50.0, step=0.1, key='C')
    H1 = st.number_input('H (wt.%)', min_value=0.0, value=5.0, step=0.1, key='H')
    N1 = st.number_input('N (wt.%)', min_value=0.0, value=1.5, step=0.1, key='N')
    O1 = st.number_input('O (wt.%)', min_value=0.0, value=40.0, step=0.1, key='O')
    ash1 = st.number_input('Ash (wt.%)', min_value=0.0, value=5.0, step=0.1, key='ash')
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="st-ba">', unsafe_allow_html=True)
    st.markdown('**HTL conditions**')
    SC1 = st.number_input('SC (%)', min_value=7.0, value=99.0, step=0.1, key='Solid_content')
    T1 = st.number_input('Tempreature (C)', min_value=0.0, value=400.0, step=0.1, key='Temperature')
    RT1 = st.number_input('Residence time (min)', min_value=0.0, value=100.0, step=0.1, key='Residence_time')
    P1 = st.number_input('Pressure (MPa)', min_value=0.0, value=50.0, step=0.1, key='Pressure')
    st.markdown('</div>', unsafe_allow_html=True)

# 收集所有输入数据
input_features = {'CCC': C1, 'HHH': H1, 'NNN': N1, 'OOO': O1, 'ash':ash1, 'Solid_content': SC1, 'Temperature': T1,'Residence_time': RT1, 'Pressure': P1}
#%%
#input_features = { 'C1': C, 'H1': H, 'N1': N, 'O1': O,  'ash1':ash, 'SC1': Solid_content, ' T1':Temperature, 'RT1': Residence_time, 'P1': Pressure}
# 当用户点击预测按钮时执行
# 在每列之上显示标题
st.write('Prediction of gaseous compositions:')# 定义三列
col1, col2, col3, col4 = st.columns(4)
if st.button('Predict'):
    prediction = predict_properties(input_features)
    # 提取每个预测值并格式化
    #CO2 = prediction[:, 0]  # 假设预测结果是一个二维数组
    #CH4 = prediction[:, 1]
    #CO = prediction[:, 2]
    #H2 = prediction[:, 3]

    # 在三列中显示预测结果
    col1.write(f'CO2 (mol/kg): prediction[:,0]')
    col2.write(f'CH4 (mol/kg): prediction[:,1]')
    col3.write(f'CO (mol/kg): prediction[:,2]')
    col4.write(f'H2 (mol/kg): prediction[:,3]')
else:
    # 按钮未点击时也在三列中显示标签
    col1.write('CO2 (mol/kg) =')
    col2.write('CH4 (mol/kg) =')
    col3.write('CO (mol/kg) =')
    col4.write('H2 (mol/kg) =')


#%%
