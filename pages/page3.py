import streamlit as st
import mysql.connector
from mysql.connector import Error
st.title("注册界面")


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
        .st-emotion-cache-jkfxgf {
            ont-family:"宋体", sans-serif;
          }
        

</style>''', unsafe_allow_html=True)


# 配置数据库连接参数
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'root',
    'database': 'user'
}
# 连接数据库
def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        print("连接成功")
    except Error as e:
        print(f"连接错误: {e}")
    return conn





# 注册新用户
def register_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        # 这里假设你有一个 users 表，其中包含 username 和 password 字段
        cursor.execute("INSERT INTO user (username, passworld) VALUES (%s, %s)", (username, password))
        conn.commit()
        return True
    except Error as e:
        print(f"注册用户时出错: {e}")
        return False
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

with st.form(key='registration_form'):
    username = st.text_input('用户名：')
    password = st.text_input('密码：', type='password')
    repassword = st.text_input("确认密码：",type = 'password')
    #password2 = st.text_input('密码：', type='password2')
    if st.form_submit_button('注册'):
        if  not username :
            st.error("用户名不能为空！")
        if  not password:
            st.error("密码不能为空！")
        if password != repassword:
            st.error("两次密码不一致！")
        # 这里可以添加注册逻辑，例如保存用户信息到数据库
        #password1 = password2
        if username and password and password == repassword:
            register_user(username,password)
            st.write('注册成功！')
        # 重新运行应用程序以显示登录界面
            st.switch_page("pages/page4.py")