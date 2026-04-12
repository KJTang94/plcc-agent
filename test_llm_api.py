import json
from openai import OpenAI

API_KEY = "sk-Nss5uw1SgcmqBu2iKmvSfSWr4znjvhvxmb4vJRImjWCb3EBz"

def test_llm_api():
    print("=== 测试LLM API连接 ===")
    print()
    
    try:
        client = OpenAI(
            api_key=API_KEY,
            base_url="https://yunwu.ai/v1"
        )
        
        print("正在调用LLM API...")
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": "你好，测试一下API是否正常工作。请回复'API测试成功'"}
            ],
            temperature=0
        )
        
        result = response.choices[0].message.content.strip()
        print("API响应: " + result)
        
        if "API测试成功" in result:
            print("[OK] LLM API调用成功！")
        else:
            print("[OK] LLM API调用成功，但响应内容不同")
            print("响应内容: " + result)
            
    except Exception as e:
        print("[FAIL] LLM API调用失败: " + str(e))
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_llm_api()