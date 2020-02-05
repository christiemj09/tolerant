# Wrap functions in error-tolerant response objects.

Example usage:

```python
from tolerant import reponse

# Usage of built-in sum() function with no error raised
sum_call = response.response(sum)([1, 2])
print(sum_call)  # Response object
print(sum_call())  # 3

# Usage with an error
sum_call = response.response(sum)(1, 2)
print(sum_call())  # None
print(sum_call.error.__class__.__name__)  # TypeError
print(sum_call.error)  # 'int' object is not iterable

# Usage with a different error
sum_call = response.response(sum)([1, 'a'])
print(sum_call())  # None
print(sum_call.error.__class__.__name__)  # TypeError
print(sum_call.error)  # unsupported operand type(s) for +: 'int' and 'str'
```