import solution

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def test(nums1, nums2, expected):
    s = solution.Solution()
    result = s.findMedianSortedArrays(nums1, nums2)
    print(f"s.findMedianSortedArrays({nums1}, {nums2}) == {expected}: {result}")
    if result == expected:
        print(f"{GREEN}Success{RESET}")
    else:
        print(f"{RED}Failure{RESET}")

def main():
    test([1, 3], [2], 2)
    test([1, 2], [3, 4], 2.5)
    test([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [0, 6, 6, 6], 9.5)
    test(list(range(100)), list(range(50)), 37)
if __name__ == "__main__":
    main()