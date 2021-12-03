# We created our class object thats automatic
class Lineup:
    
     # when the object is called it will automatically start at this function
    #initialize itself with player names
    def __init__(self, players):
        self.players = players # create and initialize a player listobject
        self.last_player_index = (len(self.players) - 1)  # set counter time (microwave) from player list

  # iterator function
    def __iter__(self):
        self.n = 0 # iterator starter
        return self

  # get item of player [current position]
    def get_player(self, n):
        return self.players[n] # return current player

    # iteration process
    def __next__(self):
        if self.n < self.last_player_index:   #check counter starter against current index
            player = self.get_player(self.n)  #define current player
            self.n += 1                       #next count
            return player
        elif self.n == self.last_player_index: #check if end  of list
            player = self.get_player(self.n)   # define current player
            self.n = 0                         # restart counter
            return player


astros = [
  'Springer',
  'Bregman',
  'Altuve',
  'Correa',
  'Reddick',
  'Gonzalez',
  'McCann',
  'Davis',
  'Tucker'
]

astros_lineup = Lineup(astros)
process = iter(astros_lineup)

print(next(process))