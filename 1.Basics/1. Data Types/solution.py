class Solution:
    # For Python Versions below 3.10 
    def dataTypeSize(self, str):
        if str == "Character":
            return 1
        elif str == "Integer":
            return 4
        elif str == "Float":
            return 4
        elif str == "Long":
            return 8
        elif str == "Double":
            return 8
        else:
            return -1
        
    # For Python Versions 3.10 and above
    def dataTypeSizeNew(self, str):
        match str:
            case "Character":
                return 1
            case "Integer":
                return 4
            case "Float":
                return 4
            case "Long":
                return 8
            case "Double":
                return 8
            case _:
                return -1

if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str = input()
        ob = Solution()
        # res = ob.dataTypeSize(str)
        res = ob.dataTypeSizeNew(str)
        print(res)