class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        f=m-1
        s=n-1
        idx=n+m-1
        while f>=0 and s>=0:
            print(nums2[s])
            if nums2[s]>nums1[f]:
                nums1[idx]=nums2[s]
                s-=1
            else: 
                nums1[idx]=nums1[f]
                f-=1
            idx-=1
        
        while s>=0:
            nums1[idx]=nums2[s]
            s-=1
            idx-=1

       
        