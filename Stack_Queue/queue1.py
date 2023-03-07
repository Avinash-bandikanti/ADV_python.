import queue
#q=queue.Queue()
q=queue.PriorityQueue()
#q.put(123)
#q.put(12)
q.put((1,"AVINASH"))
q.put((2,"AVI"))
q.put((3,"A"))
#q.put(125)
#q.put(126)
#q.put(127)
while not q.empty():
     #print(q.get()[1],end=' ')
     print(q.get(),end=" ")