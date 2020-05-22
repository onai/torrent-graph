from data_file import data
import matplotlib.pyplot as plt
import networkx as nx
import statistics as sts
import operator

def plotthis(g):

  pos = nx.spring_layout(g,scale=1) #default to scale=1
  nx.draw(g,pos, with_labels=True, node_size=1)
  plt.show()

def allpairs(g):
  path = nx.all_pairs_shortest_path_length(g)
  
  lengths = []
  for keys in path:
    for values in path[keys]: 
      if path[keys][values] != 0:
        lengths.append(path[keys][values])
  
  #print lengths
  print(sts.mean(lengths), sts.median(lengths), sts.mode(lengths)) 

def clustering(g):
    
  print(nx.clustering(g))


g = nx.Graph()
edgeList = data
g.add_edges_from(edgeList)

#allpairs(g)
pr = nx.pagerank(g)
sorted_pr = sorted(pr.items(), key=operator.itemgetter(1))
print(sorted_pr)


plotthis(g)
