import numpy as np
import json
import random 
import init
import gestion_case

def classement(): 
    i = 0
    try : 
        with open('save_game.json', 'r') as f : 
            scores = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError): 
        scores = []

    sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
    #print(sorted_scores)

    while i < 10 and i < len(sorted_scores):   
        print(f"{i+1}. {sorted_scores[i]['player_name']} - Score: {sorted_scores[i]['score']}")
        i += 1
    if not scores:
        print("Aucun score enregistré.")
    return sorted_scores

classement()  