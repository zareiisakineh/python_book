# file: ex_08_09_team_start.py
#
# Type hints are part of this exercise. Only a couple of signatures below are
# annotated, as examples of the expected style - add type hints to the rest
# yourself. Watch the three cases from the exercise: list[Player],
# Player | None, and the forward reference "Team".
#
# The number and goals setters are given almost complete, because they use
# raise. A raise stops an invalid value from ever being stored, and it is how
# we say "this is not allowed". You only add the assignment that runs when the
# value is valid - and the type hints.

# TODO: Write the Player class.
#   Attributes (leading underscore): _name, _number, _goals
#   Properties:
#     number, goals - getters arte given; each setter validates and then YOU
#                     store the valid value (see the TODO inside the setter)
#   Methods:
#     score(n=1) - add n goals THROUGH the goals setter (so validation runs)
#     __eq__     - equal if same name and number
#     __str__    - e.g. "Ada (#14, 12 goals)"

class Player:
    def __init__(self, name, number, goals=0):
        # Hint: assign _name directly, then use the setters for number and
        # goals (self.number = number) so validation runs at construction too.
        # your code here
        self._name = name
        self.number = number
        self.goals = goals
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value: int) -> None:
        if not 1 <= value <= 99:
            raise ValueError(f"Jersey number {value} must be between 1 and 99")
# TODO: the value is valid here - store it in self._number
        else:
            self._number = value

    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, value: int) -> None:
        if value < 0:
            raise ValueError(f"Goals {value} cannot be negative")
        # TODO: the value is valid here - store it in self._goals
        else:
            self._goals = value

    def score(self, n: int = 1) -> None:      # <- example: signature already typed
        if n < 1:
            print("{n} må være større enn 0")
        else:
            self.goals += n

    def __eq__(self, other: "Player") -> bool:
        return self._name == other._name and self._number == other._number
        
    def __str__(self) -> str:
        return f"{self._name} (# {self._number}, {self._goals} goals)"


# TODO: Write the Team class.
#   Attributes: _name, _players (a list of Player)
#   Properties:
#     name        - getter + setter
#     total_goals - read-only; sum of every player's goals
#     top_scorer  - read-only; the Player with most goals, or None if empty
#   Methods:
#     add(player)          - append a Player
#     __len__              - number of players
#     __contains__(player) - support "player in team"
#     __getitem__(index)   - support team[0] and team[0:2]
#     __lt__(other)        - compare teams by total_goals (for sorting)
#     __str__              - team name, count, then one player per line


class Team:
    def __init__(self, name: str, players=None):
        # Hint: store the name, and build a NEW list from players so two
        # teams never share the same underlying list.
        self._name = name
        if players == None:
            self._players = []
        else:
            self._players = list(players)
        

    # @property name (getter + setter)
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = value
        

    # @property total_goals (read-only)
    @property
    def total_goals(self) -> int:
        return sum(player.goals for player in self._players)
        

    # @property top_scorer (read-only; return None for an empty team)
    
    
    @property
    def top_scorer(self) -> Player | None:
        if self._players == []:
            return None
        else:
            return max(self._players, key=lambda player: player.goals)
        
    def add(self, player) -> None:
        self._players.append(player)

    def __len__(self) -> int:                 # <- example: signature already typed
        return len(self._players)

    def __contains__(self, player) -> bool:
        return player in self._players
        
    def __getitem__(self, index) -> Player:
    # Delegate indexing to the internal list
        return self._players[index]

    def __lt__(self, other: "Team") -> bool:
        return self.total_goals < other.total_goals

    def __str__(self) -> str:
        resultat = f"team-navn: {self._name}, {len(self._players)} player\n"
        for player in self._players:
            resultat += f"{player}\n"
        return resultat
            
            

if __name__ == "__main__":
    # TODO: create a few Players, build a Team with add(), then exercise:
    #   printing the team, "player in team", len(team), team[0], 
    #   total_goals, top_scorer, and sorting a list of teams by total_goals.
    p1 = Player("Ada", 14, 12)
    p2 = Player("Caroline", 7, 20)
    p3 = Player("Guro", 10, 8)
    p4 = Player("Aliya", 1, 5)

    team = Team("Norway")

    team.add(p1)
    team.add(p2)
    team.add(p3)

    print(team)
    print(len(team))
    print(p4 in team)
    print(team[0])
    print(team.total_goals)
    print(team.top_scorer)
    print(p1.name)
    p1.name = 'Sakineh'      # player name setter
    print(p1.name)
    team.name = 'Gorgan'     # team-name setter
    print(team)
    p1.goals =54             #goal-setter
    print(team)
    
