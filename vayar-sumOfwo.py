def sumOfTwo(self, nums: List[int], target: int) -> List[int]:
        #declaring a dictionary to keep track of all the values
        dictionary = {}
        
        # iterating over the entire array
        for i in range(len(nums)):
            #subtracting the num from the target to search for its pair
            secondNumber = target-nums[i]
            #if the pair is found, return the index of the both numbers
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                # making sure we don't get the same index twice 
                if(i != secondIndex):
                    return sorted([i, secondIndex])
                
            dictionary.update({nums[i]: i})