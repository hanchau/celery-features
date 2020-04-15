from app.etl_app import etl_app

@etl_app.task
def add(x,y):
    ret = x+y
    print("[add] : {}".format(ret))
    return ret


@etl_app.task
def sub(x,y):
    ret = x-y
    print("[sub] : {}".format(ret))
    return ret


@etl_app.task
def mul(x,y):
    ret = x*y
    print("[mul] : {}".format(ret))
    return ret


@etl_app.task
def div(x,y):
    ret = x/y
    print("[div] : {}".format(ret))
    return ret


@etl_app.task
def sum_list(list_):
    ret = sum(list_)
    print("[sum_of_list] : {}".format(ret))
    return ret
