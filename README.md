# sys.setprofile and coverage

This is a minimal example of coverage not reporting the lines run in a `sys.setprofile` callback.

To replicate:
* Create a virtualenv
* `pip install -r requirements.txt
* `coverage run -m unittest`
* `coverage report -m`

```
(profiling-sandbox) ian@ian:~/dev/profiling-sandbox$ coverage run -m unittest
<frame at 0x7f232427fd40, file '/home/ian/dev/profiling-sandbox/tests.py', line 6, code add>
<frame at 0x7f232427fd40, file '/home/ian/dev/profiling-sandbox/tests.py', line 7, code add>
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
(profiling-sandbox) ian@ian:~/dev/profiling-sandbox$ coverage report -m
Name          Stmts   Miss  Cover   Missing
-------------------------------------------
profiler.py       6      2    67%   6-7
tests.py          9      0   100%
-------------------------------------------
TOTAL            15      2    87%
```
