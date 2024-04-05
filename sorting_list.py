''' challenge:  sort this list of numbers without the sort function'''


input = emp_id = ['143', '501', '9000', '97998', 200, 9888]

sorting_list = []
for x in input:
    sorting_list.append(int(x))


for a in range(0,len(sorting_list)):
    for b in range(a+1,len(sorting_list)):
        if sorting_list[a] < sorting_list[b]:
            sorting_list[a], sorting_list[b] = sorting_list[b], sorting_list[a]

print(sorting_list)


