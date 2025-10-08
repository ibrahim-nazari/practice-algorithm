
def sameBst(nums1,nums2):
    if not nums1 and not nums2:
        return True
    if len(nums1) !=len(nums2):
        return False
    root1=nums1[0]
    root2=nums2[0]
    
    if root1 !=root2:
        return False
    left1= [a for a in nums1[1:] if a <=root1]
    right1= [a for a in nums1[1:] if a > root1]
    left2= [a for a in nums2[1:] if a <=root2]
    right2= [a for a in nums2[1:] if a > root2]
    return sameBst(left1,left2) and sameBst(right1,right2)


t=int(input())
for _ in range(t):
    nums1=list(map(int,input().split(",")))
    nums2=list(map(int,input().split(",")))
    res=sameBst(nums1,nums2)
    print(res)