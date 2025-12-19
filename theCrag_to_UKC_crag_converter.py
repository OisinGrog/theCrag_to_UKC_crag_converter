from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import route_info
import routes_csv

def scrape_route(url):
    driver = set_up_scrape() 
    driver.get(url) 
    time.sleep(5)  # Wait for the page to load completely

    scraped_routes = driver.find_elements(By.CSS_SELECTOR, ".route[data-route-tick]")
    routes = []
    
    for route in scraped_routes:
        # Can be done using a csvreader but I'm not sure what method is the most efficient
        # The data-route-tick attribute contains a CSV string with a lot of good information including the child code of the route

        try:
            route_name = route.find_element(By.CLASS_NAME, "primary-node-name").text
        except exceptions.NoSuchElementException:
            print("No route name found. False route or attribute name has changed.")
            continue

        try:
            climb_type = route.find_element(By.CSS_SELECTOR, "span.tags").text
        except exceptions.NoSuchElementException:
            print("No climb type found, skipping...")

        try:        
            grade = route.find_element(By.CLASS_NAME, "r-grade").text
        except exceptions.NoSuchElementException:
            print("No grade found, skipping...")

        # No need to throw an error if no stars are found, just set to 0
        stars = len(route.find_elements(By.CLASS_NAME, "star"))

        try:
            height = route.find_element(By.CLASS_NAME, "attr").text
            height = height.split(',')[0].strip() # Get only the height part before any comma
        except exceptions.NoSuchElementException:
            print("No height found, skipping...")

        # Could be interesting to use chatgpt to alter the description to avoid plagerism
        # Can currently get all <p> elements within the description div, then remove any with class "fa"
        try:
            description = route.find_element(By.CSS_SELECTOR, "div.markdown.desc")
            paragraphs = description.find_elements(By.CSS_SELECTOR, "p")
            for p in paragraphs[:]:
                classes = (p.get_attribute("class") or "").split()
                if "fa" in classes:
                    paragraphs.remove(p)
            
            description = ""
            for p in paragraphs:
                description = description + p.text
        except exceptions.NoSuchElementException:
            print("No description found, skipping...")
 
        bolts = None # Preventing unbound variable error
        if climb_type == "Sport" or climb_type == "Mixed trad":
            try:
                bolts = route.find_element(By.CLASS_NAME, "bolts").text
            except exceptions.NoSuchElementException:
                print("No bolts found, skipping...")

        try:
            fa = get_fa(route)
        except exceptions.NoSuchElementException:
            print("No FA info found, skipping...")
 
        pitches = None # Preventing unbound variable error
        if climb_type != "Boulder":
            pitches = 1  # Default to 1 pitch
            try:
                attr = route.find_element(By.CLASS_NAME, "attr")
                pitches = attr.find_element(By.CSS_SELECTOR, ".title [title]").text
            except exceptions.NoSuchElementException:
                print("No pitches found, skipping...")
        
        route_obj = route_info.Route(
            name=route_name,
            climb_type=climb_type,
            grade=grade,
            stars=stars,
            height=height,
            pitches=pitches,
            description=description,
            bolts=bolts,
            fa=fa
        )

        routes.append(route_obj)
        print("Added route: ", route_name)

    return routes
    
def set_up_scrape():
    options = webdriver.ChromeOptions()
    
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--log-level=3")  # Suppress logs
    options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")

    service = Service(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=options)
    return driver

def get_fa(route):
    fas = route.find_elements(By.CLASS_NAME, "fa")
    fa_obj = route_info.FAInfo(None, None, None)

    for element in fas:
        this_what = element.find_element(By.CLASS_NAME, "fa__what").text
        
        # Default FA info is the first entry in the list
        what = this_what
        who = element.find_element(By.CLASS_NAME, "fa__who").text
        when = element.find_element(By.CLASS_NAME, "fa_when").text

        # 2nd priority is FFA
        if this_what == "FFA:":
            what = this_what
            who = element.find_element(By.CLASS_NAME, "fa__who").text
            when = element.find_element(By.CLASS_NAME, "fa_when").text
        
        # 1st priority is FA
        elif this_what == "FA:":
            what = this_what
            who = element.find_element(By.CLASS_NAME, "fa__who").text
            when = element.find_element(By.CLASS_NAME, "fa_when").text

        fa_obj = route_info.FAInfo(what, who, when)
    
    if fa_obj.what is None:
        return None
    return fa_obj

if __name__ == "__main__":
    #url = "https://www.thecrag.com/en/climbing/australia/wollongong/area/11374129023"
    #url = "https://www.thecrag.com/en/climbing/australia/wollongong/area/11373956388"
    url = "https://www.thecrag.com/en/climbing/australia/blue-mountains/ikara-head"
    routes_csv.write_to_csv(scrape_route(url), "scraped_routes.csv")

