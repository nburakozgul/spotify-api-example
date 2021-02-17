import json 
import random

#Function that returns random artist from given genre as parameter
def randomArtistFromGenre(genre):
    # Opening JSON file 
    f = open('spotify/static/genres.json',) 
    
    # returns JSON object as  
    # a dictionary 
    data = json.load(f) 
    
    # Closing file 
    f.close() 

    if genre in data:
        return random.choice(data[genre])
    else:
        return None