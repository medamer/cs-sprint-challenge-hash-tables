def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for l in arrays:
        for i in range(len(l)):
            if l[i] not in cache:
                cache[l[i]] = 1
            else:
                cache[l[i]] +=1
    result = []
    for k, v in cache.items():
        if v == len(arrays):
            result.append(k)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
