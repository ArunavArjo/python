
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}


symmetric_diff_method = set_a.symmetric_difference(set_b)
print(f"Symmetric difference using .symmetric_difference(): {symmetric_diff_method}")


symmetric_diff_operator = set_a ^ set_b
print(f"Symmetric difference using the ^ operator: {symmetric_diff_operator}")


set_c = {"apple", "banana", "cherry"}
set_d = {"banana", "grape", "orange"}
symmetric_diff_fruits = set_c.symmetric_difference(set_d)
print(f"Symmetric difference of fruits: {symmetric_diff_fruits}")