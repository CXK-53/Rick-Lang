def bin_search(arr, target):
     bottom = 0
     top = len(arr) - 1
     mid = 0
     while bottom < top:
          mid = (bottom + top) // 2

          if arr[mid] < target:
               bottom = mid + 1

          elif arr[mid] > target:
               top = mid - 1

          else:
               return True
     return False