#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import networkx as nx
df=pd.read_csv("Graph.csv")
display(df)


# In[2]:


df1=df.set_index("Cities")
df1


# In[3]:


G=nx.Graph()


# In[4]:


for node in df1:
    G.add_node(node)
    for neighbor in df1.columns:
        if df1.loc[node, neighbor] != 0:
            weight = df1.loc[node, neighbor]
            G.add_edge(node, neighbor, weight=weight)


# In[5]:


print("All Cities are: ")
for node in df1:
    print(node)


# In[6]:


print("---------------------------------------Graph representation of our problem:---------------------------------------------------")
import matplotlib.pyplot as plt
pos = nx.spring_layout(G)
plt.figure(3,figsize=(15,15)) 
nx.draw(G, pos,font_size=8,node_size=40, with_labels=True)
nx.draw_networkx_edge_labels(G, pos,font_size=8, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
plt.show()


# In[7]:


source_node = input('Enter the source node:- ')
target=input('Enter the destination node:-')


# In[8]:


print("Shortest path and distance using Dijakstra algorithm:")
path = nx.dijkstra_path(G,source_node,target)
print("Shortest path:", path)
print("Path length:", nx.dijkstra_path_length(G,source_node,target))


# In[9]:


h=nx.DiGraph()
h.add_nodes_from(path)
for i in range(len(path)-1):
    h.add_edge(path[i],path[i+1], weight=df1.loc[path[i],path[i+1]])
pos = nx.spring_layout(h)
print("Path is:")
nx.draw_networkx_nodes(h,pos=pos, node_color='r')
nx.draw_networkx_edges(h,pos=pos)
nx.draw_networkx_labels(h,pos)
nx.draw_networkx_edge_labels(h, pos,font_size=8, edge_labels={(u, v): d['weight'] for u, v, d in h.edges(data=True)})


# In[10]:


all_pairs_shortest_paths = dict(nx.floyd_warshall(G))


# In[11]:


print("All pair Shortest paths using Floyd-Warshall algorithm:")
display(all_pairs_shortest_paths)


# In[12]:


print("Distance and Shortest path using Floyd Warshell algorithm:")
print(all_pairs_shortest_paths[source_node][target])
path1 = nx.shortest_path(G,source_node,target, weight='weight')
print(path1)


# In[13]:


h=nx.DiGraph()
h.add_nodes_from(path1)
for i in range(len(path1)-1):
    h.add_edge(path1[i],path1[i+1], weight=df1.loc[path1[i],path1[i+1]])
pos = nx.spring_layout(h)
print("Path is:")
nx.draw_networkx_nodes(h,pos=pos, node_color='g')
nx.draw_networkx_edges(h,pos=pos)
nx.draw_networkx_labels(h,pos)
nx.draw_networkx_edge_labels(h, pos,font_size=8, edge_labels={(u, v): d['weight'] for u, v, d in h.edges(data=True)})


# In[14]:


print("Using Bellman Ford algorithm:")
print("Shortest paths to all nodes from the Source node: {}".format(source_node))
for node in G.nodes():
    shortest_path = nx.bellman_ford_path_length(G, source_node,node)
    print("'{}',:{}".format(node,shortest_path) )


# In[15]:


print("Distance and shortest path using Bellman Ford algorithm:")
path_length = nx.bellman_ford_path_length(G, source_node,target)
path2 = nx.bellman_ford_path(G,source_node,target, weight='weight')
print(path_length)
print(path2)


# In[16]:


h=nx.DiGraph()
h.add_nodes_from(path2)
for i in range(len(path2)-1):
    h.add_edge(path2[i],path2[i+1], weight=df1.loc[path2[i],path2[i+1]])
pos = nx.spring_layout(h)
print("Path is:")
nx.draw_networkx_nodes(h,pos=pos, node_color='c')
nx.draw_networkx_edges(h,pos=pos)
nx.draw_networkx_labels(h,pos)
nx.draw_networkx_edge_labels(h, pos,font_size=8, edge_labels={(u, v): d['weight'] for u, v, d in h.edges(data=True)})


# In[ ]:




