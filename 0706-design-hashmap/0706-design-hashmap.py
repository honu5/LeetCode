class MyHashMap:

    def __init__(self):
        self.arr1=[False]*1000001

    def put(self, key: int, value: int) -> None:
        if value==0:
            self.arr1[key]="tree"
        else: self.arr1[key]=value

    def get(self, key: int) -> int:
        if self.arr1[key]=="tree":
            return 0
        elif self.arr1[key]:
            return self.arr1[key]
        return -1

    def remove(self, key: int) -> None:
        self.arr1[key]=-1


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)