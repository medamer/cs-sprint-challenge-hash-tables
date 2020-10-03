# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}
    result = []

    for i in files:
        name = i.split('/')[-1]
        if name not in cache:
            cache[name] = [i]
        else:
            cache[name].append(i)


    for n in queries:
        if n in cache:
            result.extend(cache[n])
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/foo',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
