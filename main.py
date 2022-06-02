from flask import Flask
import numpy as np
import itertools
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
    y_spacing = 100
    start_y = 100
    distance = num_hidden_neurons*num_hidden_layers*y_spacing
    num_outputs = 2
    input_layer = ''
    hidden_layer = ''
    cy = 0
    for i in range(num_inputs):
        cy += 100
        #input_layer += neuron(150, cy, 20)

    intervals = list(np.arange(start_y, distance + start_y, y_spacing))
    cy0 = start_y
    intervals_y = []
    intervals_x = []
    cx0 = 350
    for i, value in enumerate(intervals):
        cy0 += y_spacing
        if i%num_hidden_neurons == 0:
            cy0 = start_y
            if i > 0:
                cx0 += 150
        intervals_y.append(cy0)
        intervals_x.append(cx0)
        hidden_layer += neuron(cx0, cy0, 20)
    coordinates = list(itertools.product(intervals_x, intervals_y))
    for c, c_value in coordinates:
        pass



    returnStr = ''
    returnStr += '<svg width="100%" height="700px" >'
    returnStr += input_layer
    returnStr += hidden_layer
    returnStr += '</svg>'


    return returnStr

if __name__ == '__main__':
    app.run(debug=True)