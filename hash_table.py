import os
import time


def clear():
    os.system('cls')

class Node(object):
    def __init__(self, value=None, pointer=None):
        self.value = value
        self.pointer = pointer
        
    def getData(self):
        return self.value
    
    def getNext(self):
        return self.pointer
    
    def setData(self, newdata):
        self.value = newdata
        
    def setNext(self, newpointer):
        self.pointer = newpointer

class LinkedListFIFO(object):
    def __init__(self):
        self.head = None
        self.length = 0
        self.tail = None
    
    #헤드로부터 각 노드의 값을 출력한다
    def _printList(self):
        node =  self.head
        print("Head", end='')
        while node:
            print("->[%d]"%node.value, end=' ')
            node = node.pointer
        print()
        
    # 첫 번째 위치에 노드를 추가한다
    def _addFirst(self, value):
        self.length = 1
        node = Node(value)
        self.head = node
        self.tail = node
        
    #첫 번째 위치에 노드를 삭제한다
    def _deleteFirst(self):
        self.length = 0
        self.head = None
        self.tail = None
        print("연결 리스트가 비었습니다.")
    
#     def _delete(self, prev, node):
#         self.length -= 1
#         if not prev:
#             self.head = node.pointer
#         else:
#             prev.pointer = node.pointer
            
    #새 노드를 추가한다. 테일이 있다면, 테일의 다음 노드는
    # 새 노드를 가리키고 테일은 새 노드를 가리킨다
    def _add(self, value): 
        self.length += 1
        node = Node(value)
        if self.tail:
            self.tail.pointer = node # 노드가 none이 아니라면 노드의 끝에 계속 연결되는 식
        self.tail = node
#         self.head = Node(value, self.head)
    
    
# 새 노드를 가리키고, 테일은 새 노드를 가리킨다
    def addNode(self, value):
        if not self.head:
            self._addFirst(value) #최초의 헤드가 none일때는 이걸 탄다
        else:
            self._add(value)
        
    def _find(self, index):
        prev = None
        node = self.head
        i = 0
        while node and i < index :
            prev = node
            node = node.pointer
            i += 1
        return node, prev, i
        
    def _find_by_value(self, value): #value를 찾는것이라 value가 중요
        prev = None
        node = self.head
        found = False #found는 찾았냐/못찾았냐, 기본값은 false 
        while node and not found:
            if node.value == value:
                found = True
            else:
                prev = node
                node = node.pointer
        return node, prev, found
    
    def deleteNode(self, index):
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else: 
            node, prev, i = self._find(index)
            if i == index and node:
                self.length -= 1
                if i == 0 or not prev:
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("인덱스 {0}에 해당하는 노드가 없습니다.".format(index))
                
#         node, prev, i = self._find(index)
#         if index == i:
#             self._delete(prev, node)
#         else:
#             print(f"인덱스 {index}에 해당하는 노드가 없습니다.")
            
    def deleteNodeByValue(self, value): #value를 골라서 지우는 코드
        if not self.head or not self.head.pointer:
            self._deleteFirst()
        else:
            node, prev, i = self._find_by_value(value)
            if node and node.value == value:
                self. length -= 1
                if i == 0 or not prev :
                    self.head = node.pointer
                    self.tail = node.pointer
                else:
                    prev.pointer = node.pointer
            else:
                print("값 {0}에 해당하는 노드가 없습니다.".format(value))
                
#         node, prev, found = self._find_by_value(value)
#         if found:
#             self._delete(prev, node)
#         else:
#             print(f"값 {value}에 해당하는 노드가 없습니다.")
            
            
        

class HashTableLL(object):
    def __init__(self, size):
        self.size = size
        self.slots = []
        self._createHashTable()

        
    def _createHashTable(self):
        for i in range(self.size):
            self.slots.append(LinkedListFIFO()) # 통째로 만들어 붙이게 되는 식
            
    def _find(self, item):
        return item % self.size # 홀수 짝수로 나눠지게 됨
        
    def _add(self, item):
        index = self._find(item)
        self.slots[index].addNode(item) # 홀수 짝수로 분할시켜 만드는 자료구조를 해시라고 함
        
    def _delete(self, item):
        index = self._find(item)
        self.slots[index].deleteNodeByValue(item)
        
    def _print(self):
        clear()
        for i in range(self.size):
            print("[[{0}]]:".format(i), end='')
            self.slots[i]._printList()
            
    
def test_hash_tables():
    H1 = HashTableLL(8)
    for i in range(0,20):
        H1._add(i)
        H1._print()
    print("\n항목 0,1,2를 삭제합니다.")
    H1._delete(0)
    H1._delete(1)
    H1._delete(2)
    H1._print()

if __name__ == "__main__":
    test_hash_tables()