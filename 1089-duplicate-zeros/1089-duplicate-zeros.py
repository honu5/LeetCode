class Solution(object):
    def duplicateZeros(self,arr):
      n = len(arr)
      zeros = arr.count(0)   # count total zeros to duplicate
      i = n - 1
      j = n + zeros - 1      # imaginary extended array

      # move from the end
      while i >= 0:
          if j < n:
              arr[j] = arr[i]  # copy element if inside original array
          if arr[i] == 0:
              j -= 1
              if j < n:
                  arr[j] = 0  # duplicate zero
          i -= 1
          j -= 1
