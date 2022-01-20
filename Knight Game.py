import operator
from collections import deque

# import sys
# from io import StringIO
#
# input_1 = """5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
# """
#
# input_2 = """2
# KK
# KK
# """
#
# input_3 = """8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
# """
#
# sys.stdin = StringIO(input_2)


class Horse:
    def __init__(self, position):
        self.position = position
        self.connections = 0


def count_horse_connections(the_matrix: list, horse_position: list, horse_connections: int, the_size: int):
    r, c = horse_position
    if r - 2 >= 0 and c - 1 >= 0 and the_matrix[r - 2][c - 1] == 'K':
        horse_connections += 1
    if r - 2 >= 0 and c + 1 < the_size and the_matrix[r - 2][c + 1] == 'K':
        horse_connections += 1
    if r - 1 >= 0 and c - 2 >= 0 and the_matrix[r - 1][c - 2] == 'K':
        horse_connections += 1
    if r - 1 >= 0 and c + 2 < the_size and the_matrix[r - 1][c + 2] == 'K':
        horse_connections += 1
    if r + 1 < the_size and c - 2 >= 0 and the_matrix[r + 1][c - 2] == 'K':
        horse_connections += 1
    if r + 1 < the_size and c + 2 < the_size and the_matrix[r + 1][c + 2] == 'K':
        horse_connections += 1
    if r + 2 < the_size and c - 1 >= 0 and the_matrix[r + 2][c - 1] == 'K':
        horse_connections += 1
    if r + 2 < the_size and c + 1 < size and the_matrix[r + 2][c + 1] == 'K':
        horse_connections += 1
    return horse_connections


def find_every_horse(the_matrix: list, the_size: int, list_of_horses: list):
    for r in range(the_size):
        for c in range(the_size):
            if the_matrix[r][c] == 'K':
                list_of_horses.append(Horse([r, c]))
    return list_of_horses


size = int(input())
matrix = [[y for y in input()] for x in range(size)]

deleted_horses = 0

while True:
    # create a list of classes - all horses: position in matrix [row, col]
    # and number of connections with other horses = 0
    horses = []

    find_every_horse(matrix, size, horses)
    # go through the list of all horses and find the number of connections for every horse
    for horse in horses:
        horse.connections = count_horse_connections(matrix, horse.position, horse.connections, size)
    # sort the list by number of connection in descending way
    # so the first horse in sorted_horses now is the one with most connections with other horses and so on
    sorted_horses = deque(sorted(horses, key=operator.attrgetter('connections'), reverse=True))
    # go through sorted_horses and delete a horse if he has connections
    # with this logic we delete horses with MOST connections till we have 0 connections for the whole matrix
    all_connections = 0
    for horse in sorted_horses:
        current_horse_connections = count_horse_connections(matrix, horse.position, 0, size)
        all_connections += current_horse_connections
        if all_connections > 0:
            break
    # if all_connections is 0 means we have no connections in the matrix so the task is done
    if all_connections == 0:
        break
    # but if all_connections > 0 that means we have to replace the horse with most connections with "0"
    # and delete the horse from the list of horses - sorted_horses.popleft()
    # and try again the whole circle till all_connections == 0
    r, c = sorted_horses[0].position
    matrix[r][c] = '0'
    sorted_horses.popleft()
    deleted_horses += 1

print(deleted_horses)
