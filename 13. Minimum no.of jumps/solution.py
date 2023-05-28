class Graph:
    def __init__(self,n,arr):
        self.adj_list = {}
        self.length = n
        self.paths = []
        self.possible_jumps = []
        self.current_path = []
        self.jumps = 0
        # Initializing adjacency list of each vertex into an empty list
        for i in range(1,n+1):
            self.adj_list[i] = []
            self.initialize_adj_list(i,arr[i-1])

    def initialize_adj_list(self, node, distance):
        for neighbor in range(1,distance+1):
            new_position = node + neighbor
            if( new_position<= self.length):
                self.adj_list[node].append(new_position)

    def reach(self, x):
        # keeping track of no.of jumps and path
        self.jumps+=1 
        self.current_path.append(x)
        # check if last node has been reached 
        if(x == self.length):
            self.paths.append(self.current_path)
            self.possible_jumps.append(self.jumps-1)
            self.jumps -= 1
            self.current_path.pop()
            return
        for node in self.adj_list[x]:
            self.reach(node)
        self.jumps -= 1
        self.current_path.pop()

    def get_paths(self):
        return self.paths
    
    def get_min_jumps(self):
        if(len(self.possible_jumps)):
            return min(self.possible_jumps)
        return -1

class Solution:
    def minJumps(self, arr, n):
        maze = Graph(n,arr)
        maze.reach(1)
        return maze.get_min_jumps()


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		Arr = [int(x) for x in input().split()]
		ob = Solution()
		ans = ob.minJumps(Arr,n)
		print(ans)
# } Driver Code Ends



