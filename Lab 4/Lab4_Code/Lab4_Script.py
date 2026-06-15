#Student Name: Justin Lee
#Student Number: 10152040

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
def removedata(df):

    #REQ-6 - Drop unneeded columns
    df.drop(columns=['ORDER ID', 'ADDRESS', 'CITY', 'STATE', 'POSTAL CODE', 'COUNTRY'], inplace=True)

    return

def sortdata(df, name):
    
    #REQ-7 - Sort by Item number
    df.sort_values(name, ascending=True, inplace=True)

    return

def insertdata(df):

    #REQ-8 - Insert total codes from item quantity x item price
    df.insert(6, 'TOTAL PRICE', df['ITEM QUANTITY'] * df['ITEM PRICE'])

    return

def formating(data_file_path, order_date_df):

    #REQ-10 - format time, adjust all price information as money, $, comma-spearated thousands, and two decimal places
    with pd.ExcelWriter(data_file_path, engine="xlsxwriter") as writer:
        order_date_df.to_excel(writer, index=False, sheet_name="Sheet1")

    #Creating workbook and worksheet
        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]

    #REQ-10 - format template for numeric columns
        format_1 = workbook.add_format({'num_format' : '$#,##0.00'})
    
        worksheet.set_column('A:A', 11)
        worksheet.set_column('B:B', 13)
        worksheet.set_column('C:D', 15)
        worksheet.set_column('E:E', 15)
        worksheet.set_column('F:G', 13, format_1)
        worksheet.set_column('H:H', 10)
        worksheet.set_column('I:I', 30) 
    
    return

def exportfile(df, workshops_path):

  #REQ-9 - The grand sum of the total cost 
    for order_date,  order_date_df in df.groupby('ORDER DATE'):
        #print(order_date)
        #print(order_date_df)
        total_cost_sum = order_date_df['TOTAL PRICE'].sum()
        #print(total_cost_data)
        total_cost_df = pd.DataFrame({'ITEM PRICE':'GRAND TOTAL', 'TOTAL PRICE':[total_cost_sum]})
        #print(total_cost_df)
        order_date_df = pd.concat([order_date_df, total_cost_df])
        #print(order_date_df)

        fix_date = str(order_date).replace('/', '-')
        file_name = f'Orders_{fix_date}.xlsx' # 
        data_file_path = os.path.join(workshops_path,file_name)
        #print(data_file_path)

        formating(data_file_path, order_date_df)

    return

def process_order_data(data_csv, workshops_path):
    #Import order data csv that was inserted from command line
    df = pd.read_csv(data_csv)

    removedata(df)
    sortdata(df, 'ITEM NUMBER')
    insertdata(df)
    exportfile(df,workshops_path)

    return

def checkpath(argv):
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
            return True;

    return False

def main():
    #REQ-1 - Grab CSV file data from command line parameter
    from sys import argv

    if checkpath(argv) is True:
        data_csv = argv[1]      
        #Check if there is a created Orders Folder or Not
        order_path = './Orders'
        os.makedirs(order_path, exist_ok=True)

        process_order_data(data_csv, order_path)

    return

if __name__ == '__main__':
    main()