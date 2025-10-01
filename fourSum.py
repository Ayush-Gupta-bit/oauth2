def fourSum(arr, target):
    res = []
    n = len(arr)
    
    # Sort the array
    arr.sort()

    # Generate quadruplets
    for i in range(n):
      
        # Skip duplicates for i
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, n):
          
            # Skip duplicates for j
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            k, l = j + 1, n - 1

            # Two pointers approach
            while k < l:
                total = arr[i] + arr[j] + arr[k] + arr[l]
                if total == target:
                    res.append([arr[i], arr[j], arr[k], arr[l]])
                    k += 1
                    l -= 1

                    # Skip duplicates for k and l
                    while k < l and arr[k] == arr[k - 1]:
                        k += 1
                    while k < l and arr[l] == arr[l + 1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1

    return res

if __name__ == "__main__":
	arr = [10, 2, 3, 4, 5, 7, 8]
	target = 23
	ans = fourSum(arr, target)
	for v in ans:
		print(" ".join(map(str, v)))
