
def get_userinput():
    print("Input a list of numbers in the format of e.g. 12,34,54,1")
    num_list = input().split(",")
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def calculate_average(num_list):
    length = len(num_list)
    total = 0
    for i in num_list:
        total += i
    return total/length


def calculate_min_max(num_list):
    num_list = sort_numlist(num_list)
    return [num_list[0], num_list[len(num_list) - 1]]

def sort_numlist(num_list):
    return sorted(num_list)

def calculate_median(num_list):
    num_list = sort_numlist(num_list)
    length = len(num_list)
    if length % 2 == 0:
        #even
        mid = length//2
        median = (num_list[mid - 1] + num_list[mid])/2
    else:
        mid = length//2
        median = num_list[mid]
    return median

def main():
    num_list = get_userinput()
    num_list = sort_numlist(num_list)
    average = calculate_average(num_list)
    print(f"Average:", average)
    min_max = calculate_min_max(num_list)
    print(f"Min,Max:", min_max)
    median = calculate_median(num_list)
    print(f"Median:", median)

if __name__ == "__main__":
    main()
