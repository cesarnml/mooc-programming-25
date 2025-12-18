# Write your solution here
def list_sum(nums1: list, nums2: list):
    new = []
    for i in range(len(nums1)):
        new.append(nums1[i] + nums2[i])
    return new
