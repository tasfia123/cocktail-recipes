import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

import random

# COCKTAIL_API = os.getenv("COCKTAIL_API") -- NOT SURE WE NEED THIS

def liquor_type():
    liquor = input("Please select a liquor type: ")
    valid_selections = ["whiskey", "whisky", "beer", "port", "vermouth", "everclear", "absinthe", "cider", "brandy", "aperol", "wine", "gin", "vodka", "rum", "tequila"]
    if liquor not in valid_selections:
        print("OOPS, invalid liquor type. Please try again.")
        exit()
    else:
        print(f"SELECTED LIQUOR: '{liquor}'")
        
    
    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={liquor}"
    response = requests.get(request_url)
    liquor_data = json.loads(response.text)

    random_drink = liquor_data["drinks"][0]
    #random_drink = random.choice[]


    # for l in (liquor_data["drinks"]):
    #     valid_options = [l["strDrink"]]
    #     cocktail_choice = random.choice(valid_options)
    #     print("Cocktail choice:", cocktail_choice)
       #print(valid_options)

liquor_type()




# import webbrowser
# def cocktails():
#     cocktail_type = input("please select type of cocktail: ")
#     request_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_type}"
#     data = requests.get(request_url)
#     tt = json.loads(data.text)
    
    
#     for i in (tt["drinks"]):
#         print(i["strDrink"], "\n")
#         print(i["strInstructions"], "\n")
        
#         print(i["strIngredient1"])
#         print(i["strIngredient2"])
#         print(i["strIngredient3"])
#         print(i["strIngredient4"])
#         url = i["strDrinkThumb"]
#         webbrowser.open(url)
# cocktails()

## Send Email 
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
load_dotenv()

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDER_ADDRESS = os.environ.get("SENDER_ADDRESS", "OOPS, please set env var called 'SENDER_ADDRESS'")

client = SendGridAPIClient(SENDGRID_API_KEY) #> <class 'sendgrid.sendgrid.SendGridAPIClient>
print("CLIENT:", type(client))

subject = "This is the recipe for your cocktail, enjoy!"

html_content = "Cocktail Recipe"
print("HTML:", html_content)

message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS, subject=subject, html_content=html_content)

try:
    response = client.send(message)

    print("RESPONSE:", type(response)) #> <class 'python_http_client.client.Response'>
    print(response.status_code) #> 202 indicates SUCCESS
    print(response.body)
    print(response.headers)

except Exception as err:
    print("OOPS")
    print(type(err))
    print(err)
