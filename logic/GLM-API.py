#安装环境包pip install zhipuai
'''APIKey：03b60d7b276a44f7a33619aa57fe60f9'''
'''三种API调用方式
同步调用：zhipuai.model_api.invoke()调用后即可一次性获得最终结果
异步调用：zhipuai.model_api.async_invoke()调用后会立即返回一个任务 ID ，然后用任务ID查询调用结果（根据模型和参数的不同，通常需要等待10-30秒才能得到最终结果
SSE调用：zhipuai.model_api.sse_invoke()调用后可以流式的实时获取到结果直到结束
'''
import zhipuai
zhipuai.api_key = "03b60d7b276a44f7a33619aa57fe60f9"

def chat():
    response = zhipuai.model_api.invoke(
        model="chatglm_lite",
        prompt=[{"role":"user","content":"你好"}],
        #top_p = 0.7,
        #temperature = 0.9,
    )
    print(response)

#Question = input("输入：")
chat()