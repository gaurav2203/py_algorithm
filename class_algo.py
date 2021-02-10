class algorithm:
    def __init__(self,arr):
        self.arr=arr
    def selection_sort(self):
        for i in range(len(self.arr)):
            min_value= i
            for j in range(i+1, len(self.arr)):
                if self.arr[min_value]> self.arr[j]:
                    min_value= j
            self.arr[i], self.arr[min_value]= self.arr[min_value], self.arr[i]
        return self.arr
    def insertion_sort(self):
        for i in range(1,len(self.arr)):
            position= i
            current_value= self.arr[i]
            while position >0 and self.arr[position -1] > current_value:
                self.arr[position]= self.arr[position-1]
                position= position-1
            self.arr[position]= current_value
        return self.arr
    def bubble_sort(self):
        for i in range(len(self.arr)-1):
            for j in range(len(self.arr)-1 -i):
                if self.arr[j]>self.arr[j+1]:
                    self.arr[j], self.arr[j+1]= self.arr[j+1], self.arr[j]
        return self.arr     
    def binary_search(self, value):
        start=0
        end= len(self.arr)
        mid= int((start+ end)/2)
        while not(self.arr[mid] == value) and start <= end:
            if self.arr[mid]< value:
                start= mid +1
            else:
                end= mid -1
            mid= int((start+ end)/2)
        if self.arr[mid] == value:
            print("Found at ", mid+1)
        else:
            print("Not Found")