def eqindex(data):
    # Initially I thought about solving the algorithm iterating through the array
    # and using two variables (left = 0  and right = sum(data)) to be maniuplated.
    # The initial solution was working, but it was taking into account the value
    # of the number at that particular index.
    # For example, I know the first solution should return 3 and 6... I was getting
    # just 5 because including data[5] (which is 3) created 0 == 0 and it returned
    # the index.
    i = 0
    result = []
    while i < len(data):
        # After realizing I was NOT supposed to include the value of the current
        # index, I created this simple boolean to determine the sum of the two
        # sides properly.
        if sum(data[:i]) == sum(data[i+1:]):
            result.append(i)
        i += 1
    return result
    # If there is no solution... I return an empty array.
