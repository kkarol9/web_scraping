import json
from bs4 import BeautifulSoup

# Load the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all div elements with class="pprofile-activity-widget__results"
results_divs = soup.find_all('div', class_='pprofile-activity-widget__results')

# Loop through the divs and extract the name, surname, and score
data = []
for div in results_divs:
    surname = div.find('span', class_='pprofile-activity-widget__last-name')
    surname = surname.text if surname else ''
    name = div.find('span', class_='pprofile-activity-widget__first-name')
    name = name.text if name else ''
    score = div.find('div', class_='pprofile-activity-widget__result-status-text')
    score = score.text if score else ''
    data.append({'surname': surname, 'name': name, 'score': score})

# Write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data, f)
