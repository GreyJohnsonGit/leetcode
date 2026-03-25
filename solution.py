class Solution(object):
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = [nums1, nums2]
        while len(nums[0]) + len(nums[1]) > 10:
            medians = [self.median(nums[0]), self.median(nums[1])]
            if len(nums[0]) == 1 or len(nums[1]) == 1:
                exhausted_array_index = 0
                if len(nums[1]) == 1:
                    exhausted_array_index = 1
                full_array_index = 1 - exhausted_array_index
                exhausted = nums[exhausted_array_index]
                full_array = nums[full_array_index]
                
                final_element = exhausted[0]
                length = len(full_array)
                if length % 2 == 1:
                    pre_median = full_array[length // 2 - 1]
                    median = full_array[length // 2]
                    post_median = full_array[length // 2 + 1]

                    if final_element < pre_median:
                        return (pre_median + median) / 2.0
                    elif final_element > post_median:
                        return (post_median + median) / 2.0
                    else:
                        return (final_element + median) / 2.0
                        
                else:
                    pre_median = full_array[length // 2 - 1]
                    post_median = full_array[length // 2]
                    if final_element < pre_median:
                        return pre_median
                    elif final_element > post_median:
                        return post_median
                    else:
                        return final_element

            has_fewer_elements = 1
            if len(nums[0]) < len(nums[1]):
                has_fewer_elements = 0
            
            has_upper_bound = 0
            if medians[0] < medians[1]:
                has_upper_bound = 1

            to_remove_count = len(nums[has_fewer_elements]) // 2
            if has_fewer_elements == has_upper_bound:
                upper_bound = len(nums[has_fewer_elements]) - to_remove_count
                nums[has_fewer_elements] = nums[has_fewer_elements][0:upper_bound]

                has_more_elements = 1 - has_fewer_elements
                nums[has_more_elements] = nums[has_more_elements][to_remove_count:]
            else:
                nums[has_fewer_elements] = nums[has_fewer_elements][to_remove_count:]

                has_more_elements = 1 - has_fewer_elements
                upper_bound = len(nums[has_more_elements]) - to_remove_count
                nums[has_more_elements] = nums[has_more_elements][0:upper_bound]

        return self.findMedianShortArrays(nums1, nums2)
    
    def median(self, nums: list[int]) -> float:
      n = len(nums)
      if n % 2 == 1:
          return nums[n // 2]
      else:
          return (nums[n // 2 - 1] + nums[n // 2]) / 2.0

    def findMedianShortArrays(self, nums1: list[int], nums2: list[int]):
        total_length = len(nums1) + len(nums2)
        left_pointer = 0
        right_pointer = 0

        def left_or_right():
            if left_pointer == len(nums1):
                return "right"
            elif right_pointer == len(nums2):
                return "left"
            elif nums1[left_pointer] < nums2[right_pointer]:
                return "left"
            else:
                return "right"

        previous = None
        while (left_pointer + right_pointer) < total_length // 2:
            previous = left_or_right()
            if previous == "left":
                left_pointer += 1
            else:
                right_pointer += 1
  
        if total_length % 2 == 1:
          if left_or_right() == "left":
              return nums1[left_pointer]
          else:
              return nums2[right_pointer]
        else:
          sum = 0
          if previous == "left":
              sum += nums1[left_pointer - 1]
          else:
              sum += nums2[right_pointer - 1]

          if left_or_right() == "left":
              sum += nums1[left_pointer]
          else:
              sum += nums2[right_pointer]
          return sum / 2.0
                  





    