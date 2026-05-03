Perfect! Let’s go through **all 50 Python logical questions with solutions**. I’ll present each as **Question → Answer (code)** so you can practice directly.

---

## 🐍 Python Logical Questions with Solutions

### 1. Palindrome Number
```python
num = 121
temp = num
rev = 0
while num > 0:
    rev = rev*10 + num%10
    num //= 10
print("Palindrome" if temp == rev else "Not Palindrome")
```

### 2. Pyramid Pattern
```python
rows = 5
for i in range(1, rows+1):
    print(" "*(rows-i) + "*"* (2*i-1))
```

### 3. Factorial
```python
def factorial(n):
    return 1 if n==0 else n*factorial(n-1)
print(factorial(5))
```

### 4. Fibonacci Series
```python
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
```

### 5. Reverse String
```python
s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)
```

### 6. Count Vowels & Consonants
```python
s = "python"
vowels = "aeiou"
v, c = 0, 0
for ch in s:
    if ch in vowels: v+=1
    else: c+=1
print("Vowels:", v, "Consonants:", c)
```

### 7. Prime Check
```python
n = 29
flag = True
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        flag = False
        break
print("Prime" if flag else "Not Prime")
```

### 8. Sum of Digits
```python
n = 1234
s = 0
while n > 0:
    s += n % 10
    n //= 10
print(s)
```

### 9. Multiplication Table
```python
n = 5
for i in range(1, 11):
    print(n, "x", i, "=", n*i)
```

### 10. Largest of Three
```python
a, b, c = 10, 20, 15
print(max(a, b, c))
```

---

⚡ To keep this digestible, I’ll break the **50 solutions into 5 batches of 10**.  
You now have **Q1–Q10 with solutions**.  

👉 Do you want me to continue with **Q11–Q20 next**, or would you prefer me to give you the **entire set of 50 in one long response** (it’ll be very lengthy)?



Alright, let’s continue with the **next batch: Q11–Q20 with solutions** 🚀  

---

### 11. Check Anagram
```python
s1, s2 = "listen", "silent"
print("Anagram" if sorted(s1) == sorted(s2) else "Not Anagram")
```

### 12. GCD and LCM
```python
import math
a, b = 12, 18
print("GCD:", math.gcd(a, b))
print("LCM:", abs(a*b)//math.gcd(a, b))
```

### 13. Pascal’s Triangle
```python
rows = 5
for i in range(rows):
    num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num * (i-j) // (j+1)
    print()
```

### 14. Armstrong Numbers in Range
```python
for num in range(100, 1000):
    s = sum(int(d)**3 for d in str(num))
    if s == num:
        print(num)
```

### 15. Decimal to Binary
```python
n = 10
binary = ""
while n > 0:
    binary = str(n%2) + binary
    n //= 2
print(binary)
```

### 16. Second Largest in List
```python
lst = [10, 20, 4, 45, 99]
lst.sort()
print("Second Largest:", lst[-2])
```

### 17. Sort Without `sort()`
```python
lst = [5, 2, 9, 1]
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)
```

### 18. Remove Duplicates
```python
lst = [1,2,2,3,4,4,5]
unique = []
for i in lst:
    if i not in unique:
        unique.append(i)
print(unique)
```

### 19. Character Frequency
```python
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
```

### 20. Pangram Check
```python
import string
s = "The quick brown fox jumps over the lazy dog"
print("Pangram" if set(string.ascii_lowercase) <= set(s.lower()) else "Not Pangram")
```

---

✅ That’s **Q11–Q20 solved**.  
Would you like me to roll straight into **Q21–Q30** now, or do you want to pause and try these out first?


Here comes the **next batch: Q21–Q30 with solutions** 🎯  

---

### 21. Prime Numbers Between 1–100
```python
for n in range(2, 101):
    flag = True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            flag = False
            break
    if flag:
        print(n, end=" ")
```

### 22. Sum of Even Numbers in List
```python
lst = [1,2,3,4,5,6]
print(sum(x for x in lst if x%2==0))
```

### 23. Sum of Odd Numbers in List
```python
lst = [1,2,3,4,5,6]
print(sum(x for x in lst if x%2!=0))
```

### 24. Diamond Pattern
```python
rows = 5
for i in range(rows):
    print(" "*(rows-i-1) + "*"*(2*i+1))
for i in range(rows-2, -1, -1):
    print(" "*(rows-i-1) + "*"*(2*i+1))
```

### 25. Perfect Number Check
```python
n = 28
s = sum(i for i in range(1, n) if n%i==0)
print("Perfect" if s==n else "Not Perfect")
```

