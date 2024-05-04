# CRUD API Benchmarks (Python vs. Golang)
***

I've just created a simple CRUD API with golang and python,
so i can make some tests to show the performance for each language.

## Tools that i have been used

most of the time, we will use some frameworks to make our life easier,
so to make these tests more realistic, i used some popular frameworks to build my API

1. Python Frameworks and Tools:
    * [Django Framework](https://www.djangoproject.com/)
    * [Django Rest Framework(DRF)](https://www.django-rest-framework.org/)

2. Golang Frameworks and Tools:
    * [GORM (Golang Object Relational Model)](https://gorm.io/)
    * [Gin (HTTP Framework)](https://gin-gonic.com/)

## Final Results

This is the final result after using http client like `Thunder Client`,
and after running `test_api.py` that generates a number of objects and test the performance

**The device that i've used to make tests:**
    _CPU_ : intel core i7-4700MQ
    _RAM_ : 8 GB

Note: if you see something wrong please tell me, at the end of the day, i am not an expert.

### Golang  (1.21.1V linux/amd64)
---------------------------------------

For only one operation:

|   Operation   |   Time    |
|---------------|-----------|
|   `CREATE`    |    8ms    |
|   `READ`      |    7ms    |
|   `UPDATE`    |    12ms   |
|   `DELETE`    |    9ms    |
|   `LIST`      |    3ms    |

For one thousand operation:

|   Operation   |   Time    |
|---------------|-----------|
|   `CREATE`    |   3.165s  |
|   `READ`      |   1.6s    |
|   `UPDATE`    |  3.336s   |
|   `DELETE`    |   3.305s  |
|   `LIST`      |   7.8ms   |

### Python (3.9.2V)

---------------------------------------

For only one operation:

|   Operation   |   Time    |
|---------------|-----------|
|   `CREATE`    |    16ms   |
|---------------|-----------|
|   `READ`      |    10ms   |
|---------------|-----------|
|   `UPDATE`    |    13ms   |
|---------------|-----------|
|   `DELETE`    |    11ms   |
|---------------|-----------|
|   `LIST`      |    12ms   |

For one thousand operation:

|   Operation   |   Time    |
|---------------|-----------|
|   `CREATE`    |   7.401s  |
|---------------|-----------|
|   `READ`      |   6.154s  |
|---------------|-----------|
|   `UPDATE`    |  7.072s   |
|---------------|-----------|
|   `DELETE`    |   7.652s  |
|---------------|-----------|
|   `LIST`      |   21.1ms  |
