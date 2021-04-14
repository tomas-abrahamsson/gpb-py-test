# gpb-py-test

Test whether gpb python can enc/dec value larger than 64 bit unsigned int.

# Setup

- Create a python venv
- Do `pip install --upgrade google-api-python-client`
- Run `python test.py`

# Actual output

```
>python3 test.py
t0: id: 18446744073709551615

t1: id: 18446744073709551615

invalid2: t1: id: 18446744073709551615
```

The `uint70_ser_test` file was created like this:
```
13> {ok, test2, Code2} = gpb_compile:string(test2, "syntax='proto3'; message
test { uint64 id = 1; }", [maps, binary, {verify,never}]).
14> code:load_binary(test2, "test2.erl", Code2).
{module,test2}
15> file:write_file("uint70_ser_test", test2:encode_msg(#{id => (1 bsl 70)-1},
test)).
```
