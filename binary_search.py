def binary_search(arr, value):
    start=0
    end= len(arr)
    mid= int((start+ end)/2)
    while not(arr[mid] == value) and start <= end:
        if arr[mid]< value:
            start= mid +1
        else:
            end= mid -1
        mid= int((start+ end)/2)
    if arr[mid] == value:
        print("Found at ", mid+1)
    else:
        print("Not Found")