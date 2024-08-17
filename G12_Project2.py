## Python Project-2 

# Importing requirements
import json
import requests
import csv
#############################################################

# Purpose: A function to read the urls.txt file in text mode.
# Parameters: The name of the file with its extention.
# Returns: A list containing the urls as individual elements.
def read_file(fileName): 
    file = open(fileName,"r")
    return ([x.rstrip() for x in file.readlines()])
#############################################################

# Purpose: A function to request the json data for the url given.
# Parameters: A list of url's that we need the json data of.
# Returns: A list of usable python objects converted using json functions.

def request_data(url_list):
    py_objects = []
    for url in url_list:
        response = requests.get(url)
        mlb_json = json.loads(response.text)
        json_str = json.dumps(mlb_json)
        py_object = json.loads(json_str)
        py_objects.append(py_object)
    return (py_objects)
#############################################################

# Purpose: A minor function that requests the game data using the PK ID and pre-existing functions.
# Parameter: The game_pk ID to be requested, passed as a string.
# Returns: Calls the request_data function, with the url as a list for that function. Returns py_object of a particular game.
def request_game_data(game_pk):

    game_url = 'https://statsapi.mlb.com/api/v1/game/' + game_pk + '/content'
    return(request_data([game_url]))
#############################################################

# Purpose: Function that is used to create our .csv file.
# Parameter: Rows of csv data that has to be written as a nested list.
def csv_writer(row_data):
    with open('MLBData.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Date','Home Team', 'Away Team', 'Game PK', 'Headline', 'MP4'])
        writer.writerows(row_data)
#############################################################

# Purpose: The main function that processes the python object data to retreive embedded info.
def extract_data():

    # Initialising an empty list for storing rows of data for the .csv
    data_rows = []

    # Reading the urls.txt file, requesting json data for each url, returns list with python objects for each url.
    multiple_days_data = request_data(read_file('urls.txt'))

    # Iterates through any number of days of data
    for single_day_data in multiple_days_data:

        # Retreiving the number of games for the specific day so we can iterate accordingly
        total_games = (single_day_data['dates'][0]['totalGames'])

        # Date of the game day (Remains same for all the no. of games for the day. Hence, remains out of the following for loop)
        date = (single_day_data['dates'][0]['date'])

        # Indexes through the python object data for the specific day, indexes through all the games for the day; extracting needed info
        for game in range(total_games):

            # Game PK ID for the specific game
            game_pk = (single_day_data['dates'][0]['games'][game]['gamePk'])

            # Away team name- for the specific game
            away_team = (single_day_data['dates'][0]['games'][game]['teams']['away']['team']['name'])

            # Home team name- for the specific game
            home_team = (single_day_data['dates'][0]['games'][game]['teams']['home']['team']['name'])

            # Retreiving a game's specific game data as a python object to be utilised for extracting highlight/ headline name and MP4 URL
            game_pk_pyobject = (request_game_data(str(game_pk)))

            # Highlight name taken through the game_pk_object
            headline = (game_pk_pyobject[0]['highlights']['highlights']['items'][0]['headline'])

            # The highlight's associated MP4 URL
            headline_url = (game_pk_pyobject[0]['highlights']['highlights']['items'][0]['playbacks'][0]['url'])

            # Getting all the details together in a list to be written as a row's data
            row_data = [date, home_team, away_team, game_pk, headline, headline_url]

            # Finally gets appended to the collection of rows.
            data_rows.append(row_data)

    # Function that is called with the collection of row's passed as an argument to be written into our output .csv file
    csv_writer(data_rows)

# Calling the main function
extract_data()

#########################################################################################################################