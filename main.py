from flask import Flask
import numpy as np
app = Flask(__name__)


def neuron(cx, cy, r):
    circle = '<circle class="neuron" id="{cx}_{cy}" cx="{cx}" cy="{cy}" r="{r}" stroke="black" stroke-width="2" fill="none" />\n'
    circle = circle.format(cx=cx, cy=cy, r=r)
    return circle

def weight():
    pass

@app.route('/')
def hello_world():
    num_inputs = 3
    num_hidden_layers = 2
    num_hidden_neurons = 3
    num_outputs = 2
    input_layer = ''
    hidden_layer = ''
    cy = 0
    for i in range(num_inputs):
        cy += 100
        input_layer += neuron(150, cy, 20)

    cx = 150
    layer_data = {}
    for k in range(num_hidden_layers):
        cx += 150
        cy2 = 0
        for j in range(num_hidden_neurons):
            cy2 += 100
            hidden_layer += neuron(cx, cy2, 20)
            node_name = 'node_{layer_number}_{node_number}'.format(layer_number=k, node_number=j)
            layer_data[node_name] = (cx, cy2)

    m = 0
    for n in range(num_hidden_layers):
        node_name0 = 'node_{layer_number}_{node_number}'.format(layer_number=n, node_number=m)
        for m in range(num_hidden_neurons):
            pass


    returnStr = ''
    returnStr += '<svg width="100%" height="700px" >'
    returnStr += input_layer
    returnStr += hidden_layer
    returnStr += '</svg>'


    return returnStr

if __name__ == '__main__':
    app.run(debug=True)