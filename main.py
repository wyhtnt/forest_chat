import streamlit as st
st.subheader("温馨森林语")

st.markdown('''
<style>
        /*标题居中*/
        .st-emotion-cache-pgf13w {
            text-align: center;
            margin: 0 auto;
            width: 50%;
        }
          
        .st-emotion-cache-12h5x7g {
            font-family:"宋体", sans-serif;
          }
        
        /*图片居中*/
        img {
            text-align: center;
            margin: 0 auto;
            width: 50%;
        } 
        /*文字字体*/
        h3{
            font-family : "宋体", sans-serif;
        }
        
        .st-emotion-cache-1rsyhoq p{
            font-family: "宋体", sans-serif;
        }
        
        
        /*按钮*/
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
            width: 15vh; 
            height: 5vh; 
        }
     
</style>''',unsafe_allow_html=True)



container1 = st.container(border=True)
# 快来与小动物AI互动吧，让它们成为您生活中不可或缺的一部分！无论您是孤独的旅人，还是忙碌的都市人，这些小动物AI都将带给您无尽的温暖和陪伴。
container1.markdown(
            "欢迎来到智能小动物的神奇世界！它们不仅是您忠实的伙伴，更是您心灵的倾听者和智慧的引导者。它们将用它们独特的智慧和幽默，与您分享生活的点点滴滴，让您在忙碌的生活中找到一丝慰藉。:balloon:")
st.balloons()
container1.image("all.jpg",width=200,use_column_width=False)
# st.markdown('''
#
# .st-emotion-cache-1fulpqd{
# <style>
# left:50%
# </style>
# }
#
# ''',unsafe_allow_html=True)
if st.button('进入'):
    st.switch_page('pages/page2.py')







