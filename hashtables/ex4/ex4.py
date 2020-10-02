def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    for i in a:
        if i < 0:
            i = i* -1
        if i not in cache:
            cache[i] = 1
        else:
            cache[i] +=1
    result = []
    for k, v in cache.items():
        if v == 2:
            result.append(k)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
