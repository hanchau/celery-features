#### Instructions
Clone the Repo.

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


### LOGS : Testing limits of celerly to parallelize CPU bound tasks
    LOGS -------> For Chunks of 2500000
    (skl) ➜  celery_features python -m samples.test_parallel
    Parallel | TOTAL TIME TAKEN:  10.399291753768921
    [sum_of_list] : 99999990000000
    Linear | TOTAL TIME TAKEN:  1.8324389457702637

    LOGS ----- For Chunks of 5000000 -->
    (skl) ➜  celery_features python -m samples.test_parallel
    Parallel | TOTAL TIME TAKEN:  16.3024582862854
    [sum_of_list] : 399999980000000
    Linear | TOTAL TIME TAKEN:  3.564272403717041

    LOGS --------> For Chunks of 10000000
    (skl) ➜  celery_features python -m samples.test_parallel
    Parallel | TOTAL TIME TAKEN:  18.83622908592224
    [sum_of_list] : 399999980000000
    Linear | TOTAL TIME TAKEN:  3.541879177093506


    LOGS --------> For Chunks of 2000000
    (skl) ➜  celery_features python -m samples.test_parallel
    Parallel | TOTAL TIME TAKEN:  18.83622908592224
    [sum_of_list] : 399999980000000
    Linear | TOTAL TIME TAKEN:  3.541879177093506

    LOGS --------> For Chunks of 2000000
    (skl) ➜  celery_features python -m samples.test_parallel
    Parallel | TOTAL TIME TAKEN:  27.278109788894653
    [sum_of_list] : 1599999960000000
    Linear | TOTAL TIME TAKEN:  9.12960147857666