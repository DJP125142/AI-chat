from dotenv import load_dotenv
import os

# 加载.env文件
load_dotenv()

def init():
    # 在环境变量中配置openai的key和代理地址
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    os.environ["OPENAI_API_BASE"] = os.getenv("OPENAI_API_BASE")
