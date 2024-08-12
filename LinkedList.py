class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data=data, next=self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty..!")
            return

        llstr = ''
        itr = self.head
        while itr:
            llstr += str(itr.data) + '--> '
            itr = itr.next

        print(llstr)

    def insert_at_ending(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def len_of_linkedList(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_ending(data)

    def remove_at(self, index):
        if index < 0 or index >= self.len_of_linkedList():
            raise Exception("Invalid index..!")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.len_of_linkedList():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return

        count = 0
        itr = self.head

        while itr:

            if data_after == itr.data:
                break
            count += 1
            itr = itr.next

        return self.insert_at(count + 1, data_to_insert)

    def remove_by_value(self, data):
        if self.head is None:
            return

        itr = self.head
        count = 0
        found = False
        while itr:
            if itr.data == data:
                found = True
                break
            count += 1
            itr = itr.next

        if found:
            return self.remove_at(count)
        else:
            # raise ValueError(f"{data} not found in the list.")
            print(f"{data} not found in the list.")


if __name__ == "__main__":
    ll = Linkedlist()
    ll.insert_at_beginning(44)
    ll.insert_at_beginning(22)
    ll.insert_at_ending(66)
    ll.print()
    print(ll.len_of_linkedList())
    ll2 = Linkedlist()
    ll2.insert_values(["apple", "banana", "cherry", "dragon fruit", "emu apple"])
    ll2.print()
    print(ll2.len_of_linkedList())
    ll2.remove_at(2)
    ll2.print()
    print(ll2.len_of_linkedList())
    ll2.insert_at(0, "watermelon")
    ll2.print()
    print(ll2.len_of_linkedList())
  
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
