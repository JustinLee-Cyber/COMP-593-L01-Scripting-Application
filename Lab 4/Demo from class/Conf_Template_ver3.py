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
        # https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html
    df = pd.read_csv(conference_workshops_data_csv)
    #print(df)

    # Insert "TOTAL COST" column (Tickets * Price) into the DataFrame
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert

    df.insert(7,'TOTAL COST',df['TICKETS'] * df['PRICE PER TICKET'])
    #print(df)

    # Remove the (Level) column from the DataFrame that is not needed
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html
    df.drop(columns=['SHORT','Level'], inplace=True)
    #print(df)

    # Groups data by (TRACK) and iterate (using for loop)
        # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

    for track, track_df in df.groupby('TRACK'):
        # Display the loop outcomes 
        #print(track)
        #print(track_df)
        
        # Remove the 'TRACK' column - Not needed now
        track_df.drop(columns='TRACK', inplace=True)
        #print(track_df)
        
        # Sort items in descending order by attendee ID 
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values 

        track_df.sort_values('ATTENDEE ID', ascending=False, inplace=True)
        #print(track_df)
        
        # Append a "Average TICKETS Bought for each track" as a row
        average_tickets = track_df['TICKETS'].mean()
        #print(average_tickets)
        average_tickets_df = pd.DataFrame({'SESSION NAME':'Average','TICKETS':[average_tickets]})
        #print(average_tickets_df)

        # Concatenation of two Dataframes average_tickets_df & track_df
        track_df = pd.concat([track_df,average_tickets_df])
        #print(track_df)

        # Determine the file name and full path of the Excel sheets 
        # Name file based on Track (e.g., TRACK_Cloud Ops.xlsx)
        file_name = f'TRACK_{track}.xlsx' # 
        track_file_path = os.path.join(workshops_path,file_name)
        #print(track_file_path)

        # Export the data to Excel sheets using XlsxWriter and pandas packages
            # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html
        
        with pd.ExcelWriter(track_file_path, engine="xlsxwriter") as writer:
            track_df.to_excel(writer, index=False, sheet_name="Sheet1")
     
            # Get the xlsxwriter workbook and worksheet objects.
                # https://xlsxwriter.readthedocs.io/example_pandas_column_formats.html
            workbook = writer.book
            worksheet = writer.sheets["Sheet1"]
        
            # Define format template for numeric columns & Style
                # https://xlsxwriter.readthedocs.io/worksheet.html#worksheet-set-column
            format_1 = workbook.add_format({"num_format" : "0.0"})
            format_2 = workbook.add_format({"num_format" : "0%"})
            format_3 = workbook.add_format({"num_format" : "$#,##0_);($#,##0)"})
            format_4 = workbook.add_format({'bold': True})
            format_5 = workbook.add_format({'align': 'center'})

            # Apllying Formatting for each column / Set column widths
            worksheet.set_column('A:B', 14) # WORKSHOP ID & ATTENDEE ID 
            worksheet.set_column('C:C', 20) # SESSION NAME
            worksheet.set_column('D:D', 9, format_1) # TICKETS
            worksheet.set_column('E:E', 15, format_5) # PRICE PER TICKET
            worksheet.set_column('F:F', 12, format_3) # TOTAL COST
            worksheet.set_column('G:G', 13, format_4) # ATTENDEE NAME
            
        # Remark:
        # When you use with pd.ExcelWriter(...) as writer:
        # the context manager automatically handles the closing 
        # and saving of the Excel file once the block of code inside 
        # the with statement is finished, even if an error occurs during processing.
            # https://xlsxwriter.readthedocs.io/index.html

        # writer.close() # No need to call writer.close() since "with" statement is used.

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