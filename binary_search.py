"""
///
///                           Binary Search
///                 Personal Project By Aaron Ramos 2025
///
/// @binary_search.py
/// @author Aaron Ramos (ramosaaron2@gmail.com)
///
"""

""" PROBLEM """
# Given a deck of cards in **decreasing order**, pick out a card 
# containing a given number by turning over as few cards as possible

# i.e. "Given a list of integers in decreasing order and a desired 
# integer, return the index of the desired integer""

""" SOLUTIONS """
# Brute force approach: Iterate over the list of given integers until
# the observed integer matches the desired integer

# SOLUTION: Use binary search algorithm
# 1. Pick the middle element, if it matches the desired integer, return index
# 2. Otherwise, check if element < or > than desired int
# 3. If <, repeat Step 1 but from beginning until middle of list
#    If >, repeate Step 1 but from middle until end of list
# 4. Repeate until integer is found, o.w. return -1

def test_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

def locate_card(cards, query):
    low = 0
    high = len(cards)-1

    while low <= high:
        mid = (low + high) // 2
        result = test_location(cards, query, mid)

        if result == 'found':
            return mid
        
        elif result == 'left':
            high = mid - 1
        
        elif result == 'right':
            low = mid + 1

    print("Card not found :(")
    return -1

def main():

    tests = []

    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 7},
            'output': 3
    })

    tests.append({
        'input': {
            'cards': [13, 11, 10, 7, 4, 3, 1, 0],
            'query': 1},
            'output': 6
    })
    
    tests.append({
        'input': {
            'cards': [9, 7, 5, 2, -9],
            'query': 4},
            'output': -1
    })

    tests.append({
        'input': {
            'cards': [],
            'query': 7},
            'output': -1
    })

    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 3},
            'output': 7
    })

    tests.append({
        'input': {
            'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],
            'query': 6},
            'output': 2
    })

    total = len(tests)
    passed = 0
    for test in tests:
        if locate_card(**test['input']) == test['output']:
            print(f"\nCards: {test['input']['cards']}\nQuery: {test['input']['query']}\nOutput: {locate_card(**test['input'])}")
            print("Test passed!")
            passed += 1
        else:
            print(f"\nCards: {test['input']['cards']}\nQuery: {test['input']['query']}\nOutput: {locate_card(**test['input'])}")
            print("Test failed :(")
        
    print(f"\nTESTS PASSED: ({passed}/{total})")

if __name__ == "__main__":
    main()