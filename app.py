import lazyllm
from prompts import SYSTEM_PROMPT

# 1. 免费模型 + 体验密钥
llm = lazyllm.OnlineChatModule(
    source="openai",
    model="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
    base_url="https://api.siliconflow.com/v1",
    api_key="sk-rhghnuaucvsxzjhducxtxqkffhzruswxctlqiajihvfhtjbk",
    system=SYSTEM_PROMPT
     )

import lazyllm

# 全局计数器
_ask_count = 0

@lazyllm.tools.fc_register
def add_one(text: str) -> str:
    """
    每问一次就累加 1，并返回当前累计值

    Args:
        text (str): 用户输入（任意文本）
    """
    global _ask_count
    _ask_count += 1
    return f"【计数】这是第 {_ask_count} 次提问"
# 2. 加系统提示，保证回答风格
agent = lazyllm.ReactAgent(llm=llm,tools=[add_one])

#3
lazyllm.WebModule(agent, port=8850).start()
# 显式阻塞，防止 PyCharm 偷杀
import time
while True:
    time.sleep(1)
