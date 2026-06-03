from src.llm import call_llm
from src.output_parser import clean_markdown_output, is_markdown_note
from src.prompts import build_explain_prompt


def main():
    print("我的 AI 应用项目开始了")
    print("当前功能：输入一个知识点，让 AI 生成 Markdown 学习笔记。")

    topic = input("请输入要学习的主题：")

    prompt = build_explain_prompt(topic)

    print("\n正在调用大模型，请稍等...\n")

    raw_answer = call_llm(prompt)

    answer = clean_markdown_output(raw_answer)

    print("下面是 AI 生成的 Markdown 学习笔记：\n")
    print(answer)

    if is_markdown_note(answer):
        print("\n格式检查：通过，AI 输出符合 Markdown 学习笔记格式。")
    else:
        print("\n格式检查：未完全通过，后续可以继续优化 Prompt。")


if __name__ == "__main__":
    main()