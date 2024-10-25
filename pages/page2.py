import streamlit as st
#图片
container = st.container()
# container.image("img\c.png")
# 创建一个容器
container_1 = st.container()
container_2 = st.container()

# 在容器中使用columns布局，并调整宽度以实现居中
col1, col2 = container_1.columns([1, 1])

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
            width: 10vh; 
            height: 4vh; 
        }

</style>''', unsafe_allow_html=True)

# 指定音频文件的路径或URL
video = 'animal.mp4'

# 使用st.audio来嵌入音频
container.video(video, format="video/mp4", start_time=0, autoplay=True)
st.markdown('''
<style>
.st-emotion-cache-12h5x7g 
</style>

''',unsafe_allow_html=True)


# 在中间的列中放置按钮
with col1:
    denglu = st.button('登录')    #.st-emotion-cache-12h5x7g
with col2:
    zhuce = st.button('注册')    #.st-emotion-cache-12h5x7g
if denglu:
    st.switch_page('pages/page4.py')
if zhuce:
    st.switch_page('pages/page3.py')


