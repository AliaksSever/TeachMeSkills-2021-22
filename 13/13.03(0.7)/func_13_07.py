def sum_of_elements(self):
    sum = 0
    for i in self.data:
        for j in i:
            sum += j
    return sum


def max_el_of_matrix(self):
    max_el = self.data[0][0]
    for i in self.data:
        for j in range(len(i)):
            if max_el < i[j]:
                max_el = i[j]
    return max_el


def min_el_of_matrix(self):
    min_el = self.data[0][0]
    for i in self.data:
        for j in range(len(i)):
            if min_el > i[j]:
                min_el = i[j]
    return min_el