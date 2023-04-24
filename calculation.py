
def get_userinput():
    num_list = input().split(",")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list
def calculate_average(num_list):
    length = len(num_list)
    total = 0
    for i in num_list:
        total += i
    print(f"Average: ", total/length)
    return

def calculate_min_max(num_list):
    print(f"Min,Max", num_list[0], num_list[len(num_list) - 1])
    return
def sort_numlist(num_list):
    return sorted(num_list)
def calculate_median(num_list):
    length = len(num_list)
    if length % 2 == 0:
        #even
        mid = length//2
        median = (num_list[mid - 1] + num_list[mid])/2
    else:
        mid = length//2 - 1
        median = num_list[mid]
    print(f"Median: ", median)
    return
def main():
    num_list = get_userinput()
    num_list = sort_numlist(num_list)
    calculate_average(num_list)
    calculate_min_max(num_list)
    calculate_median(num_list)

if __name__ == "__main__":
    main()
