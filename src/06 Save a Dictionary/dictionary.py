''' Save a dictionary to a file. Read the saved dictionary from the file. 
    Use pickle module for serialization 
    
    Output:
    Dictionary successfully saved to file
    {1: 'a', 2: 'b', 3: 'c', 4: 'd'}'''

import pickle

def save_dict(dict_data, file_path):
    ''' Save dictionary to file '''
    with open(file_path, 'wb') as fp:
        pickle.dump(dict_data, fp)
        print('Dictionary successfully saved to file')

def load_dict(file_path):
    ''''Read dictionary from file '''
    with open(file_path, 'rb') as fp:
        dict_data = pickle.load(fp)
        return dict_data
    
if __name__ == '__main__':
    file_path = "save_dictionary.pkl"
    example_data = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
    save_dict(example_data, file_path)
    print(f"Read data from the file:\n{load_dict(file_path)}")
