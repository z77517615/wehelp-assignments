# 要求一：函式與流程控制
def calculate(min, max):
    sum=0
    for n in range (min, max+1): 
        sum=sum+n
    print(sum)
calculate(1, 3)
calculate(4, 8)

# 要求二：Python 字典與列表、JavaScript 物件與陣列
def avg(data):
    x = (data["employees"])
    sum=0
    for dic in x:
       sum=sum+(dic["salary"])
    result=(sum/data["count"])
    print(result)
avg({"count":3,"employees":
[{"name":"John","salary":30000},
{"name":"Bob","salary":60000},
{"name":"Jenny","salary":50000},
]})


# # 要求三：演算法
# 解法一:時間複雜度:O(n^2)
def maxProduct(nums):
    if len(nums)>2:   
        max=0
        for x in (nums) :  //n
            for y  in (nums):  //n
                if x==y :
                    continue
                result=(x*y)
                if(result>max):
                    max=result
            
        print(max)
    else: print(nums[0]*nums[1])  

# # 要求三：演算法
# 解法二:時間複雜度:O(n^2)
def maxProduct(nums):
    nums=sorted(nums)
    if len(nums)<=2:
        print (nums[0]*nums[1])
    elif nums[len(nums)-1]*nums[len(nums)-2] >= nums[0]*nums[1]:
            print (nums[len(nums)-1]*nums[len(nums)-2])

    else :print (nums[0]*nums[1])

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0])# 得到 2

# 要求四 ：演算法
def twoSum(nums, target):
    for x in range(0,len(nums)-1):
        for y in range (x+1,len(nums)):
            if nums[x]+nums[y]==target:
                return [x,y]
           
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 

# 要求五 ( Optional )：演算法
def maxZeros(nums):
    max_time=0
    result=0
    for i in nums:
        if i==0:
            max_time=max_time+1
            result=max(result,max_time)
        else:
            max_time=0
    print(result)

maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3

