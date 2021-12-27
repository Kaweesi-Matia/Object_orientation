
"""Using object oriented programming to access properties of different 
football teams in premier league"""

class premier_league:
    def __init__(self,color,coach,stadium,position):
        self.color=color
        self.coach=coach
        self.stadium=stadium
        self.position=position
        
    # Instantiating football teams
Man_utd = premier_league("red", "Rangnick"," Oldtrafford" , 7)
Chelsea = premier_league("blue", "Tuchel", "Stamford bridge", 3)
Man_city = premier_league("Skyblue", "Pep", "Etihad", 1)
Arsenal = premier_league("red", "Arteta", "Emirates", 4)
Liverpool = premier_league("red", "Klopp", "Anifield", 2)
Tottenham = premier_league("white", "Conte", "Tottenham hotspur", 5)
Westham = premier_league("claret", "Moyes", "London", 6)
Wolves = premier_league("orange", "Lage", "Mollineux", 8)
Brighton = premier_league("blue and white", "Potter", "Amex", 9)
Leicester_city = premier_league("blue", "Brendan", "king power", 10)
Astonvilla = premier_league("maroon", "Gerald", "Villa park", 11)
Crystalpalace = premier_league("red and blue", "Viera", "schulst park", 12)
Southampton = premier_league("red", "Hassentil", "st mary's", 14)
Everton = premier_league("blue", "Benitez", "Goodison park", 15)
Leeds = premier_league("white", "Bielsa", "Elland road", 16)
Watford = premier_league("yellow", "Ranieri", "Vicarage road", 17)
Burnley = premier_league("maroon", "Dyce", "Turf moor", 18)
Newcastle = premier_league("white and black", "Howe", "St james park", 19)
Norwich = premier_league("yellow", "Smith", "carol road", 20)
Brentford = premier_league("white and red", "Frank", "Brentford community", 13)


print(Man_utd.position)
print(Newcastle.coach)
   