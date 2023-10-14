def transformation(line_a, line_b, line_c):
    result = {}
    for no, line in enumerate((line_a, line_b, line_c)):
        for key, value in line:
            if key not in result:
                result[key] = [0, 0, 0]
            result[key][no] = value
        
        return result


line_a = ((1, 2), (4, 3), (5, 1)) 
line_b = ((1, 3), (2, 4), (5, 2)) 
line_c = ((2, 5), (4, 1), (10, 1))
print(transformation(line_a, line_b, line_c))