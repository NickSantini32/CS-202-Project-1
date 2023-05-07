from queue import PriorityQueue

grid = [
    # ["x","x","x"," ","x"," ","x"," ","x","x"],
    # [" ","2","3","4","5","6","7","8","9","1"]
    ['x', 'x', 'x', ' ', 'x', '5', 'x', '8', 'x', 'x'],
    ['1', ' ', ' ', ' ', '2', '3', '4', '6', '7', '9']
]  
phase = 0

def makeHash(state):
  str = ""
  for row in state:
    for entry in row:
      if entry != "x":
        str += entry

  return str

def addIfNotSeen(state, queue, seen):
  if (makeHash(state) not in seen):
    queue.append(state)
    seen.update({makeHash(state): True})
    # print(makeHash(state))

def addIfNotSeenPriority(node, queue, seen):
  if (makeHash(node.state) not in seen):
    queue.put((computeManhattanDist(node), node))
    seen.update({makeHash(node.state): node.parent})
    # print(makeHash(state))

def uniform():
    
    queue = [grid]
    seen = {}

    while len(queue) > 0:
    # if True:
      state = queue.pop(0)
      # print(len(queue))
      # print(len(seen))
      
    #for state in queue:\

      if state[1] == ["1","2","3","4","5","6","7","8","9"," "]:
        print("Solution found!")
        print("Size of queue: " + str(len(queue)))
        print("Explored nodes: " + str(len(seen)))
        return 

      for i, entry in enumerate(state[1]): #bottom row
        if entry == " ":
          if i != 0: # if not first column, do left swap
            new_state = [list.copy(state[0]), list.copy(state[1])]
            new_state[1][i] = state[1][i-1]
            new_state[1][i-1] = state[1][i]
            addIfNotSeen(new_state, queue, seen)

          if i != len(state[1])-1: # if not last column, do right swap
            new_state = [list.copy(state[0]), list.copy(state[1])]
            new_state[1][i] = state[1][i+1]
            new_state[1][i+1] = state[1][i]
            addIfNotSeen(new_state, queue, seen)

      for i, entry in enumerate(state[0]): #top row
        if entry != "x":
          if entry == " " and state[1][i] != " ": # if empty and bottom is not empty, do down swap
            new_state = [list.copy(state[0]), list.copy(state[1])]
            new_state[0][i], new_state[1][i] = state[1][i], state[0][i]
            addIfNotSeen(new_state, queue, seen)

          if entry != " " and state[1][i] == " ": # if top is not empty and bottom is empty, do up swap
            new_state = [list.copy(state[0]), list.copy(state[1])]
            new_state[0][i], new_state[1][i] = state[1][i], state[0][i]
            addIfNotSeen(new_state, queue, seen)

      # print("queue")
      # for t in queue:
      #   print(t[0])
      #   print(t[1])
      #   print("")


def computeManhattanDist(node):
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

class Node:
  def __init__(self, state, parent, depth):
    self.state = state
    self.parent = parent
    self.depth = depth

  def __lt__(self, other):
    return computeManhattanDist(self) + self.depth < computeManhattanDist(other) + other.depth
  
  def __gt__(self, other):
    return computeManhattanDist(self) + self.depth > computeManhattanDist(other) + other.depth
  
  def __eq__(self, other):
    return computeManhattanDist(self) + self.depth == computeManhattanDist(other) + other.depth

def manhattan():
    
    queue = PriorityQueue()
    queue.put((0, Node(grid, None, 0)))

    seen = {}
    count=0
    global phase

    while not queue.empty():
    # if True:
      node = queue.get()
      # print(node[0]) #print priority     
      # print(phase)
      cost = node[0]
      node = node[1]
      # print(node.state[0])
      # print(node.state[1])
      
      # print(queue.qsize())
      # print(len(seen))
      # print("")
      
    #for state in queue:\

      # if phase == 9:
      #   count += 1
      #   while not queue.empty():
      #     temp = queue.get()
      #     print(temp[0])
      #     print(temp[1].state[0])
      #     print(temp[1].state[1])
      #     print("")
      #   return

      # if count == 10:
        
      
      if node.state[1] == ["1","2","3","4","5","6","7","8","9"," "]:
        print("Solution found!")
        print("Size of queue: " + str(queue.qsize()))
        print("Explored nodes: " + str(len(seen)))
        # while not queue.empty():
        #   temp = queue.get()
        #   print(temp[0])
        #   print(temp[1].state[0])
        #   print(temp[1].state[1])
        #   print("")
        return

      #island approach. if we make it to an island, clear queue and move towards next island
      if node.state[1][phase] == str(phase+1):
        phase += 1
        # queue = PriorityQueue()
        # newQ = PriorityQueue()
        # while not queue.empty():
        #   temp = queue.get()
        #   newQ.put((temp[0] + 500, temp[1]))

        # queue = newQ
        # queue.put((cost, node))



      #queuing function
      for i, entry in enumerate(node.state[1]): #bottom row
        if entry == " ":
          if i != 0: # if not first column, do left swap
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1)
            new_node.state[1][i] = node.state[1][i-1]
            new_node.state[1][i-1] = node.state[1][i]
            addIfNotSeenPriority(new_node, queue, seen)

          if i != len(node.state[1])-1: # if not last column, do right swap
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1)
            new_node.state[1][i] = node.state[1][i+1]
            new_node.state[1][i+1] = node.state[1][i]
            addIfNotSeenPriority(new_node, queue, seen)

      for i, entry in enumerate(node.state[0]): #top row
        if entry != "x":
          if entry == " " and node.state[1][i] != " ": # if empty and bottom is not empty, do down swap
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1)
            new_node.state[0][i] = node.state[1][i]
            new_node.state[1][i] = node.state[0][i]
            addIfNotSeenPriority(new_node, queue, seen)

          if entry != " " and node.state[1][i] == " ": # if top is not empty and bottom is empty, do up swap
            new_node = Node([list.copy(node.state[0]), list.copy(node.state[1])], node, node.depth+1)
            new_node.state[0][i] = node.state[1][i]
            new_node.state[1][i] = node.state[0][i]
            addIfNotSeenPriority(new_node, queue, seen)
          
# uniform() 
manhattan()







