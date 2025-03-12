def main():
    count = int(input())
    act = [] # insert  getMin  removeMin
    nums = []
    for i in range(count):
        act.append(list(input().split()))

def getMin(nums):
    nums.sort()
    return nums[0]

def solve(nums, act):
    for action, num in act:
        if action == "insert":
            nums.append(num)
        elif action == "getMin":
            minNum = getMin(nums)
            print(minNum)
        elif action == "removeMin":
            minNum = getMin(nums)
            nums.remove(minNum)
        else:
            pass




main()