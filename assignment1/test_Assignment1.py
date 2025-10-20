import Assignment1 as As
import numpy as np
import marshal
import base64

solution = '''
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AAAkAHIWfQN0AwAAAAAAAAAAfAOrAQAAAAAAAH0CWQBkAH0DfgN8AlMAZAB9A34DdwF3AHgDWQB3ASkDTtrIb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tva29rb2tyiQAAACkC2glFeGNlcHRpb27aA3N0cikEclQAAADaD2xvbmdfdHVwbGVfY29wedoLdHVwbGVfZXJyb3LaAWVzBAAAACAgICByCwAAANoTZ2V0X2xvbmdfdHVwbGVfY29weXKTAAAAsgAAAHNKAAAAgADwAgUFHdgaJKFRmC2ID9ggKogPmASYE9AIHdgWGogL8AYADBfQBBb49AUADBXyAAEFHdwWGZghk2aMC9gLFtAEFvvwBQEFHfpzEAAAAIIMEACQCS8DmQsqA6oFLwNjAAAAAAAAAAAAAAAAAgAAAAMAAADzGgAAAJcAZAFnAWQCegUAAGcBZAJ6BQAAfQB8AFMAKQNOZwAAAAAAACRAcokAAAByBQAAACkB2gxsaXN0X29mX2xpc3RzAQAAACByCwAAANoQZ2V0X2xpc3Rfb2ZfbGlzdHKWAAAAvAAAAHMaAAAAgADYFRmQRpgzkUqQPKAD0RMjgEzYCxfQBBdyDQAAAGMBAAAAAAAAAAAAAAADAAAAAwAAAPMwAAAAlwB0AQAAAAAAAAAAagIAAAAAAAAAAAAAAAAAAAAAAAB8AKsBAAAAAAAAfQF8AVMAcgQAAACpAtoCbnDaBWFycmF5KQJyUAAAANoKbG9uZ19hcnJheXMCAAAAICByCwAAANoOZ2V0X2xvbmdfYXJyYXlynAAAAMMAAABzFgAAAIAA3BETlxiRGJgp0xEkgErYCxXQBBVyDQAAAGMBAAAAAAAAAAAAAAADAAAAAwAAAPMwAAAAlwB0AQAAAAAAAAAAagIAAAAAAAAAAAAAAAAAAAAAAAB8AKsBAAAAAAAAfQF8AVMAcgQAAABymAAAACkC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AAByQgAAAHJFAAAAckkAAAByTQAAAHJRAAAAclUAAAByWQAAAHJcAAAAcmAAAAByZQAAAHJoAAAAcmsAAABybgAAAHJyAAAAcnUAAAByeAAAAHJ8AAAAcn8AAABygwAAAHKHAAAAcosAAABykwAAAHKWAAAAcpwAAABynwAAAHKpAAAAcrQAAAByuAAAAHK9AAAAcsAAAABywwAAAHLHAAAAcsoAAAByzAAAAHIFAAAAcg0AAAByCwAAANoIPG1vZHVsZT5yzgAAAAEAAABz8wAAAPADAQEB2wAS8goDASDyDAIBEPIKAgEY8goCARbyCgIBFfIKAgEa8goCAR/yCgIBEfIKAgER8goCARHyCgIBGfIKAgEZ8goCARnyCgIBFvIKAgEV8g4BASTyCAEBJvIIAgEV8goCARbyCgIBHPIKAgEb8goCARnyCgIBGfIKAgEX8goCARjyCgIBEfIKAgER8goCARHyCgIBEvIKAgES8goCARLyCgIBG/IKAgEb8goDARryDAcBF/IUAgEY8g4CARbyCgIBFvIMCAET8hoGARXyEgIBF/IKAgEX8goCARjyCgIBG/IKAgEb8goCARvzCgcBFXINAAAA
'''


