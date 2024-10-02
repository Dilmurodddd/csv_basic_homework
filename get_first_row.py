def get_first_row(data):   
   """
   Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
   """
   
   return data.split("\n")[1]

fayl = open("data.csv").read()

data2 = get_first_row(fayl)

print(data2)

# Read the csv file