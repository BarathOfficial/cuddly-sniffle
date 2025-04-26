from openai import OpenAI


client = OpenAI(base_url="https://openrouter.ai/api/v1",
                api_key="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")

def Get_query(content):
    completion = client.chat.completions.create(
        extra_body={},
        model="deepseek/deepseek-r1-zero:free",
        messages=[
            {
            "role": "user",
            "content": content
            }
        ]
    )
    return completion



