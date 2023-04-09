import re
import json
from PyMovieDb import IMDB

class MyIMDB:
    def __init__(self):
        self.ratings = {}
        self.imdb = IMDB()

    def getRatting(self, titulo):
        
        print("getRatting() " + titulo)

        jsonText = self.imdb.get_by_name(titulo)
        myDict = json.loads(jsonText)
        
        rating = 0
        if "rating" in myDict:
            if (myDict["rating"]["ratingValue"] != None):
                rating = myDict["rating"]["ratingValue"]
        

        return str(rating)