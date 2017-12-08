import math

def distance_generator(maximum_distance):
    minimum_distance = maximum_distance // 2

    for i in range(4):
        for distance in range(maximum_distance, minimum_distance, -1):
            yield distance
        for distance in range(minimum_distance, maximum_distance):
            yield distance

def calculate_distance(start):
    root_rounded_up_to_nearest_odd_number = math.ceil(math.sqrt(start)) // 2 * 2 + 1
    maximum_value_on_square = root_rounded_up_to_nearest_odd_number ** 2
    maximum_distance = root_rounded_up_to_nearest_odd_number - 1

    distance_sequence = distance_generator(maximum_distance)

    for step in range(maximum_value_on_square, start, -1):
        next(distance_sequence)

    print(next(distance_sequence))

calculate_distance(312051)
