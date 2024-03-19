import requests
from flask import request
from bs4 import BeautifulSoup 
from flask import Flask   
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r'/*': {"origins": '*'}})

#Get the External links from the Url Page 
#Create an endpoint to receive POST requests
@app.route('/Scraping', methods=['POST'])
def get_external_links(): # WHEN A POST REQUEST IS MADE ON THE URL http://127.0.0.1:5000/Scraping THE get_external_links() IS TRIGGERED  
    try:
        url = request.json.get('url')  # GET THE URL FROM THE REQUEST BODY

        # MAKE A GET REQUEST TO THE PROVIDED URL 

        response = requests.get(url) # THE CODE  MAKES A GET REQUEST TO THE PROVIDED URL USING `requests` LIBRARY

        # PARSE THE HTML CONTENT USING BeautifulSoup , THE PURPOSE OF PARSE IS TO TAKE INPUT DATA AND CONVERT IT INTO A STRUCTURE FORM   
        soup = BeautifulSoup(response.content, 'html.parser') # THE PURPOSE OF BEAUTIFULSOUP IS FOR SCRAPING THE DATA FROM THE HTML AND XML FILE 

        # FINDS ALL THE ANCHOR TAG ON THE PAGE AND ITERATE THROUGH THEM
        all_links = soup.find_all('a')

        external_links = []
        for link in all_links:
            href = link.get('href')
            if href:
                if url not in href and not href.startswith('#'):
                        if not href.startswith('https://'):
                            external_links.append(href)

        return {'external_links': external_links}, 200

    except Exception as e:
        return {'error': str(e)}, 500
    

    
if __name__ == "__main__":
    app.run(debug=True, port=5000)