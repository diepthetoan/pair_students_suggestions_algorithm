def sort_scores(arr):
  result = {}
  print('------')
  for i in range(len(arr)):
    result[i] = arr[i]

  sorted_scores = {k: v for k, v in sorted(result.items(), key=lambda item: item[1])}
  return sorted_scores
  
print(sort_scores([2,9,4,5,1,8]))
