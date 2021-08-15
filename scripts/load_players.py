from players.models import Player
import requests

def run():
    
    response = requests.get('https://www.easports.com/fifa/ultimate-team/api/fut/item?page=1')
    total_pages = response.json()['totalPages']
    
    for i in range(1,total_pages+1):
        url = f'https://www.easports.com/fifa/ultimate-team/api/fut/item?page={i}'
        response_clycle = requests.get(url)
        players = response_clycle.json()['items']
        for player in players:
            
            try:
                Player.objects.get(name=player['firstName'], lastname=player['lastName'])
            except:
                p = Player(name=player['firstName'], lastname=player['lastName'], position=player['position'], nation=player['nation']['name'], team=player['club']['name'])
                p.save()