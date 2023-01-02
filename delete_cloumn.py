import csv

# Open the input CSV file
with open('Tweets\merged.csv', 'r') as input_file:
    # Create a CSV reader
    reader = csv.reader(input_file)

    # Open the output CSV file
    with open('Tweets\output.csv', 'w') as output_file:
        # Create a CSV writer
        writer = csv.writer(output_file)

        # Iterate over the rows in the input file
        for row in reader:
            # Delete the column by slicing the row and excluding the column
            # For example, to delete the second column, use row[:1] + row[2:]
            new_row = row[:1] + row[2:]
            writer.writerow(new_row)
