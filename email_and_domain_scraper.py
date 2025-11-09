import requests                 # to download the webpage content
from bs4 import BeautifulSoup   # for parsing HTML easily
import re                       # for pattern matching (finding emails/domains)
import csv                      # To save data into a CSV file

# Choose a target URL (use a safe, test-friendly site)
url = "https://scrapepark.org/"

# Send a GET request to fetch the page's HTML
# (Some sites block bots; always check permissions)
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract all text from the page 
page_text = soup.get_text()

# Define regular expressions for email and domain patterns
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
domain_pattern = r"\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b"

# Find all matches using re.findall()
emails = re.findall(email_pattern, page_text)
domains = re.findall(domain_pattern, page_text)

# Display the results
print("=== Emails Found ===")
for email in emails:
    print(email)

print("\n=== Domains Found ===")
for domain in domains:
    print(domain)

# Save results to a CSV file
# Each row will contain an email or domain type
csv_filename = "scraped_results.csv"

with open(csv_filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    # Write header row
    writer.writerow(["Type", "Value"])

    # Write all emails
    for email in emails:
        writer.writerow(["Email", email])

    # Write all domains
    for domain in domains:
        writer.writerow(["Domain", domain])

print(f"\nResults saved to '{csv_filename}' successfully!")