import math

def square(v):
	return v**2

def summation(var_arr):
	total = 0;
	for num in var_arr:
		total = total+num
	return total

def euclidean_distance(arr_one, arr_two):
	dist = []
	temp = []
	for x in range(0, len(arr_one)-1):
		temp.append(arr_one[x] - arr_two[x])
		dist.append(square(temp[x]))
	return math.sqrt(summation(dist))
	
def switch(x):
	return {
        'Iris-setosa\n': '1',
        'Iris-versicolor\n': '2',
		'Iris-virginica\n': '3',
		'Iris-setosa\n': '1',
        'Iris-versicolor\n': '2',
		'Iris-virginica': '3'
    }[x]

def data_conversion(string_unsplit):
	split_arr = string_unsplit.split(',')
	
	# if split_arr[4] == 'Iris-setosa':
		# split_arr[4] = '1'
		# print split_arr[4]
	# elif split_arr[4] is 'Iris-versicolor':
		# split_arr[4] == '2'
	# elif split_arr[4] is 'Iris-virginica':
		# split_arr[4] == '3'
	# print  split_arr
	split_arr[4] = switch(split_arr[4])
	
	return [float(n) for n in split_arr]

def weighted_KNN(training_file_name, testing_file_name):
	train = open(training_file_name)
	test = open(testing_file_name)
	#main_counter = 0
	#final_answer_arr = []
	types = []
	for test_line in test:
		test_ints = data_conversion(test_line)
		#counter = 0
		for training_line in train:
			training_ints = data_conversion(training_line)
			arr_w = []
			arr_w_y = []
			dist_array = []
			for i in range (0, len(training_ints)):
				dist_array.append(euclidean_distance(test_ints, training_ints))
			total_d = summation(dist_array)
			w = 1/total_d
			w_y = w*test_ints[4]
			arr_w.append(w)
			arr_w_y.append(w_y)
			#counter = counter+1
		number_type = int(summation(arr_w_y)/summation(arr_w))
		if  number_type == 1:
			types.append("Iris-setosa")
		elif number_type == 2:
			types.append("Iris-versicolor")
		elif number_type == 3:
			types.append("Iris-virginica")
		
	return types
	
answers = weighted_KNN('train.txt', 'test.txt')
print answers
	