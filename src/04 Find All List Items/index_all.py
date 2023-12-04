'''Find all items in a multidimensional list

List example:  example = [[[[1, 2, 3], 2,], [1, 3, 2]], [1, 2, 3]]

Output:
Found the following occurances of the item : 2 in the multudim. array: 
 [[0, 0, 0, 1], [0, 0, 1], [0, 1, 2], [1, 1]]'''

def index_all(list_of_objects, item, item_indicies, indices=None):
    ''' Find all the instances of the item in the list_of_objects'''
    if indices is None:
        indices = []

    for i, element in enumerate(list_of_objects):
        current_indices = indices + [i]

        if isinstance(element, list):
            # Recursively search nested lists
            result = index_all(element, item, item_indicies, current_indices)
            if result is not None:
                item_indicies.append(result)
        elif element == item:
            # Element found, return the indices
            return current_indices
    return None


if __name__== '__main__':
    example = [[[[1, 2, 3], 2,], [1, 3, 2]], [1, 2, 3]]
    item_indicies = []
    index_all(example, 2, item_indicies)
    print(f"Found the following occurrences of the item : 2 in the multudim. array: \n {item_indicies}")

