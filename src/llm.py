from langchain_openai import ChatOpenAI

from src.config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    MODEL_NAME,
    check_config,
)


def get_llm():
    """
    创建并返回一个大模型对象。
    这里使用 LangChain 的 ChatOpenAI 类调用 DeepSeek。
    """
    check_config()

    llm = ChatOpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url=DEEPSEEK_BASE_URL,
        model=MODEL_NAME,
        temperature=0.3,
    )

    return llm


def call_llm(prompt):
    """
    输入 prompt,调用大模型,返回回答文本。
    """
    llm = get_llm()

    response = llm.invoke(prompt)

    return response.content