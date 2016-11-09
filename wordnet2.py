
from __future__ import division
import sys
import nltk
from nltk.corpus import wordnet as wn
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import pylab as plt
import pygraphviz
import matplotlib.pyplot as plt


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("/Users/rithintl/projectdp/cleandata.txt")
data = fp.read()

#to tokenize input text into sentences

print ('\n-----\n'.join(tokenizer.tokenize(data)))# splits text into sentences

#to tokenize the tokenized sentences into words

tokens = nltk.wordpunct_tokenize(data)
text = nltk.Text(tokens)
words = [w.lower() for w in text]  
print (words)     #to print the tokens

for a in words:
    syns = wn.synsets(a)
    print ("synsets:", syns)

   # for s in syns:
         #for l in s.lemmas:
             #print (l.name)
         #print (s.definition)
         #print (s.examples)




def closure_graph(synset, fn):
    seen = set()
    graph = nx.DiGraph()
 
    def recurse(s):
        if not s in seen:
            seen.add(s)
            graph.add_node(s.name)
            for s1 in fn(s):
                graph.add_node(s1.name)
                graph.add_edge(s.name, s1.name)
                recurse(s1)
    recurse(synset)
    return graph
woman = wn.synset('woman.n.01')
graph = closure_graph(woman,lambda s: s.hypernyms())
pos = graphviz_layout(graph)
nx.draw_networkx_nodes(graph,pos,node_size=50,node_color='w',alpha=0.4)
nx.draw_networkx_edges(graph,pos,alpha=0.4,node_size=0,width=1,edge_color='m')
 
# Label style variables...
nx.draw_networkx_labels(graph,pos,fontsize=14)
font = {'fontname'   : 'Helvetica',
    'color'      : 'k',
    'fontweight' : 'bold',
    'fontsize'   : 14}
 
# Figure style variables...
plt.title("Visualizing WordNet relationships as graphs", font)
plt.axis('off')
plt.show()
 

