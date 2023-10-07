class Player:
 def play(self):
   print("The player is playing cricket")
class Batsman(Player):
 def play(self):
   print("The Batsman is Batting")
class Bowler(Player):
  def play(self):
    print("The Bowler is Bowling")
# Create objects of Batsman and Bowler classes
batsman= Batsman() 
bowler= Bowler() 
# Call the paly() method for each object
batsman.play()
bowler.play()