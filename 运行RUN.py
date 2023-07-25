'''运行文件。不用修改运行路径，RUN.py必须要在项目文件夹内'''
'''如果是运行在终端的话，直接保存，浏览器就可以同步修改，不用再运行这个文件'''
'''注意！有时候直接运行终端会无效，只有运行此文件，终端才能真正发生更改'''
import os
PATH = os.path.split(os.path.realpath(__file__))[0]#获取RUN.py的路径
os.system('cd ' + PATH)#进入路径
os.system('uvicorn main:app --reload')#运行FastAPI


'''
uvicorn main:app 命令含义如下:

main：main.py 文件（一个 Python "模块"）。
app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
--reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
'''