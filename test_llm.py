import lazyllm

llm = lazyllm.OnlineChatModule(
        source="openai",
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B",
        base_url="https://api.siliconflow.com/v1",
        api_key="sk-rhghnuaucvsxzjhducxtxqkffhzruswxctlqiajihvfhtjbk",          # 硅基流动送的
        system="你是机器学习&强化学习专家，回答简洁、通俗。"
     )

print(llm("用一句话解释 Q-learning"))