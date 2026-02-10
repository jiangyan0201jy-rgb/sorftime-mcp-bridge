import os
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 从环境变量获取 API Key，如果没有设置则使用你提供的默认值
SORFTIME_KEY = os.environ.get('SORFTIME_API_KEY', 'sk4rzxnrru5xvjfoalmzdtzxne1wut09')

@app.route('/')
def home():
    return "Sorftime MCP Bridge is Running!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    asin = data.get('asin')
    
    if not asin:
        return jsonify({"error": "Missing ASIN"}), 400

    # 这里封装调用 Sorftime API 的逻辑
    # 注意：这里的 URL 是示例，请根据 Sorftime 实际 API 文档修改路径
    sorftime_url = f"https://api.sorftime.com/v1/asin/{asin}" 
    headers = {"Authorization": f"Bearer {SORFTIME_KEY}"}
    
    try:
        # 实际开发时请根据 Sorftime 接口文档调整请求方式
        # response = requests.get(sorftime_url, headers=headers)
        # result = response.json()
        
        # 模拟返回给 n8n 的结果
        result = {"status": "success", "asin": asin, "message": "Data fetched using Sorftime Key"}
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
