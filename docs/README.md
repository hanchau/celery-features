#### Instructions
Start the workers.
> terminal 1
```
$ celery -A app.etl_app worker --loglevel=INFO -n gen_worker@instance1 --concurrency=1
```
> terminal 2
```
$ celery -A app.etl_app worker --loglevel=INFO -n gen_worker@instance2 --concurrency=1
```

Start the main process.
> terminal 3
 ```
 python -m samples.<file_name.py>
 ```


#### Please refer to these links

-   [Canvas: Designing Work-flows](https://docs.celeryproject.org/en/stable/userguide/canvas.html)
-   [Workers Guide](https://docs.celeryproject.org/en/stable/userguide/workers.html)
-   [Daemonization](https://docs.celeryproject.org/en/stable/userguide/daemonizing.html)
-   [Periodic Tasks](https://docs.celeryproject.org/en/stable/userguide/periodic-tasks.html)
-   [Routing Tasks](https://docs.celeryproject.org/en/stable/userguide/routing.html)
