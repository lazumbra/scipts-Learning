#https://leetcode.com/problems/rotate-array/discuss/390391/4-methods-in-python-%3A-index-assign-list-slicing-reversed
class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.reverse()
        print('reverse', nums)
        nums[:k] = nums[:k][::-1]
        print('KLKDF', nums)
        
        nums[k:] = nums[k:][::-1]
        print('FINAL ',nums)

        

if __name__ == "__main__":
    lista = [1,2]
    Solution().rotate(lista, 3)   
    print('lista', lista)

    lista1 = [1, 2, 3, 4, 5]

    print(lista1[0:3][::-1])
    print(lista1[3:][::-1])
