# Python Project 2: MLB Game Data Extraction

## Description
This project is a Python application designed to retrieve and process Major League Baseball (MLB) game data from the MLB Stats API. The application reads URLs from a text file, fetches JSON data from the specified URLs, and processes the data to extract specific information. The extracted data is then saved to a CSV file for easy access and analysis.

This project builds on concepts introduced in a previous JavaScript project (INFO-6144) but is implemented entirely in Python. The focus is on handling JSON data, navigating complex Python dictionaries, and generating output files in CSV format.

## Objective
The main goals of this project are:
1. Fetch JSON data from a list of URLs.
2. Process the data to extract relevant information about MLB games.
3. Save the processed data to a CSV file.

## Requirements
- Python 3.x
- `requests` library for making HTTP requests.
- A text file named `urls.txt` containing URLs to fetch the data from.
- Internet connection to access the MLB Stats API.

## Setup
1. Install the required Python library using pip:
   ```bash
   pip install requests
   ```
2. Place the `urls.txt` file in the same directory as this script.
3. Ensure the `urls.txt` file contains valid URLs pointing to MLB Stats API endpoints.

## Usage
1. Run the Python script using the command:
   ```bash
   python G12_Project2.py
   ```
2. The script will:
   - Read URLs from the `urls.txt` file.
   - Fetch JSON data from each URL.
   - Extract specific game-related information, including the date, home team, away team, game ID (PK), headline, and MP4 URL.
   - Save the extracted data to a CSV file named `MLBData.csv`.

## Code Explanation

### Functions
- **`read_file(fileName)`**:
  - Reads the `urls.txt` file and returns a list of URLs.
- **`request_data(url_list)`**:
  - Takes a list of URLs and returns a list of Python objects (dictionaries) containing the JSON data.
- **`request_game_data(game_pk)`**:
  - Requests detailed game data using the game's PK ID.
- **`csv_writer(row_data)`**:
  - Writes the extracted data to a CSV file named `MLBData.csv`.
- **`extract_data()`**:
  - The main function that orchestrates reading URLs, fetching data, extracting relevant information, and writing it to a CSV file.

### Example `urls.txt` File
The `urls.txt` file should contain one URL per line, pointing to the MLB Stats API for a specific game day. Example:
```
https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2023-08-01
https://statsapi.mlb.com/api/v1/schedule?sportId=1&date=2023-08-02
```

### CSV Output
The script generates a CSV file named `MLBData.csv` with the following columns:
- Date
- Home Team
- Away Team
- Game PK
- Headline
- MP4

Each row in the CSV file represents a specific MLB game and its associated data.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## References
- [MLB Stats API](https://statsapi.mlb.com/)
- [JSON in Python](https://docs.python.org/3/library/json.html)
