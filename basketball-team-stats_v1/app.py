from constants import PLAYERS, TEAMS    # Importing constants file


def clean_data(data):   # Clean guardian, experience, and height data of each player
    cleaned = []
    
    for player in data:
        fixed = {}
        # Keep the name of player
        fixed["name"] = player["name"] 
        print(player["name"])
        # Split guardian into a list
        fixed["guardians"] = player["guardians"].split(" and ")
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
        if player['experience']:
            experienced.append(player)
        else:
            inexperienced.append(player)

    # Calculate how many players each team should have, and how many from each category
    num_players_per_team = len(players) // len(teams) #  6 players per team
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
            if inexperienced:
                balanced_teams[team]['inexperienced'].append(inexperienced.pop(0))

    return balanced_teams


def display_team_stats(balanced_teams): # Display team stats
    print("\n *** Team Stats *** \n")

    for team, players in balanced_teams.items():
        total_players = len(players['experienced']) + len(players['inexperienced'])

        # Get all player names as a comma-separated string
        experienced_players_names = []
        for player in players['experienced']:
            experienced_players_names.append(player['name'])

        inexperienced_players_names = []
        for player in players['inexperienced']:
            inexperienced_players_names.append(player['name'])

        all_players_names = experienced_players_names + inexperienced_players_names
        all_players_names_str = ", ".join(all_players_names)

        # Count of experienced and inexperienced players
        experienced_count = len(players['experienced'])
        inexperienced_count = len(players['inexperienced'])

        # Calculate average height 
        total_height = 0
        for player in players['experienced'] + players['inexperienced']:
            total_height += player['height']

        average_height = total_height / total_players
        average_height = round(average_height, 2)

        # Get all guardians as a comma-separated string
        guardians = []
        for player in players['experienced'] + players['inexperienced']:
            for guardian in player['guardians']:
                guardians.append(guardian)

        guardians_str = ", ".join(guardians)

        print(f"Team: {team}")
        print(f"Total Players: {total_players}")
        print(f"Players: {all_players_names_str}")
        print(f"Number of Experienced Players: {experienced_count}")
        print(f"Number of Inexperienced Players: {inexperienced_count}")
        print(f"Average Height: {average_height}")
        print(f"Guardians: {guardians_str}\n")


if __name__ == "__main__":              # Running app.py file directly

    cleaned_players = clean_data(PLAYERS)  # Calling clean_data function
    print(cleaned_players)

    balanced_teams = balance_teams(TEAMS, cleaned_players)
    print(balanced_teams)

    display_team_stats(balanced_teams)