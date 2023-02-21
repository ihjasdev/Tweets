import csv
import re

# Open the CSV file
with open('Tweets/language.csv', 'r') as f:
  # Use the csv.reader() function to read the contents of the file into a list of rows
  rows = csv.reader(f)

  # Iterate over the rows
  for row in rows:
    # Check if the row contains any unstructured data
    if any(re.search(r'[^\w\s]', cell) for cell in row):
      # If the row contains unstructured data, remove it
      row = [re.sub(r'[^\w\s]', '', cell) for cell in row]
    
    # Write the modified row back to the CSV file
    csv.writer(f).writerows(rows)
    
