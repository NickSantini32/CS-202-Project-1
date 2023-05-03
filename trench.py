
grid = [
    ["x","x","x"," ","x"," ","x"," ","x","x"],
    [" ","2","3","4","5","6","7","8","9","1"]
]  

def makeHash(state):
  str = ""
  for entry in state[1]:
    str += entry
  str += state[0][3]
  str += state[0][5]
  str += state[0][7]
  return str

def addIfNotSeen(state, queue, seen):
  if (makeHash(state) not in seen):
    queue.append(state)
    seen.update({makeHash(state): True})
    # print(makeHash(state))

def uniform():
    
    queue = [grid]
    seen = {}

    while len(queue) > 0:
    # if True:
      state = queue.pop(0)
      print(len(queue))
      print(len(seen))
      print()
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


          
uniform()            
    






