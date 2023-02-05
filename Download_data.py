import requests
from bs4 import BeautifulSoup

def get_data():

    url = "https://ztm.gda.pl/rozklady"

    response = requests.get(url)

    if response.status_code==200:

        soup = BeautifulSoup(response.text, "html.parser")

        route_list = soup.find_all("ul", class_="route-type-list")

        return route_list
    else:
        return False




