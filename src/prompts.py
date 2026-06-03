from langchain_core.prompts import ChatPromptTemplate


explain_prompt_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
你是一名非常耐心的 AI 应用开发入门老师。
你的任务是用适合小白理解的方式解释技术概念。

回答要求：
1. 语言通俗，不要堆专业术语。
2. 如果必须出现专业术语，要顺手解释。
3. 回答要和“课程资料智能问答助手”这个项目联系起来。
4. 输出格式必须清晰，适合整理成学习笔记。
""",
        ),
        (
            "human",
            """
请你讲解下面这个知识点：

知识点：{topic}

请严格按照下面格式回答：

一、它是什么
用通俗语言解释这个概念。

二、为什么要学它
说明它在 AI 应用开发项目里的作用。

三、简单例子
给出一个容易理解的小例子。

四、常见错误
列出初学者容易犯的错误。

五、项目中的用法
说明它将来会怎么用在“课程资料智能问答助手”项目里。
""",
        ),
    ]
)


def build_explain_prompt(topic):
    """
    根据用户输入的知识点，生成 LangChain PromptValue。
    """
    prompt = explain_prompt_template.invoke(
        {
            "topic": topic
        }
    )
    return prompt