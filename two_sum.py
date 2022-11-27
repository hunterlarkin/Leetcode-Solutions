#https://leetcode.com/problems/two-sum/


def twosum(list, target):
    answer_list = []
    for i in range(len(list)):
        for x in range(1, len(list)):
            if list[i] + list[x] == target:
                answer_list.append(i)
                answer_list.append(x)
                return answer_list
    if not answer_list:
        print("No combination adds up to target")
        return 

        

def main():
    array = []
    array_size = int(input("Enter size of array "))
    target = int(input("Enter target number "))
    
    for i in range (0, array_size):
        array.append(int(input()))

    print("The indices are:", twosum(array, target))


if __name__ == "__main__":
    main()