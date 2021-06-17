from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

def search_lyric(array,query):
    lenth = len(query)
    left_value = query.replace('?', 'a')
    right_value = query.replace('?', 'z')
    return count_by_range(array[lenth],left_value, right_value)

def solution(words, queries):
    answer = []
    classified = [[] for _ in range(10001)]
    classified_rev = [[] for _ in range(10001)]
    for word in words:
        classified[len(word)].append(word)
        classified_rev[len(word)].append(word[::-1])
    for i in range(10001):
        classified[i].sort()
        classified_rev[i].sort()
    for query in queries:
        if query[-1] == '?':
            answer.append(search_lyric(classified,query))
        else:
            answer.append(search_lyric(classified_rev,query[::-1]))
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

result = solution(words, queries)
print(result)