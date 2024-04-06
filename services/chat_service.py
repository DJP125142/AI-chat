# 1. 读取知识库文档
txt = ""
with open("data/qxy-1.txt", encoding="utf-8") as f:
    for line in f:
        txt += line.strip()

# 2. 构建chain --- 用户输入 + 文档 = 完整的promt -> gpt -> 结果
from services.init import init
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

init()
template = """参考以下文档回答问题:
{document}

问题:
{question}
"""


def ask_question(question):
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

