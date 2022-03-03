import requests
from bs4 import BeautifulSoup


class ThingsInformation:
    def getInformationOfThings(self: str, tag_id: str):
        response = requests.get(self, headers={'User-Agent': 'Mozilla/5.0'}).content
        parsed = BeautifulSoup(response, 'html.parser')
        return parsed.find('table', {'id': tag_id}).get_text()
