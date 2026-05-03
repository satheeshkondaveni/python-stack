Great — I’ve now persisted your request to document the **Python logical interview questions and answers**. Let’s bring everything together in one place so you have a complete prep guide for your **first two requests**.  

---

# 📘 Python Logical Interview Prep (Senior-Level, 11+ Years Experience)

---

## **Set 1: Advanced Logical Questions & Answers**

### 1. Concurrency & Parallelism
- **Q:** How would you design a system that processes millions of log entries per second using Python?  
- **A:** Use **multiprocessing** for CPU-bound tasks, **asyncio** for I/O-bound tasks. `threading` is limited by the GIL. Best design: hybrid of **asyncio + multiprocessing**.

---

### 2. Memory Optimization
- **Q:** How to process a dataset too large for memory?  
- **A:** Use **generators** (`yield`) and **iterators** to stream data. Example: `for line in open("bigfile.txt")`.

---

### 3. Detect Cycles in Directed Graph
```python
def has_cycle(graph):
    visited, stack = set(), set()
    def dfs(node):
        if node in stack: return True
        if node in visited: return False
        visited.add(node); stack.add(node)
        for nei in graph.get(node, []):
            if dfs(nei): return True
        stack.remove(node)
        return False
    return any(dfs(n) for n in graph)
```

---

### 4. Singleton Logger
```python
import threading
class Logger:
    _instance = None
    _lock = threading.Lock()
    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance
```

---

### 5. LRU Cache
```python
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache: return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

---

### 6. Rate Limiter
- **Answer:** Use **token bucket algorithm** with Redis for distributed systems. Each request consumes a token; tokens refill at fixed rate.

---

### 7. Logical Trap
```python
def foo(x=[]):
    x.append(1)
    return x
print(foo())  # [1]
print(foo())  # [1, 1]
```
- **Answer:** Default mutable arguments persist across calls.  
- Fix: `def foo(x=None): x = x or []; x.append(1); return x`

---

### 8. Optimization Challenge
- **Answer:** Profile with `cProfile`. Replace nested loops with **set lookups, NumPy vectorization, or caching**.

---

---

## **Set 2: More Advanced Logical Questions & Answers**

### 1. Immutable vs Mutable Trap
```python
a = (1, [2, 3])
a[1].append(4)
print(a)  # (1, [2, 3, 4])
```
- Tuples are immutable, but the list inside is mutable.

---

### 2. Metaprogramming
```python
class EnforceToDict(type):
    def __init__(cls, name, bases, dct):
        if 'to_dict' not in dct:
            raise TypeError(f"{name} must implement to_dict()")
        super().__init__(name, bases, dct)
```
- Trade-off: Metaclasses are powerful but complex; decorators are simpler.

---

### 3. Performance Profiling
- **Answer:** Use `cProfile` for CPU, `line_profiler` for line-level, `tracemalloc` for memory. Identify bottleneck → optimize.

---

### 4. Serialization Challenge
- **Answer:** JSON doesn’t support cycles.  
- Solution: custom encoder or use `pickle` (unsafe). Safer: `json` with IDs to break cycles.

---

### 5. Concurrency Puzzle
```python
counter = 0
```
- **Answer:** Counter will be less than 2,000,000 due to race condition.  
- Fix: Use `threading.Lock` or `multiprocessing.Value`.

---

### 6. Decorator Logic
```python
import time, functools
def retry(max_attempts=3, backoff=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = 1
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
                    delay *= backoff
        return wrapper
    return decorator
```

---

### 7. Security-Oriented Question
- **Answer:** Avoid `pickle` for untrusted input. Use `json`, `yaml.safe_load`, or schema-based serialization.

---

### 8. Functional Programming
```python
def cat(file):
    with open(file) as f:
        for line in f: yield line
def grep(pattern, lines):
    for line in lines:
        if pattern in line: yield line
def sort(lines): return sorted(lines)
def uniq(lines):
    seen = set()
    for line in lines:
        if line not in seen:
            seen.add(line); yield line
pipeline = uniq(sort(grep("error", cat("log.txt"))))
for line in pipeline: print(line)
```

---

### 9. Longest Palindromic Substring
```python
def longest_palindrome(s):
    res = ""
    for i in range(len(s)):
        temp = expand(s, i, i)
        if len(temp) > len(res): res = temp
        temp = expand(s, i, i+1)
        if len(temp) > len(res): res = temp
    return res
def expand(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
```

---

### 10. Distributed Task Queue
- **Answer:** Components: Broker (Redis/RabbitMQ), Workers, Result Backend.  
- Ensure fault tolerance with retries, acknowledgments, monitoring.  
- This is essentially how **Celery** works.

---

---

✨ Now you have **all questions and answers from both sets** documented in one place.  

Would you like me to **restructure this into a polished “Interview Prep Guide” format** (with sections like *Concepts*, *Code Challenges*, *System Design*) so it reads like a professional study document?