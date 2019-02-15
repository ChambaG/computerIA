import random
import math

make_input = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 1 Audi
              [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 2 Chrysler
              [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 3 Honda
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 4 Kia
              [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 5 Mitsubishi
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 6 Suzuki
              [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 7 Land Rover
              [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 8 BMW
              [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 9 Dodge
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 10 Hyundai
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 11 Lexus
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 12 Nissan
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 13 Toyota
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 14 Ford
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 15 Infiniti
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 16 Mazda
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 17 Pontiac
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],  # 18 Volkswagen
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],  # 19 Acura
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],  # 20 Chevrolet
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],  # 21 GMC
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  # 22 Jeep
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],  # 23 Mercedez-Benz
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # 24 Subaru
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],  # 25 Volvo
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]]  # 26 Other

                    # Y__N
output_correction = [[0, 1],  # 1
                     [0, 1],  # 2
                     [1, 0],  # 3
                     [0, 1],  # 4
                     [1, 0],  # 5
                     [0, 1],  # 6
                     [0, 1],  # 7
                     [0, 1],  # 8
                     [0, 1],  # 9
                     [0, 1],  # 10
                     [1, 0],  # 11
                     [1, 0],  # 12
                     [1, 0],  # 13
                     [1, 0],  # 14
                     [0, 1],  # 15
                     [1, 0],  # 16
                     [1, 0],  # 17
                     [0, 1],  # 18
                     [0, 1],  # 19
                     [0, 1],  # 20
                     [0, 1],  # 21
                     [0, 1],  # 22
                     [0, 1],  # 23
                     [0, 1],  # 24
                     [0, 1],  # 25
                     [0, 1]]  # 26


class Neuron:

    def __init__(self, num):
        self.weight_list = []
        self.value_list = []
        self.num_inputs = num
        self.sum = 0
        self.output = 0

        for x in range(0, self.num_inputs - 1):
            self.weight_list.append(random.uniform(-0.1, 0.1))
            self.value_list.append(0)
        # add the bias value and weight
        self.weight_list.append(random.uniform(-0.1, 0.1))
        self.value_list.append(1)

        # self.calculate()

    def calculate(self):
        self.sum = 0
        for x in range(0, self.num_inputs):
            self.sum += self.weight_list[x] * self.value_list[x]
        self.output = sigmoid(self.sum)


def sigmoid(x):  # using custom sigmoid
    # ans = 1 / (1 + 2.718 ** (-x))
    if x < -4:
        ans = 0.0  # Less than -4
    elif x <= -3:
        ans = (0.029 * x) + 0.13  # Interval[-4, -3]
    elif x <= -2:
        ans = (0.076 * x) + 0.27  # Interval(-3, -2]
    elif x < -1:
        ans = (0.16 * x) + 0.43  # Interval(-2, -1)
    elif x <= 1:
        ans = (0.231 * x) + 0.5  # Interval[-1, 1]
    elif x <= 1.8:
        ans = (0.16 * x) + 0.58  # Interval(1, 1.8]
    elif x <= 2:
        ans = (0.087 * x) + 0.71  # Interval(1.8, 2]
    elif x <= 3:
        ans = (0.07 * x) + 0.75  # Interval(2, 3]
    elif x <= 4:
        ans = (0.031 * x) + 0.86  # Interval(3, 4]
    else:
        ans = 1.0  # Greater than 4
    return ans


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))


# initialize the layers
input_layer = [Neuron(1) for i in range(0, 26)]
hidden_layer1 = [Neuron(27) for x in range(0, 128)]
hidden_layer2 = [Neuron(129) for y in range(0, 128)]
output_layer = [Neuron(129) for z in range(0, 2)]

# initialize the error matrices
input_error = []
hidden1_error = []
hidden2_error = []
output_error = []

# create error matrix
# create error list for output
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


