import streamlit as st
import pandas as pd

# 页面配置
st.set_page_config(
    page_title="学生练习数据查询",
    page_icon="📊",
    layout="centered"
)

# 标题
st.title("📊 学生练习数据查询系统")
st.markdown("---")

# 加载数据
@st.cache_data
def load_data():
    df = pd.read_excel("data.xlsx")
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"数据加载失败: {e}")
    st.stop()

# 搜索框
st.markdown("### 🔍 请输入查询信息")
search_input = st.text_input(
    "输入手机号或学号", 
    placeholder="例如：13912345678",
    label_visibility="collapsed"
)

if st.button("查询", type="primary"):
    if not search_input.strip():
        st.warning("请输入手机号或学号")
    else:
        search_input = search_input.strip()
        
        # 尝试匹配手机号
        try:
            phone = int(search_input)
            result = df[df['手机号'] == phone]
        except:
            # 匹配学号
            result = df[df['用户ID'].str.contains(search_input, case=False, na=False)]
        
        if len(result) == 0:
            st.error("未找到相关信息，请检查输入")
        else:
            row = result.iloc[0]
            
            st.success("✅ 查询成功！")
            st.markdown("---")
            
            # 基本信息
            col1, col2 = st.columns(2)
            with col1:
                st.metric("姓名", str(row['用户昵称']))
                st.metric("班级", str(row['用户标签']))
            with col2:
                st.metric("练习次数", f"{int(row['练习次数'])}次")
                st.metric("练习时长", str(row['练习时长']))
            
            st.markdown("---")
            
            # 成绩信息
            st.markdown("### 📈 成绩信息")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("最高分", f"{int(row['最高分数'])}分")
            with col2:
                st.metric("平均分", f"{int(row['平均分数'])}分")
            with col3:
                st.metric("最低分", f"{int(row['最低分数'])}分")
