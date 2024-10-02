def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    d = data.split("\n")
    
    a = []
    
    for c in d:
        a.append(c.split(",")[1])
    return a

fayl = open("data.csv").read()

data2 = get_first_column(fayl)

print(data2)
    
# Read the csv file