import json
from bs4 import BeautifulSoup

# Load the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all div elements with class="pprofile-activity-widget"
activity_divs = soup.find_all('div', class_='pprofile-activity-widget')

# Loop through the divs and extract the name and surname
data = []
for div in activity_divs:
    surname = div.find('span', class_='pprofile-activity-widget__last-name')
    surname = surname.text if surname else ''
    name = div.find('span', class_='pprofile-activity-widget__first-name')
    name = name.text if name else ''
    data.append({'surname': surname, 'name': name})

# Write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data, f)
