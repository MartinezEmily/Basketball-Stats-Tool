from constants import PLAYERS, TEAMS    # Importing constants file


def clean_data(data):   # Clean guardian, experience, and height data of each player
    cleaned = []
    
    for player in data:
        fixed = {}
        # Keep the name of player
        fixed["name"] = player["name"] 
        print(player["name"])
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


def balance_teams(teams, players):    # Distribute players evenly across teams, balancing total number and experience
    experienced = []
    inexperienced = []

    for player in players:  # Create two categories: experienced vs inexperienced
        if player['experience'] == 'YES':
            experienced.append(player)
        else:
            inexperienced.append(player)

    # Experience level distribution
    experienced_players_per_team = len(experienced) // len(teams)   # 3 experienced players per team
    inexperienced_players_per_team = len(inexperienced) // len(teams)   # 3 inexperienced players per team

    # Distribute players evenly across teams
    balanced_teams = {}
    for team in teams:
        balanced_teams[team] = {'experienced': [], 'inexperienced': []}

    # Distribute experienced players evenly across teams
    while experienced:
        for team in teams:
            if experienced:
                balanced_teams[team]['experienced'].append(experienced.pop(0))

    # Distribute inexperienced players evenly across teams
    while inexperienced:
        for team in teams:
            if experienced:
                balanced_teams[team]['inexperienced'].append(inexperienced.pop(0))

    return balanced_teams

if __name__ == "__main__":              # Running app.py file directly

    cleaned_players = clean_data(PLAYERS)  # calling clean_data function
    print(cleaned_players)

    balanced_teams = balance_teams(TEAMS, cleaned_players)
    print(balanced_teams)
