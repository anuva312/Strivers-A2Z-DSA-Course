class Solution:
    # For Python Versions below 3.10 
    def dataTypeSize(self, str):
        if str == "Character":
            return 1
        elif str == "Integer":
            return 2
        elif str == "Long":
            return 4
        elif str == "Float":
            return 4
        elif str == "Double":
            return 8
        else:
            return 0
        
    # For Python Versions 3.10 and above
    def dataTypeSizeNew(self, str):
        match str:
            case "Character":
                return 1
            case "Integer":
                return 2
            case "Long":
                return 4
            case "Float":
                return 4
            case "Double":
                return 8
            case _:
                return 0

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        # res = ob.dataTypeSize(str)
        res = ob.dataTypeSizeNew(str)
        print(res)