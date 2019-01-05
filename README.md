[Talk at pybits](https://youtu.be/rzpP05WJilo)

# Setup
1. Install pipenv
`pip install pipenv`
2. Install python dependencies
`pipenv install`

# Running
## notebook
`pipenv run jupyter notebook python_concurrency.ipynb`
## webserver (required for http client examples)
`pipenv run python scripts/server.py`

# Notes

### The free lunch is over
- we've gone from khz to ghz in 20 years
- but we can't fit more transistors onto ICs anymore.

- Adding resources to a system is called vertical scaling
  If we can't vertically scale up, how do we achieve more throughput ?

- we do it by adding 'more' of that resource, instead of using more powerful
  resource

- This is called scaling horizontally

- some languages which offer better constructs for concurrency, and they are
    gaining traction.

### cocurrency is the way forward
- Ahmdal's Law says that throughput gains are bounded by how much of the program
  has to run in a sequential manner.
  (The more you can can parallelize, the faster you can go)

 - web scale applications like gmail take this to its pinnacle.
 - Their application runs on millions of CPUs.
 - Those don't typically fit on a sigle machine
 - that becomes the domain distributed computing

 - You can run tensorflow on your puny laptop,
  or train your models on the cloud where
  multitudes of processors will help get the job done much faster.

 - This is explains a rise of languages that can tackle the challenges of distributed computing head on.

- better resource utilization since we don't waste CPU cycles busy waiting
- allows us to make games and UIs, applications where user shouldn't be kept
    waiting by the program for feedback
- The real world is concurrent !

- The phenomena we're talking about is everpresent around us, though it's of particular interest in CS.
- If all this talk of processors, and web scale confused you, let's take a more grounded example.
- there's been way too much talk without seeing any action

## Concurrency is not parallelism
- Knowing this distinction allows you to pick the right tool for the right job

- by intelligently mixing CPU-bound and I/O-bound threads, developers can get the most
efficiency out of their code.

- Apparently, Python is bad for programming concurrent programs because only one
  python thread can run at a time.  That is unfortunately correct.

- but if that were the case. python would lose out to other languages.
  though it seems to be going from strength to strength

## Threading in python
Advantages: so what are they good for ?

- scheduled preemptively - which means that the scheduler decides when to switch
  context,
  so you don't have to handle it in code.
  Python threads map directly on to OS threads, and are scheduled by the OS.
  Also Cpython avoids a lot of complexity in it's own implementation.

- Multiple threads are excellent for speeding up blocking I/O bound programs,
  because the scheduler is I/O aware. Instead of waiting on I/0

- don't have to write any extra code for it. by the OS, easier python implementation

- They have a smaller memory footprint than processes.

- Threads share resources, and thus communication between them is easier

### Disdavantages
- GIL means no parallel threads

- While communication between threads may be easier,
- you must be very careful not to implement code that is subject to race conditions.
  It is a comparitively quite difficult to get this right.

- Hard to test, hard to spot bugs in the code, hard to reproduce bugs.

- It's computationally expensive to switch context between multiple threads.
  By adding multiple threads, you could see a degradation in your program's
  overall performance if not used correctly. Especially with irresponsible locking

- Preemptive scheduling is a double edged sword like most things in CS.
- Easy to execute threads, but since you can't make any assumptions about
  when the task switch might happen, you have to guard portions of your code
  that access a shared resource(The critical section).


### The dreaded GIL

- Python threads have to acquire a mutex lock on the interpreter to execute.

- What that essentially means is that only one thread can run in a python
  process at one time, utilizing only one core at a time.

- It is necessary because python interpreters internal datastructures, aren't thread safe.

- people have been successful at removing the GIL before,
but at the cost having severly degraded single CPU performance, lowering overall performance quite a bit in
most cases.

- Note that the GIL is present in only the default implementation - CPython,
  and doesn't exist in runtimes who support parallel threads like Jython, IronPython

## Multiprocessing

- The model of having GIL with parallelism deferred to the OS via the

- For utilizing multiple cores, multiprocessing module works well.

### Advantages:
- They are better than multiple threads at handling CPU-intensive tasks

- We can sidestep the limitations of the GIL by spawning multiple processes

- workers model - eg. __Gunicorn__ - If you've run any python webapp/service in production, you might have heard of it.
- Suppose your program is leaking memory, by no fault for your own, It's a bug
  in one of the libraries you are using. You can kill off the process when it
  isn't serving a requests, if its memory grows beyond some threshold. You can't
  do something like this with threads or coroutines.

### Disadvantages:
- No shared memory between processes - have to implement some form of IPC, which is much more resource heavy on the computer.

- slower context switches.

- more startup cost.

## Async
### Advantages:
- very low cost, since no context switch. Incidentally they're cheaper than function calls. Cheaper switching mechanism among all techniques. People prefer this model to locking,
- No cost of synchronization = less CPU consumption. Async servers > threaded servers. You can run many many more async tasks than threads.

### disadvantages:
- Need code that gives up control
- Need an event loop
- Everything has to be non-blocking.
- Need to learn a lot of new things - new syntax, new libraries(aysnc versions), eventloops, futures.
- Your program doesn't have to block on a slow network call, your program can be doing other things. This is the foundation of AJAX
- highly successful model for web servers. This is how nodejs and nginx handle massive scale.

## conclusion

So this is what we have realized so far:

- Sync: Blocking operations.
- Async: Non blocking operations.
- Concurrency: Making progress together.
- Parallelism: Making progress in parallel.
- locking: avoid
- Parallelism implies Concurrency. But Concurrency doesn’t always mean Parallelism.
