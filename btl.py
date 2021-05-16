# NOTE: Python 3.7+ or CPython 3.6

def sort_scores(arr): # arr=[2,9,4,5,1,8]
  result = {}
  # convert [2,9,4,5,1,8] to {0: 2, 1: 9, 2: 4, 3: 5, 4: 1, 5: 8}
  for i in range(len(arr)):
    result[i] = arr[i]

  # sort dictionary by value
  sorted_scores = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
  return sorted_scores # result: {4: 1, 0: 2, 2: 4, 3: 5, 5: 8, 1: 9}

def sort_scores_in_weeks(arrs): # arrs=[[2,9,4,5,1,8], [5,1,9,2,6,7], [1,2,7,5,3,6]]
  return [sort_scores(arr)
            for arr in arrs]

print(sort_scores_in_weeks([[2,9,4,5,1,8], [5,1,9,2,6,7], [1,2,7,5,3,6]]))

# Bắt cặp học viên
def pair_students(sorted_scored): # sorted_scored: {4: 1, 0: 2, 2: 4, 3: 5, 5: 8, 1: 9}
  length = len(sorted_scored)
  pairs = [(i, length - i - 1) 
            for i in range(length//2)] # pairs: [(0, 5), (1, 4), (2, 3)]
  cmax = 0
  for pair in pairs:
    cmax += min(10, sorted_scored[pair[0]] + sorted_scored[pair[1]]) # cmax = 29
  return {'pairs': pairs, 'cmax': cmax}

print(pair_students(sort_scores([2,9,4,5,1,8])))


# TODO: 
# - Chạy pair_students cho điểm của tuần kế tiếp
# - So sánh cmax của tuần kế tiếp => chọn cách bắt cặp nào có cmax nào lớn hơn
# - Tiếp tục cho hết 10 tuần 