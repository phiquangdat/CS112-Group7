import copy

max_len = 0
sum_val = 0
res = []

def find_max_length(A, N, X, len_, curr_sum, curr_res):
    global max_len, sum_val, res
    if curr_sum % X == 0 and len_ > max_len:
        max_len = len_
        sum_val = curr_sum
        res = copy.deepcopy(curr_res)
    if N == 0:
        return
    find_max_length(A[1:], N-1, X, len_, curr_sum, curr_res)
    curr_res[len_] = A[0]
    find_max_length(A[1:], N-1, X, len_+1, curr_sum+A[0], curr_res)

N, X = map(int, input().split())
A = list(map(int, input().split()))

curr_res = [0] * N
find_max_length(A, N, X, 0, 0, curr_res)

print(max_len)
print(sum_val)
for i in range (max_len):
    print(res[i], end = ' ')
    