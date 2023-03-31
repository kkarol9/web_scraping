import json
from bs4 import BeautifulSoup

# read index.html file and parse with Beautiful Soup
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# find all div elements with class="pprofile-activity-widget"
widgets = soup.find_all('div', class_='pprofile-activity-widget')

# process each widget
data = []

for widget in widgets:
    # try to find the title
    title_elem = widget.find('div', class_='pprofile-activity-widget__title')
    title = title_elem.text.strip() if title_elem else ''

    # try to find the details
    details_elem = widget.find('div', class_='pprofile-activity-widget__details pprofile-activity-widget__details--MT')
    details = details_elem.text.strip() if details_elem else ''

    # find all div elements with class="pprofile-activity-widget__results" within the current widget
    result_widgets = widget.find_all('div', class_='pprofile-activity-widget__results')

    # process each result widget
    for result_widget in result_widgets:
        # try to find the surname
        surname_elem = result_widget.find('span', class_='pprofile-activity-widget__last-name')
        surname = surname_elem.text.strip() if surname_elem else ''

        # try to find the first name
        first_name_elem = result_widget.find('span', class_='pprofile-activity-widget__first-name')
        first_name = first_name_elem.text.strip() if first_name_elem else ''

        # try to find the results
        results_elem = result_widget.find('div', class_='pprofile-activity-widget__result-status-text')
        results = results_elem.text.strip() if results_elem else ''

        # append the data to the list
        data.append({
            'title': title,
            'details': details,
            'surname': surname,
            'first_name': first_name,
            'results': results
        })

# write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data, f)


"""
import json
from bs4 import BeautifulSoup

# Load the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all div elements with class="pprofile-activity-widget"
activity_divs = soup.find_all('div', class_='pprofile-activity-widget')

# Loop through the divs and extract the data
data = []
for div in activity_divs:
    title = div.find('div', class_='pprofile-activity-widget__title')
    title = title.text if title else ''
    details = div.find('div', class_='pprofile-activity-widget__details pprofile-activity-widget__details--MT')
    details = details.text if details else ''
    results = div.find('div', class_='pprofile-activity-widget__results')
    results = results.text if results else ''
    data.append({'title': title, 'details': details, 'results': results})



# Write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data, f)


#, encoding='utf-8')
"""
a