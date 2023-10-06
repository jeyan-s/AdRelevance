from collections import defaultdict as dd 

class Node:
    def __init__(self, Element):
        self.data = Element
        self.prev = None
        self.next = None

class HistoryCache:
    def __init__(self, Capacity = 10):
        self.Capacity = Capacity
        self.Hash = dd(lambda: False)
        self.Right = Node(-1)
        self.Left = Node(-1)
        self.Left.next = self.Right
        self.Right.prev = self.Left 
        self.Frequency = dd(int)

    # @private
    def Delete(self, RecentlyUsed):
        Previous = RecentlyUsed.prev
        Next = RecentlyUsed.next 
        Previous.next = Next 
        Next.prev = Previous

    def Add(self, RecentlyUsed):
        Previous = self.Right.prev 
        Next = self.Right 
        RecentlyUsed.prev = Previous
        RecentlyUsed.next = Next
        Previous.next = RecentlyUsed
        Next.prev = RecentlyUsed

    def AddHistory(self, History):
        RecentlyUsed = self.Hash[History]
        self.Frequency[History] += 1
        if RecentlyUsed:
            self.Delete(RecentlyUsed)
            t = Node(History)
            self.Hash[History] = t
            self.Add(t)
        else:
            RecentlyUsed = Node(History)
            self.Add(RecentlyUsed)
            self.Hash[History] = RecentlyUsed
            self.Capacity -= 1
            if self.Capacity < 0:
                self.Hash[self.Left.next.data] = False
                self.Frequency[self.Left.next.data] = 0
                self.Delete(self.Left.next)
                self.Capacity += 1

    def Display(self):
        head = self.Left.next 
        while head.next:
            print(head.data)
            head = head.next

    def MostFrequentHistory(self):
        FrequentRate = max(self.Frequency.values())
        Tail = self.Right.prev 
        while Tail.prev:
            if self.Frequency[Tail.data] == FrequentRate:
                return Tail.data
            Tail = Tail.prev

# CacheSystem = Cache(2)

# Coding = ('Python', 'Coding', 'Language')
# Game = ('Asphalt', 'Car', 'Racing')
# Animal = ('Snake', 'Anaconda', 'Forest')

# Contents = [Coding, Game, Animal, Coding, Coding, Animal, Coding, Coding, Coding, Coding, Animal]

# for x in Contents:
#     CacheSystem.AddElement(x)

# print(CacheSystem.GetReleventAd())

# Output: Most Recent Search Tags (Top 10 Ad Tag Recommendations)