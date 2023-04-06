
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
data2 = []
for div in activity_divs:

    city = div.find('span', class_='pprofile-activity-widget__location pprofile-activity-widget__details-pair')
    city = city.text if city else ''

    nation = div.find('span', class_='pprofile-activity-widget__nation pprofile-activity-widget__details-pair')
    nation = nation.text if nation else ''

    tournament_type = div.find('span', class_='pprofile-activity-widget__tournament-type pprofile-activity-widget__details-pair')
    tournament_type = tournament_type.text if tournament_type else ''

    surface = div.find('span', class_='pprofile-activity-widget__surface')
    surface = surface.text if surface else ''

    draw = div.find('span', class_='pprofile-activity-widget__draw pprofile-activity-widget__details-pair')
    draw = draw.text if draw else ''

    type = div.find('span', class_='pprofile-activity-widget__type pprofile-activity-widget__details-pair')
    type = type.text if type else ''

    entry = div.find('span', class_='pprofile-activity-widget__entry pprofile-activity-widget__details-pair')
    entry = entry.text if entry else ''

    results_divs = div.find_all('div', class_='pprofile-activity-widget__results')
    #results = [divss.span for divss in results_divs]
    #results = results.text if results else ''
    for r in results_divs:
        round = div.find('span', class_='pprofile-activity-widget__round-inner')
        round = round.text if round else ''

        data2.append({'Round' : round})

    
    results_set_divs = div.find_all('div', class_='pprofile-activity-widget__result-status-text')
    results_set = [div_set.ol.text for div_set in results_set_divs]

    """
    -> zwraca samo Hard
    surface_tag = soup.find('span', {'class': 'pprofile-activity-widget__surface'})

    surface_tag = surface_tag.find('strong')
    surface = surface_tag.text
    """
    
    """


    results_divs2 = div.find_all('ol', class_='pprofile-activity-widget__set-scores')
    results2 = [divss2.text for divss2 in results_divs2]
"""




    data.append({'City': city, 'Nation' : nation, 'Tournament type': tournament_type, 'Surface' : surface,
                 'Draw' : draw, 'Type' : type, 'Entry' : entry, 'Set sccore:' : results_set, 'Round' : round})

data.append(dates)

# Write the data to data.json
with open('data.json', 'w') as f:
    json.dump(data, f)