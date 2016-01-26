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
	for x in range(0, arr_one.len()-1):
		temp[x] = arr_one[x] - arr_two[x]
		dist[x] = square(temp[x])
	return Math.sqrt(summation(dist))

def data_conversion(string_unsplit):
	split_arr = string_unsplit.split(',')
	if split_arr[4] == 'Iris-setosa':
		split_arr[4] = '1'
	elif split_arr[4] == 'Iris-versicolor':
		split_arr[4] == '2'
	elif split_arr[4] == 'Iris-virginica':
		split_arr[4] == '3'

	return [float(n) for n in split_arr]

def weighted_KNN(training_file_name, testing_file_name):
	train = open(training_file_name)
	test = open(testing_file_name)
	#main_counter = 0
	#final_answer_arr = []
	types = []
	for test_line in test:
		test_ints = data_conversion(test_line)
		counter = 0
		for training_line in train:
			training_ints = data_conversion(training_line)
			arr_w_y = []
			arr_w_y = []
			dist_array = []
			for i in range (0, training_ints.len()):
				dist_array = euclidean_distance(test_ints, training_ints)
			total_d = summation(dist_array)
			w = 1/total_d
			w_y = w*test_ints[4]
			arr_w[counter] = w
			arr_w_y[counter] = w_y 
			counter = counter+1
		number_type = int(summation(arr_w_y)/summation(arr_w))
		if  number_type == 1:
			types.append("Iris-setosa")
		elif number_type == 2:
			types.append("Iris-versicolor")
		elif number_type == 3:
			types.append("Iris-virginica")
		
	return types