import random
import input

# Set the cars from the list 'training cars' into a new variablefvc
raw_data = input.training_cars
print(len(raw_data))

training_data = [[0 for j in range(3)] for i in range(700)]  # Create a 2D list of dimensions 300x4
for i in range(0, len(input.training_cars)):
    training_data[i][0] = float(raw_data[i].qualify_make()) * 1000
    training_data[i][1] = float(raw_data[i].qualify_model()) * 1000
    training_data[i][2] = float(raw_data[i].qualify_damage()) * 1000

for i in range(0, len(training_data)):
    print(training_data[i])

#training_data  = [[2005, '0', '0', '0'], [0, '1', '0.625', '1']]


# Comes from interview [Yes, No]
output_correction = [[1.0 for i in range(2)] for x in range(700)]

'''
for i in range(0, 400):
    output_correction[i][0] = float(0)
    output_correction[i][1] = float(1)

for i in range(400, 700):
    output_correction[i][1] = float(0)

print(output_correction)
'''


class Neuron:

    def __init__(self, num):
        self.weight_list = []
        self.value_list = []
        self.num_input = num
        self.sum = 0
        self.output = 0

        # Assign random number to weight_list and 0 to value_list
        for x in range(0, self.num_input - 1):
            self.weight_list.append(random.uniform(-0.1, 0.1))
            self.value_list.append(0)

        # Add the a random bias to weight_list
        self.weight_list.append(random.uniform(-0.1, 0.1))
        self.value_list.append(1)

    def calculate(self):
        self.sum = 0
        for i in range(0, self.num_input):
            self.sum = float(self.weight_list[i]) * float(self.value_list[i])

        self.output = sigmoid(self.sum)


def sigmoid(x):

    ans = 1 / (1 + 2.718 ** (-x))

    return ans


def sigmoid_prime(x):
    return sigmoid(x) * (1 - sigmoid(x))



# initialize the layers.
input_layer = [Neuron(1) for i in range(0, 4)]
hidden_layer1 = [Neuron(5) for x in range(0, 64)]
hidden_layer2 = [Neuron(65) for y in range(0, 32)]
output_layer = [Neuron(33) for z in range(0, 2)]

# initialize the error matrices
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


def back_propagation(learning_rate, case):

    for x in range(0, len(output_layer)):
        output_error[x] = float(sigmoid_prime(output_layer[x].sum)) * float((output_correction[case][x]) - float(output_layer[x].output))

    for x in range(0, len(hidden_layer2)):
        temp = 0
        for y in range(0, len(output_layer)):
            temp += output_layer[y].weight_list[x] * output_error[y]
        hidden2_error[x] = sigmoid_prime(hidden_layer2[x].sum) * temp

    for x in range(0, len(hidden_layer1)):
        temp = 0
        for y in range(0, len(hidden_layer2)):
            temp += hidden_layer2[y].weight_list[x] * hidden2_error[y]
        hidden1_error[x] = sigmoid_prime(hidden_layer1[x].sum) * temp

    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2) + 1):
            output_layer[x].weight_list[y] = output_layer[x].weight_list[y] + (
                learning_rate * output_layer[x].value_list[y] * output_error[x])

    for x in range(0, len(hidden_layer2)):
        for y in range(0, len(hidden_layer1) + 1):
            hidden_layer2[x].weight_list[y] = hidden_layer2[x].weight_list[y] + (
                learning_rate * hidden_layer2[x].value_list[y] * hidden2_error[x])

    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer) + 1):
            hidden_layer1[x].weight_list[y] = float(hidden_layer1[x].weight_list[y]) + (
                learning_rate * float(hidden_layer1[x].value_list[y]) * float(hidden1_error[x]))


def forward_propagation(case):

    for x in range(0, len(hidden_layer1)):
        for y in range(0, len(input_layer)):
            hidden_layer1[x].value_list[y] = training_data[case][y]

    for x in range(0, len(hidden_layer1)):
        hidden_layer1[x].calculate()

    for x in range(0, len(hidden_layer2)):
        for y in range(0 , len(hidden_layer1)):
            hidden_layer2[x].value_list[y] = hidden_layer1[y].output

    for x in range(0, len(hidden_layer2)):
        hidden_layer2[x].calculate()

    for x in range(0, len(output_layer)):
        for y in range(0, len(hidden_layer2)):
            output_layer[x].value_list[y] = hidden_layer2[y].output

    for x in range(0, len(output_layer)):
        output_layer[x].calculate()

    if float(output_layer[0].output) < float(output_layer[1].output):
        print("It doesn't qualify")
    else:
        print("Yes it does qualify")


def print_layer(layer):
    for x in range(0, len(layer)):
        print("Node " + str(x) + "'s output was: " + str(layer[x].output))


def write_weights_to_file():  # run after a successful train() is called
    fw = open("file_weights.txt", "w+")

    for x in range(0, len(network)):
        for y in range(0, len(network[x])):
            for z in range (0, len(network[x][y].weight_list)):
                fw.write(str(network[x][y].weight_list[z]) + "\n")
    fw.close()


def read_weights_from_file():					# run before run() is called
    count = 0
    fr = open("file_weights.txt", "r")
    temp = fr.read().splitlines()

    for x in range(0, len(network)):
        for y in range(0, len(network[x])):
            for z in range(0, len(network[x][y].weight_list)):
                network[x][y].weight_list[z] = float(temp[count])
                print(temp[count])
                count += 1

    # print(temp)

    fr.close()


def train():

    iterations = 0
    learning_rate = 0.05
    while iterations < 500:
        case = 0
        while case < 700:
            forward_propagation(case)
            back_propagation(learning_rate, case)

            print("Node for yes: " + str(output_layer[0].output) + " " + str(case) + " | " + str(iterations))
            print("Node for no: " + str(output_layer[1].output) + " " + str(case) + " | " + str(iterations))
            print()

            # write_weights_to_file()

            case += 1
        iterations += 1


def run():

    #ead_weights_from_file()
    train()

    input = [2015, 125, 687.5, 8000]

    for x in range(0, 30):
        training_data[x] = input

    forward_propagation(0)
    print_layer(output_layer)
    print()


run()
