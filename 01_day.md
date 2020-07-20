```python
a = 123
a = -178
a = 0
```


```python
a = 1.2
a = -3.45
```


```python
a = 4.24E10
a = 4.24e-10
```


```python
a = 0o177
```


```python
a = 0x8ff
b = 0xABC
```


```python
a = 3
b = 4
a + b
```




    7




```python
a * b
```




    12




```python
a / b
```




    0.75




```python
a // b
```




    0




```python
a ** b
```




    81




```python
a % b
```




    3




```python
7 % 3
```




    1




```python
3 % 7
```




    3




```python
7 / 4
```




    1.75




```python
7 // 4
```




    1




```python
14 / 3
```




    4.666666666666667




```python
14 // 3
```




    4




```python
14 % 3
```




    2




```python
"Life is too short, you need Python"
```




    'Life is too short, you need Python'




```python
"a"
```




    'a'




```python
"123"
```




    '123'




```python
""123""
```


      File "<ipython-input-22-e2fece9a7579>", line 1
        ""123""
            ^
    SyntaxError: invalid syntax
    



```python
"\"123\""
```




    '"123"'




```python
"Hello world"
```




    'Hello world'




```python
'Python is fun'
```




    'Python is fun'




```python
""" Life is too short, You need Python"""
```




    ' Life is too short, You need Python'




```python
''' Life is too short, You need Python '''
```




    ' Life is too short, You need Python '




```python
Python's favorite food is perl
```


      File "<ipython-input-28-b75c51646192>", line 1
        Python's favorite food is perl
                                      ^
    SyntaxError: EOL while scanning string literal
    



```python
food = "Python's favorite food is perl"
```


```python
food
```




    "Python's favorite food is perl"




```python
food = 'Python's favorite food is perl'
```


      File "<ipython-input-31-336a85538234>", line 1
        food = 'Python's favorite food is perl'
                       ^
    SyntaxError: invalid syntax
    



```python
"Python is very easy." he says.
```


      File "<ipython-input-32-f87acc609a0a>", line 1
        "Python is very easy." he says.
                                ^
    SyntaxError: invalid syntax
    



```python
say = '"Python is very easy." he says.'
```


```python
say
```




    '"Python is very easy." he says.'




```python
food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\" he says."
```


```python
food
```




    "Python's favorite food is perl"




```python
say
```




    '"Python is very easy." he says.'




```python
multiline = "Life is too short\nYou need python"
```


```python
multiline
```




    'Life is too short\nYou need python'




```python
multiline = '''
Life is too short
You need python
'''
```


```python
multiline
```




    '\nLife is too short\nYou need python\n'




```python
print(multiline)
```

    
    Life is too short
    You need python
    
    


```python
multiline = "Life is too short\nYou need python"
```


```python
print(multiline)
```

    Life is too short
    You need python
    


```python
multiline = '''Life is too short
You need python'''
```


```python
print(multiline)
```

    Life is too short
    You need python
    


```python
head = "Python"
tail = " is fun!"
head + tail
```




    'Python is fun!'




```python
a = "python"
a * 2
```




    'pythonpython'




```python
print("=" * 10)
print("My program")
print("=" * 10)
```

    ==========
    My program
    ==========
    


```python
a = "Life is too short"
len(a)
```




    17




```python
b = "You need Python"
len(b)
```




    15




```python
a = "Life is too short, You need python"
a[3]
```




    'e'




```python
a[0]
```




    'L'




```python
a[1]
```




    'i'




```python
a[2}]
```


      File "<ipython-input-58-aff20f9dd934>", line 1
        a[2}]
           ^
    SyntaxError: invalid syntax
    



```python
a[2]
```




    'f'




```python
a[3]
```




    'e'




```python
a[4]
```




    ' '




```python
a = "Life is too short, You need python"
a[0]
```




    'L'




```python
a[2]
```




    'f'




```python
a[12]
```




    's'




```python
a[-1]
```




    'n'




```python
a[-0]
```




    'L'




```python
a[-2]
```




    'o'




```python
a[-5]
```




    'y'




```python
a = "Life is too short, You need python"
b = a[0] + a[1] + a[2] + a[3]
b
```




    'Life'




```python
a = "Life is too short, You need Python"
a[0:4]
```




    'Life'




```python
a[0:3]
```




    'Lif'




```python
a[0:5]
```




    'Life '




```python
a[0:2]
```




    'Li'




```python
a[5:7]
```




    'is'




```python
a[12:17]
```




    'short'




```python
a[19:]
```




    'You need Python'




```python
a[:17]
```




    'Life is too short'




```python
a[:]
```




    'Life is too short, You need Python'




```python
a[19:-7]
```




    'You need'




```python
a = "20010331Rainy"
date = a[:8]
weather= a[8:]
date
```




    '20010331'




```python
weather
```




    'Rainy'




```python
a = "20010331Rainy"
date = a[:8]
weather= a[8:]
print(date)
print(weather)
```

    20010331
    Rainy
    


```python
a = "20010331Rainy"
year = a[:4]
date = a[4:8]
weather= a[8:]
print(year)
print(date)
print(weather)
```

    2001
    0331
    Rainy
    


```python
a = "Pithon"
a[1]
```




    'i'




```python
a[1] = 'y'
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-85-d5923cc78d10> in <module>
    ----> 1 a[1] = 'y'
    

    TypeError: 'str' object does not support item assignment



```python
a = "Pithon"
a[:1]
a[2:]
a[:1] + 'y' + a[2:]
```




    'Python'




```python
a = "Pithon"
a[:1]
print(a)
a[2:]
print(a)
a[:1] + 'y' + a[2:]
```

    Pithon
    Pithon
    




    'Python'




```python
a = "Pithon"
a[:1]
print(a[:1])
a[2:]
print(a[2:])
a[:1] + 'y' + a[2:]
```

    P
    thon
    




    'Python'




```python
"I eat %d apples." % 3
```




    'I eat 3 apples.'




```python
"I et %s apples." % "five"
```




    'I et five apples.'




```python
number = 3
"I eat %d apples." % number
```




    'I eat 3 apples.'




```python
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
```




    'I ate 10 apples. so I was sick for three days.'




```python
"I have %s apples" % 3
```




    'I have 3 apples'




```python
" rate is %s" % 3.234
```




    ' rate is 3.234'




```python
"Error is %d%." %98
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-95-46f709d82ee0> in <module>
    ----> 1 "Error is %d%." %98
    

    ValueError: incomplete format



```python
"Error is %d%%." % 98
```




    'Error is 98%.'




```python
"%10s" % "hi"
```




    '        hi'




```python
"%-10sjane" % "hi"
```




    'hi        jane'




```python
"%0.4f" % 3.42134234
```




    '3.4213'




```python
"%10.4f" % 3.42134234
```




    '    3.4213'




```python
"%0.4f" % 3.42137112
```




    '3.4214'




```python
"I eat {0} apples".format(3)
```




    'I eat 3 apples'




```python
"I eat {0} apples".format("five")
```




    'I eat five apples'




```python
number = 3
"I eat {0} apples".format(number)
```




    'I eat 3 apples'




```python
number =10 
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number,day)
```




    'I ate 10 apples. so I was sick for three days.'




```python

```
