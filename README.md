# fetch-entrepreneur-images
A script that fetches a collection of images 

Python script using the `requests` and `BeautifulSoup` libraries to scrape images of the 30 orators listed in the table. Additionally, the script uses `Pillow` to save the images. For this example, we will use Google Images to find the orators' images.

To get started, you need to install the necessary packages:

```bash
pip install requests beautifulsoup4 pillow
```

Here is the Python script:

```python
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
```

### Explanation:

1. **Import Libraries**: The script imports `requests` for making HTTP requests, `BeautifulSoup` from `bs4` for parsing HTML, `Image` and `BytesIO` from `Pillow` for handling image data, and `os` for directory operations.
2. **Orators List**: A list of the orators whose images need to be scraped.
3. **Google Search URL**: The base URL for Google Image search queries.
4. **Create Directory**: Checks and creates a directory named `orator_images` to store the images.
5. **Scraping Loop**:
   - The script loops through each orator name, constructs the search URL, and requests the Google Images search results page.
   - It parses the HTML to find image tags and extracts the URL of the first image result.
   - Downloads the image and saves it using the `Pillow` library.

### Notes:
- Google might block automated requests, so for a production scenario, consider using a more sophisticated approach with error handling, request throttling, or using an API service for image search.
- The script assumes the second `img` tag contains the desired image, which might not always be the case. You might need to refine the selection logic based on actual Google Images HTML structure.

Ensure you run this script in an environment where scraping Google is permissible, and consider adding user-agent headers or using services that respect search engines' terms of service.
