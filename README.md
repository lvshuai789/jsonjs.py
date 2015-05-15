# jsonjs.py
Simple module with two methods to write and read a Python dictionary into a valid Javascript file containing the dictionary as JSON.

This Python dictionary
```python
{
    'rootOne' : {
        'aKey' : 100
    },
    'rootVar' : {
        'anotherKey' : 'another value'
    }
}
```

is equivalent to this Javascript file

```javascript
var rootOne =
{ 
  'aKey' : 100
};
var rootVar = 
{
    'anotherKey' : 'another value'
}
```

and vice-versa. There are only two methods relevant to the operation. See `__main__` code for more info.