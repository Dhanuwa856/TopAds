from bs4 import BeautifulSoup
import requests
import pandas as pd


# Base Url of the website
base_url= "https://geebo.com/rentals-roommates/list/property/9-homes-/mobile//page/{}"


# Number of pages to scrape
num_pages = 10

# Initialize lists
titles = []
locations = []
prices = []
types = []
descriptions = []
urls = []
infos =[]


# Iterate over each page
for page_num in range(1,num_pages+1):
  url = base_url.format(page_num)
  
  # Send a GET request to the page URL
  response = requests.get(url)
  soup = BeautifulSoup(response.text,"html.parser")
  
  # Properties List
  property_list = soup.find_all("table",class_="element")
  
  # Extract data from each property item
  
  for items in property_list:
    # Title
    title = items.find("a",class_="title")
    # title available 
    if title == []:
      title_available = "Title Not Available"
    else:
      title_available = "Title Available"
      
    for title_list in title:
      main_title = title_list.text.strip()
  
    if title_available == "Title Not Available":
     title_set = "Title Not Available"
    elif title_available == "Title Available":
     title_set = main_title
    # print("Title :",title_set) 
    titles.append(title_set)
    
    # location
    location = items.find("span",class_="location")
    
    # location available
    if location == []:
     location_available = "Location Not Available"
    else:
      location_available = "Location Available"
      
    for location_list in location:
      main_location = location.text.strip()
    
    
    if location_available == "Location Not Available":
      location_set = "Location Not Available"
    elif location_available == "Location Available":
      location_set = main_location
    # print("Location :",location_set)  
    locations.append(location_set)
    
    # Price
    price = items.find("div",class_="price")
    
    # Price Available
    if price == []:
      price_available = "Price Not Available"
    else:
      price_available = "Price Available"
    
    for price_list in price:
      main_price = price_list.text.strip()
    
    if price_available == "Price Not Available":
      price_set = "Price Not Available"
    elif price_available == "Price Available":
      price_set = main_price
    # print("Price :",price_set)  
    prices.append(price_set)
    
    # type 
    type = items.find("strong",class_="type_date")
    
    # type available
    if type == []:
      type_available = "Type Not Available"
    else:
      type_available = "Type Available"
    
    for type_list in type:
      type_main = type_list.text.strip()
    
    if type_available == "Type Not Available":
      type_set = "Type Not Available"
    elif type_available == 'Type Available':
      type_set = type_main
    # print("Type :",type_set)  
    types.append(type_set)
    
    # description
    description = items.find("div",class_="brief")
    span = description.find("span")
    
    # description available
    
    if span == []:
      description_available = "Description Not Available"
    else:
      description_available = "Description Available"
    
    for span_list in span:
      main_description = span_list.text.strip()
    
    if description_available == "Description Not Available":
      description_set = "Description Not Available"
    elif description_available == "Description Available":
      description_set = main_description
    # print("Description:",description_set)  
    descriptions.append(description_set)
    
    
    # get item url
    
    item_url = title["href"]
    urls.append(item_url)
    
    # item page 
    
    item_page_response = requests.get(item_url)
    item_page_soup = BeautifulSoup(item_page_response.text,"html.parser")
    
    # Info
    
    info = item_page_soup.find_all("table",class_="info")
    
    for info_list in info:
     ul_elements = info_list.find_all("ul")

# Extract the text content of each <li> element and store it in a list
     li_texts = [li.text.strip() for li in ul_elements]

# Join the list elements with a comma to create a comma-separated string
     comma_separated_string = ", ".join(li_texts)

    # print("Info :",comma_separated_string)
    infos.append(comma_separated_string)
   
# Create a DataFrame from the collected data
data = {"Title": titles, "Price": prices, "Description": descriptions,"Location":locations, "Type":types,"url":urls,"Info":infos}
  
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
df.to_excel("geebo.xlsx",index=False)
print("Data successfully exported to geebo.xlsx")
  

 
    
    
      
    


     

  

