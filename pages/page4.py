import streamlit as st
import mysql.connector
from mysql.connector import Error


st.title("登录界面")
# 数据库配置参数
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'user'
}
# 创建数据库连接的函数
def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            print('连接成功')
    except Error as e:
        print(f"连接错误: {e}")
    return conn

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
# 验证用户登录信息的函数
def verify_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM user WHERE username = %s AND passworld = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    print(user)
    cursor.close()
    conn.close()
    return user

with ((st.form(key='login_form'))):
    username = st.text_input('用户名：')
    password = st.text_input('密码：', type='password')
    #password2 = st.text_input('密码：', type='password2')
    if st.form_submit_button('登录'):
        if not username:
            st.error("用户名不能为空！")
        if not password:
            st.error("密码不能为空！")
        # 这里可以添加注册逻辑，例如保存用户信息到数据库
        #password1 = password2
        if username and password:
            user = verify_user(username,password)
            if user:
                st.success("登录成功！")
                st.switch_page('pages/page5.py')
            else:
                st.error("用户名或密码错误！")

