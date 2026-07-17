class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        result =[]
        for i in nums :
            if i in count:
                count[i]+=1
            else:
                count[i]=1
            
        sorted_nums = sorted(count.items(), key =lambda x: x[1], reverse = True)
        for i in range(k):
            result.append(sorted_nums[i][0])
        return result
