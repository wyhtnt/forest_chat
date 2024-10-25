import streamlit as st
from zhipuai import ZhipuAI
import requests
import os

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
            font-size: 16px;
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
         /* 容器样式，用于居中按钮 */
        .st-emotion-cache-1qjhv5t {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 20vh; 
            height: 8vh; 
        }

</style>''', unsafe_allow_html=True)

def download_image(url, save_path):
    # 发送HTTP GET请求，获取图片内容
    response = requests.get(url)

    # 检查请求是否成功
    if response.status_code == 200:
        # 确保保存路径的目录存在
        os.makedirs(os.path.dirname(save_path), exist_ok=True)

        # 打开一个文件用于保存图片
        with open(save_path, 'wb') as f:
            f.write(response.content)
            print(f"图片已保存到 {save_path}")
    else:
        print(f"下载失败，状态码：{response.status_code}")


if "header" not in st.session_state:
    st.session_state.header=""
# 创建大模型出来
client = ZhipuAI(api_key="5e69c633b6ce05f532ab5f5cf17ad292.Ik54y5IbJDaMHy5a")

# print(response.data[0].url)

st.markdown("## 灵感涌现，字里行间绘出独特的印记")
st.markdown("### 描述你的专属宠物，开启聊天之旅吧。")
url = ""

if "button" not in st.session_state:
    st.session_state.button = True




problem = st.chat_input("请描述您想交谈的伙伴（如果不满意可再加具体细节，继续生成）")
if problem:
    with st.chat_message("user"):
        st.write(problem)
    # 在用户的描述中强制加入动物相关的提示词
    animal_prompt = "一只手绘风格的可爱小动物"
    prompt = f"{problem} {animal_prompt}"
    response = client.images.generations(
        model="cogview-3-plus",  # 填写需要调用的模型编码
        prompt=prompt,
    )

    # 输出找到
    with st.chat_message("assistant"):
        # if st.session_state.button :
        st.image(response.data[0].url,width=100)
        download_image(response.data[0].url,".\pages\photo\photo.jpg")
            # st.session_state.button = False
        url = response.data[0].url
        st.session_state.header = url


if st.button("确认"):
    # if not st.session_state.button :
    st.switch_page('pages/page6.py')




