
from app.etl_app import etl_app

# task callback
@etl_app.task()
def type_error(x):
    print("[ERROR: Wrong Types] :",x)


# non task callback
# def type_error():
    # print("[ERROR: Wrong Types] :")


@etl_app.task
def on_chord_error(request, exc, traceback):
    # print('Task {0!r} raised error: {1!r}'.format(request.id, exc))
    print('HEY WE JUST ENTERED IN A CALLBACK')
