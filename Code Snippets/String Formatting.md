# String Formatting

## The .format() function

### Example 1

```python
my_num = 5
my_string = 'Hello'

new_string = "My secret number is {} and My secret code word is {}".format(my_num, my_string)
```

<b>Output:</b>
My secret number is 5 and My secret code word is Hello.

### Example 2

To print inverted commas in the string we use the following formatting.

```python
f = "my_num is {}, and my_str is \"{}\".".format(my_num, my_str)
```
<b>Output:</b>
my_num is 5, and my_str is "Hello".

### Example 3

We can also assign names to the place holders.

```python
f = "my_num is {n}, and my_str is '{s}'.".format(n=my_num, s=my_str)
```
<b>Output:</b>
my_num is 5, and my_str is 'Hello'.

### Example 4

```python
my_num = 5
my_str = 'Hello'

f = "my_num is {my_num}, and my_str is '{my_str}'.".format()
```

<b>Output:</b>
my_num is 5, and my_str is 'Hello'.


