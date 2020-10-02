# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here

    cache = {}

    for f in files:
        for q in queries:
            if q in f:
                if q not in cache:
                    cache[q] = f
                else:
                    return cache[q]
    
    result = []

    for k, v in cache.items():
        result.append(v)
        
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
