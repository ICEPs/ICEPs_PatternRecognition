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
	# if split_arr[4] == 'Iris-setosa\n':
	# 	split_arr[4] = '1.0'
	# elif split_arr[4] == 'Iris-versicolor\n':
	# 	split_arr[4] = '2.0'
	# elif split_arr[4] == 'Iris-virginica\n':
	# 	split_arr[4] = '3.0'
	split_arr[4] = switch(split_arr[4])
	# print "Split Arr: %s" % split_arr
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
	fo = open("foo.txt", "w")
	for test_line in test:
		type1 = 0
		type2 = 0
		type3 = 0
		answers = []
		determinant = []
		# print "test count: %d" % test_count
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
		
		# print "Determinant: %s" % determinant
		answers = sorted(determinant, key=lambda x: x[0])
		print determinant
		fo.write(str(test_line_complete)+"\n")
		for lines in answers:
			fo.write("Test Number: %s, line answer: %s\n" % (test_count, lines))

		for x in range(k_num):
			fo.write("Before: \n")
			fo.write("Type 1: %d\n" % type1)
			fo.write("Type 2: %d\n" % type2)
			fo.write("Type 3: %d\n" % type3)
			fo.write("answer: %s \n" % str(answers[x][1]))

			if answers[x][1] == 1.0:
				type1 = type1+1
			elif answers[x][1] == 2.0:
				type2 = type2+1
			elif answers[x][1] == 3.0:
				type3 = type3+1
			
			fo.write("After: \n")
			fo.write("Type 1: %d\n" % type1)
			fo.write("Type 2: %d\n" % type2)
			fo.write("Type 3: %d\n" % type3)
		fo.write(str(greaterThan(type1, type2, type3))+"\n")

		if type1 == greaterThan(type1, type2, type3):
			types.append('Iris-setosa')
		elif type2 == greaterThan(type1, type2, type3):
			types.append('Iris-versicolor')
		elif type3 == greaterThan(type1, type2, type3):
			types.append('Iris-virginica')
		print types[test_count]
		fo.write(str(types[test_count])+"\n")
		
		# if type1 > type2:
		# 	if type1 > type3:
		# 		types.append("Iris-setosa")
		# elif type2 > type1:
		# 	if type2 > type3:
		# 		types.append("Iris-versicolor")
		# elif type3 > type1:
		# 	if type3 > type2:
		# 		types.append("Iris-virginica")



		test_count = test_count + 1
	fo.close()
	return types


knn_list = knn(15, '../iris.data', '../bezdekIris.data')
print len(knn_list)



# strrrrring = '5.4,3.4,1.7,0.2,Iris-setosa'
# print data_conversion(strrrrring)

# fo = open('../iris.data')
# fo2 = open('../bezdekIris.data')
# print fo.name


# counter = 0;
# for line in fo:
# 	print "This is line number: " + str(counter)
# 	counter = counter+1
# 	data_arr = line.split(',')
# 	data_count = 0;
# 	for iris in fo2:
# 		print "DATA %s" % data_count
# 		data_count = data_count+1
# 		print iris