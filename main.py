from src.llm import call_llm
from src.prompts import build_explain_prompt


def main():
    print("我的 AI 应用项目开始了")
    print("当前功能：输入一个知识点，让 AI 按固定格式讲解。")

    topic = input("请输入要学习的主题：")

    prompt = build_explain_prompt(topic)

    print("\n正在调用大模型，请稍等...\n")

    answer = call_llm(prompt)

    print("下面是 AI 的回答：\n")
    print(answer)


if __name__ == "__main__":
    main()