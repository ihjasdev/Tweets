import csv

# Open the input CSV file
with open('merged.csv', 'r') as in_file:
    # Create a CSV reader
    reader = csv.reader(in_file)
    
    # Open the output CSV file
    with open('output.csv', 'w') as out_file:
        # Create a CSV writer
        writer = csv.writer(out_file)
        
        # Iterate through the rows of the input CSV file
        for row in reader:
            # Use a list comprehension to remove unwanted characters
            # from each element in the row
            modified_row = [elem.replace('@', '') for elem in row]
            
            # Write the modified row to the output CSV file
            writer.writerow(modified_row)
