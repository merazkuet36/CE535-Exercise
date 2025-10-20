import Ex8
import marshal
import base64
import math

solution = '4wAAAAAAAAAAAAAAAAEAAAAAAAAA8xYAAACXAGQAhABaAGQBhABaAWQChABaAnkDKQRjAQAAAAAAAAAAAAAABQAAAAMAAADzmAAAAJcAZwB9AXQBAAAAAAAAAABkAXwAZAJ6AAAAqwIAAAAAAABEAF01AAB9AmQDfQN0AQAAAAAAAAAAZAF8AqsCAAAAAAAARABdDgAAfQR8AnwEegYAAGQEaygAAHMBjAxkBX0DAQBuAQQAfANzAYwlfAFqAwAAAAAAAAAAAAAAAAAAAAAAAHwCqwEAAAAAAAABAIw3BAB8AVMAKQZO6QIAAADpAQAAAFTpAAAAAEapAtoFcmFuZ2XaBmFwcGVuZCkF2gFO2gZwcmltZXPaAW7aCGlzX3ByaW1l2gFpcwUAAAAgICAgIPoKRXg4U29sdS5wedoLZmluZF9wcmltZXNyDwAAAAIAAABzXwAAAIAA4A0PgEb0BgAOE5AxkGGYAZFjjl2IAeATF4gI9AYAEheQcZghlhuIQeAPEJAxiXWYAYt64BsgkAjhEBXwDQASHfISAAwU4AwSj02JTZgh1Qwc8CEADhvwJAAMEoBN8wAAAABjBAAAAAAAAAAAAAAABgAAAAMAAADzmAAAAJcAfAB8AnoLAAB9BHwBfAN6CwAAfQVnAH0GdAEAAAAAAAAAAHwDqwEAAAAAAABEAF0vAAB9B3wFfAd6BQAAfQh0AQAAAAAAAAAAfAKrAQAAAAAAAEQAXRoAAH0JfAR8CXoFAAB9CnwGagMAAAAAAAAAAAAAAAAAAAAAAAB8CnwIZgKrAQAAAAAAAAEAjBwEAIwxBAB8BlMAKQFOcgYAAAApC9oBd9oBaNoBTXIJAAAA2gZzaXplX3jaBnNpemVfedoQbm9kZV9jb29yZGluYXRlc9oBatoBeXINAAAA2gF4cwsAAAAgICAgICAgICAgIHIOAAAA2hRnZXRfbm9kZV9jb29yZGluYXRlc3IbAAAAHQAAAHNiAAAAgADYDQ6QEYlVgEbYDQ6QEYlVgEbYFxnQBBTcDRKQMY5YiAHYDBKQUYlKiAHcERaQcZYYiEHYEBaYEZEKiEHYDBzXDCPRDCOgUagBoEbVDCvxBQASGvAFAA4W8AoADBzQBBtyEAAAAGMBAAAAAAAAAAAAAAAEAAAAAwAAAPMwAAAAlwBpAH0BZAF9AnwARABdDAAAfQN8A3wBfAI8AAAAfAJkAXoNAAB9AowOBAB8AVMAKQJOcgQAAACpACkEchcAAADaBW5vZGVz2ghub2RlX3RhZ9oFY29vcmRzBAAAACAgICByDgAAANoJZ2V0X25vZGVzciEAAAArAAAAcy8AAACAANgMDoBF2A8QgEjbESGIBdgaH4gFiGiJD9gIEJBBiQ2JCPAFABIi8AYADBGATHIQAAAATikDcg8AAAByGwAAAHIhAAAAch0AAAByEAAAAHIOAAAA2gg8bW9kdWxlPnIiAAAAAQAAAHMUAAAA8AMBAQHyBBcBEvI2CQEc8xwGARFyEAAAAA=='


def test_N():
    try:
        Ex8.N
        print('Variable N found!')
    except:
        print('Variable N does not exist')
        assert False
    if not isinstance(Ex8.N, float) and not isinstance(Ex8.N, int):
        print(f'Invalid N = {Ex8.N}')
        assert False
    else:
        print(f'Valid N = {Ex8.N}')
    if Ex8.N < 2 or Ex8.N > 1000:
        print(f'N should in the range(2, 1000) for testing purpose')
        assert False
    else:
        print(f'Valid N = {Ex8.N}')


def test_primes():
    try:
        Ex8.primes
        print('Variable primes found!')
    except:
        print('Variable primes does not exist')
        assert False

    exec(marshal.loads(base64.b64decode(solution)))
    primes = locals()['find_primes'](Ex8.N)

    if len(Ex8.primes) != len(primes):
        print(f'Invalid number of primes = {len(Ex8.primes)}')
        assert False
    else:
        print(f'Valid number of primes = {len(Ex8.primes)}')

    for n in primes:
        if n not in Ex8.primes:
            print(f'Prime number {n} is not found in your list')
            assert False
        else:
            print(f'Prime number {n} is found in your list')


