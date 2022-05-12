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

  def ChildGenerator (self, prev, parent_map):
    children = []
    if not self.boat:
      for x in self.left:
        new_left = self.left[:]
        new_right = self.right[:]
        new_left.remove(x)
        new_right.append(x)

        if sorted(new_left) not in RiverCrossing.GameOver and not RiverCrossing.prev_state(prev, new_left, new_right, not self.boat):
                    child = RiverCrossing(new_left, new_right, not self.boat, [])
                    children.append(child)
                    parent_map[child] = self
      if sorted(self.left) not in RiverCrossing.GameOver and not RiverCrossing.prev_state(prev, self.left[:], self.right[:], not self.boat):
                child = RiverCrossing(self.left[:], self.right[:], not self.boat, [])
                children.append(child)
                parent_map[child] = self
    else:
      for x in self.right:
                new_left = self.left[:]
                new_left.append(x)
                new_right = self.right[:]
                new_right.remove(x)

                if sorted(new_right) not in RiverCrossing.GameOver and not RiverCrossing.prev_state(prev, new_left, new_right, not self.boat):
                    child = RiverCrossing(new_left, new_right, not self.boat, [])
                    children.append(child)
                    parent_map[child] = self

      if sorted(self.right) not in RiverCrossing.GameOver and not RiverCrossing.prev_state(prev, self.left[:], self.right[:], not self.boat):
                child = RiverCrossing(self.left[:], self.right[:], not self.boat, [])
                children.append(child)
                parent_map[child] = self
    self.children = children

  @staticmethod
  def prev_state(prev, left, right, boat):
        return any(
            sorted(left) == sorted(x.left) and
            sorted(right) == sorted(x.right) and
            boat == x.boat
            for x in prev
        )

def find_solution(root, isDFS=False):
    '''
    Find a solution to the River Crossing Problem.
    isDFS: True for DFS, False for BFS
    '''
    visit = [root]
    node = root
    prev = []
    parent_map = {root: None}

    while visit:
        node = visit.pop()
        if not RiverCrossing.prev_state(prev, node.left, node.right, node.boat):
            prev.append(node)
        node.ChildGenerator(prev, parent_map)


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
