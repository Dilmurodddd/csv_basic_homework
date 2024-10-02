#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    a = data.split("\n")
    
    l = []
    aa = 0
    for x in a:
        l.append(str(aa) + "-" + x.split(",")[1])

        aa += 1
    return l
# open the file
fayl = open("data.csv").read()

data1 = get_column_names(fayl)

print(data1)
# Read the csv file