

def are_same_bst(array1,array2):
    if len(array2) !=len(array1):
        return False
    if not array1 and not array2:
        return True
    if array2[0] !=array1[0]:
        return False
    def get_subtrees(array):
        root=array[0]
        left=[x for x in array[1:] if x < root]
        right=[x for x in array[1:] if x >= root]
        return left, right
    

    left1,right1=get_subtrees(array1)
    left2,right2=get_subtrees(array2)

    return are_same_bst(left1,left2) and are_same_bst(right1,right2)



num_test_case=int(input())
for _ in range(num_test_case):
    array1=list(map(int,input().split(",")))
    array2=list(map(int,input().split(",")))
    print(are_same_bst(array1,array2))