import random
import input

# Comes from training_data.txt
training_data = input.car_list

# Comes from interview
car_output = []


class Neuron():

    def __init__(self, num):
        self.weight_list = []
        self.value_list = []
        self.num_input = num
        self.sum = 0
        self.output = 0

        # Assign random number to weight_list and 0 to value_list
        for x in range(0, self.num_inputs - 1):
            self.weight_list.append(random.uniform(-0.1, 0.1))
            self.value_list.append(0)

        # Add the a random bias to weight_list
        self.weight_list.append(random.uniform(-0.1, 0.1))
        self.value_list.append(1)

    def calculate(self):
        self.sum = 0
        for i in range(0, self.num_input):
            self.sum = self.weight_list[i] * self.value_list[i]

        self.output = sigmoid(self.sum)


def sigmoid(x):

    ans = 1 / (1 + 2.718 ** (-x))

    return ans


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


# Initialize the layers
input_layer = [Neuron(1) for i in range(0, 35)]
hidden_layer1 = [Neuron(36) for x in range(0, 64)]
hidden_layer2 = [Neuron(67) for y in range(0, 128)]
hidden_layer3 = [Neuron(129) for w in range(0, 128)]
output_layer = [Neuron(129) for z in range(0, 2)]

# Initialize the error matrices
input_error = []
hidden1_error = []
hidden2_error = []
hidden3_error = []
output_error = []


def forward_propagation(test_case):

    # Set the inputs to the hidden layer 1 using the new calculated values from the input layer.
    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer)):
            hidden_layer1[x].value_list[y] = training_data[test_case][y]  # used with out input layer

    # calculate with the new inputs
    for x in range(0, len(hidden_layer1)):
        hidden_layer1[x].calculate()

    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1)):
            hidden_layer2[x].value_list[y] = hidden_layer1[y].output

    for x in range(0, len(hidden_layer2)):
        hidden_layer2[x].calculate()

    for x in range(0, len(hidden_layer3)):
        for y in range(0, len(hidden_layer2)):
            hidden_layer3[x].value_list[y] = hidden_layer1[y].output

    for x in range(0, len(hidden_layer3)):
        hidden_layer3[x].calculate()

    # Set the inputs to the output layer using the new calculated values from the hidden layer.
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2)):
            output_layer[x].value_list[y] = hidden_layer2[y].output

    # calculate with the new input
    for x in range(0, len(output_layer)):
        output_layer[x].calculate()


def train_one(test_case):

    iterations = 0
    learning_rate = 0.1

    while iterations < 500:
        forward_propagation(test_case)
        back_propagation(test_case, learning_rate)
        iterations += 1


def back_propagation(test_case, learning_rate):
    # Calculate error for output layer
    for x in range(0, len(output_layer)):
        output_error[x] = sigmoid_prime(output_layer[x].sum) * (training_data[test_case][x] - output_layer[x].output)

    # Calculate error for hidden layer 3
    for x in range(0, len(hidden_layer3)):
        temp = 0
        for y in range(0, len(hidden_layer2)):
            temp += output_layer[y].weight_list[x] * output_error[y]

    # Calculate error for hidden layer 2
    for x in range(0, len(hidden_layer2)):
        temp = 0
        for y in range(0, len(output_layer)):
            temp += hidden_layer3[y].weight_list[x] * output_error[y]
        hidden2_error[x] = sigmoid_prime(hidden_layer2[x].sum) * temp

    # Calculate error for hidden layer 1
    for x in range(0, len(hidden_layer1)):
        temp = 0
        for y in range(0, len(hidden_layer2)):
            temp += hidden_layer2[y].weight_list[x] * hidden2_error[y]
        hidden1_error[x] = sigmoid_prime(hidden_layer1[x].sum) * temp

    # Assign new weights to output layer.
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer3) + 1):
            output_layer[x].weight_list[y] = output_layer[x].weight_list[y] + (
                        learning_rate * output_layer[x].value_list[y] * output_error[x])

    # Assign new weights to hidden layer 3
    for x in range(0, len(hidden_layer3)):
        for y in range(0, len(hidden_layer2)):
            output_layer[x].weight_list[y] = output_layer[x].weight_list[y] + (
                learning_rate * output_layer[x].value_list[y] * output_error[x])

    # Assign new weights to hidden layer 2
    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1) + 1):
            hidden_layer2[x].weight_list[y] = hidden_layer2[x].weight_list[y] + (
                        learning_rate * hidden_layer2[x].value_list[y] * hidden2_error[x])

    # Assign new weights to hidden layer 1
    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer) + 1):
            hidden_layer1[x].weight_list[y] = hidden_layer1[x].weight_list[y] + (
                        learning_rate * hidden_layer1[x].value_list[y] * hidden1_error[x])


def print_layer(layer):
    for x in range(0, len(layer)):
        print("Node " + str(x) + "'s output was: " + str(layer[x].output))


def train():
    iterations = 0
    learning_rate = 0.1

    print()
    while iterations < 500:  # loop repeated 500 times
        test_case = 0

        # TODO Finish construction of training_data[]
        while True:  # loop for each
            forward_propagation(test_case)
            back_propagation(test_case, learning_rate)
            print(str(output_layer[test_case].output) + " " + str(test_case))
            test_case += 1

        iterations += 1


def run():
    train()
    car_input = []
    testing = 0

    # TODO Import the batch of cars that has to be tested for prediction
    while testing < len(car_input):
        forward_propagation(car_input[testing])
        testing += 1


run()
