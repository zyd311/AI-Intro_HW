# Chatbot: DeepSeek API 对话示例
# 运行前请安装依赖: pip install openai
import os
from openai import OpenAI

def init_deepseek_client():
    """初始化 DeepSeek 客户端"""
    # 方式1：从环境变量读取 (推荐)
    api_key = os.getenv("DEEPSEEK_API_KEY", "请替换为你的API Key")
    # 方式2：直接写在这里 (不推荐，不安全)
    # api_key = "sk-..."
    
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )
    return client

def chat_with_deepseek(user_prompt):
    """与 DeepSeek 进行对话"""
    client = init_deepseek_client()
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.7 # 创意程度 0-1
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ 对话失败: {str(e)} \n请检查 API Key 是否正确。"

if __name__ == "__main__":
    print("=== DeepSeek Chatbot (输入 'quit' 退出) ===")
    while True:
        user_input = input("\n你: ")
        if user_input.lower() in ["quit", "退出", "q"]:
            print("Chatbot: 👋 再见！")
            break
        reply = chat_with_deepseek(user_input)
        print(f"Chatbot: {reply}")