def back_propagation(test_case, learning_rate):
    # Calculate error for output layer
    for x in range(0, len(output_layer)):  # loop good
        output_error[x] = sigmoid_prime(output_layer[x].sum) * (letter_output[test_case][x] - output_layer[x].output)

    # Calculate error for hidden layer
    for x in range(0, len(hidden_layer2)):  # loop good
        temp = 0
        for y in range(0, len(output_layer)):
            temp += output_layer[y].weight_list[x] * output_error[y]
        hidden2_error[x] = sigmoid_prime(hidden_layer2[x].sum) * temp

    for x in range(0, len(hidden_layer1)):  # good
        temp = 0
        for y in range(0, len(hidden_layer2)):
            temp += hidden_layer2[y].weight_list[x] * hidden2_error[y]
        hidden1_error[x] = sigmoid_prime(hidden_layer1[x].sum) * temp

    """
    # Calculate error for input layer
    for x in range(0, len(input_layer)):
        temp = 0
        for y in range(0, len(hidden_layer1)):
            temp += hidden_layer1[y].weight_list[x] * hidden1_error[y]
        input_error[x] = sigmoid_prime(input_layer[x].sum) * temp
    """

    # Assign new weights to output layer.
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2) + 1):
            output_layer[x].weight_list[y] = output_layer[x].weight_list[y] + (
                        learning_rate * output_layer[x].value_list[y] * output_error[x])

    # Assign new weights to hidden layer 1.
    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1) + 1):
            hidden_layer2[x].weight_list[y] = hidden_layer2[x].weight_list[y] + (
                        learning_rate * hidden_layer2[x].value_list[y] * hidden2_error[x])

    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer) + 1):
            hidden_layer1[x].weight_list[y] = hidden_layer1[x].weight_list[y] + (
                        learning_rate * hidden_layer1[x].value_list[y] * hidden1_error[x])

    # Input layer does not have any weights.


def forward_propagation(test_case):
    """
    # used with input layer
    # Puts in the inputs to the input layer
    for x in range(0, len(input_layer)):
        input_layer[x].value_list[0] = input_vector[test_case][x]

    # calculate with the new inputs
    for x in range(0, len(input_layer)):
        input_layer[x].calculate()
    """

    # Set the inputs to the hidden layer 1 using the new calculated values from the input layer.
    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer)):
            # hidden_layer1[x].value_list[y] = input_layer[y].output    # used with input layer
            hidden_layer1[x].value_list[y] = letter_input[test_case][y]  # used with out input layer

    # calculate with the new inputs
    for x in range(0, len(hidden_layer1)):
        hidden_layer1[x].calculate()

    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1)):
            hidden_layer2[x].value_list[y] = hidden_layer1[y].output

    for x in range(0, len(hidden_layer2)):
        hidden_layer2[x].calculate()

    # Set the inputs to the output layer using the new calculated values from the hidden layer.
    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2)):
            output_layer[x].value_list[y] = hidden_layer2[y].output

    # calculate with the new input
    for x in range(0, len(output_layer)):
        output_layer[x].calculate()


def print_layer(layer):
    for x in range(0, len(layer)):
        print("Node " + str(x) + "'s output was: " + str(layer[x].output))


"""
def train_one(test_case):
    # test_case = 0
    iterations = 0
    learning_rate = 0.1

    # print()
    while iterations < 25:        # loop until trained for a single input
        # print()
        # print("Iteration = " + str(iterations))

        forward_propagation(test_case)

        back_propagation(test_case, learning_rate)

        # print("testing case = " + str(test_case) + "\nnetwork calculated: ")
        # print_layer(output_layer)

        # print()

        iterations += 1

"""


def train():
    # test_case = 0
    iterations = 0
    learning_rate = 0.1

    print()
    while iterations < 6000:  # loop until trained for a single input
        test_case = 0

        # print()
        # print("Iteration = " + str(iterations))

        while test_case < 26:  # loop for each input
            """
            if iterations > 50:
                learning_rate = 0.05
            """
            forward_propagation(test_case)

            back_propagation(test_case, learning_rate)

            print(str(output_layer[test_case].output) + " " + str(test_case))

            test_case += 1

        iterations += 1


def run():
    train()
    user_input = int(input("What Letter would you want to test: "))

    while user_input != 30:
        forward_propagation(user_input)

        print_layer(output_layer)
        print()

        user_input = int(input("What Letter would you want to test: "))

run()