import numpy as np


def sigmoid (x):
    return 1/(1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)


inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
expectedoutput = np.array([[0],[1],[1],[0]])

epochs = 11000
lr = 0.1
inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2,2,1


hiddenweights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
hiddenbias =np.random.uniform(size=(1,hiddenLayerNeurons))
outputweights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
outputbias = np.random.uniform(size=(1,outputLayerNeurons))

print("Initial hidden weights: ",end='')
print(*hiddenweights)
print("Initial hidden biases: ",end='')
print(*hiddenbias)
print("Initial output weights: ",end='')
print(*outputweights)
print("Initial output biases: ",end='')
print(*outputbias)


#Training algorithm
for _ in range(epochs):
	#Forward Propagation
	hidden_layer_activation = np.dot(inputs,hiddenweights)
	hidden_layer_activation += hiddenbias
	hidden_layer_output = sigmoid(hidden_layer_activation)

	output_layer_activation = np.dot(hidden_layer_output,output_weights)
	output_layer_activation += outputbias
	predictedoutput = sigmoid(output_layer_activation)

	#Backpropagation
	error = expectedoutput - predictedoutput
	d_predicted_output = error * sigmoid_derivative(predictedoutput)

	error_hidden_layer = d_predicted_output.dot(output_weights.T)
	d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)


	outputweights += hidden_layer_output.T.dot(d_predicted_output) * lr
	outputbias += np.sum(d_predicted_output,axis=0,keepdims=True) * lr
	hiddenweights += inputs.T.dot(d_hidden_layer) * lr
	hiddenbias += np.sum(d_hidden_layer,axis=0,keepdims=True) * lr

print("Final hidden weights: ",end='')
print(*hiddenweights)
print("Final hidden bias: ",end='')
print(*hiddenbias)
print("Final output weights: ",end='')
print(*outputweights)
print("Final output bias: ",end='')
print(*outputbias)
print("\nOutput from neural network after 10,000 epochs: ",end='')
print(*predictedoutput)
