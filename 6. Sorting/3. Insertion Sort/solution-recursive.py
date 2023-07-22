from typing import List

def insert(a: List[int], j: int, key : int) -> int:
   if(j>=0 and a[j]>key):
         a[j+1] = a[j]
         return insert(a,j-1,key)
   return j+1
   
def insertionSort(a: List[int], n: int) -> None:
   for i in range(1,n):
      key = a[i]
      curr_pos = insert(a,i-1,key)
      a[curr_pos]=  key