# def test_w():
#     try:
#         Ex8.w
#         print('Variable w found!')
#     except:
#         print('Variable w does not exist')
#         assert False
#     if not isinstance(Ex8.w, float) and not isinstance(Ex8.w, int):
#         print(f'Invalid w = {Ex8.w}')
#         assert False
#     else:
#         print(f'Valid w = {Ex8.w}')
#     if Ex8.w <= 0 or Ex8.w > 1000:
#         print(f'w should in the range(0, 1000) for testing purpose')
#         assert False
#     else:
#         print(f'Valid w = {Ex8.w}')


# def test_h():
#     try:
#         Ex8.h
#         print('Variable h found!')
#     except:
#         print('Variable h does not exist')
#         assert False
#     if not isinstance(Ex8.h, float) and not isinstance(Ex8.h, int):
#         print(f'Invalid h = {Ex8.h}')
#         assert False
#     else:
#         print(f'Valid h = {Ex8.h}')
#     if Ex8.h <= 0 or Ex8.h > 1000:
#         print(f'h should in the range(0, 1000) for testing purpose')
#         assert False
#     else:
#         print(f'Valid h = {Ex8.h}')


# def test_M():
#     try:
#         Ex8.M
#         print('Variable M found!')
#     except:
#         print('Variable M does not exist')
#         assert False
#     if not isinstance(Ex8.M, int):
#         print(f'Invalid M type = {type(Ex8.M)}')
#         assert False
#     else:
#         print(f'Valid M = {Ex8.M}')
#     if Ex8.M <= 0 or Ex8.M > 1000:
#         print(f'M should in the range(0, 1000) for testing purpose')
#         assert False
#     else:
#         print(f'Valid M = {Ex8.M}')


# def test_N():
#     try:
#         Ex8.N
#         print('Variable N found!')
#     except:
#         print('Variable N does not exist')
#         assert False
#     if not isinstance(Ex8.N, int):
#         print(f'Invalid N type = {type(Ex8.N)}')
#         assert False
#     else:
#         print(f'Valid N = {Ex8.N}')
#     if Ex8.N <= 0 or Ex8.N > 1000:
#         print(f'N should in the range(0, 1000) for testing purpose')
#         assert False
#     else:
#         print(f'Valid N = {Ex8.N}')


# def test_node_coordinates():
#     try:
#         Ex8.node_coordinates
#         print('Variable node_coordinates found!')
#     except:
#         print('Variable node_coordinates does not exist')
#         assert False

#     if not isinstance(Ex8.node_coordinates, list):
#         print(f'Invalid node_coordinates type = {type(Ex8.node_coordinates)}')
#         assert False
#     else:
#         print(f'Valid node_coordinates = {Ex8.node_coordinates}')

#     exec(marshal.loads(base64.b64decode(solution)))
#     node_coordinates = locals()['get_node_coordinates'](
#         Ex8.w, Ex8.h, Ex8.M, Ex8.N)
#     if len(Ex8.node_coordinates) != len(node_coordinates):
#         print(f'Invalid node_coordinates length = {len(Ex8.node_coordinates)}')
#         assert False
#     else:
#         print(f'Valid node_coordinates length = {len(Ex8.node_coordinates)}')

#     for i in range(len(Ex8.node_coordinates)):
#         if len(Ex8.node_coordinates[i]) != 2:
#             print(
#                 f'Invalid node_coordinates size = {len(Ex8.node_coordinates[i])}')
#             assert False

#         for j in [0, 1]:
#             if abs(Ex8.node_coordinates[i][j] - node_coordinates[i][j]) > 1e-6:
#                 print(
#                     f'Invalid node_coordinates[{i}][{j}] = {Ex8.node_coordinates[i][j]}')
#                 assert False
#             else:
#                 print(
#                     f'Valid node_coordinates[{i}][{j}] = {Ex8.node_coordinates[i][j]}')


# def test_nodes():
#     try:
#         Ex8.nodes
#         print('Variable nodes found!')
#     except:
#         print('Variable nodes does not exist')
#         assert False

#     if not isinstance(Ex8.nodes, dict):
#         print(f'Invalid nodes type = {type(Ex8.nodes)}')
#         assert False
#     else:
#         print(f'Valid nodes = {Ex8.nodes}')

#     exec(marshal.loads(base64.b64decode(solution)))
#     nodes = locals()['get_nodes'](Ex8.node_coordinates)

#     if len(Ex8.nodes) != len(nodes):
#         print(f'Invalid nodes length = {len(Ex8.nodes)}')
#         assert False
#     else:
#         print(f'Valid nodes length = {len(Ex8.nodes)}')

#     for tag in nodes:
#         if tag not in Ex8.nodes:
#             print(f'Missing node tag = {tag}')
#             assert False
#         crds = nodes[tag]
#         crds2 = Ex8.nodes[tag]
#         if len(crds) != 2:
#             print(f'Invalid node coordinates size = {len(crds)}')
#             assert False
#         for j in [0, 1]:
#             if abs(crds[j] - crds2[j]) > 1e-6:
#                 print(f'Invalid node coordinates[{tag}][{j}] = {crds[j]}')
#                 assert False
#             else:
#                 print(f'Valid node coordinates[{tag}][{j}] = {crds[j]}')