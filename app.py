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
    C1 = input_features['C'] 
    H1 = input_features['H'] 
    N1= input_features['N'] 
    O1 = input_features['O'] 
    ash1 = input_features['ash'] 
    SC1 = input_features['Solid_content']
    T1 = input_features['Temperature']
    P1 = input_features['Pressure'] 
    RT1 = input_features['Residence_time']
   

    # 4. 合并输入特征并转换为 NumPy 数组
    input_array = np.array([C1,H1,N1,O1,ash1,SC1,T1,P1,RT1])

    # 5. 使用模型进行预测
    prediction = model.predict(input_array)
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
st.markdown('<h1 class="big-font">Predict properties of bio-oil producted from co-liquefaction</h1>', unsafe_allow_html=True)


# 输入字段布局
col1, col2= st.columns(2)



with col1:
    st.markdown(f'<div class="st-bc">', unsafe_allow_html=True)
    st.markdown('**Elementary compositions**')
    C1 = st.number_input('C (wt.%)', min_value=0.0, value=50.0, step=0.1, key='c_sew_sludge')
    H1 = st.number_input('H (wt.%)', min_value=0.0, value=5.0, step=0.1, key='h_sew_sludge')
    o_sewage_sludge = st.number_input('O (wt.%)', min_value=0.0, value=40.0, step=0.1, key='o_sew_sludge')
    s_sewage_sludge = st.number_input('S (wt.%)', min_value=0.0, value=0.5, step=0.1, key='s_sew_sludge')
    n_sewage_sludge = st.number_input('N (wt.%)', min_value=0.0, value=1.5, step=0.1, key='n_sew_sludge')
    ash_sewage_sludge = st.number_input('Ash (wt.%)', min_value=0.0, value=5.0, step=0.1, key='ash_sew_sludge')
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="st-ba">', unsafe_allow_html=True)
    st.markdown('**HTL conditions**')
    c_algae_biomass = st.number_input('C (wt.%)', min_value=0.0, value=50.0, step=0.1, key='c_alg_biomass')
    h_algae_biomass = st.number_input('H (wt.%)', min_value=0.0, value=6.0, step=0.1, key='h_alg_biomass')
    o_algae_biomass = st.number_input('O (wt.%)', min_value=0.0, value=44.0, step=0.1, key='o_alg_biomass')
    s_algae_biomass = st.number_input('S (wt.%)', min_value=0.0, value=0.0, step=0.1, key='s_alg_biomass')
    n_algae_biomass = st.number_input('N (wt.%)', min_value=0.0, value=1.0, step=0.1, key='n_alg_biomass')
    ash_algae_biomass = st.number_input('Ash (wt.%)', min_value=0.0, value=5.0, step=0.1, key='ash_alg_biomass')
    st.markdown('</div>', unsafe_allow_html=True)

# 收集所有输入数据
input_features = {
    'C_sewage_sludge': c_sewage_sludge,
    'H_sewage_sludge': h_sewage_sludge,
    'O_sewage_sludge': o_sewage_sludge,
    'S_sewage_sludge': s_sewage_sludge,
    'N_sewage_sludge': n_sewage_sludge,
    'Ash_sewage_sludge': ash_sewage_sludge,
    'C_algae_biomass': c_algae_biomass,
    'H_algae_biomass': h_algae_biomass,
    'O_algae_biomass': o_algae_biomass,
    'S_algae_biomass': s_algae_biomass,
    'N_algae_biomass': n_algae_biomass,
    'Ash_algae_biomass': ash_algae_biomass,
    'Temperature': temperature,
    'Solid_content': solid_content,
    'Residence_time': residence_time,
    'Mass_ratio_sewage_sludge': mass_ratio_sewage_sludge,
    'Mass_ratio_algae_biomass': mass_ratio_algae_biomass,
}
#%%
# 当用户点击预测按钮时执行
# 在每列之上显示标题
st.write('Prediction of bio-oil properties:')# 定义三列
col1, col2, col3, col4 = st.columns(4)

# 当用户点击预测按钮时执行
if st.button('Predict'):
    prediction = predict_properties(input_features)
    
    # 提取每个预测值并格式化
    CO2 = prediction[:, 0]  # 假设预测结果是一个二维数组
    CH4 = prediction[:, 1]
    CO = prediction[:, 2]
    H2 = prediction[:, 3]

    # 在三列中显示预测结果
    col1.write(f'CO2 (mol/kg): {CO2:.2f}')
    col2.write(f'CH4 (mol/kg): {CH4:.2f}')
    col3.write(f'CO (mol/kg): {CO:.2f}')
    col4.write(f'H2 (mol/kg): {H2:.2f}')
else:
    # 按钮未点击时也在三列中显示标签
    col1.write('CO2 (mol/kg) =')
    col2.write('CH4 (mol/kg) =')
    col3.write('CO (mol/kg) =')
    col4.write('H2 (mol/kg) =')


#%%
