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
	elif split_arr[4] == 'Iris-virginica'
		split_arr[4] == '3'

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
	loop_count = 0
	for test_line in test:
		determinant = []
		answers = []
		type1 = 0
		type2 = 0
		type3 = 0
		test_line_complete = data_conversion(test_line)
		test_line_vectors = test_line_complete[0:4]
		for train_line in train:
			train_line_complete = data_conversion(train_line)
			train_line_vectors = train_line_complete[0:4]
			determinant[loop_count] = [euclidean_distance(test_line_vectors, train_line_vectors), train_line_complete[4])
			if loop_count < test.len():
				loop_count = loop_count+1
			else:
				loop_count = 0
		answers = sorted(determinant, key=lambda x: x[0])
		for x in range(0, k_num-1):
			if answers[x] == 1.0:
				type1 = type1+1
			elif answers[x] == 2.0:
				type2 = type2+1
			elif answers[x] == 3.0:
				type3 = type3+1

		if type1 == greaterThan(type1, type2, type3):
			types.append("Iris-setosa")
		elif type2 == greaterThan(type1, type2, type3):
			types.append("Iris-versicolor")
		elif type3 == greaterThan(type1, type2, type3):
			types.append("Iris-virginica")
	return types







# strrrrring = '5.4,3.4,1.7,0.2,Iris-setosa'
# print data_conversion(strrrrring)

# fo = open('poker-hand-training-true.data')
# print fo.name


# counter = 1;
# for line in fo:
# 	print "This is line number: " + str(counter)
# 	counter = counter+1
# 	data_arr = line.split(',')
# 	for datum in data_arr:
# 		print datum