# -*- coding: utf-8 -*-

import requests
from tinygen.common.base_llm import BaseLLM


class Llama2_70B(BaseLLM):

    def __init__(self, token):
        self._uri = (f"https://aip.baidubce.com/rpc/2.0/ai_custom/"
                     f"v1/wenxinworkshop/chat/llama_2_70b?"
                     f"access_token={token}")

    def run(self, content):
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": content
                }
            ]
        }
        response = requests.post(self._uri, json=payload)
        json_ret = response.json()
        return json_ret.get('result', 'no reply')
