# players


## 1. Cloning the repository
```
https://github.com/fabianMM04/players.git
```
## 2. go to the project and build with docker-compose
```
cd players
docker-compose build
```
## 3. Run the script to load data in postgres with docker-compose
```
docker-compose run api python manage.py runscript load_players
```
## 4. Run project with docker-compose
```
docker-compose up
```
## 5. API players
```
* GET: localhost:8000/api/v1/players
response: {"Page": 1, "totalPages": 1555, "Items": 10, "totalItems": 15548, "Players": [{"name": "C. Ronaldo", "position": "ST", "nation": "Portugal"}, {"name": "Luka", "position": "CM", "nation": "Croatia"}, {"name": "Lionel", "position": "CF", "nation": "Argentina"}, {"name": "Edson", "position": "CAM", "nation": "Brazil"}, {"name": "Neymar", "position": "CAM", "nation": "Brazil"}, {"name": "Luis", "position": "ST", "nation": "Uruguay"}, {"name": "Eden", "position": "LW", "nation": "Belgium"}, {"name": "Robert", "position": "ST", "nation": "Poland"}, {"name": "Marco", "position": "CAM", "nation": "Germany"}, {"name": "Diego", "position": "CAM", "nation": "Argentina"}]}


```
## 6. API team
```
* POST: localhost:8000/api/v1/team
  Header: Content-Type: application/json
  Body: {
    "Name": "",
    "Page": 3
  }
  Response: {"Page": 3, "totalPages": 1555, "Items": 10, "totalItems": 15546, "Players": [{"name": "Sergio", "position": "ST", "nation": "Argentina"}, {"name": "Fabio", "position": "ST", "nation": "Italy"}, {"name": "Christian", "position": "CAM", "nation": "Denmark"}, {"name": "Sadio", "position": "LW", "nation": "Senegal"}, {"name": "Gerard", "position": "CB", "nation": "Spain"}, {"name": "Karim", "position": "ST", "nation": "France"}, {"name": "Jadon", "position": "RM", "nation": "England"}, {"name": "Pierre-Emerick", "position": "ST", "nation": "Gabon"}, {"name": "Kalidou", "position": "CB", "nation": "Senegal"}, {"name": "Raheem", "position": "RW", "nation": "England"}]}
