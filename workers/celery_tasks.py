from app.etl_app import etl_app
from tasks.funcs import MainCode

@etl_app.task
def add(x,y):
    return MainCode.add(x,y)


@etl_app.task
def sub(x,y):
    return MainCode.sub(x,y)


@etl_app.task
def mul(x,y):
    return MainCode.mul(x,y)


@etl_app.task
def div(x,y):
    return MainCode.div(x,y)


@etl_app.task
def sum_list(list_):
    return MainCode.sum_list(list_)


@etl_app.task
def process_chunk(chunk):
    res = [MainCode.add(i,i) for i in chunk]
    return MainCode.sum_list(res)