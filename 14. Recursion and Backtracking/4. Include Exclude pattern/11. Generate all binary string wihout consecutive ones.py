from typing import List

def generateString(N: int) -> List[str]:
    result = []
    func(N, result, "", 0)
    return result

def func(N, result, string, idx):
    if idx == N:
        result.append(string)
        return
    func(N, result, string+"0", idx+1)
    if not string or string[-1] != "1":
        func(N, result, string+"1", idx+1)
