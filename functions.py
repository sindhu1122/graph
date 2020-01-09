def edgesdisplay(dic):
  edges = []
  for node in dic:
    for edg in dic[node]: 
      edges.append((node, edg)) 
  print(edges) 

def insert(dic,u,v):
  if(u not in dic):
    dic[u]=list(v)
  else:
    if(v not in dic[u]):
      dic[u].append(v)
  edgesdisplay(dic)

def deleteedge(dic,u,v):
  dic[u].remove(v)
  edgesdisplay(dic)

def deletenode(dic,u):
  del dic[u]
  for n in dic:
    for m in dic[n]:
      if(m == u):
        dic[n].remove(m)
  edgesdisplay(dic)
