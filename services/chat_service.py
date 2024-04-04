# services/chat_service.py

# 假设的 init 函数和 GPT 模型接口
import init
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# 初始化模型等资源
init.init()

# 定义模板
template = """参考以下文档回答问题:
{document}

问题:
{question}
"""


def ask_question(document, question):
    # 创建 prompt
    prompt_text = template.format(document=document, question=question)

    # 配置模型和解析器
    model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    output_parser = StrOutputParser()

    # 构建处理链
    prompt = ChatPromptTemplate.from_template(prompt_text)
    chain = prompt | model | output_parser

    # 调用模型
    result = chain.invoke({"document": document, "question": question})

    # 返回结果
    return result

