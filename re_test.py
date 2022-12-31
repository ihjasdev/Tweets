import csv
from textblob import TextBlob

# Open the CSV file in read mode
with open('data1.csv', 'r') as f:
  # Create a CSV reader object
  reader = csv.reader(f)
  
  # Open a new CSV file for writing
  with open('sentiment.csv', 'w', newline='') as f:
    # Create a CSV writer object
    writer = csv.writer(f)
    
    # Iterate over the rows in the CSV file
    for row in reader:
      # Use TextBlob to perform sentiment analysis on the text in the first column
      text = row[3]
      blob = TextBlob(text)
      polarity, subjectivity = blob.sentiment
      
      # Write the sentiment analysis results to the new CSV file
      writer.writerow([polarity, subjectivity])

print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")
