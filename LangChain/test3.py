from langchain.chat_models import init_chat_model

# LangChain 封装了更上层的方法，让我们初始化模型
# fGPT_model = init_chat_model(model="gpt-4o-mini", model_provider="openai", temperature=0.3)
# print(f"GPT-4o-mini:{fGPT_model.invoke('你是谁？').content}")

deepseek_model = init_chat_model(model="deepseek-chat", model_provider="deepseek", temperature=0.3)
# deepseek_model = init_chat_model(model="deepseek-chat", temperature=0.3)

print(f"deepseek-chat:{deepseek_model.invoke('你是谁？').content}")