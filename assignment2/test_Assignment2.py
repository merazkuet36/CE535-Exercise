import Assignment2
import marshal
import base64
import math

solution = '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'

def test_tolerance():
    try:
        Assignment2.tolerance
        print('Variable tolerance found!')
    except:
        print('Variable tolerance does not exist')
        assert False

    if not isinstance(Assignment2.tolerance, float):
        print(f'Invalid tolerance type = {type(Assignment2.tolerance)}')
        assert False
    else:
        print(f'Valid tolerance = {Assignment2.tolerance}')

    if Assignment2.tolerance < 0 or Assignment2.tolerance > 0.1:
        print(f'Invalid tolerance = {Assignment2.tolerance}')
        assert False
    else:
        print(f'Valid tolerance = {Assignment2.tolerance}')


def test_pi_approx():
    try:
        Assignment2.pi_approx
        print('Variable pi_approx found!')
    except:
        print('Variable pi_approx does not exist')
        assert False

    if not isinstance(Assignment2.pi_approx, float):
        print(f'Invalid pi_approx type = {type(Assignment2.pi_approx)}')
        assert False
    else:
        print(f'Valid pi_approx = {Assignment2.pi_approx}')

    exec(marshal.loads(base64.b64decode(solution)))
    pi_approx = locals()['compute_pi'](Assignment2.tolerance)

    if abs(pi_approx - Assignment2.pi_approx) > Assignment2.tolerance:
        print(f'Invalid pi_approx = {Assignment2.pi_approx}')
        assert False
    else:
        print(f'Valid pi_approx = {Assignment2.pi_approx}')


# schedule = [
#     [6, 11, 'Albany'],
#     [6, 42, 'Salem'],
#     [7, 24, 'Oregon City'],
#     [8, 20, 'Portland'],
#     [8, 38, 'Vancouver'],
#     [9, 11, 'Kelso-Longview'],
#     [9, 52, 'Centralia'],
#     [10, 13, 'Olympia-Lacey'],
#     [10, 53, 'Tacoma'],
#     [11, 22, 'Tukwila']]


# def test_schedule():
#     try:
#         Assignment2.schedule
#         print('Variable schedule found!')
#     except:
#         print('Variable schedule does not exist')
#         assert False
#     if not isinstance(Assignment2.schedule, list):
#         print(f'Invalid schedule = {Assignment2.schedule}')
#         assert False
#     else:
#         print(f'Valid schedule = {Assignment2.schedule}')

#     if Assignment2.schedule != schedule:
#         print(f'Invalid schedule = {Assignment2.schedule}')
#         assert False
#     else:
#         print(f'Valid schedule = {Assignment2.schedule}')


# def test_start_stop():
#     try:
#         Assignment2.start_stop
#         print('Variable start_stop found!')
#     except:
#         print('Variable start_stop does not exist')
#         assert False

#     if not isinstance(Assignment2.start_stop, str):
#         print(f'Invalid start_stop = {Assignment2.start_stop}')
#         assert False
#     else:
#         print(f'Valid start_stop = {Assignment2.start_stop}')

#     if Assignment2.start_stop not in [s[2] for s in schedule]:
#         print(f'Invalid start_stop = {Assignment2.start_stop}')
#         assert False
#     else:
#         print(f'Valid start_stop = {Assignment2.start_stop}')


# def test_end_stop():
#     try:
#         Assignment2.end_stop
#         print('Variable end_stop found!')
#     except:
#         print('Variable end_stop does not exist')
#         assert False
#     if not isinstance(Assignment2.end_stop, str):
#         print(f'Invalid end_stop = {Assignment2.end_stop}')
#         assert False
#     else:
#         print(f'Valid end_stop = {Assignment2.end_stop}')
#     if Assignment2.end_stop not in [s[2] for s in schedule]:
#         print(f'Invalid end_stop = {Assignment2.end_stop}')
#         assert False
#     else:
#         print(f'Valid end_stop = {Assignment2.end_stop}')


# def test_start_time():
#     try:
#         Assignment2.start_time
#         print('Variable start_time found!')
#     except:
#         print('Variable start_time does not exist')
#         assert False
#     if not isinstance(Assignment2.start_time, int) and not isinstance(Assignment2.start_time, float):
#         print(f'Invalid start_time = {Assignment2.start_time}')
#         assert False
#     else:
#         print(f'Valid start_time = {Assignment2.start_time}')

#     exec(marshal.loads(base64.b64decode(solution)))
#     travel_time_result, start_time, end_time = locals()['travel_time'](
#         Assignment2.start_stop, Assignment2.end_stop)

#     if Assignment2.start_time != start_time:
#         print(f'Invalid start_time = {Assignment2.start_time}')
#         assert False
#     else:
#         print(f'Valid start_time = {Assignment2.start_time}')


# def test_end_time():
#     try:
#         Assignment2.end_time
#         print('Variable end_time found!')
#     except:
#         print('Variable end_time does not exist')
#         assert False
#     if not isinstance(Assignment2.end_time, int) and not isinstance(Assignment2.end_time, float):
#         print(f'Invalid end_time = {Assignment2.end_time}')
#         assert False
#     else:
#         print(f'Valid end_time = {Assignment2.end_time}')

#     exec(marshal.loads(base64.b64decode(solution)))
#     travel_time_result, start_time, end_time = locals()['travel_time'](
#         Assignment2.start_stop, Assignment2.end_stop)

#     if Assignment2.end_time != end_time:
#         print(f'Invalid end_time = {Assignment2.end_time}')
#         assert False
#     else:
#         print(f'Valid end_time = {Assignment2.end_time}')


# def test_travel_time():
#     try:
#         Assignment2.travel_time
#         print('Variable travel_time found!')
#     except:
#         print('Variable travel_time does not exist')
#         assert False
#     if not isinstance(Assignment2.travel_time, int) and not isinstance(Assignment2.travel_time, float):
#         print(f'Invalid travel_time = {Assignment2.travel_time}')
#         assert False
#     else:
#         print(f'Valid travel_time = {Assignment2.travel_time}')

#     exec(marshal.loads(base64.b64decode(solution)))
#     travel_time_result, start_time, end_time = locals()['travel_time'](
#         Assignment2.start_stop, Assignment2.end_stop)
#     if Assignment2.travel_time != travel_time_result:
#         print(f'Invalid travel_time = {Assignment2.travel_time}')
#         assert False
#     else:
#         print(f'Valid travel_time = {Assignment2.travel_time}')

