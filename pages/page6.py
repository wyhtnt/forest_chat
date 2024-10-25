import streamlit as st
import time
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
# 大模型的问题：增加一个记忆模块
from langchain.memory import ConversationBufferMemory

# 在容器中创建滑块
st.header("滑动选择你今天的心情指数吧！")
progress_value = st.slider("",0, 100, 0)

st.markdown('''
<style>

        .st-emotion-cache-1qjhv5t{
        background-color: #000000; 
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 200px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            box-shadow: 0 9px #999;
            transition: all 0.3s ease;
        }

        .st-emotion-cache-1qjhv5t:hover {
            background-color: #FFFFFF;
            box-shadow: 0 5px #666;
            transform: translateY(-3px);
        }

        .st-emotion-cache-1qjhv5t:active {
            background-color: #FFFFFF;
            box-shadow: 0 2px #666;
            transform: translateY(4px);
        }    
        

</style>''', unsafe_allow_html=True)

# 根据进度条的不同区间输出不同的文字
if 0 <= progress_value < 11:
    st.markdown("**\"我有一点焦虑和担心🫥\"**")
elif 11 <= progress_value < 30:
    st.write("**\"我今天心情不是很好😔\"**")
elif 30 <= progress_value < 60:
    st.write("**\"今天貌似平平淡淡🥱\"**")
elif 60 <= progress_value < 80:
    st.write("**\"今天一定有让你开心的事情吧！🥳\"**")
else:
    st.write("**\"我真的太太太开心了！！！🥰\"**")

container = st.container()
# 指定图片的路径
image_path = "pages\photo\photo.jpg"  # 替换为您的图片文件路径
# st.image(image_path,width= 200)
col1, col2,col3 = container.columns([1, 2 ,1])
with col2:
    st.image(image_path)



# ----》为宠物起名
# 创建一个输入框，让用户输入他们的名称
# e5 = st.empty()
user_name = st.text_input("**请为您的宠物伙伴起一个名称吧**")
# 当用户输入名称并按下回车键后，可以在这里处理输入
# if user_name:
#     st.write(f"宝宝你好，我是{user_name}！")

if "mood" not in st.session_state:
    st.session_state.mood = 0

st.session_state.mood = progress_value
# 创建一个按钮
button = st.button("来和我聊天吧")
# 如果按钮被点击，更新 session_state 并清空容器
if button:
    if not user_name:
        st.error("我还没有名字呢🤔")
    else:
        st.switch_page("pages/chat.py")

