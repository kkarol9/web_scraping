import json
from bs4 import BeautifulSoup

# read index.html file and parse with Beautiful Soup
with open('index.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# find all div elements with class="pprofile-activity-widget"
widgets = soup.find_all('div', class_='pprofile-activity-widget')

# process each widget
data = []
data2 = []

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

        rezka = result_widget.find('span', class_='pprofile-activity-widget__results-inner')
        rezka = rezka.text if rezka else ''

        # append the data to the list
        data.append({
            'surname': surname,
            'first_name': first_name,
            'results': rezka,
            'score' : results 
        })
    data2.append({
        'title': title,
        'details': details,
        'score' : data

 })

# write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data2, f)



