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
	for x in range(0, len(arr_one)):
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
	split_arr[4] = switch(split_arr[4])
	return [float(n) for n in split_arr]

def greaterThan(a, b, c):
	greatest = a
	if b > a:
		greatest = b
	if c > a:
		greatest = c
		if b > c:
			greatest = b
	return greatest

def knn(k_num, training_file_name, testing_file_name):
	train = open(training_file_name)
	test = open(testing_file_name)
	types = []
	test_count = 0
	correct_counter = 0
	for test_line in test:
		type1 = 0
		type2 = 0
		type3 = 0
		answers = []
		determinant = []
		test_line_complete = data_conversion(test_line)
		test_line_vectors = test_line_complete[0:4]
		train.seek(0,0)
		loop_count = 0
		for train_line in train:
			train_line_complete = data_conversion(train_line)
			train_line_vectors = train_line_complete[0:4]
			matrix = [euclidean_distance(test_line_vectors, train_line_vectors), train_line_complete[4]]
			determinant.append(matrix)
			loop_count = loop_count+1
		
		answers = sorted(determinant, key=lambda x: x[0])

		for x in range(k_num):
			if answers[x][1] == 1.0:
				type1 = type1+1
			elif answers[x][1] == 2.0:
				type2 = type2+1
			elif answers[x][1] == 3.0:
				type3 = type3+1

		if type1 == greaterThan(type1, type2, type3):
			types.append('Iris-setosa\n')
		elif type2 == greaterThan(type1, type2, type3):
			types.append('Iris-versicolor\n')
		elif type3 == greaterThan(type1, type2, type3):
			types.append('Iris-virginica\n')

		string_test_arr = test_line.split(',')

		if string_test_arr[4] == types[test_count]:
			correct_counter = correct_counter + 1

		test_count = test_count + 1
	div = float (correct_counter)/test_count
	return div


knn_list = knn(13, '../iris.data', '../bezdekIris.data')
print knn_list
