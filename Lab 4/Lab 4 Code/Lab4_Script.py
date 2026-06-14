# pandas package
import pandas as pd
# os package 
import os
# sys package
import sys
# datetime package
import datetime
# re package
import re


"""
Description:
    Divides Conference Workshop data CSV file into divisional report Excel files.
"""
def process_workshops_record_data(data_csv, workshops_path):
    
    print(data_csv,workshops_path)

    return

def main():
    # Paths for input data and output directory

    #REQ-1 - Grab CSV file data from command line parameter
    from sys import argv

    #REQ-2 If no command line parameter is provided, provide error message than exit
    if len(argv) < 2:
        print('Error: No path was input, please include path to CSV file.')
        sys.exit()   
    #REQ-3 If path was found, check if CSV is called for, if not error message and exit
    else:    
        data_csv = argv[1]
        if not data_csv.endswith('.csv'):
            print('Error: Path given does not include .csv.')
            sys.exit()
        else:
            workshops_path = '.\\Orders'
            # Call the processing function
            process_workshops_record_data(data_csv, workshops_path)

    return

if __name__ == '__main__':
    main()