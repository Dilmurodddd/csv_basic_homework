def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    s = data.split("\n")
    return len(s[0].split(","))
# open the file
fayl = open("data.csv").read()

data = find_number_of_columns(fayl)

print(data)
# Read the csv file