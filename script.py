import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os

# List of orators
orators = [
    "Jean Paul Ago", "Tobias Lütke", "Jeff Bezos", "Doug Warner", "Scott Cook",
    "Arancha Gonzalez", "Jeff Bezos", "Jack Ma", "Jamie Ross", "Marcus Sheridan",
    "John Rampton", "Richard Branson", "Jeff Eisenberg", "Craig Davis", "Pawel Grabowski",
    "Hil Davis", "Joel Anderson", "Benjamin Cohen", "Raj Aggarwal", "Steve Wynkoop",
    "Seth Godin", "John Rampton", "Katrina Lake", "Elon Musk", "Ashton Kutcher",
    "Ian Schafer", "Kunal Bahl", "Ken Goldstein", "Bill Gates", "Eric Fulwiler"
]

# Google search URL
search_url = "https://www.google.com/search?tbm=isch&q="

# Create directory to save images
if not os.path.exists('orator_images'):
    os.makedirs('orator_images')

for orator in orators:
    # Search for the orator on Google Images
    response = requests.get(search_url + orator)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the first image result
    img_tags = soup.find_all('img')
    if img_tags:
        img_url = img_tags[1]['src']
        
        # Download the image
        img_response = requests.get(img_url)
        img = Image.open(BytesIO(img_response.content))

        # Save the image
        img_name = f'orator_images/{orator.replace(" ", "_")}.jpg'
        img.save(img_name)
        print(f'Saved image for {orator}')
    else:
        print(f'No image found for {orator}')
