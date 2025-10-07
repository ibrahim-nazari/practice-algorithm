
def process_match(match_data,team1,team2,score1,score2):
    if team1 not in match_data:
        match_data[team1]=[0,0,0,0,0,0]   # points, wins, draw, loss, goals-scored, goals-received
    if team2 not in match_data:
        match_data[team2]=[0,0,0,0,0,0]   # points, wins, draw, loss, goals-scored, goals-received
    match_data[team1][4] +=score1
    match_data[team1][5] +=score2
    match_data[team2][4] +=score2
    match_data[team2][5] +=score1
    if score1 > score2:
        match_data[team1][0] += 3 # points
        match_data[team1][1] += 1 # win
        match_data[team2][3] += 1 # loss
    elif score2 > score1:
        match_data[team2][0] += 3 # points
        match_data[team2][1] += 1 # win
        match_data[team1][3] += 1 # loss
    else:
         match_data[team1][0] += 1 # points
         match_data[team1][2] += 1 # points
         match_data[team2][0] += 1 # pints
         match_data[team2][2] += 1 # pints

def sort_match_data(match_data):
    return sorted(match_data.items(),key=lambda team: (-team[1][0],-team[1][1],-team[1][2],team[1][3],-team[1][4],team[1][5]))
         
def find_result(tcs):
    for i,match_list in enumerate(tcs):
        match_data={}
        for match_contest in match_list:
            team1=match_contest.split("[")[0].strip()
            team2=match_contest.split("]")[1].strip()
            score_part=match_contest.split("[")[1]
            score1,score2=map(int,score_part.split("]")[0].split("-"))
             
             
            process_match(match_data,team1,team2,score1,score2)
        sorted_data=sort_match_data(match_data)
        for team,status in sorted_data:
            print(f"{team},{status[0]},{status[1]},{status[2]},{status[3]},{status[4]},{status[5]}")
        if i < len(tcs) -1:
            print()
            
        

def main():
    T=int(input())
    tcs=[]
    for _ in range(T):
        M=int(input())
        match_list=[input().strip() for _ in range(M)]
        tcs.append(match_list)
    find_result(tcs)

    

if __name__=="__main__":
    main()