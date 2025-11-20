num_list = []
reversed_list = []
for i in range(1,11):
    num_list.append(int(i))

extracted_list = num_list[0:5]
reversed_list = extracted_list.copy()
reversed_list.reverse()

print(f"Original list: {num_list}")
print(f"Extracted first five elements: {extracted_list}")
print(f"Reversed extracted elements: {reversed_list}")