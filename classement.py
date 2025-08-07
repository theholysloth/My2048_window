import numpy as np
import json
import random 
import init
import gestion_case

def classement(): 
    try : 
        with open('save_game.json', 'r') as f : 
            scores = json.load(f)
    except(FileNotFoundError, json.JSONDecodeError): 
        scores = []

    for i , data in enumerate(scores): 
        sorted_scores = sorted(scores, key=lambda x: x['score'], reverse=True)
        if i < 10:  
            print(f"{i+1}. {data['player_name']} - Score: {data['score']}")
        else:
            break
    if not scores:
        print("Aucun score enregistré.")
    return sorted_scores

