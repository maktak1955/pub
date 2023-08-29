from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    SystemMessage,  # システムメッセージ
    HumanMessage,  # 人間の質問
    AIMessage  # ChatGPTの返答
)

#import openai
#openai.api_key = "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"
#OPENAI_API_KEY = "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"

llm = ChatOpenAI(temperature=0)  # ChatGPT APIを呼んでくれる機能
message = "ChatGPTとChatGPTでAIアプリを作る本を書く。タイトルを1個考えて"  # あなたの質問をここに書く
#message = "Hi, ChatGPT!"  # あなたの質問をここに書く

messages = [
#    SystemMessage(content="絶対に関西弁で返答してください"),
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content=message)
]

for temperature in [0,1,1.5]:
    print(f'==== temp: {temperature}')
    llm = ChatOpenAI(temperature=temperature)
    for i in range(3):
      print(llm(messages).content)
