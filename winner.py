
import math

teams = ["Duke", "Arkansas", "Houston", "Villanova"]


stats = {
    "Duke": {
        "FGA": 60.3,
        "FG%": .49,
        "2PA": 38.5,
        "2P%": .56,
        "3PA": 21.9,
        "3P%": .37,
        "FTA": 17.2,
        "FT%": .73

    },
    "Arkansas": {
        "FGA": 60.5,
        "FG%": .43,
        "2PA": 39.8,
        "2P%": .50,
        "3PA": 20.8,
        "3P%": .30,
        "FTA": 22.8,
        "FT%": .75


    },
    "Houston": {
        "FGA": 59.7,
        "FG%": .46,
        "2PA": 36.5,
        "2P%": .54,
        "3PA": 23.3,
        "3P%": .34,
        "FTA": 17.4,
        "FT%": .66
    },
    "Villanova": {
        "FGA": 56.2,
        "FG%": .43,
        "2PA": 30.2,
        "2P%": .50,
        "3PA": 26,
        "3P%": .360,
        "FTA": 16.9,
        "FT%": .82
    },
    "St. Peter's": {
        "FGA": 54.7,
        "FG%": .43,
        "2PA": 38,
        "2P%": .46,
        "3PA": 16.7,
        "3P%": .35,
        "FTA": 20.7,
        "FT%": .698
    },
    "North Carolina": {
        "FGA": 61.4,
        "FG%": .45,
        "2PA": 37.9,
        "2P%": .50,
        "3PA": 23.5,
        "3P%": .36,
        "FTA": 18.4,
        "FT%": .76

    }

}


def points_for_win(team): 
    FGA = stats[team]["FGA"]
    FGP = stats[team]["FG%"]
    TwoPA = stats[team]["2PA"]
    TwoPP = stats[team]["2P%"]
    ThreePA = stats[team]["3PA"]
    ThreePP = stats[team]["3P%"]
    FTA = stats[team]["FTA"]
    FTP = stats[team]["FT%"]

    FG = math.floor(FGA * FGP)
    TwoP = math.floor(TwoPA * TwoPP)
    ThreeP = math.floor(ThreePA * ThreePP)
    FT = math.floor(FTA * FTP)
    points = FG + TwoP + ThreeP + FT
    


    return math.floor(points), team

def findWinner(team, team1):

    points, name = points_for_win(team)
    points1, name1 = points_for_win(team1)

    if points > points1:
        return {
            "winner": {
                "name": name,
                "points": points
            },
            "loser": {
                "name": name1,
                "points": points1
            }
        }
    else:
        return {
            "winner": {
                "name": name1,
                "points": points1
            },
            "loser": {
                "name": name,
                "points": points
            }
        }
   
        



"""winner1, points1 = findWinner(teams[0], teams[1])
winner2, points2 = findWinner(teams[2], teams[3])
winner3, points3 = findWinner("St. Peter's", "North Carolina")
winner, points = findWinner(winner1, winner2)


print(f
Houston  ⎼⎼⎼┑
        {winner2}⎼⎼⎼┑
Villanova ⎼⎼⎼┚      
                {winner}
Duke    ⎼⎼⎼┑       
       {winner1} ⎼⎼⎼┚
Arkansas⎼⎼⎼┚
St. Peter's  ⎼⎼⎼┑
            {winner3}
North Carolina ⎼⎼⎼┚ 
)"""
