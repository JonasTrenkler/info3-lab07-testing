---
title: Info3 - Lab 07 - Testing
author: [Aaron Rau, Jonas Trenkler]
date: 2023-06-19
lang: "en-US"
keywords: [testing, TDD]
---

# Info3 - Lab 07 - Testing

## 1. Getting Started

Closed-box tests only have the interface to work with.
A method that returns the absolute of an integer should have a simple signature like `absolute(i)`, with only a single parameter, expected to be an integer.
As Python is a dynamically typed language there is no guarantee that the caller respects this limitation.
While using type-hints helps to reduce errors while writing the code, the method is still callable during runtime.

Therefore this is one equivalence class: *Invalid input* or `NaN` (though not `math.nan` or `float("nan")`).
The implementation has to decide how to handle this if there is no specification.
Without knowledge of that, it is impossible to design a closed boxed test (unless you try it out).
One reasonable way to handle invalid inputs would be to throw a [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError).
Another less obvious way would be to use error codes, for example negative integers.

Apart from that there are numbers, not differentiating between integers and floating point numbers in the following equivalence classes:

- below 0
- above 0
- 0

Treating 0 differently might not be necessary, but it is certainly a special case worth to look at.
The floating point numbers in Python adhere to IEEE 754, which does define both positive and negative zero, see [Signed Zero (Wikipedia)](https://en.wikipedia.org/wiki/Signed_zero).
The negative zero behaves like a negative number, for example in multiplication, but it is equal to 0 in a boolean statement.
Therefore the following is possible in python:

```python
In [7]: 0.0 * 2
Out[7]: 0.0

In [8]: -0.0 * 2
Out[8]: -0.0

In [9]: 0.0 * -2
Out[9]: -0.0

In [10]: 0.0 == -0.0
Out[10]: True
```

From the above we could argue that there are three equivalence classes:

1. numbers from 0.0 to positive infinity
2. numbers from -0.0 to negative infinity
3. invalid inputs, NaN

