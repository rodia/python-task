import requests
import json

HOST = 'https://montanaflynn-fifa-world-cup.p.rapidapi.com/'
TEAMS_TAG = 'teams'
ROUNDS_TAG = 'rounds'
GAMES_TAG = 'games'
PERSONS_TAG = 'persons'
GOALS_TAG = 'goals'

EXIT_OPTION = 6

options = [
  TEAMS_TAG,
  ROUNDS_TAG,
  GAMES_TAG,
  PERSONS_TAG,
  GOALS_TAG
]

headers = {
  'x-rapidapi-host': "montanaflynn-fifa-world-cup.p.rapidapi.com",
  'x-rapidapi-key': "f581c7d487msh83585873521a99dp1d7fdajsn6ccd71eccbea",
  'accepts': 'json'
}

def main():
  while True:
    print_menu()
    option = int(input('Igrese su opción: '))

    if option == EXIT_OPTION:
      break

    evaluate(option)
  ## teams = request_by_tag(TEAMS_TAG)

def print_menu():
  print('1. Mostrar todos los equipos')
  print('2. Mostrar todos las vueltas')
  print('3. Mostrar todos los juegos')
  print('4. Mostrar todos los jugadores')
  print('5. Mostrar todos los goles')
  print('6. Salir')

def evaluate(option):
  tag = options[option-1]

  data = request_by_tag(tag)

  if tag == TEAMS_TAG:
    print_teams(data)
  elif tag == ROUNDS_TAG:
    print_rounds(data)
  elif tag == GAMES_TAG:
    print_games(data)
  elif tag == PERSONS_TAG:
    print_persons(data)
  elif tag == GOALS_TAG:
    print_goals(data)
  else:
    print('Opción no válida')

def print_teams(data):
  for element in data:
    print ('{:<4} {:<30} {:<10}'.format(element["id"], element["title"], element["club"], '|'))

def print_rounds(data):
  for element in data:
    print ('{:<4} {:<30} {:<10} {:<10}'.format(element["id"], element["title"], element["start_at"], element["end_at"], '|'))

def print_games(data):
  teams = request_by_tag(TEAMS_TAG)
  for element in data:
    team_a = next(data for data in teams if data["id"] == element["team1_id"])
    team_b = next(data for data in teams if data["id"] == element["team2_id"])
    result = "Result {} - {}".format(element["score1"], element["score2"])
    print ('{:<4} {:<20} {:<20} {:<10}'.format(element["id"], team_a["title"], team_b["title"], result, '|'))

def print_persons(data):
  for element in data:
    print ('{:<4} {:<30} {:<10}'.format(element["id"], element["name"], element["nationality_id"], '|'))

def print_goals(data):
  persons = request_by_tag(PERSONS_TAG)
  games = request_by_tag(GAMES_TAG)
  teams = request_by_tag(TEAMS_TAG)
  for element in data:
    person = next(data for data in persons if data["id"] == element["person_id"])
    game = next(data for data in games if data["id"] == element["game_id"])
    team = next(data for data in teams if data["id"] == element["team_id"])
    print ('{:<20} {:<20} {:<20} {:<4}'.format(person["name"], game.get("title", ""), team.get("title", ""), element["score1"], '|'))

def request_by_tag(tag):
  url = HOST + tag
  response = requests.request("GET", url, headers=headers)

  return json.loads(response.text)

if __name__ == '__main__':
  main()
