# not so good approach (worst approach)
# mylist_1 = []
# mylist_1.append('batman')
# mylist_1.append('superman')
# mylist_1.append('spiderman')
# print(mylist_1)
# mylist_1.pop(0)
# print(mylist_1)
# -----------------------------
# better approach
# from collections import deque
# mlist  =  deque()
# mlist.append("batman")
# mlist.append("superman")
# mlist.append("Aquaman")
# print(mlist)
# mlist.popleft()
# print(mlist)

#---- one another approach
# from queue import Queue
# mylist = Queue()
# mylist.put("superman")
# mylist.put("aquaman")
# mylist.put("flash")
# print(mylist.get())
