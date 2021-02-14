import json 
import random

#Function that returns random artist from given genre as parameter
def randomArtistFromGenre(genre):
    # Opening JSON file 
    f = open('static/genres.json',) 
    
    # returns JSON object as  
    # a dictionary 
    data = json.load(f) 
    
    # Closing file 
    f.close() 

    return random.choice(data[genre])