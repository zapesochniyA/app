from typing import List

arr_to_check: List[str] = ["hello", "2", "world", ":-)"]


def check_arr(arr: List[str]) -> List[str]:
    if len(arr) == 0:
        return []
    out_arr: List[str] = []
    for i in arr:
        if len(i) <= 3:
            out_arr.append(i)
    return out_arr


print(check_arr(arr_to_check))
