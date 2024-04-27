from services.init import init
import urllib.request
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

init()
def ask_question(question,type,filename):
    if type == 1:
        # 问题模版为空，直接处理问题
        template = ""
    elif type == 2:
        # 问题模版
        template = """参考以下文档回答问题:
            {document}

            问题:
            {question}
            """
        # 获取知识库文档
        txt = ""
        # 判断是否为网络资源
        if "http" in filename:
            # 从网络读取
            with urllib.request.urlopen(filename) as f:
                for line in f:
                    txt += line.decode("utf-8").strip()
        else:
            # 从本地文件读取
            with open("data/" + filename, encoding="utf-8") as f:
                for line in f:
                    txt += line.strip()

    # 创建 prompt
    prompt = ChatPromptTemplate.from_template(template)
    # 配置模型和解析器
    model = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
    output_parser = StrOutputParser()
    # 构建处理链
    chain = prompt | model | output_parser
    # 使用处理链处理问题
    result = chain.invoke({"document": txt, "question": question})
    # 返回结果
    return result

