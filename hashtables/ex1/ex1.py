def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}


    for i in range(len(weights)):
        for j in range(i+1, len(weights)):
            if weights[i] + weights[j] == limit:
                if j > i:
                    cache[(weights[j],weights[i])] = (j, i)
                    return cache[(weights[j],weights[i])]
                else:
                    cache[(weights[i],weights[j])] = (i, j)
                    return cache[(weights[i],weights[j])]

    return None


weights_4 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_4, 5, 21))
