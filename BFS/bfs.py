import queue
from mymap import myMap
from modules import showResult

def BFS(start, goal):
  q = queue.deque() # khởi tạo queue
  q.append(start)  # enqueue
  
  previous = [] # khởi tạo previous kiểu dictionary
  for city in myMap.keys():
    previous.append((city, None))
  previous = dict(previous)
  
  while 1:
    curCity = q.popleft() # dequeue
    for city in myMap[curCity].keys(): # Các điểm có thể đi đến được từ điểm hiện tại
      if previous[city] == None: # Nếu chưa đi qua điểm này
        q.append(city) # Thêm vào hàng đợi
        previous[city] = curCity # Lưu lại dấu vết
        if city == goal:
          print('Success!')
          showResult(previous, start, goal)
          return True # Tìm thấy goal

    if len(q) == 0:
      print('Fail!')
      return False # Không thể đi đến goal từ start
    
start = "A" #điểm bắt đầu
goal = "C"   #điểm kết thúc

BFS(start, goal)
