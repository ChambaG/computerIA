import random
import math
import time
from  CarClass import Car

make_input = []

class Neuron():

    def __init__(self, num):
        self.weight_list = []
        self.value_list = []
        self.num_inputs = num
        self.sum = 0
        self.output = 0

        for i in range(0, self.num_inputs - 1):
            self.weight_list.append(random.uniform(-0.1, 0.1))
            self.value_list.append(0)

        # Bias
        self.weight_list.append(random.uniform(-0.1, 0.1))
        self.value_list.append(1)

    def calculate(self):
        self.sum = 0
        for i in range(0, self.num_inputs):
            self.sum += self.weight_list[i] * self.value_list[i]
        self.output = sigmoid(self.sum)


def sigmoid(x):

    ans = 1 / (1 + (2.718 ** (-x)))
    return ans


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


input_layer = [Neuron(1) for i in range(0, 78)]
hidden_layer1 = [Neuron(79) for i in range(0, 512)]
hidden_layer2 = [Neuron(513) for i in range(0, 64)]
output_layer = [Neuron(65)]

input_error = []
hidden1_error = []
hidden2_error = []
output_error = []

for x in range(0, len(input_layer)):
    input_error.append(0)
for x in range(0, len(hidden_layer1)):
    hidden1_error.append(0)
for x in range(0, len(hidden_layer2)):
    hidden2_error.append(0)
for x in range(0, len(output_layer)):
    output_error.append(0)

error_matrix = [input_error, hidden1_error, hidden2_error, output_error]
network = [input_layer, hidden_layer1, hidden_layer2, output_layer]


def print_layer(layer):
    for i in range(0, len(layer)):
        print("Node " + str(i) + "'s output was: " + str(layer[i].output))


def forward_propagation(test_case):

    # Set inputs for the first hidden layer
    print(len(make_input))
    print(len(hidden_layer1))
    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer)):
            hidden_layer1[x].value_list[y] = make_input[test_case][y]
    # Calculate
    for i in range(0, len(hidden_layer1)):
        hidden_layer1[i].calculate()

    # Set inputs for the second hidden layer
    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1)):
            hidden_layer2[x].value_list[y] = hidden_layer1[y].output
    # Calculate
    for i in range(0, len(hidden_layer2)):
        hidden_layer2[i].calculate()

    # Set inputs for the output layer
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2)):
            output_layer[x].value_list[y] = hidden_layer2[y].output
    # Calculate
    for i in range(0, len(output_layer)):
        output_layer[x].calculate()


def backward_propagation(test_case, learning_rate):

    # Calculate error for output layer
    for x in range(0, len(output_layer)):
        output_error[x] = sigmoid_prime(output_layer[x].sum) * (make_output[test_case][x] - output_layer[x].output)

    # Calculate error for second hidden layer
    for x in range(0, len(hidden_layer2)):
        temp = 0
        for y in range(0, len(output_layer)):
            temp += output_layer[y].weight_list[x] * output_error[y]
        hidden2_error[x] = sigmoid_prime(hidden_layer2[x].sum) * temp

    # Calculate error for first hidden layer
    for x in range(0, len(hidden_layer1)):
        temp = 0
        for y in range(0, len(hidden_layer2)):
            temp += hidden_layer2[y].weight_list[x] * hidden2_error[y]
        hidden1_error[x] = sigmoid_prime(hidden_layer1[x].sum) * temp

    # Assign new weights to output layer
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2) + 1):
            output_layer[x].weight_list[y] = output_layer[x].weight_list[y] + (learning_rate * output_layer[x].
                                                                               value_list[y] * output_error[x])

    # Assign new weights to second layer
    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1) + 1):
            hidden_layer2[x].weight_list[y] = hidden_layer2[x].weight_list[y] + (learning_rate * hidden_layer2[x].
                                                                                 value_list[y] * hidden2_error[x])

    # Assign new weights to first layer
    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer) + 1):
            hidden_layer1[x].weight_list[y] = hidden_layer1[x].weight_list[y] + (learning_rate * hidden_layer1[x].
                                                                                 value_list[y] * hidden1_error[x])


def write_weights_to_file():  # run after a successful train() is called
    fw = open("file_weights.txt", "w+")

    for x in range(0, len(network)):
        for y in range(0, len(network[x])):
            for z in range (0, len(network[x][y].weight_list)):
                fw.write(str(network[x][y].weight_list[z]) + "\n")
    fw.close()


def read_weights_from_file():					# run before run() is called
    count = 0
    fr = open("/Users/salvag/Documents/GitHub/computerIA/file_weights.txt", "r")
    temp = fr.read().splitlines()

    for x in range(0, len(network)):
        for y in range(0, len(network[x])):
            for z in range(0, len(network[x][y].weight_list)):
                network[x][y].weight_list[z] = float(temp[count])
                count += 1

    # print(temp)

    fr.close()


def train():
    iterations = 0
    learning_rate = 0.5
    while iterations < 1:
        test_case = 0

        print(iterations)
        while test_case < 1709:
            forward_propagation(test_case)
            backward_propagation(test_case, learning_rate)
            print(str(output_layer[0].output) + " " + str(test_case + 1) + " | Expected output: " + str(make_output[test_case]))
            test_case += 1

            write_weights_to_file()

        iterations += 1


def quali(car_input):
    read_weights_from_file()
    print("Entered neural network")
    for i in range(0, len(car_input)):
        car_input[i].qualify()
        make_input.append(car_input[i].input)
        print(car_input[i].show())
        print(make_input[i])

    for i in range(0, len(make_input)):
        forward_propagation(i)
        car_input[i].show()
        print_layer(output_layer)
