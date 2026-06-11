# pandas package
import pandas as pd
# os package 
import os

"""
Description:
    Divides Conference Workshop data CSV file into divisional report Excel files.
"""
def process_workshops_record_data(conference_workshops_data_csv, workshops_path):
    # Import the workshops data from the CSV file into a DataFrame
    df = pd.read_csv(conference_workshops_data_csv)
    #print(df)

        # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html

    # Insert "TOTAL COST" column (Tickets * Price) into the DataFrame
    df.insert(7, 'TOTAL COST', df['TICKETS']*df['PRICE PER TICKET'])        
    #print(df)

        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert

    # Remove the (Level) column from the DataFrame that is not needed
    df.drop(columns=['Level', 'SHORT'], inplace=True)
    #print(df)

        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html

    # Groups data by (TRACK) and iterate (using for loop)
    for track, track_df in df.groupby('TRACK'):
        #print(track)
        #print(track_df)
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html
       
        # Remove the 'TRACK' column - Not needed now
        track_df.drop(columns=['TRACK'], inplace=True)
        #print(track)
        #print(track_df)
        
        # Sort items in descending order by attendee ID
        track_df.sort_values(by='ATTENDEE ID', ascending=False, inplace=True)
        #print(track)
        #print(track_df)
        
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values 

        # Append a "Average TICKETS Bought for each track" as a row
        average_tickets = track_df['TICKETS'].mean()
        #print(average_tickets)

        # Concatenation of two Dataframes average_tickets_df & track_df
        average_tickets_df = pd.DataFrame({'SESSION NAME': 'Average', 'TICKETS': [average_tickets]})
        #print(average_tickets_df)
        track_df = pd.concat([track_df, average_tickets_df])
        #print(track_df)

        # Determine the file name and full path of the Excel sheets 
        # Name file based on Track (e.g., TRACK_Cloud Ops.xlsx)

        file_name = f'TRACK{track}.xlsx'
        #print(file_name)
        track_file_path = os.path.join(workshops_path, file_name)
        #print(track_file_path)

        # Export the data to Excel sheets using XlsxWriter and pandas packages
        with pd.ExcelWriter(track_file_path, engine='xlsxwriter') as writer:
            track_df.to_excel(writer, index=False, sheet_name='Sheet1')

            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
     
        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = writer.sheets["Sheet1"]

            # https://xlsxwriter.readthedocs.io/example_pandas_column_formats.html
        
        # Define format template for numeric columns (0%)
        format_1 = workbook.add_format({'bold': True})
        format_2 = workbook.add_format({'num_format': '0%'})

        # Apllying Formatting for each column / Set column widths

        worksheet.set_row(0, None, format_1)
        worksheet.set_column('A:A', 20)
        

        worksheet.set_column('B:B', 20, format_1)

        
        #worksheet.set_column('C:C', 20, format_2)
            # https://xlsxwriter.readthedocs.io/worksheet.html#worksheet-set-column
        
        #writer.close()
        
    return

def main():
    # Paths for input data and output directory
    conference_workshops_data_csv = 'conference_data1.csv'
    workshops_path = '.\\Workshops'
    
    # Call the processing function
    process_workshops_record_data(conference_workshops_data_csv, workshops_path)

    return
if __name__ == '__main__':
    main()