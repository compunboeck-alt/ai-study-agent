def clean_markdown_output(text):
    """
    清理大模型输出的 Markdown 文本。

    主要作用：
    1. 去掉前后空白
    2. 去掉模型可能包裹的 ```markdown 代码块标记
    3. 返回清理后的 Markdown 文本
    """
    text = text.strip()

    if text.startswith("```markdown"):
        text = text.removeprefix("```markdown").strip()

    if text.startswith("```"):
        text = text.removeprefix("```").strip()

    if text.endswith("```"):
        text = text.removesuffix("```").strip()

    return text


def is_markdown_note(text):
    """
    简单检查模型输出是否符合 Markdown 学习笔记格式。
    """
    required_parts = [
        "#",
        "## 1. 它是什么",
        "## 2. 为什么要学它",
        "## 3. 简单例子",
        "## 4. 常见错误",
        "## 5. 在项目中的用法",
        "## 6. 今日小结",
    ]

    for part in required_parts:
        if part not in text:
            return False

    return True