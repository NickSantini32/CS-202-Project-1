from queue import PriorityQueue

grid = [
    ["x","x","x"," ","x"," ","x"," ","x","x"],
    [" ","2","3","4","5","6","7","8","9","1"]
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
    queue.put((computeManhattan(node), node))
    seen.update({makeHash(node.state): True})
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


def computeManhattan(node):
  # dist = 0 # manhattan for just 1
  # for i, list in enumerate(state):
  #   for j, item in enumerate(list):
  #     if item == "1":
  #       dist = j + (1-i)
      
  dist = 0 # manhattan for 1 and spaces to be forward
  for i, list in enumerate(node.state):
    for j, item in enumerate(list):
      if item == "1":
        dist = j + (1-i)
      
  dist += node.depth

  return dist

  # dist = 0 # manhattan for all people
  # for i, list in enumerate(state):
  #   for j, item in enumerate(list):
  #     if item != "x" and item != " ":
  #       dist += abs(int(item) - (j+1)) + (1-i) 

  # global phase
  # dist = 0
  # if phase == 0: #get 1 to pos 3
  #   for i, list in enumerate(state):
  #     for j, item in enumerate(list):
  #       if item == "1":
  #         dist += abs(-3 + j)
  #   if dist == 0:
  #     phase += 1

  # elif phase == 1: # get 1 to pos 3 but up
  #   for i, list in enumerate(state):
  #     for j, item in enumerate(list):
  #       if item == "1":
  #         dist += abs(-3 + j) + i
  #   if dist == 0:
  #     phase += 1

  # elif phase == 2: #get all 3 spaces in front 
  #   for i, list in enumerate(state):
  #     for j, item in enumerate(list):
  #       if item == "1":
  #         dist += abs(-3 + j) + i
  #       if item == " ":
  #         dist += j + (1-i)
  #   if dist == 0:
  #     phase += 1

  # elif phase == 3: #get 1 to the front
  #   for i, list in enumerate(state):
  #     for j, item in enumerate(list):
  #       if item == "1":
  #         dist += j + (1-i)
  #   if dist == 0:
  #     phase += 1

  # elif phase == 4: #organize the rest
  #   for i, list in enumerate(state):
  #     for j, item in enumerate(list):
  #       if item != "x" and item != " ":
  #         dist += abs(int(item) - (j+1)) + (1-i)


  

class Node:
  def __init__(self, state, parent, depth):
    self.state = state
    self.parent = parent
    self.depth = depth

def manhattan():
    
    queue = PriorityQueue()
    queue.put((0, Node(grid, None, 0)))

    seen = {}

    while not queue.empty():
    # if True:
      node = queue.get()
      print(node[0]) #print priority  
      # global phase
      # print(phase)
      cost = node[0]
      node = node[1]
      # print(state[0])
      # print(state[1])
      # print("")
      # print(queue.qsize())
      # print(len(seen))
      
    #for state in queue:\

      if node.state[1] == ["1","2","3","4","5","6","7","8","9"," "]:
        print("Solution found!")
        print("Size of queue: " + str(len(queue)))
        print("Explored nodes: " + str(len(seen)))
        return 

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







