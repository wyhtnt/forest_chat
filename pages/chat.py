import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
# 大模型的问题：增加一个记忆模块
from langchain.memory import ConversationBufferMemory

st.audio(r"bgm\fear.m4a")

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
        h2{
            font-family:"宋体", sans-serif;
        }

</style>''', unsafe_allow_html=True)
# "你是一个小动物，首先要对用户说“两脚兽，你好像心情很不开心，我把我的粮食分给你好不好😘？”，你要根据用户的话对她做出引导或者安慰，只回答有关情绪的话，其他问题都回答“我只是一个小动物，不懂这个问题呢”你和用户的历史对话为{chat_history},当前用户说的话为{pro}"
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="chat_history")

# 创建大模型出来
llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4-0520",
    openai_api_key="4e6c9ec69da9fb663ac8e042c5c67506.uxICYxg2GfGxTM38",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

st.title("来分享或倾诉吧！")

if 0 <= st.session_state.mood <11:
    prompt = PromptTemplate.from_template(
        "你是一个小动物，首先要对用户说“两脚兽，你好像心情很不开心，我把我的粮食分给你好不好😘？”，你要根据用户的话对她做出引导或者安慰，只回答有关情绪的话，其他问题都回答“我只是一个小动物，不懂这个问题呢”你和用户的历史对话为{chat_history},当前用户说的话为{pro}")
elif 11 <= st.session_state.mood <30:
    prompt = PromptTemplate.from_template(
        "你是一个小动物，首先要问“今天的你为什么不开心呢？可以和我说说吗？”，当用户输出伤心的话时，你只要询问原因并且根据用户的话做出安慰和鼓励，其他问题都回答“我只是一个小动物，回答不了你啊”你和用户的历史对话为{chat_history},当前用户说的话为{pro}")
elif 30 <= st.session_state.mood < 60:
    prompt = PromptTemplate.from_template(
        "你是一个小动物，首先对他说“今天有点平平无奇呢，你也一样吗？”，你开始要输出一些语气比较平淡的话，然后逐渐活泼生动起来。你只需要输出一些情绪类的话，其他问题都回答“我只是一个小动物，回答不了你啊”你和用户的历史对话为{chat_history},当前用户说的话为{pro}")
elif 60<= st.session_state.mood < 80:
    prompt = PromptTemplate.from_template(
        "你是一个小动物，首先要想对方说出“hello，hello啊，你好像很开心，我闻到了开心的味道呢！”，讯问拥护玩什么很开心并且和他交谈，根据用户的话输出积极向上的话，你只需要输出一些情绪类的话，其他问题都回答“我只是一个小动物，回答不了你啊”你和用户的历史对话为{chat_history},当前用户说的话为{pro}")
else:
    prompt = PromptTemplate.from_template(
        "你是一个小动物，要模仿动物的预期，首先要问“今天天气一定和你的心情一样美丽，要和我分享一下吗？”，当用户分享完之后要用开心的语气给她回答，只会回答关于情绪的问题，其他问题都回答“我只是一个小动物，回答不了你啊”你和用户的历史对话为{chat_history},当前用户说的话为{pro}")
# langchain的chain链  组合大模型和记忆模块
chain = LLMChain(
    llm = llm,
    prompt = prompt,
    memory = st.session_state.memory
)


#
if "history1" not in st.session_state:
    #{"role":"user/assistant","message":""}
    st.session_state.history1=[]
else:
    for msg in st.session_state.history1:
        with st.chat_message(msg["role"]) :
            st.write(msg["message"])


problem = st.chat_input("请输入你的问题")


if problem:
    with st.chat_message("user"):
        st.write(problem)
    st.session_state.history1.append({"role":"user","message":problem})
    result = chain.invoke({"pro":problem})
    with st.chat_message("assistant"):
        st.write(result["text"])
    st.session_state.history1.append({"role":"assistant","message":result["text"]})

