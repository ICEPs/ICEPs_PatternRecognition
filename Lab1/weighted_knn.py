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

def weighted_KNN(k_num, training_file_name, testing_file_name):

	train = open(training_file_name)
	test = open(testing_file_name)
	types = []
	for test_line in test:
		answers = []
		determinant = []
		test_line_complete = data_conversion(test_line)
		test_line_vectors = test_line_complete[0:4]
		train.seek(0,0)
		for train_line in train:
			train_line_complete = data_conversion(train_line)
			train_line_vectors = train_line_complete[0:4]
			matrix = [euclidean_distance(test_line_vectors, train_line_vectors), train_line_complete[4]]
			determinant.append(matrix)
		
		answers = sorted(determinant, key=lambda x: x[0])
		w_array = []
		w_y_array = []
		for x in range(k_num):
			squared_dist = square(answers[x][0])
			if answers[x][0] != 0:
				w = 1/squared_dist
			else:
				w = 0
			w_array.append(w)
			w_y = w*answers[x][1]
			w_y_array.append(w_y)
			
		number_type = int((summation(w_y_array))/(summation(w_array)))
		if  number_type == 1:
			types.append("Iris-setosa")
		elif number_type == 2:
			types.append("Iris-versicolor")
		elif number_type == 3:
			types.append("Iris-virginica")
	return types
		
final = weighted_KNN(3, 'train.txt', 'test.txt')
print final
	