#安装环境包pip install zhipuai
'''APIKey：'''
'''三种API调用方式
同步调用：zhipuai.model_api.invoke()调用后即可一次性获得最终结果
异步调用：zhipuai.model_api.async_invoke()调用后会立即返回一个任务 ID ，然后用任务ID查询调用结果（根据模型和参数的不同，通常需要等待10-30秒才能得到最终结果
SSE调用：zhipuai.model_api.sse_invoke()调用后可以流式的实时获取到结果直到结束
'''
import zhipuai
zhipuai.api_key = "5abc1fc2f19d7f09f4aa7c5394c528c7.v8MCrNVNWfYusjBs"

def chat():
    response = {'code': 200, 'msg': '操作成功',
                'data': {'request_id': '7768921906578633313',
                         'task_id': '7768921906578633313',
                         'task_status': 'SUCCESS',
                         'choices': [{'role': 'assistant', 'content': '"你好👋!我是人工智能助手 ChatGLM-6B,很高兴见到你,欢迎问我任何问题。"'}], 'usage': {'total_tokens': 27}},
                'success': True}


    #zhipuai.model_api.invoke(
    #    model="chatglm_lite",
    #    prompt=[{"role":"user","content":"你好"}],
    #    top_p = 0.7,
    #    temperature = 0.9,
    #)
    return response

#Question = input("输入：")
print(chat()["data"]["choices"][0]["content"])
