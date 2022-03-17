# source https://favtutor.com/blogs/depth-first-search-python
#  Sử dụng từ điển Python để hoạt động như một danh sách
graph = {
  '5' : ['7','3'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Đặt để theo dõi các nút đã truy cập của biểu đồ.

def dfs(visited, graph, node):  #chức năng của dfs 
    if node not in visited: 
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("biểu đồ Depth-First Search")
dfs(visited, graph, '5')