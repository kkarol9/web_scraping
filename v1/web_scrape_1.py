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
#data2 = []
for div in activity_divs:
    activity_divs2 = soup.find_all('div', class_='pprofile-activity-widget__results ')
    for div2 in activity_divs2:

        surname = div.find('span', class_='pprofile-activity-widget__last-name')
        surname = surname.text if surname else ''
        #name = div.find('span', class_='pprofile-activity-widget__first-name')
        #name = name.text if name else ''
        #score_all = div.find('div', class_='pprofile-activity-widget__result-status-text')
        #score_all = score_all.text if score_all else ''

    #score1 = div.find('li', class_='pprofile-activity-widget__score')
    #score1 = score1.text if score1 else ''

        data.append({'surname': surname}) #'name': name, 'score': score_all}) #'set 1': score1, 'score': score_all})
    #data2.append(data)

# Write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data, f)


"""
data = []
for div in activity_divs:
    surname = div.find('span', class_='pprofile-activity-widget__last-name')
    surname = surname.text if surname else ''
    name = div.find('span', class_='pprofile-activity-widget__first-name')
    name = name.text if name else ''
    score_all = div.find('div', class_='pprofile-activity-widget__result-status-text')
    score_all = score_all.text if score_all else ''
    all = div.find('span', class_='pprofile-activity-widget__last-name')
    all = all.text if all else ''
    #score1 = div.find('li', class_='pprofile-activity-widget__score')
    #score1 = score1.text if score1 else ''

    data.append({'surname': surname, 'name': name, 'score': score_all}) #'set 1': score1, 'score': score_all})
"""
