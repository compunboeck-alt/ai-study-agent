import os   #用来读取系统环境变量
from dotenv import load_dotenv #读取.env文件


load_dotenv()


PROJECT_NAME = "课程资料智能问答助手"
VERSION = "0.1.0"

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
MODEL_NAME = os.getenv("MODEL_NAME", "deepseek-chat")


def check_config():
    """
    检查必要配置是否存在。
    如果没有配置 API Key,就主动报错,方便我们定位问题。
    """
    if not DEEPSEEK_API_KEY:
        raise ValueError(
            "没有找到 DEEPSEEK_API_KEY,请检查 .env 文件是否存在，并且是否填写了 API Key。"
        )