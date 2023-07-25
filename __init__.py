'''这里存放的是一些全局变量，比如templates'''
from fastapi import FastAPI
from starlette.templating import Jinja2Templates

app = FastAPI()#对于下级精准调用上级的想法：即便对于此函数没有继承关系，但调用仍然会无法运行。#main里必须要有app，不能从别处继承
templates = Jinja2Templates(directory="./templates")#这个是使用模板必须的，否则就只能写html'''<html代码>'''
