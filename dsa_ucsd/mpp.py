def mpp(arr):
    arr.sort()
    return arr[-1]*arr[-2]

if __name__=="__main__":
    _ = int(input())
    input_numbers=list(map(int,input().split()))
    print(mpp(input_numbers))