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

def merge_sort(lis):
    if(len(lis) <= 1):
        return None

    l = lis[:len(lis) // 2]
    r = lis[len(lis) // 2:]

    merge_sort(l)
    merge_sort(r)

    l_ind, r_ind, merge_ind = 0, 0, 0
    while l_ind < len(l) and r_ind < len(r):
        if l[l_ind] < r[r_ind]:
            lis[merge_ind] = l[l_ind]
            l_ind += 1
        else:
            lis[merge_ind] = r[r_ind]
            r_ind += 1
        merge_ind += 1

    while l_ind < len(l):
        lis[merge_ind] = l[l_ind]
        l_ind += 1
        merge_ind += 1
    while r_ind < len(r):
        lis[merge_ind] = r[r_ind]
        r_ind += 1
        merge_ind += 1

def get_mergeSort(lis):
    if(len(lis) <= 1):
        return lis
    l = lis[:len(lis) // 2]
    r = lis[len(lis) // 2:]
    sorted_l = get_mergeSort(l)
    sorted_r = get_mergeSort(r)
    return merge(sorted_l, sorted_r)

def merge(left, right):
    new_list = []
    while(len(left) > 0 and len(right) > 0):
        if(left[0] < right[0]):
            new_list.append(left.pop(0))
        else:
            new_list.append(right.pop(0))
    new_list.extend(left)
    new_list.extend(right)
    return new_list

def main():
    # print(my_min([1, 2, 3, 4, 5, 6]))
    # print(my_min([6, 4, 1, 2, 3, 7]))

    lis1 = [1, 2, 3, 4, 5, 6]
    lis2 = [6, 4, 1, 2, 3, 7]

    # select_sort(lis1)
    # select_sort(lis2)
    merge_sort(lis2)
    print(lis1, lis2)

if __name__ == "__main__":
    main()