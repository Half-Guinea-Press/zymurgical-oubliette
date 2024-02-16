## Dependencies
## Initial Variables
## Functions
## Main Body Of Code
## Load Existing Data
## Gather Nodes
## Describe Nodes
## Establish Edges
## Descibe Edges
## Disagregate Data
## Build JSON
## Export JSON

import json

jsondata = {}
nodes = []
links = []
node = {}
link = {}

node['id'] = "source"
node['group'] = 1
nodes.append(node)

node['id'] = "target"
node['group'] = 2
nodes.append(node)

link['source'] = "source"
link['target'] = "target"
link['value'] = 1
links.append(link)

jsondata['nodes'] = nodes
jsondata['links '] = links
print(json.dumps(jsondata))

import ipywidgets as widgets
from ipywidgets import VBox, HBox, Text, Button
from IPython.display import display

todo = []

def completed_sentence(sentence):
    def remove_sentence(_):
        global render_sentences
        try:
            if todo.index(sentenceField.value) >= 0:
                todo.remove(sentenceField.value)
        except:
            pass
        render_sentences(_)
                
    sentenceField = Text(value=sentence)
    removeButton = Button(description='Remove', button_style='danger')
    removeButton.on_click(remove_sentence)
    sentence_view = HBox([sentenceField, removeButton])
    return sentence_view

def render_sentences(_):
    """ To update the view """
    global a,b
    if a.value != '':
        todo.append(a.value)
    a.value = ''
    todoWidget.children = tuple\
        ([VBox([VBox([completed_sentence(each) 
                for each in todo]),
            HBox([a, b])])])
    
# Setting up a basic view- with an empty field and a button
a = widgets.Text(value='')
b = widgets.Button(description='Add')                                 
a.on_submit(render_sentences)
b.on_click(render_sentences)

todoWidget = widgets.HBox([a, b])
display(todoWidget)

jsondata = {}
agent={}
content={}
agent['agentid'] = 'john'
content['eventType'] = 'view'
content['othervar'] = "new"

jsondata['agent'] = agent
jsondata['content'] = content
print(json.dumps(jsondata))

# print {"content": {"eventType": "view", "othervar": "new"}, "agent": {"agentid": "john"}}

   
# create a list of a dictionaries
data = [{1: 'Geeks', 2: 'GeeksforGeeks'}, {1: 'Python', 2: 'Programming'}]
print(data)
 
# update the dictionary value
data[0][3] = "World"
data[0][2] = "Hello"
del data[1][2]
 
print(data)

  
# create a list of a dictionary
# with single dictionary element
data = [ {1: "Geeks", 2: "GeeksforGeeks"} ]
print(data)
 
# create a new dictionary to be appended
new_data = {1: "Python", 2: "Programming"}
 
# appending the new dictionary to
# the original list of dictionary
data.append(new_data)
print(data)
