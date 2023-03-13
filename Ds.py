#!/usr/bin/env python
# coding: utf-8

# In[5]:


#linkedlist
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next

if __name__=='__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist.head.next = second; 
    second.next = third; 
    llist.printList()


# In[3]:


#stack
stack = []
 
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack')
print(stack)
 

print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are popped:')
print(stack)
 


# In[4]:


#Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
 

def printInorder(root):
 
    if root:
        printInorder(root.left)
        print(root.val),
        printInorder(root.right)
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val),
def printPreorder(root):
    if root:
        print(root.val),
        printPreorder(root.left)
        printPreorder(root.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Preorder traversal of binary tree is")
printPreorder(root)
 
print("\nInorder traversal of binary tree is")
printInorder(root)
 
print("\nPostorder traversal of binary tree is")
printPostorder(root)


# In[7]:


#Recursion
def printFun(test):
 
    if (test < 1):
        return
    else:
 
        print(test, end=" ")
        printFun(test-1) 
        print(test, end=" ")
        return
test = 6
printFun(test)


# In[9]:


def search(arr, n, x):
 
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
 
 

arr = [2, 3, 4, 10, 40]
x = 30
n = len(arr)
 

result = search(arr, n, x)
if(result == -1):
    print("Element is not Exist")
else:
    print("Element at index", result)


# In[11]:


#BubbleSort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [1, 6, 5, 2, 4, 3, 7]
bubbleSort(arr)
 
print ("Sorted array is:")
for i in range(len(arr)):
    print ("%d" %arr[i]),


# In[14]:


#queue
queue = []
 

queue.append('a')
queue.append('b')
queue.append('c')
 
print("Initial queue")
print(queue)
print("\nElements dequeued ")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))
 
print("\nRemoving elements")
print(queue)


# In[ ]:




