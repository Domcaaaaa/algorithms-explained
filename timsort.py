def binary_search(the_array, item, start, end):
    if start > end:
        return start

    mid = round((start + end) / 2)

    if the_array[mid] < item:
        return binary_search(the_array, item, start, mid - 1)

    elif the_array[mid] > item:
        return binary_search(the_array, item, mid + 1, end)

    else:
        return mid
    
def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        for j in range(index, pos, -1):
            the_array[j] = the_array[j - 1]
        the_array[pos] = value
    return the_array

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

def timsort(the_array):
    runs = []
    length = len(the_array)
    new_run = [the_array[0]]

    for i in range(1, length):
        if i == length - 1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i - 1]:
            if not new_run:
                runs.append([the_array[i]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = []
        else:
            new_run.append(the_array[i])

    if new_run:
        runs.append(new_run)

    sorted_runs = []
    for run in runs:
        sorted_runs.append(insertion_sort(run))

    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array

print(timsort([548, 213, 786, 92, 447, 655, 324, 889, 110, 731, 1, -6]))