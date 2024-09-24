import requests
from bs4 import BeautifulSoup

def web_scrape(rashifal):
    print(rashifal)
    url = f"https://www.hamropatro.com/rashifal/daily/{rashifal}"
    
    print(f"Fetching URL: {url}")
    response = requests.get(url)
    
    if response.status_code == 200:
            
        # Parsing the HTML Content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Finding the Rashifal 
        rashifal_entry = soup.find('h2', class_='maintitle')
        
        if rashifal_entry:
            # Extracting the Title
            title = rashifal_entry.find('span').text.strip()
            
            # Extracting the description of the respective rashifal
            desc_div = soup.find('div', class_='desc')
            description = desc_div.find('p').text.strip() if desc_div else "Description NOT FOUND"
            
            with open('output.txt', 'a', encoding='utf-8') as f:
                f.write(f"Title: {title}\n")
                f.write(f"Description: {description}")  
                f.write("\n")
        else:
            print(f"Could not find Rashifal for {rashifal}.")
    else:
        print(f"Failed to retrieve the webpage for {rashifal}. Status code: {response.status_code}")

print("Script started")
# Ask the user for their zodiac sign
sign = input("Enter your zodiac sign (e.g., Mesh, Singha): ").strip()
web_scrape(sign)
