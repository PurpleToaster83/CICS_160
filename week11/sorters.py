def my_min(lis):
    cur_min_ind = 0
    for i in range(1, len(lis)):
        if lis[i] < lis[cur_min_ind]:
            cur_min_ind = i
    return cur_min_ind

def select_sort(lis):
    for i in range(len(lis) - 1):
        cur_min_ind = my_min(lis[i:]) + i
        lis[i], lis[cur_min_ind] = lis[cur_min_ind], lis[i]

# Sn = n/2 (a1 + a2) --> O(n^2)
def other_select_sort(lis):
    for i in range(len(lis) - 1):
        cur_min = i
        for j in range(i + 1, len(lis)):
            if(lis[j] < lis[cur_min]):
                cur_min = j

        lis[i], lis[cur_min] = lis[cur_min] = lis[i]

def insertion_sort(lis):
    n = len(lis)

    for u_i in range(1, n):
        u_val = lis[u_i]
    s_i = u_i - 1
    while s_i >= 0:
        if(u_val < lis[s_i]):
            lis[s_i + 1] = lis[s_i]
            s_i -= 1
        else:
            break
    lis[s_i + 1] = u_val 

def main():
    # print(my_min([1, 2, 3, 4, 5, 6]))
    # print(my_min([6, 4, 1, 2, 3, 7]))

    lis1 = [1, 2, 3, 4, 5, 6]
    lis2 = [6, 4, 1, 2, 3, 7]

    select_sort(lis1)
    select_sort(lis2)
    print(lis1, lis2)

if __name__ == "__main__":
    main()