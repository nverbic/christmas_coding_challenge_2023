''' Merge a list of CSV files 

Output:
   Name  Midterm  Final   Lab
0   Tony       61     51   NaN
1   Nick       98     91   NaN
2  Keith       85     73   NaN
3  Alice       52     87  79.0
4  Steve       84     53  77.0
5  Ralph       82     83  91.0

all_students.csv:
Name,Midterm,Final,Lab
Tony,61,51,
Nick,98,91,
Keith,85,73,
Alice,52,87,79.0
Steve,84,53,77.0
Ralph,82,83,91.0

'''
import pandas as pd

def merge_csv(csv_files, merged_csv_file ):
    ''' Merge a list of csv files into a new csv file '''
    data_frame = []

    for csv_file in csv_files:
        data_frame.append(pd.read_csv(csv_file))

    # Concatinate data frames and ignore index (start new indexing)
    data_frame_merged  = pd.concat(data_frame, ignore_index=True)
    print(data_frame_merged.head(10))

    # Save to .csv file format, ignore indexes
    data_frame_merged.to_csv(merged_csv_file, index=False)

if __name__ == '__main__':
    merge_csv(['src/12 Merge CSV Files/class1.csv', 'src/12 Merge CSV Files/class2.csv'], 'all_students.csv')
