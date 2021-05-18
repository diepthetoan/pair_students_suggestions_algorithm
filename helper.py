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

# Dùng để tính cmax cho nhiều tuần tương ứng với 1 pairs nhất định 
def count_cmax(sorted_scored_array, pairs):
  cmax = 0
  # sorted_scores_before
  for sorted_scored in sorted_scored_array:
    for pair in pairs:
      cmax += min(10, sorted_scored[pair[0]] + sorted_scored[pair[1]])
  
  return cmax

# Bắt cặp học viên
def pair_students(sorted_scored): # sorted_scored: {4: 1, 0: 2, 2: 4, 3: 5, 5: 8, 1: 9}
  length = len(sorted_scored)
  keys = list(sorted_scored.keys())
  pairs = [(keys[i], keys[length - i - 1])
            for i in range(length//2)] # pairs: [(0, 5), (1, 4), (2, 3)]
  cmax = count_cmax([sorted_scored], pairs) # cmax = 29
  return {'sorted_scored': [sorted_scored], 'pairs': pairs, 'cmax': cmax}

print(pair_students(sort_scores([8.83, 7, 6.33, 9.67, 6.83, 9.67])))


def handle_algorithm(weeks):
  week_cmax = pair_students(sort_scores(weeks[0])) # {'sorted_scored': [[(0, 5), (1, 4), (2, 3)], []], 'pairs': pairs, 'cmax': cmax}
  for i in range(1, len(weeks)):
    sorted_scores_before = week_cmax['sorted_scored'] # array
    sorted_scores_week = sort_scores(weeks[i])

    # Tên biến lấy ví dụ đang xét ở tuần thứ 3
    # pairs students in a week
    paired_3 = pair_students(sorted_scores_week)

    # cmax33 là cmax của tuần thứ 3 với pairs 3
    # cmax_13_23 là cmax của 2 tuần 1 và 2 với pairs 3
    cmax33 = paired_3["cmax"]
    cmax_13_23 = count_cmax(sorted_scores_before, paired_3['pairs'])

    # cmax31 là cmax của tuần thứ 3 với pairs best (week_cmax['pairs'])
    # cmax_11_21 là cmax của 2 tuần 1 và 2 với pairs best (week_cmax['pairs'])
    cmax31 = count_cmax([sorted_scores_week], week_cmax['pairs'])
    cmax_11_21 = week_cmax['cmax']

    # SO sánh cmax của 3 tuần giữa: pairs 3 và pairs best và chọn pairs có cmax tổng lớn hơn 
    if cmax33 + cmax_13_23 > cmax31 + cmax_11_21:
      week_cmax['pairs'] = paired_3['pairs']
      week_cmax['cmax'] = cmax33 + cmax_13_23
    else:
      week_cmax['cmax'] = cmax31 + cmax_11_21
    
    week_cmax['sorted_scored'].append(sorted_scores_week)

  print('Result Paired:', week_cmax['pairs'])
  print('Result Cmax:', week_cmax['cmax'])


