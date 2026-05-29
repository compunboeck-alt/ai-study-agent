from src.prompts import build_explain_prompt
def main():
    print("我的AI应用项目开始了")

    topic=input("请输入要学习的主题：")

    prompt=build_explain_prompt(topic)

    print("\n下面是生成的prompt:")

    print(prompt)

if __name__ == "__main__":
    main()