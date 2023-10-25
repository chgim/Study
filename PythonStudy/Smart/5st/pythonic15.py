def function(a, b, c):
    print(a, b, c)


# 예제1
# value = (1, 2, 3)
# function(value)
# TypeError: function() missing 2 required positional arguments: 'b' and 'c'
# function(*value)  # 값을 풀어서 전달 가능

# 예제2
value = {"a": 1, "b": 2, "c": 3}
# function(a=1, b=2, c=3)
function(**value)


def function(**kwargs):
    print(kwargs)


value = {"a": 1, "b": 2, "c": 3}
function(**value)
