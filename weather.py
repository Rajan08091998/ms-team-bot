import requests

def weather(city):
    
    url = "https://weatherapi-com.p.rapidapi.com/current.json"

    querystring = {"q":f"{city}"}

    headers = {
        "X-RapidAPI-Key": "f4067b6c17msh27ff12ff8851761p1e5a91jsn84f68964b543",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json()
    
    text = ''
    try:
        text = (u'Current temperature in %s is %d℃' % (response['location']['name'], response['current']['temp_c']))
    except:    
        text = ('Please enter a valid city')



    return text
