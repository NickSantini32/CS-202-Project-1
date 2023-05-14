from queue import PriorityQueue

grid = [
    ["x","x","x"," ","x"," ","x"," ","x","x"],
    [" ","2","3","4","5","6","7","8","9","1"]
    # ['x', 'x', 'x', ' ', 'x', '5', 'x', '8', 'x', 'x'],
    # ['1', ' ', ' ', ' ', '2', '3', '4', '6', '7', '9']
    # ['x', 'x', 'x', ' ', 'x', '5', 'x', '7', 'x', 'x'],
    # ['1', ' ', ' ', ' ', '2', '3', '4', '6', '9', '8']
]  
phase = 0 # phase + 1 = the number that the heuristic is trying to put into its position

def makeHash(state):
  str = ""
  for row in state:
    for entry in row:
      if entry != "x":
        str += entry

  return str

def addToQueueIfNotSeen(state, queue, seen, type):
  if type == "manhattan custom":
      addIfNotSeenManhattanCustom(state, queue, seen)
    
  elif type == "uniform":
      addIfNotSeenUniform(state, queue, seen)

  elif type == "misplaced":
      addIfNotSeenMissingTile(state, queue, seen)

  elif type == "manhattan":
      addIfNotSeenManhattan(state, queue, seen)

def addIfNotSeenManhattan(node, queue, seen):
  if (makeHash(node.state) not in seen):
    queue.put((computeManhattanDist(node), node))
    seen.update({makeHash(node.state): True})

def addIfNotSeenUniform(node, queue, seen):
  if (makeHash(node.state) not in seen):
    queue.put((node.depth, node))
    seen.update({makeHash(node.state): True})

def addIfNotSeenManhattanCustom(node, queue, seen):
  if (makeHash(node.state) not in seen):
    queue.put((computeManhattanDistCustom(node), node))
    seen.update({makeHash(node.state): True})

def addIfNotSeenMissingTile(node, queue, seen):
  if (makeHash(node.state) not in seen):
    queue.put((computeMissingTileDist(node), node))
    seen.update({makeHash(node.state): True})

#eliminate phase by just doing 500 * each unsolved soldier
def computeManhattanDistCustom(node): #generates custom manhattan distance heuristic
  global phase
  dist = 0

  # manhattan for just phase
  for i, list in enumerate(node.state):
    for j, item in enumerate(list):
      if item == str(phase+1):
        dist = (abs(phase - j)) * 3 + (1-i) # distance of target num weighted 3 times more than depth
      
  dist += (9 - phase) * 500
  dist += node.depth

  return dist

def computeManhattanDist(node): 
  dist = 0

  for i, list in enumerate(node.state):
    for j, item in enumerate(list):
      if item != " " and item != "x":
        dist += (abs(int(item) - (j+1))) * 3 + (1-i) # distance of target num weighted 3 times more than depth
      
  dist += node.depth

  return dist

def computeMissingTileDist(node):
  state = node.state
  dist = 0
  for i, item in enumerate(state[0]):
    if i < 8 and item != str(i+1):
      dist += 1

  return (dist * 2) + node.depth

def getTraceback(node):
  trace = []
  cur = node
  while cur.state[0] != grid[0] or cur.state[1] != grid[1]:
    trace.append(cur)
    cur = cur.parent

  trace.append(cur)
  trace.reverse()
  return trace

class Node:
  def __init__(self, state, parent, depth, type):
    self.state = state
    self.parent = parent
    self.depth = depth
    self.type = type #heuristic type

  def __lt__(self, other):
    return self.evaluateBasedOnType() < other.evaluateBasedOnType()
  
  def __gt__(self, other):
    return self.evaluateBasedOnType() > other.evaluateBasedOnType()
  
  def __eq__(self, other):
    return self.state[0] == other.state[0] and self.state[1] == other.state[1]
  
  def evaluateBasedOnType(self):
    if self.type == "manhattan custom":
      return computeManhattanDistCustom(self)
    
    elif self.type == "uniform":
      return self.depth

    elif self.type == "misplaced":
      return computeMissingTileDist(self)

    elif self.type == "manhattan":
      return computeManhattanDist(self)

def search(type):
    
    queue = PriorityQueue()
    queue.put((0, Node(grid, None, 0, type)))

    seen = {}
    global phase #used for custom manhattan heuristic

    while not queue.empty():
      node = queue.get() 
      node = node[1]

      if type == "manhattan custom" :
        #island approach. if we make it to an island, move towards next island
        while node.state[1][phase] == str(phase+1):
          phase += 1

        #if we need to go back an island, regress the phase
        temp = 0
        while temp < phase:
          if (node.state[1][temp] != str(temp+1)):
            phase = temp + 1
            break
          temp += 1

      # print(phase)
      # print(node.state[0])
      # print(node.state[1])
      
      # print(queue.qsize())
      # print(len(seen))
      # print("")

      #solution found
      if node.state[1] == ["1","2","3","4","5","6","7","8","9"," "]:
        print("Solution found!")
        print("Algorithm: " + type)
        print("Size of queue: " + str(queue.qsize()))
        print("Explored nodes: " + str(len(seen)))
        print("Depth: " + str(node.depth))
        print("")
        print("Traceback: ")
        trace = getTraceback(node)
        for t in trace:
          print(t.state[0])
          print(t.state[1])
          print("")
        return    

      #queuing function
      for i, entry in enumerate(node.state[1]): #left right
        if entry != " ": #if entry is not empty
          j = i - 1 
          while j >= 0 and node.state[1][j] == " ": #while left is empty and not out of bounds
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1, type)
            new_node.state[1][i] = node.state[1][j]
            new_node.state[1][j] = node.state[1][i]
            addToQueueIfNotSeen(new_node, queue, seen, type)
            j -= 1

          j = i + 1
          while j < len(node.state[1]) and node.state[1][j] == " ": #while right is empty and not out of bounds
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1, type)
            new_node.state[1][i] = node.state[1][j]
            new_node.state[1][j] = node.state[1][i]
            addToQueueIfNotSeen(new_node, queue, seen, type)
            j += 1

      for i, entry in enumerate(node.state[0]): #up down
        if entry != "x":
          if entry == " " and node.state[1][i] != " ": # if empty and bottom is not empty, do down swap
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1, type)
            new_node.state[0][i] = node.state[1][i]
            new_node.state[1][i] = node.state[0][i]
            addToQueueIfNotSeen(new_node, queue, seen, type)

          if entry != " " and node.state[1][i] == " ": # if top is not empty and bottom is empty, do up swap
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1, type)
            new_node.state[0][i] = node.state[1][i]
            new_node.state[1][i] = node.state[0][i]
            addToQueueIfNotSeen(new_node, queue, seen, type)

    #queue is empty
    print("no solution found")
    return 
          
# search("uniform")
# search("misplaced")
search("manhattan")
search("manhattan custom")







