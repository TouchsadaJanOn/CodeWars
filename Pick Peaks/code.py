def pick_peaks(arr):
    sol =  {"pos": [], "peaks": []}
    flat = 0
    for i, num in enumerate(arr):
        if i == 0 or i == len(arr)-1:  # I am first or last item
            continue
        if arr[i+1] < num > arr[i-1]:  # I am a peak!
            sol["pos"].append(i)
            sol["peaks"].append(num)
        if arr[i-1] < num == arr[i+1]: # maybe platuaus
            flat = i
        if arr[i-1] == num > arr[i+1] and flat: # definitely a platuaus
            sol["pos"].append(flat)
            sol["peaks"].append(arr[flat])
            flat = 0
        elif arr[i-1] == num < arr[i+1] and flat: # not a platuaus
            flat = 0
            
            
    return sol
