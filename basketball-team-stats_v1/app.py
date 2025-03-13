from constants import PLAYERS, TEAMS    # Importing constants file


def clean_data(data):   # Clean guardian, experience, and height data of each player
    cleaned = []
    
    for player in data:
        fixed = {}
        # Keep the name of player
        fixed["name"] = player["name"]
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

    for player in players:  # Create two categories: experienced and inexperienced
        if player["experience"]:
            experienced.append(player)
        else:
            inexperienced.append(player)

    # Calculate how many players each team should have, and how many from each category
    num_players_per_team = len(players) // len(teams) #  6 players per team
    experienced_players_per_team = len(experienced) // len(teams)   # 3 experienced players per team
    inexperienced_players_per_team = len(inexperienced) // len(teams)   # 3 inexperienced players per team

    # Distribute players evenly across teams
    balanced_teams = {
        team: {
            "experienced": [], 
            "inexperienced": [],
            "total_experienced": 0,
            "total_inexperienced": 0,
            "average_height": 0
        } for team in teams 
    }

    # Distribute experienced players evenly across teams
    while experienced:
        for team in teams:
            if experienced:
                balanced_teams[team]["experienced"].append(experienced.pop(0))

    # Distribute inexperienced players evenly across teams
    while inexperienced:
        for team in teams:
            if inexperienced:
                balanced_teams[team]["inexperienced"].append(inexperienced.pop(0))

    # Set total_experienced, total_inexperienced, and average_height after distributing players to ensure accurate calculations.
    for team in teams:
        team_data = balanced_teams[team]
        team_data["total_experienced"] = len(team_data["experienced"])
        team_data["total_inexperienced"] = len(team_data["inexperienced"])

        # Calculate average height 
        total_height = 0
        for player in team_data["experienced"] + team_data["inexperienced"]:
            total_height += player["height"]

        team_data["average_height"] = round(total_height / num_players_per_team, 2)

    return balanced_teams

def display_team_stats(balanced_teams): # Display team stats
    print("\n *** Team Stats *** \n")

    for team, team_data in balanced_teams.items():
        total_players = len(team_data["experienced"]) + len(team_data["inexperienced"])

        # Sort players by height: experienced and inexperienced
        team_data['experienced'] = sorted(team_data['experienced'], key = lambda player: player['height'])
        team_data['inexperienced'] = sorted(team_data['inexperienced'], key = lambda player: player['height'])

        # Get all player names as a comma-separated string
        experienced_players_names = []
        for player in team_data["experienced"]:
            experienced_players_names.append(player["name"])

        inexperienced_players_names = []
        for player in team_data["inexperienced"]:
            inexperienced_players_names.append(player["name"])

        all_players_names = experienced_players_names + inexperienced_players_names
        all_players_names_str = ", ".join(all_players_names)

        # Count of experienced and inexperienced players
        experienced_count = len(team_data["experienced"])
        inexperienced_count = len(team_data["inexperienced"])

        # Get all guardians as a comma-separated string
        guardians = []
        for player in team_data["experienced"] + team_data["inexperienced"]:
            for guardian in player["guardians"]:
                guardians.append(guardian)

        guardians_str = ", ".join(guardians)




def show_menu(teams, balanced_teams):
    while True:
        print(""" BASKETBALL TEAM STATS TOOL
        --- Main Menu---
        A) Display Team Stats
        B) Quit
        """)

        choice = input("Enter an option:    ").upper()

        if choice == "A": 
            print("""A) Panthers
            B) Bandits
            C) Warriors\n
            """)

            team_choice = input("Enter an option:   ").upper()
            options_for_teams = {"A": "Panthers", "B": "Bandits", "C":"Warriors"}

            if team_choice in options_for_teams:
                selected_team = options_for_teams[team_choice]
                print(f"\nTeam: {selected_team} Stats")
                print("----------------")
                display_team_stats({selected_team: balanced_teams[selected_team]})
                input("\nPress ENTER to continue...")
            else: 
                print("\nInvalid choice! Please enter A, B, or C.")

        elif choice == "B":
            print("\nThank you for using the Basketball Team Stats tool! Goodbye! \n")
            break

        else: 
            print("\nInvalid choice! Please enter A or B.")










if __name__ == "__main__":              # Running app.py file directly

    cleaned_players = clean_data(PLAYERS)  # Calling clean_data function
    print(cleaned_players)

    balanced_teams = balance_teams(TEAMS, cleaned_players)
    print(balanced_teams)

    display_team_stats(balanced_teams)