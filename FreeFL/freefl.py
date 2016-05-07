from bs4 import BeautifulSoup

import requests

U_AGENT = "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MHC19J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.105 Mobile Safari/537.36"
MOBILE_HEADERS = {'user_agent':U_AGENT}
LOCATION_URL = 'http://m.countdown.tfl.gov.uk/stopsNearLocation/'
SEARCH_URL = 'http://m.countdown.tfl.gov.uk/search/'
ARRIVALS_URL = 'http://m.countdown.tfl.gov.uk/arrivals/'

class BusInfo():
    def __init__(self,_id,_name):
        self.id = _id
        if not _name:
            info = BeautifulSoup(requests.get(ARRIVALS_URL+_id).text,
                                 'html.parser').find('span','stopInfo')
            self.name = info.string.strip().replace('\n','').replace('\t','') #This is awful
        else:
            self.name = _name

    @staticmethod
    def search(search_string):
        dat = requests.get(SEARCH_URL,
                           params={'searchTerm', search_string}).text
        soup = BeautifulSoup(dat,'html.parser')
        if dat.find(id="placeList") is not None:
            #Interpreted as a geographic name by TFL, returns a list of ids to narrow down from
            #The user has to pick one, so give them the name and the ids
            matches = soup.find(id="placeList").find_all('a')
            results = {match.string:match.get('href').split('/')[-1] for match in matches}
            # TODO: Sometimes there's more than 1 page of results...
        else:
            # Showing stops near the location, return a list of possible ids
            matches = soup.find_all('tr')
            results = {}
            for match in matches:
                _id = match.get('id').split('-')[-1]
                info = match.find('td','information')
                name = info.a.string.strip() + ' ' + info.span.string
                routes = info.find(id='stopPoint'+'-'+_id+'-routes').string.strip()
                results[_id] = {'name':name,'route':routes}
            return results

    @staticmethod
    def search_by_location_id(_id):
        dat = BeautifulSoup(requests.get(LOCATION_URL+_id).text, 'html.parser')
        matches = dat.find_all('tr')
        results = {}
        for match in matches:
            _id = match.get('id').split('-')[-1]
            info = match.find('td','information')
            name = info.a.string.strip() + ' ' + info.span.string
            routes = info.find(id='stopPoint'+'-'+_id+'-routes').string.strip()
            results[_id] = {'name':name,'route':routes}
        return results

    # @staticmethod
    # def search_by_coordinates(lat,lon):
    #     pass

    def get_live_data(self):
        """Return a list of dicts with data about each upcoming bus."""
        dat = requests.get(ARRIVALS_URL+self.id)
        soup = BeautifulSoup(dat.text,'html.parser')
        arrivals = [el.find_all('td') for el in soup.find_all('tr')[1:]]
        busses = []
        for bus in arrivals:
            busses.append({el.get('class')[0]:el.string.strip() for el in bus})
        return busses
