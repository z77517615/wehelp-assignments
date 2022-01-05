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
def maxProduct(nums):
    if len(nums)>2:
        max=0
        for x in (nums) :
            for y  in (nums):
                if x==y :
                    continue
                result=(x*y)
                if(result>max):
                    max=result
            
        print(max)
    else: print(nums[0]*nums[1])  

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