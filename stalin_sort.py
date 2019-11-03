def communism_is_wonderful(array):

    result = [array[0]]

    if len(array) > 1:

        prev = array[0]

        for elem in array[1:]:

            if elem >= prev:
                result.append(elem)

            else:
                print("OFF TO THE GULAGS")

            prev = elem

    return result