def solution(l, t):
    current_numbers = []
    lower_index = 0
    upper_index = 0

    for number in l:
        current_numbers.append(number)
        current_sum = sum(current_numbers)

        while current_sum >= t:
            if current_sum == t:
                return [lower_index, upper_index]
            else:
                current_numbers.pop(0)
                lower_index += 1
                current_sum = sum(current_numbers)
        upper_index += 1
    return [-1, -1]
