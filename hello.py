# NAME: OLOYEDE TOMIWA
# MATRIC NO: 230502051

def total_sum(arr):
    total = 0
    for i in arr:
        total += i
    return total
print(total_sum([1, 2, 3, 4, 5])) 

#Time Complexity

#O(n) — The function iterates through all n elements of the list once.#
#Each iteration performs a constant-time addition, so total work grows linearly with the size of the list.#

#Space Complexity

#O(1) — The function uses only a fixed amount of extra memory (total variable), regardless of the input size. The list itself is not copied or modified.#