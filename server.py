from flask import Flask, request
import wikipedia as wiki
import random
from math import floor
# from cockroach import Cockroach
from pony.flask import Pony
from pony.orm import *
from datetime import datetime
# import PIL
# app = Flask(__name__)
db_params = dict(provider='cockroach', user='rudransh', host='free-tier.gcp-us-central1.cockroachlabs.cloud', port=26257, database='shiny-wolf-1947.defaultdb', password = "mypassword")


app = Flask(__name__)
app.config.update(dict(
    DEBUG = True,
    PONY = db_params
))
Pony(app)


db = Database()
class User(db.Entity):
    # def __init__(self, table,userid, password, )
    
    _table_ = 'HAHA'
    user_id = PrimaryKey(str)
    password = Required(str)
    searchQ = Set('Search')

class Search(db.Entity):
  _table_ = 'NANA'
  # id = PrimaryKey(int)
  user = Required('User')
  searchText = Required(str)
  searchIntent = Required(str)
  imageLink = Required(str)
  searchKeyWord = Required(str)



sql_debug(True)  # Print all generated SQL queries to stdout
db.bind(**db_params)  # Bind Database object to the real database
db.generate_mapping(create_tables=True)  


@db_session  # db_session decorator manages the transactions
def add_values(userid, searchtext, searchintent, imagelink, searchkeyword):
  Search(user = User.get(user_id = userid), searchText = searchtext, searchIntent =searchintent, imageLink=imagelink, searchKeyWord = searchkeyword)

@db_session
def create_user(userid, password):
  User(user_id = userid, password = password, searchQ = None)




@app.route('/') # this is the home page route
def hello_world(): # this is the home page function that generates the page code
    return "Hello world!"

active_user = None

@app.route('/login', methods =  ["POST"])
def login():
  global active_user
  req = request.get_json(force = True, silent = True)
  # print(req.get('username'))
  try:
    user = User.get(user_id = req.get('username'))
    if not user:
      return "UserNotFound"
    # request.args
    # active_user = req.get('username')
    elif user.password != req.get('password'):
      return "WrongPassword"
    else:
      active_user = req.get('username')
      return "success"
  except Exception as e:
    return str(e)


@app.route('/wordcloud', methods = ['GET'])
def return_words():
  if not active_user:
    return "Sorry you need to be logged in to use this endpoint"
  else:
    a = select(s.searchKeyWord for s in Search if s.user.user_id == active_user)[:]
    a = list(a)
    return " ".join(a)

  
@app.route('/register', methods = ['POST'])
def signup():
  global active_user
  req = request.get_json(force = True, silent = True)  
  username = req.get('username')
  password = req.get('password')
  # print(user, password)
  try:
    user = User.get(user_id = username)
    if not user:
      print('i was here')
        # create_user(userid = user, password = password)
      User(user_id = username, password = password)
      active_user = username;
      return "SUCESSS, Your ID is created"
    else:
      return "FALIURE, Your ID was already taken"
  except Exception as e:
    return str(e)



def ProperNounExtractor(text):
    # Importing the required libraries
    import nltk 
    from nltk.corpus import stopwords 
    # from nltk.tokenize import word_tokenize, sent_tokenize
    print('PROPER NOUNS EXTRACTED :')
    ans = []
    sentences = nltk.sent_tokenize(text)
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        words = [word for word in words if word not in set(stopwords.words('english'))]
        tagged = nltk.pos_tag(words)
        for (word, tag) in tagged:
            if "NN" in tag: # If the word is a proper noun
                ans.append(word)
                print(word)
    return ans

@app.route('/test')
def hola():
  # create_user('1', 2)
  # return wiki.summary('Daisy', sentences = 2, auto_suggest= False)
  # return test()
  
  


  
  return x
  
  test()
  test()
  # Search()
  print(active_user)
  return 'added'

def numberOfCases(state):
  url = "https://coronaclusters.in/{state}".format(state = state)
  from requests_html import HTMLSession
  print(url)
  session = HTMLSession()
  response = session.get(url)
  raw_reponse = response.html.find('.card ')
  x = [" ".join(x.text.split('\n')) for x in raw_reponse[:4]]
  conf, act,rec, dea = x
  return (conf, act,rec, dea)
  



def PlanADayacation(begin, end):
  url = "https://api.distancematrix.ai/maps/api/distancematrix/json?origins={begin}&destinations={end}&key=uWau1hZ5fdlHk6azyDkLRlp8rjKJo".format(begin = begin, end = end)
  import requests
  resp = requests.get(url)
  res = resp.json().get("rows")[0]
  distance = res.get("elements")[0].get("distance").get("text")
  duration = res.get("elements")[0].get("duration").get("text")
  secs = res.get("elements")[0].get("duration").get("value")
  destinationState = resp.json()["destination_addresses"][0].split(",")[1].lower().strip()
  originState = resp.json()["origin_addresses"][0].split(",")[1].lower().strip()
  print(destinationState,originState )
  if " " in originState:
    originState = "-".join(originState.split(" "))
  if " " in destinationState:
    destinationState = "-".join(destinationState.split(" "))
  print(destinationState,originState )

  
  casesFrom = numberOfCases(destinationState)
  casesTo = numberOfCases(originState)
  
  return_text = "It is not advised to travel at this moment. However, these are some stats to help you make your decision. \n The distance between {begin} and {end} is {distance}. It will take you about {time} to reach there. There are about {casesfrom} from the place you are beginning your journey. There are about {casesto} in the place you are going. Wear your mask and follow the guidelines carefully".format(begin = begin, end = end, distance = distance, time = duration, casesfrom = casesFrom, casesto = casesTo)

  return return_text

  



  


