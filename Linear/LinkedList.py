class LinkedList:
    def __init__(self):
        self.head=None
    class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
    def AddFirst(self,data):
        new_node=self.Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def AddLast(self,data):
        new_node=self.Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            current_node=self.head
            while(current_node.next is not None):
                current_node=current_node.next
            current_node.next=new_node
    def PrintLinkedList(self):
        if self.head is None:
            print(" linkedlist is empty ")
        current_node=self.head
        while( current_node is not None):
            print(f" {current_node.data} ->",end='')
            current_node=current_node.next
        print()
    def DeleteFront(self):
        if self.head is None:
            print(" linkedList is empty ")
            return
        self.head=self.head.next
    def DeleteLast(self):
        if self.head is None:
            print(" list is empty ")
            return
        if self.head.next is None:
            self.head=self.head.next
        current_node=self.head
        while(current_node.next.next is not None):
            current_node=current_node.next
        current_node.next=None

LL=LinkedList()
LL.AddFirst(1)
LL.AddFirst(2)
LL.AddFirst(3)
LL.AddLast(100)
LL.PrintLinkedList()
LL.DeleteFront()
LL.PrintLinkedList()
LL.DeleteLast()
LL.PrintLinkedList()

