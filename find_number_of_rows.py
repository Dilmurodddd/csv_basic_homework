def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    return len(data.split("\n"))
# open the file
fayl = open("data.csv").read()

data1 = find_number_of_rows(fayl)

print(data1)
# Read the csv file
