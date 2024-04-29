"""
Download MP3 files from a webpage
"""
import re
import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage containing MP3 links
BASE_URL = 'https://svenskadagfordag.se/ljud/ljud-svenska-dag-for-dag-d/vecka-{}-{}'
urls = [BASE_URL.format(i, j) for i in range(1, 10) for j in ['d', 'hoeroevningar-d']]

# Fetch the webpage content
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all MP3 hyperlinks on the page
    for link in soup.find_all('a', href=re.compile(r'http.*\.mp3')):
        mp3_url = link['href']
        filename = mp3_url.split('/')[-1]  # Extract the filename from the URL
        mp3_content = requests.get(mp3_url).content

        # Save the MP3 content to a local file
        with open(filename, 'wb') as mp3_file:
            mp3_file.write(mp3_content)

        print(f"Downloaded: {filename}")

    print("All MP3 files of downloaded successfully!")
