# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
from .config import *
import openai


class ChatGPT:

    # @param api_key ChatGPT 的 API Key
    def __init__(self, api_key=CHATGPT_API_KEY) -> None:
        openai.api_key = api_key
        self.messages = CHATGPT_INIT_MESSAGES

    def send(self, text, messages=None) -> str:
        """
        向ChatGPT发送消息
        :param text: 要发送的信息
        :param messages: 要发送的信息列表（上下文）
        :return: GPT响应的消息
        """
        # 如果没有自定义的messages, 则使用默认的messages
        if not messages:
            messages = self.messages

        # 确保发送给ChatGPT的消息不超过10条
        # 但是要保留开头的角色定义
        if len(messages) > 9:
            messages = messages[0:1] + messages[-8:]

        # 生成新的消息
        message = {"role": "user", "content": text}
        messages.append(message)
        self.messages.append(message)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )

        # 将回应的消息添加到消息队列
        message = response['choices'][0]['message']
        self.messages.append(message)

        return message
