# Opening a file consumes a system resource (file handle)

file = open("movie_data.txt", "w")

# Write data to the file
file.write("Movie data")

# Close the file to release the system resource
file.close()

# Context Manager automatically manages the file resource

with open("movie_data.txt", "w") as file:

    # Write data to the file
    file.write("Movie data")

# The file is automatically closed here,
# even if an error occurs inside the with block
import json,requests
API_URL = "http://www.omdbapi.com/"

# Movie Search
movie_name = input("Enter movie name: ")

# API Request
response = requests.get(API_URL, params={"query": movie_name})

# Data Fetch
movie_data = response.json()

# Save data to file using Context Manager
with open("movie_data.json", "w", encoding="utf-8") as file:

    json.dump(movie_data, file, indent=4)

# File is automatically closed here
