# op1 should contain all the characters which are present in str1 but NOT present in str2.
# op2 should contain all the characters which are present in str2 but NOT present in str1.


NO_OF_CHARS = 256


def tolist(string_1):
	temp = []
	for i in string_1:
		temp.append(i)
	return temp

def tostring_1(List):
	return ''.join(List)


def getCharCountArray(string_1):
	count = [0] * NO_OF_CHARS
	for j in string_1:
		count[ord(j)] += 1
	return count

def removecharsfirst(string_1, string_2):
	count = getCharCountArray(string_2)
	ip_ind = 0
	res_ind = 0
	temp = ''
	str_list = tolist(string_1)

	while ip_ind != len(str_list):
		temp = str_list[ip_ind]
		if count[ord(temp)] == 0:
			str_list[res_ind] = str_list[ip_ind]
			res_ind += 1
		ip_ind += 1
	return tostring_1(str_list[0:res_ind])

def removeCharsecond(string_1, string_2):
	count = getCharCountArray(string_2)
	ip_ind = 0
	res_ind = 0
	temp = ''
	str_list = tolist(string_1)

	while ip_ind != len(str_list):
		temp = str_list[ip_ind]
		if count[ord(temp)] == 0:
			str_list[res_ind] = str_list[ip_ind]
			res_ind += 1
		ip_ind += 1
	return tostring_1(str_list[0:res_ind])


# Example strings
string_1 = "BC"
string_2 = "BANGALORE"

print("option 1 :", removecharsfirst(string_1, string_2))

print("option 2 :", removeCharsecond(string_2, string_1))

