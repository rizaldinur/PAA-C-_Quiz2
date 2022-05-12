class RiverCrossing:
  GameOver = [
              ["Carrot","Goat","Wolf"],
              ["Goat","Wolf"],
              ["Carrot","Goat"]
  ]

  #Constructor
  def __init__ (self, left=["Wolf", "Carrot", "Goat"], right=[], boat=False,
                children=[]):
    self.left = left
    self.right = right
    self.boat = boat
    self.children = children
 
  def __str__(self):
    return str(self.left) + str(self.right) + ("Left" if not self.boat else "Right")
  

 
  
  @staticmethod
  def prev_state(prev, left, right, boat):
        return any(
            sorted(left) == sorted(x.left) and
            sorted(right) == sorted(x.right) and
            boat == x.boat
            for x in prev
        )

    

print("Choose Method:")
print("1. DFS")
print("2. BFS")
menu = int(input())-1
root = RiverCrossing()

count = 0
if (menu):
    solution = find_solution(root, isDFS=False)
    print("BFS solution = \n")
    for i in solution:
        count = count+1
        print("Steps #" + str(count) + ":")
        print(i, '\b')
        print("\n")
else:    
    solution = find_solution(root, isDFS=True)
    print("DFS solution = \n")
    for i in solution:
        count = count+1
        print("Step #" + str(count) + ":")
        print(i, '\b')
        print("\n")
