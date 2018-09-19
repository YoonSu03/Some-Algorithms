" It can add every number!"

def add(*args):
    result = 0
    for thing in args:
        if type(thing) == int:
            result += thing
        elif type(thing) == str:
            result += int(thing)
        elif type(thing) == list:
            for t in thing:
                if type(t) == list:
                    result += add(t)
                else:
                    result += t
    return result

print(add(1, 2, [[1, 3, 5], 1, 2, [1, [1, [1, 3, 8, 300]]]], [1], [1,2,[3, 5, [2]]]))
