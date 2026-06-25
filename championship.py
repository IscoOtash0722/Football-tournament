teams = {
    "Real Madrid": {
        "points": 0,
        "goals": 0, 
        "goal_difference": 0,
        "matches": 0 
    },
    "Barcelona": {
        "points": 0,
        "goals": 0,
        "goal_difference": 0,
        "matches": 0
    },
    "Real Betis": {
        "points": 0,
        "goals": 0,
        "goal_difference": 0,
        "matches": 0
    }
}

while True:
    print("\nMENU: ")
    print("1. Show all teams")
    print("2. Add the team")
    print("3. delete the team")
    print("4. show the statistic table")
    print("5. Play match")
    print("6. Exit")
    print("7. Show the champion")
    user_1 = int(input("choose the option: "))
    if user_1 == 1:
        for name, stats in teams.items():
            print(name)
    elif user_1 == 2:
        user_2 = input("write the team which you want to add: ").title().strip()
        if user_2 in teams:
            print(f"{user_2} is already in table! Baka!")
        else:
            teams[user_2] = {
    "points": 0,
    "goals": 0,
    "goal_difference": 0,
    "matches": 0
}
            print(f"{user_2} added successfully!")
            continue
    elif user_1 == 3:
        user_3 = input("write the team to delete: ").title().strip()
        if user_3 in teams:
            del teams[user_3]
            print(f"{user_3} has deleted")
        else:
            print("team not found")
    elif user_1 == 4:
         for team, stats in sorted(teams.items(), key=lambda x:( x[1]["points"], x[1]["goal_difference"]), reverse=True):
            print(team)
            print(f"points: {stats["points"]}")
            print(f"goals: {stats["goals"]}")
            print(f"goal diff: {stats["goal_difference"]}")
            print(f"matches: {stats["matches"]}")
    elif user_1 == 5:
        a = input("write the first team: ").title().strip()
        b = input("write the second team: ").title().strip()
        if a == b:
            print("teams must be different!")
            continue
        if a in teams and b in teams:
            c = int(input(f"write the goals of {a}: "))
            d = int(input(f"write the goals of {b}: "))
    
            if c > d:
                teams[a]["points"] += 3
                teams[a]["goals"] += c
                teams[b]["goals"] += d
                teams[a]["goal_difference"] += c - d
                teams[b]["goal_difference"] += d - c
                teams[a]["matches"] += 1
                teams[b]["matches"] += 1
            
            elif d > c:
                teams[b]["points"] += 3
                teams[b]["goals"] += d
                teams[a]["goals"] += c
                teams[a]["goal_difference"] += c - d
                teams[b]["goal_difference"] += d - c
                teams[a]["matches"] += 1
                teams[b]["matches"] += 1
            
            else:
                teams[a]["points"] += 1
                teams[a]["goals"] += c
                teams[b]["points"] += 1
                teams[b]["goals"] += d
                teams[a]["matches"] += 1
                teams[b]["matches"] += 1
        else:
            print("team not found!")
            continue
    
        for team, stats in sorted(teams.items(), key=lambda x:( x[1]["points"], x[1]["goal_difference"]), reverse=True):
            print(team)
            print(f"points: {stats["points"]}")
            print(f"goals: {stats["goals"]}")
            print(f"goal diff: {stats["goal_difference"]}")
            print(f"matches: {stats["matches"]}")

        user = input("continue? (Yes/No: )").title().strip()
        if user == "No":
            break
    elif user_1 == 6:
            print("you exit")
            break
    elif user_1 == 7:
        champion = sorted(teams.items(),key=lambda x: (x[1]["points"],x[1]["goal_difference"]),reverse=True)[0]
        champion_name, champion_stats = champion

        print(f"Champion: {champion_name}")
        print(f"Points: {champion_stats['points']}")
        