def test_compare():
    """Test string comparison"""
    try:
        As.s1
        As.s2
        As.s3
        print('Variable s1, s2, and s3 found!')
    except:
        print('Variable s1, s2, or s3 does not exist')
        assert False
    try:
        As.checkS1S2
        As.checkS1S3
        print('Variable checkS1S2 and checkS1S3 found!')
    except:
        print('Variable checkS1S2 or checkS1S3 does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    print(f'locals = {locals()}')

    if As.checkS1S2 != locals()['compare_strings'](As.s1, As.s2, As.s3)[0]:
        print(f'Incorrect checkS1S2 = {As.checkS1S2}')
        assert False
    else:
        print(f'Correct checkS1S2 = {As.checkS1S2}')
    if As.checkS1S3 != locals()['compare_strings'](As.s1, As.s2, As.s3)[1]:
        print(f'Incorrect checkS1S3 = {As.checkS1S3}')
        assert False
    else:
        print(f'Correct checkS1S3 = {As.checkS1S3}')
    print(f'Passed to test string comparison')


def test_concatenate():
    """Concatenate two strings"""
    try:
        As.first
        As.last
        print('Variable first and last found!')
    except:
        print('Variable "first" or "last" does not exist')
        assert False
    try:
        As.name
        print('Variable "name" found!')
    except:
        print('Variable "name" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.name != locals()['get_name'](As.first, As.last):
        print(f'Incorrect name = {As.name}')
        assert False
    else:
        print(f'Correct name = {As.name}')


def test_repeat():
    """repeat strings"""
    try:
        As.large_string
        print('Variable "large_string" found!')
    except:
        print('Variable "large_string" does not exist')
        assert False

    name = As.first + ' ' + As.last
    exec(marshal.loads(base64.b64decode(solution)))
    if As.large_string != locals()['get_large_string'](name):
        assert False
    else:
        print(f'Correct large_string')


def test_test_string():
    """Test strings with in and not in"""
    try:
        As.checkFirst
        As.checkLast
        print('Variable "checkFirst" and "checkLast" found!')
    except:
        print('Variable "checkFirst" or "checkLast" does not exist')
        assert False
    name = As.first + ' ' + As.last
    exec(marshal.loads(base64.b64decode(solution)))
    if As.checkFirst != locals()['get_checkFirst'](name, As.first):
        print(f'Incorrect checkFirst = {As.checkFirst}')
        assert False
    else:
        print(f'Correct checkFirst = {As.checkFirst}')
    if As.checkLast != locals()['get_checkLast'](name, As.last):
        print(f'Incorrect checkLast = {As.checkLast}')
        assert False
    else:
        print(f'Correct checkLast = {As.checkLast}')


def test_length():
    """Test string length and f-string formatting"""
    try:
        As.L_large_string
        As.format_large_string
        print('Variable "L_large_string" and "format_large_string" found!')
    except:
        print('Variable "L_large_string" or "format_large_string" does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    if As.L_large_string != locals()['get_L_large_string'](As.large_string):
        print(f'Incorrect L_large_string length = {As.L_large_string}')
        assert False
    else:
        print(f'Correct L_large_string length = {As.L_large_string}')
    if As.format_large_string != locals()['get_format_large_string'](As.L_large_string):
        print(f'Incorrect format_large_string')
        assert False
    else:
        print(f'Correct format_large_string')


def test_positive_indexing():
    """Test string positive indexing"""
    try:
        As.name1
        As.name2
        As.nameN
        print('Variable "name1", "name2" and "nameN" found!')
    except:
        print('Variable "name1", "name2" or "nameN" does not exist')
        assert False
    name = As.first + ' ' + As.last
    exec(marshal.loads(base64.b64decode(solution)))
    if As.name1 != locals()['get_name1'](name):
        print(f'Incorrect name1 = {As.name1}')
        assert False
    else:
        print(f'Correct name1 = {As.name1}')
    if As.name2 != locals()['get_name2'](name):
        print(f'Incorrect name2 = {As.name2}')
        assert False
    else:
        print(f'Correct name2 = {As.name2}')
    if As.nameN != locals()['get_nameN'](name):
        print(f'Incorrect nameN = {As.nameN}')
        assert False
    else:
        print(f'Correct nameN = {As.nameN}')


def test_negative_indexing():
    """Test string negative indexing"""
    try:
        As.reverse_name1
        As.reverse_name2
        As.reverse_nameN
        print('Variable "reverse_name1", "reverse_name2" and "reverse_name1" found!')
    except:
        print(
            'Variable "reverse_name1", "reverse_name2" or "reverse_nameN" does not exist')
        assert False
    name = As.first + ' ' + As.last
    exec(marshal.loads(base64.b64decode(solution)))
    if As.reverse_name1 != locals()['get_reverse_name1'](name):
        print(f'Incorrect reverse_name1 = {As.reverse_name1}')
        assert False
    else:
        print(f'Correct reverse_name1 = {As.reverse_name1}')
    if As.reverse_name2 != locals()['get_reverse_name2'](name):
        print(f'Incorrect reverse_name2 = {As.reverse_name2}')
        assert False
    else:
        print(f'Correct reverse_name2 = {As.reverse_name2}')
    if As.reverse_nameN != locals()['get_reverse_nameN'](name):
        print(f'Incorrect reverse_nameN = {As.reverse_nameN}')
        assert False
    else:
        print(f'Correct reverse_nameN = {As.reverse_nameN}')


def test_slicing():
    """Test string slicing"""
    try:
        As.first_copy
        As.last_copy
        print('Variable "first_copy" and "first_copy" found!')
    except:
        print('Variable "first_copy" or "last_copy" does not exist')
        assert False
    name = As.first + ' ' + As.last
    exec(marshal.loads(base64.b64decode(solution)))
    if As.first_copy != locals()['get_first_copy'](name, As.first):
        print(f'Incorrect first_copy = {As.first_copy}')
        assert False
    else:
        print(f'Correct first_copy = {As.first_copy}')
    if As.last_copy != locals()['get_last_copy'](name, As.first):
        print(f'Incorrect last_copy = {As.last_copy}')
        assert False
    else:
        print(f'Correct last_copy = {As.last_copy}')


def test_combined_list():
    """Test combined list"""
    try:
        As.mixed_list
        As.mixed_list2
        print('Variable "mixed_list" and "mixed_list2" found!')
    except:
        print('Variable "mixed_list" or "mixed_list2" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.combined_list != locals()['get_combined_list'](As.mixed_list, As.mixed_list2):
        print(f'Incorrect combined_list = {As.combined_list}')
        assert False
    else:
        print(f'Correct combined_list = {As.combined_list}')


def test_combined_tuple():
    """Test combined tuple"""
    try:
        As.mixed_tuple
        As.mixed_tuple2
        print('Variable "mixed_tuple" and "mixed_tuple2" found!')
    except:
        print('Variable "mixed_tuple" or "mixed_tuple2" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.combined_tuple != locals()['get_combined_tuple'](As.mixed_tuple, As.mixed_tuple2):
        print(f'Incorrect combined_tuple = {As.combined_tuple}')
        assert False
    else:
        print(f'Correct combined_tuple = {As.combined_tuple}')


def test_long_list():
    """Test long list"""
    try:
        As.long_list
        print('Variable "long_list" found!')
    except:
        print('Variable "long_list" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.long_list != locals()['get_long_list']():
        print(f'Incorrect long_list = {As.long_list}')
        assert False
    else:
        print(f'Correct long_list = {As.long_list}')


def test_long_tuple():
    """Test long tuple"""
    try:
        As.long_tuple
        print('Variable "long_tuple" found!')
    except:
        print('Variable "long_tuple" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.long_tuple != locals()['get_long_tuple']():
        print(f'Incorrect long_tuple = {As.long_tuple}')
        assert False
    else:
        print(f'Correct long_tuple = {As.long_tuple}')


def test_check_first_list():
    """Test check first list"""
    try:
        As.check_first_list
        print('Variable "check_first_list" found!')
    except:
        print('Variable "check_first_list" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.check_first_list != locals()['get_check_first_list'](As.combined_list):
        print(f'Incorrect check_first_list = {As.check_first_list}')
        assert False
    else:
        print(f'Correct check_first_list = {As.check_first_list}')


def test_check_last_list():
    """Test check last list"""
    try:
        As.check_last_list
        print('Variable "check_last_list" found!')
    except:
        print('Variable "check_last_list" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.check_last_list != locals()['get_check_last_list'](As.combined_list):
        print(f'Incorrect check_last_list = {As.check_last_list}')
        assert False
    else:
        print(f'Correct check_last_list = {As.check_last_list}')


def test_check_1_tuple():
    """Test check 1 tuple"""
    try:
        As.combined_tuple
        print('Variable "combined_tuple" found!')
    except:
        print('Variable "combined_tuple" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.check_1_tuple != locals()['get_check_1_tuple'](As.combined_tuple):
        print(f'Incorrect check_1_tuple = {As.check_1_tuple}')
        assert False
    else:
        print(f'Correct check_1_tuple = {As.check_1_tuple}')


def test_check_5_tuple():
    """Test check 5 tuple"""
    try:
        As.combined_tuple
        print('Variable "combined_tuple" found!')
    except:
        print('Variable "combined_tuple" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.check_5_tuple != locals()['get_check_5_tuple'](As.combined_tuple):
        print(f'Incorrect check_5_tuple = {As.check_5_tuple}')
        assert False
    else:
        print(f'Correct check_5_tuple = {As.check_5_tuple}')


def test_L_long_list():
    """Test L long list"""
    try:
        As.L_long_list
        print('Variable "L_long_list" found!')
    except:
        print('Variable "L_long_list" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.L_long_list != locals()['get_L_long_list'](As.long_list):
        print(f'Incorrect L_long_list = {As.L_long_list}')
        assert False
    else:
        print(f'Correct L_long_list = {As.L_long_list}')


def test_L_long_tuple():
    """Test L long tuple"""
    try:
        As.L_long_tuple
        print('Variable "L_long_tuple" found!')
    except:
        print('Variable "L_long_tuple" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.L_long_tuple != locals()['get_L_long_tuple'](As.long_tuple):
        print(f'Incorrect L_long_tuple = {As.L_long_tuple}')
        assert False
    else:
        print(f'Correct L_long_tuple = {As.L_long_tuple}')


def test_list1():
    """Test list1"""
    try:
        As.list1
        print('Variable "list1" found!')
    except:
        print('Variable "list1" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.list1 != locals()['get_list1'](As.combined_list):
        print(f'Incorrect list1 = {As.list1}')
        assert False
    else:
        print(f'Correct list1 = {As.list1}')


def test_list2():
    """Test list2"""
    try:
        As.list2
        print('Variable "list2" found!')
    except:
        print('Variable "list2" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.list2 != locals()['get_list2'](As.combined_list):
        print(f'Incorrect list2 = {As.list2}')
        assert False
    else:
        print(f'Correct list2 = {As.list2}')


def test_listN():
    """Test listN"""
    try:
        As.listN
        print('Variable "listN" found!')
    except:
        print('Variable "listN" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.listN != locals()['get_listN'](As.combined_list):
        print(f'Incorrect listN = {As.listN}')
        assert False
    else:
        print(f'Correct listN = {As.listN}')


def test_tuple1():
    """Test tuple1"""
    try:
        As.tuple1
        print('Variable "tuple1" found!')
    except:
        print('Variable "tuple1" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.tuple1 != locals()['get_tuple1'](As.combined_tuple):
        print(f'Incorrect tuple1 = {As.tuple1}')
        assert False
    else:
        print(f'Correct tuple1 = {As.tuple1}')


def test_tuple2():
    """Test tuple2"""
    try:
        As.tuple2
        print('Variable "tuple2" found!')
    except:
        print('Variable "tuple2" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.tuple2 != locals()['get_tuple2'](As.combined_tuple):
        print(f'Incorrect tuple2 = {As.tuple2}')
        assert False
    else:
        print(f'Correct tuple2 = {As.tuple2}')


def test_tupleN():
    """Test tupleN"""
    try:
        As.tupleN
        print('Variable "tupleN" found!')
    except:
        print('Variable "tupleN" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.tupleN != locals()['get_tupleN'](As.combined_tuple):
        print(f'Incorrect tupleN = {As.tupleN}')
        assert False
    else:
        print(f'Correct tupleN = {As.tupleN}')


def test_first_four_list():
    """Test first four list"""
    try:
        As.first_four_list
        print('Variable "first_four_list" found!')
    except:
        print('Variable "first_four_list" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.first_four_list != locals()['get_first_four_list'](As.combined_list):
        print(f'Incorrect first four list = {As.first_four_list}')
        assert False
    else:
        print(f'Correct first four list = {As.first_four_list}')


def test_last_four_tuple():
    """Test last four tuple"""
    try:
        As.last_four_tuple
        print('Variable "last_four_tuple" found!')
    except:
        print('Variable "last_four_tuple" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.last_four_tuple != locals()['get_last_four_tuple'](As.combined_tuple):
        print(f'Incorrect last four tuple = {As.last_four_tuple}')
        assert False
    else:
        print(f'Correct last four tuple = {As.last_four_tuple}')


def test_long_list_copy():
    """Test long list copy"""
    try:
        As.long_list
        print('Variable "long_list" found!')
    except:
        print('Variable "long_list" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.long_list_copy != locals()['get_long_list_copy'](As.long_list):
        print(f'Incorrect long list copy = {As.long_list_copy}')
        assert False
    else:
        print(f'Correct long list copy = {As.long_list_copy}')


def test_long_tuple_copy():
    """Test long tuple copy"""
    try:
        As.tuple_error
        print('Variable "tuple_error" found!')
    except:
        print('Variable "tuple_error" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.tuple_error != locals()['get_long_tuple_copy'](As.long_tuple):
        print(f'Incorrect tuple error = {As.tuple_error}')
        assert False
    else:
        print(f'Correct tuple error = {As.tuple_error}')


def test_list_of_list():
    """Test list of list"""
    try:
        As.list_of_list
        print('Variable "list_of_list" found!')
    except:
        print('Variable "list_of_list" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.list_of_list != locals()['get_list_of_list']():
        print(f'Incorrect list of list = {As.list_of_list}')
        assert False
    else:
        print(f'Correct list of list = {As.list_of_list}')


def test_long_array():
    """Test long array"""
    try:
        As.long_array
        print('Variable "long_array" found!')
    except:
        print('Variable "long_array" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if (As.long_array != locals()['get_long_array'](As.long_list)).all():
        print(f'Incorrect long array = {As.long_array}')
        assert False
    else:
        print(f'Correct long array = {As.long_array}')


def test_big_matrix():
    """Test big matrix"""
    try:
        As.big_matrix
        print('Variable "big_matrix" found!')
    except:
        print('Variable "big_matrix" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if (As.big_matrix != locals()['get_big_matrix'](As.list_of_list)).all():
        print(f'Incorrect big matrix = {As.big_matrix}')
        assert False
    else:
        print(f'Correct big matrix = {As.big_matrix}')


def test_watches():
    """Test watches"""
    try:
        As.watches
        print('Variable "watches" found!')
    except:
        print('Variable "watches" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.watches != locals()['get_watches']():
        print(f'Incorrect watches = {As.watches}')
        assert False
    else:
        print(f'Correct watches = {As.watches}')


def test_user_info():
    """Test user info"""
    try:
        As.user_info
        print('Variable "user_info" found!')
    except:
        print('Variable "user_info" does not exist')
        assert False
    exec(marshal.loads(base64.b64decode(solution)))
    if As.user_info != locals()['get_updated_user_info']():
        print(f'Incorrect user info = {As.user_info}')
        assert False
    else:
        print(f'Correct user info = {As.user_info}')


def test_check_user1():
    """Test check user1"""
    try:
        As.check_user1
        print('Variable "check_user1" found!')
    except:
        print('Variable "check_user1" does not exist')
        assert False
    user_info = {
        'user1': 12345,
        'user2': 58493,
        'user3': 21297
    }
    exec(marshal.loads(base64.b64decode(solution)))
    if As.check_user1 != locals()['get_check_user1'](user_info):
        print(f'Incorrect check user1 = {As.check_user1}')
        assert False
    else:
        print(f'Correct check user1 = {As.check_user1}')


def test_check_user2():
    """Test check user2"""
    try:
        As.check_user2
        print('Variable "check_user2" found!')
    except:
        print('Variable "check_user2" does not exist')
        assert False
    user_info = {
        'user1': 12345,
        'user2': 58493,
        'user3': 21297
    }
    exec(marshal.loads(base64.b64decode(solution)))
    if As.check_user2 != locals()['get_check_user2'](user_info):
        print(f'Incorrect check user2 = {As.check_user2}')
        assert False
    else:
        print(f'Correct check user2 = {As.check_user2}')


def test_number_users():
    """Test number users"""
    try:
        As.number_users
        print('Variable "number_users" found!')
    except:
        print('Variable "number_users" does not exist')
        assert False
    user_info = {
        'user1': 12345,
        'user2': 58493,
        'user3': 21297
    }
    exec(marshal.loads(base64.b64decode(solution)))
    if As.number_users != locals()['get_number_users'](user_info):
        print(f'Incorrect number users = {As.number_users}')
        assert False
    else:
        print(f'Correct number users = {As.number_users}')


def test_user_password_1():
    """Test user password 1"""
    try:
        As.user_password_1
        print('Variable "user_password_1" found!')
    except:
        print('Variable "user_password_1" does not exist')
        assert False
    user_info = {
        'user1': 12345,
        'user2': 58493,
        'user3': 21297
    }
    exec(marshal.loads(base64.b64decode(solution)))
    if As.user_password_1 != locals()['get_user_password_1'](user_info):
        print(f'Incorrect user password 1 = {As.user_password_1}')
        assert False
    else:
        print(f'Correct user password 1 = {As.user_password_1}')


def test_user_password_2():
    """Test user password 2"""
    try:
        As.user_password_2
        print('Variable "user_password_2" found!')
    except:
        print('Variable "user_password_2" does not exist')
        assert False
    user_info = {
        'user1': 12345,
        'user2': 58493,
        'user3': 21297
    }
    exec(marshal.loads(base64.b64decode(solution)))
    if As.user_password_2 != locals()['get_user_password_2'](user_info):
        print(f'Incorrect user password 2 = {As.user_password_2}')
        assert False
    else:
        print(f'Correct user password 2 = {As.user_password_2}')


def test_user_password_3():
    """Test user password 3"""
    try:
        As.user_password_3
        print('Variable "user_password_3" found!')
    except:
        print('Variable "user_password_3" does not exist')
        assert False
    user_info = {
        'user1': 12345,
        'user2': 58493,
        'user3': 21297
    }
    exec(marshal.loads(base64.b64decode(solution)))
    if As.user_password_3 != locals()['get_user_password_3'](user_info):
        print(f'Incorrect user password 3 = {As.user_password_3}')
        assert False
    else:
        print(f'Correct user password 3 = {As.user_password_3}')