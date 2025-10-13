# Assignment1
# Import
import numpy as np

# String operations

s1 = 'week1'
s2 = "week1"
s3 = 'Week1'
checkS1S2 = s1 == s2
checkS1S3 = s1 == s3

# String concatenate
first = 'Montaseer'
last = 'Meraz'
name = first + ' ' + last

# Repeat strings
# repeated 1000 times
large_string = (name + ', ') * 1000

# Test strings
checkFirst = first in name
checkLast = (last not in name) 


# String length and format
L_large_string = len(large_string)
format_large_string = f'Length of large_string = {L_large_string}'

# String indexing (positive and negative)
name1 = name[0]
name2 = name[1]
nameN = name[len(name) - 1]

reverse_name1 = name[-1]
reverse_name2 = name[-2]
reverse_nameN = name[-len(name)]

# String slicing to retrieve first and last names
first_copy = name[:len(first)]
last_copy = name[len(first)+1:]

# List and tuple operations
# Define mixed list/tuple
mixed_list = [3.14, 7, 'alpha', 'beta']
mixed_tuple = (3.14, 7, 'alpha', 'beta')

# Concatenate
mixed_list2 = ['gamma', 42]
mixed_tuple2 = ('delta', -1)
combined_list = mixed_list + mixed_list2
combined_tuple = mixed_tuple + mixed_tuple2

# Repeat lists and tuples
long_list = [0] * 200
long_tuple = ('',) * 300

# tests
check_first_list = 'first' in combined_list
check_last_list  = 'last'  in combined_list
check_1_tuple    = 1 not in combined_tuple
check_5_tuple    = 5 not in combined_tuple

# Lengths
L_long_list = len(long_list)
L_long_tuple = len(long_tuple)

# Indexing
list1 = combined_list[0]
list2 = combined_list[1]
listN = combined_list[-1]

tuple1 = combined_tuple[-1]
tuple2 = combined_tuple[-2]
tupleN = combined_tuple[-len(combined_tuple)]

# Slicing
first_four_list = combined_list[:4]
last_four_tuple = combined_tuple[-4:]

# difference
long_list_copy = long_list[:]
long_list_copy[:100] = [1] * 100

long_tuple_copy = long_tuple[:]
try:
    # modify tuple
    long_tuple_copy[-100:] = ('ok',) * 100
except Exception as e:
    tuple_error = str(e)

# Array operations
list_of_list = [[10] * 100 for _ in range(100)]

# 1D array
long_array = np.array(long_list)

# 2D array
big_matrix = np.array(list_of_list)

# print shapes
print(f'dimension of long_array = {long_array.shape}')
print(f'dimension of big_matrix = {big_matrix.shape}')

# Set operations
watches = set()
for _id in ['D84HD90', '45DMCO8', 'DINF30A', 'ER07DP3', 'XNCV5O9', '45DMCO8']:
    watches.add(_id)

# Dictionary operations
user_info = {
    'user1': 12345,
    'user2': 58493,
    'user3': 21297
}

check_user1 = 'user1' in user_info
check_user2 = 'user5' in user_info

number_users = len(user_info)

user_password_1 = user_info['user1']
user_password_2 = user_info['user2']
user_password_3 = user_info['user3']

# Change password of user2
user_info['user2'] = 99009