### 26. Digital Root
```python
n = 9875
while n > 9:
    n = sum(int(d) for d in str(n))
print(n)
```

### 27. Count Words in Sentence
```python
s = "Python is fun to learn"
print(len(s.split()))
```

### 28. Longest Word in Sentence
```python
s = "Python programming is amazing"
words = s.split()
print(max(words, key=len))
```

### 29. Palindrome String
```python
s = "madam"
print("Palindrome" if s == s[::-1] else "Not Palindrome")
```

### 30. All Substrings of String
```python
s = "abc"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
```

---

✅ That’s **Q21–Q30 solved**.  
Would you like me to keep rolling into **Q31–Q40** right away?

Here’s the **next batch: Q31–Q40 with solutions** 🔥  

---

### 31. Missing Number in Sequence
```python
lst = [1,2,3,5,6]
n = max(lst)
missing = [i for i in range(1, n+1) if i not in lst]
print("Missing:", missing)
```

### 32. Duplicate Number in List
```python
lst = [1,2,3,2,4,5,1]
dup = []
for i in lst:
    if lst.count(i) > 1 and i not in dup:
        dup.append(i)
print("Duplicates:", dup)
```

### 33. Rotate List by k
```python
lst = [1,2,3,4,5]
k = 2
rotated = lst[k:] + lst[:k]
print(rotated)
```

### 34. Intersection of Two Lists
```python
a = [1,2,3,4]
b = [3,4,5,6]
print(list(set(a) & set(b)))
```

### 35. Union of Two Lists
```python
a = [1,2,3]
b = [3,4,5]
print(list(set(a) | set(b)))
```

### 36. String Rotation Check
```python
s1, s2 = "abcd", "cdab"
print("Rotation" if len(s1)==len(s2) and s2 in s1+s1 else "Not Rotation")
```

### 37. First Non-Repeating Character
```python
s = "swiss"
for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
```

### 38. Maximum Occurring Character
```python
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(max(freq, key=freq.get))
```

### 39. Strong Number
```python
import math
n = 145
s = sum(math.factorial(int(d)) for d in str(n))
print("Strong Number" if s==n else "Not Strong")
```

### 40. Sum of Series (1 + 1/2 + ... + 1/n)
```python
n = 5
s = sum(1/i for i in range(1, n+1))
print(s)
```

---

✅ That’s **Q31–Q40 solved**.  
We’re almost there! Shall I go ahead and finish with the **final batch Q41–Q50**?
Here’s the **final batch: Q41–Q50 with solutions** 🎉  

---

### 41. Random Number Without `random` Module
```python
import time
n = int(str(time.time()).split(".")[1]) % 100
print(n)
```

### 42. Swap Two Numbers Without Temp Variable
```python
a, b = 5, 10
a, b = b, a
print(a, b)
```

### 43. Median of List
```python
lst = [1,2,3,4,5]
lst.sort()
n = len(lst)
if n%2==0:
    median = (lst[n//2-1] + lst[n//2]) / 2
else:
    median = lst[n//2]
print(median)
```

### 44. Mode of List
```python
lst = [1,2,2,3,3,3,4]
freq = {}
for i in lst:
    freq[i] = freq.get(i, 0) + 1
mode = max(freq, key=freq.get)
print(mode)
```

### 45. ASCII Value of Character
```python
ch = 'A'
print(ord(ch))
```

### 46. Convert String to Title Case Without `title()`
```python
s = "hello world from python"
words = s.split()
title_case = " ".join(w[0].upper()+w[1:] for w in words)
print(title_case)
```

### 47. Largest Palindrome Substring
```python
def is_palindrome(s):
    return s == s[::-1]

s = "babad"
longest = ""
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        sub = s[i:j]
        if is_palindrome(sub) and len(sub) > len(longest):
            longest = sub
print(longest)
```

### 48. Prime Factors of Number
```python
n = 84
i = 2
factors = []
while n > 1:
    if n % i == 0:
        factors.append(i)
        n //= i
    else:
        i += 1
print(factors)
```

### 49. Sum of Squares of First n Natural Numbers
```python
n = 5
s = sum(i*i for i in range(1, n+1))
print(s)
```

### 50. Hollow Square Pattern
```python
n = 5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
```

---

✅ That’s **all 50 Python logical questions with solutions** completed!  
You now have a full practice set covering loops, recursion, strings, lists, and patterns.  

Would you like me to **bundle these into a single structured notebook-style format** (like a study guide), so you can run them sequentially in one go?
