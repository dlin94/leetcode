# Start with the tallest person. If more than one tallest, pick the one that has
# the smallest k (they must all be different). By definition, this k must be 0.
# Remove this person from the people list and put it in the ans list.
# Continuously find the tallest person in the people list as its shrinks.
def reconstruct_queue(people):
    ans = []
    next_tallest = [0, 0]
    while len(people) > 0:
        max_height = -1
        max_height_k = -1
        for person in people:
            if person[0] > max_height:
                max_height = person[0]
                max_height_k = person[1]
                next_tallest = person
            elif person[0] == next_tallest[0] and person[1] < next_tallest[1]:
                max_height_k = person[1]
                next_tallest = person
        ans.insert(next_tallest[1], next_tallest)
        people.remove(next_tallest)
        print(next_tallest)
    return ans

def reconstruct_queue_with_sort(people):
    ans = []
    people.sort(key=lambda a: [a[0], -a[1]], reverse=True) # descending height, ascending k
    for p in people:
        ans.insert(p[1], p)
    return ans

print(reconstruct_queue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
print(reconstruct_queue_with_sort([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))