def HowManyCases(country):
  url = "https://api.covid19api.com/live/country/{country}/status/confirmed/date/2021-07-16".format(country = country)
  import requests

  resp = requests.get(url)
  res = resp.json()[0]
  confirmed = res.get("Confirmed")
  deaths = res.get("Deaths")
  recovered = res.get("Recovered")
  active = res.get("Active")
  return_text = "The case statistics of {country} is as follows \n Confirmed Cases={confirmed} \n Number of Deaths = {deaths} \n Number of People recovered = {recovered}\n Number of active cases= {active}".format(country = country, confirmed = confirmed, deaths= deaths, recovered = recovered, active = active)

  return return_text
  


def IsItSafe_Country(country):
  url = "https://travel.state.gov/content/travel/en/traveladvisories/traveladvisories/{country}-travel-advisory.html".format(country = country) 
  from requests_html import HTMLSession
  print(url)
  session = HTMLSession()
  response = session.get(url)
  raw_reponse = response.html.find('.tsg-rwd-emergency-alert-text', first= True).text
  # processed_response = featured_snippets_handler(raw_reponse)
  print(raw_reponse)
  data = raw_reponse.split(".")
  if "Do not travel" in " ".join(data[:2]):
    return ". ".join(data[:2])
  else:
    idx = [i for i, v in enumerate(data) if "Country Summary" in v]
    # print(idx)
    # print(len(data))
    if len(idx)<1:
      return ". ".join(data[:2])
    return_text = data[:2] + data[idx[0]:idx[0]+4] 
    
    # print(raw_reponse)
    return ". ".join(return_text)

    
def try_add_values(userid, searchtext, searchintent, imagelink, searchkeyword):
  try:
    add_values(userid = active_user, searchtext = searchtext,searchintent= searchintent,  imagelink = "yoImage", searchkeyword = searchkeyword)
    return "Added"
    
  except Exception as e:
    if "Attribute" in str(e):
      return "Not Log In"




@app.route('/webhook', methods=['POST'])
def webhook():

  returnText = "Ooops, Something Went Wrong"
  theWhatIntentReturnText = ""
  try:
    req = request.get_json(force = True, silent = True)

    res = req.get('queryResult')
 
    # print(searchKeyword)
    intent = req.get('queryResult').get("intent").get('displayName')
    if intent == "IsItSafeIntentCountry":
      searchtext = res.get("queryText")
      searchKeyword = res.get("parameters").get("geo-country")
      return_text = IsItSafe_Country(searchKeyword.lower())
      text = try_add_values(userid = active_user, searchtext = searchtext, searchintent = intent, searchkeyword = searchKeyword, imagelink = "yo")
      if text == "Not Log In":
        return {
            "fulfillmentText": "Sorry but you need to log in first",
            "source":"webhook"
          }
      else:
        # return_text = IsItSafe_Country(searchKeyword)
        return {
            "fulfillmentText": return_text,
            "source":"webhook"
          }
      
      
    # print("Control def not here not here")
    
    if intent == "HowManyCasesCountry":
      # print('here')
      searchtext = res.get("queryText")
      searchKeyword = res.get("parameters").get("geo-country")
      return_text = HowManyCases(searchKeyword.lower())
      text = try_add_values(userid = active_user, searchtext = searchtext, searchintent = intent, searchkeyword = searchKeyword, imagelink = "yo")
      if text == "Not Log In":
        return {
            "fulfillmentText": "Sorry but you need to log in first",
            "source":"webhook"
          }
      else:
        return {
            "fulfillmentText": return_text,
            "source":"webhook"
          }

    if intent == "IWantToTravelindia":
      res = req.get('queryResult')
      searchtext = res.get("queryText")
      searchKeyword1 = res.get("parameters").get("geo-city")
      searchKeyword2 = res.get("parameters").get("geo-city1")
      
      
      return_text = PlanADayacation(searchKeyword1, searchKeyword2)
      text = try_add_values(userid = active_user, searchtext = searchtext, searchintent = intent, searchkeyword = searchKeyword1+searchKeyword2, imagelink = "yo")
      if text == "Not Log In":
        return {
            "fulfillmentText": "Sorry but you need to log in first",
            "source":"webhook"
          }
      else:
        return {
            "fulfillmentText": return_text,
            "source":"webhook"
          }



      
      
    
      return {
          "fulfillmentText": returnText,
          "source": 'webhook'
      }

    
  except Exception as e:
    print("def not here")
    return {
        "fulfillmentText": str(e),
        "source": 'webhook'
    }
  print("hell not here")
  
  return {
        "fulfillmentText": 'Something is probably wrong',
        "source": 'webhook'
    }
   
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080) # This line is required to run Flask on repl.it
