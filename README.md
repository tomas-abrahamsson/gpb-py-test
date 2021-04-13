# gpb-py-test

Test whether gpb python can enc/dec value larger than 64 bit unsigned int.

# Setup

- Create a python venv
- Do `pip install --upgrade google-api-python-client`
- Run `python test.py`

# Expectation

For the second function:

```
Traceback (most recent call last):
  File "test.py", line 39, in <module>
    invalid()
  File "test.py", line 22, in invalid
    t0.id = 295147905179352825855
ValueError: Value out of range: 295147905179352825855
```
