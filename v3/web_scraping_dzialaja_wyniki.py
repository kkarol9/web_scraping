"""
import json
from bs4 import BeautifulSoup

# Read HTML file and parse with Beautiful Soup
with open('index.html', 'r', encoding='utf-8') as fp:
    soup = BeautifulSoup(fp, 'html.parser')

# Find all divs with class "pprofile-activity-widget"
activity_widgets = soup.find_all('div', class_='pprofile-activity-widget')

# Loop through activity widgets and extract data
data = []
for widget in activity_widgets:
    # Extract title and details
    title_div = widget.find('div', class_='pprofile-activity-widget__title')
    title = title_div.span.text if title_div else ''
    
    details_div = widget.find('div', class_='pprofile-activity-widget__details pprofile-activity-widget__details--MT')
    details = details_div.span.text if details_div else ''
    
    # Extract results
    results_divs = widget.find_all('div', class_='pprofile-activity-widget__results')
    results = [div.span.text for div in results_divs]
    
    # Add data to list
    data.append({
        'title': title,
        'details': details,
        'results': results
    })

# Write data to JSON file
with open('data.json', 'w') as fp:
    json.dump(data, fp)
"""

import json
from bs4 import BeautifulSoup

# Load the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

dates = [span.text for span in soup.find_all("span", class_="pprofile-activity-tournament__date")]




# Find all div elements with class="pprofile-activity-widget"
activity_divs = soup.find_all('div', class_='pprofile-activity-widget')

# Loop through the divs and extract the data
data = []
for div in activity_divs:

    title = div.find('div', class_='pprofile-activity-widget__title')
    title = title.text if title else ''
    details = div.find('div', class_='pprofile-activity-widget__details pprofile-activity-widget__details--MT')
    details = details.text if details else ''
    #results = div.find('div', class_='pprofile-activity-widget__results')
    #results = results.text if results else ''
    results_divs = div.find_all('div', class_='pprofile-activity-widget__results')
    results = [divss.span.text for divss in results_divs]

    results_divs2 = div.find_all('ol', class_='pprofile-activity-widget__set-scores')
    results2 = [divss2.text for divss2 in results_divs2]





    data.append({'title': title, 'details': details, 'results': results, 'results 2': results2})

data.append(dates)

# Write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data, f)