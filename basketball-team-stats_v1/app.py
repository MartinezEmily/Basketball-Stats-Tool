from constants import PLAYERS, TEAMS    # Importing constants file

def clean_data(data):   # Fix guardian, experience and height of each player data
    cleaned = []
    
    for player in data:
        fixed = {}
        # Keep the name of player
        fixed["name"] = player["name"] 
        print(player["email"])
        # Split guardian into a list
        fixed["guardian"] = player["guardians"].split(" and ")
        # Convert experience to boolean
        if player["experience"] == "YES":
            fixed["experience"] = True
        else:
            fixed["experience"] = False
        # Convert height to integer
        fixed["height"] = int(player["height"].split()[0])
    
        cleaned.append(fixed) 
    return cleaned


if __name__ == "__main__":              # Running app.py file directly

    cleaned_players = clean_data(PLAYERS)  # calling clean_data function
    print(cleaned_players)