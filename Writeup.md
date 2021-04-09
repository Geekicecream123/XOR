The XOR function outputs 1 when the input is (0,1)or(1,0) and 0 when (1,1)or (0,0) are inputed.
These are the inputs and expected outputs which were used while building the neural 
neural network.Before running the forward prop the weights and biases were randomly initlaiized  so that they could learn something useful,if they were initlaiized to 0
all the neurons would have given the same output,learning nothing new.In the forward pass,the activation of the hidden and output layers were computed,using
the sigmoid activation function,Although better activation functions like Relu are available ,but since the datasize is small the problem of
not learning new parameters as data size grows due to flattening of the sigmoid graph did not arise.Then using backprop which is essentially the chain rule,T
the expectedvalue-the values from the forward prop in,gives use the derivative .
These derivative are used to update the value of weights and biases
using (Wo-learningrate*derivate),these run over 11000 epochs gave a learning curve which was decreasing.The gradient descent runs over 11000 times to give this graph.
I have read that other gradient method like stochastic gradient descent (takes single step after every training example) and minibatches (takes
step after 32,64 ,128examples) which is much compuationally less time consuming.
While making this project i knew the theory as i have done Machine learning course by Andrew Ng and 3 courses of deeplearning spealisation.I am not
yet comfortable with using python numpy as i lack practice so i took  help from a number of websites for the code.
