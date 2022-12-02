import sys
import csv
# import os, psutil # memory usage

COL_FILENAME = "filename" # name of inserted column for filename


def create_row(col_value, output_column_names):
    """Creates new row by mapping row values to the associated column.

    Parameters
    ----------
    col_value : dictionary
        dictionary mapping column name to current row's value
    output_column_names : list
        list of column names that will be outputted to new file

    Returns
    -------
    string
        row to be outputted to stdout
    """
    row = []
    for name in output_column_names:
        if name in col_value:
            row.append(f'\"{col_value[name]}\"')
        else:
            row.append(f'\"\"')
    return ",".join(row)

def extract_rows(file, file_name, output_column_names):
    """Parses the specified file row by row and feeds it to the 
    create_row function.

    Parameters
    ----------
    file : TextIOWrapper
        current csv file we are reading from
    file_name : string
        name of current file
    output_column_names : list
        list of column names that will be outputted to new file

    Returns
    -------
    None
    """
    csv_reader = csv.reader(file, delimiter=',')
    # get column names of current file and add filename
    column_names = next(csv_reader)
    column_names.append(COL_FILENAME)
    # initialize dictionary relating column names to values
    col_value = {}
    # iterate over csv lines
    for line in csv_reader:
        line.append(file_name)
        # set col_value dictionary
        for i in range(len(column_names)):
            col_value[column_names[i]] = line[i]
        row = create_row(col_value, output_column_names)
        print(row)

def combine_files(file_names, output_column_names):
    """main function for sending new csv to stdout. Calls extract_rows
    function which in turn calls creat_row function.

    Parameters
    ----------
    file_names : list
        list of file names as strings
    output_column_names : list
        list of column names that will be outputted to new file

    Returns
    -------
    None
    """
    for fn in file_names:
        with open(fn, 'r') as f:
            extract_rows(f, fn, output_column_names)

def extract_columns(file_names):
    """gets column names from inputted files and store in list

    Parameters
    ----------
    file_names : list
        list of file names as strings

    Returns
    -------
    list
        list of column names across all csv files
    """
    column_names = []
    for fn in file_names:
        with open(fn, 'r') as f:
            csv_reader = csv.reader(f, delimiter=',')
            header = next(csv_reader)
            for column_name in header:
                if column_name not in column_names:
                    column_names.append(column_name)
    return column_names

def main():
    file_names = sys.argv[1:]
    output_column_names = extract_columns(file_names)
    output_column_names.append(COL_FILENAME) # append "filename" column
    print("\"" + "\",\"".join(output_column_names) + "\"")
    combine_files(file_names, output_column_names)

    # memory usage
    # process = psutil.Process(os.getpid())
    # print(process.memory_info().rss)  # in bytes 

if __name__ == "__main__":
    main()