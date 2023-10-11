def parse_team_data(data_str):
    team_data = data_str.split(",")
    team_name = team_data[0]
    points = 3 * int(team_data[1]) + int(team_data[3])
    goal_difference = int(team_data[4]) - int(team_data[5])
    return [team_name, points, goal_difference]

def sorted_team(teams):
    for i in range(len(teams)):
        j = i
        while j > 0 and teams[j][1] >= teams[j - 1][1]:
            if teams[j][1] == teams[j - 1][1] and teams[j][2] <= teams[j - 1][2]:
                break
            teams[j], teams[j - 1] = teams[j - 1], teams[j]
            j -= 1

def print_team_results(teams):
    print("== results ==")
    for team in teams:
        print(f"['{team[0]}', {{'points': {team[1]}}}, {{'gd': {team[2]}}}]")

input_data = input("Enter Input : ").split("/")
teams = [parse_team_data(team_str) for team_str in input_data]
sorted_team(teams)
print_team_results(teams)