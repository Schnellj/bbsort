def backtrack_sort(keywords_with_weights):
    def compare(item1, item2):
        # Comparison based on weights
        return item1[1] > item2[1]  # "Better" means higher weight

    sorted_list = [keywords_with_weights[0]]  # Start with the first keyword as the current "best"

    for i in range(1, len(keywords_with_weights)):
        current = keywords_with_weights[i]
        j = 0

        while j < len(sorted_list):
            if compare(current, sorted_list[j]):
                # If current is better, insert it at the correct position
                sorted_list.insert(j, current)
                current = sorted_list.pop()  # Remove the old element that was displaced
                j = 0  # Restart comparisons for the displaced element
            else:
                j += 1

        # If current was not inserted, it is less than all elements in sorted_list
        if current not in sorted_list:
            sorted_list.append(current)

    return sorted_list


if __name__ == "__main__":
    # Define keywords with weights (keyword, weight)
    keywords_with_weights = [
        ("apple", 3),
        ("banana", 5),
        ("cherry", 2),
        ("date", 7),
        ("elderberry", 1),
        ("fig", 6),
        ("grape", 4),
        ("honeydew", 8),
        ("kiwi", 9),
        ("lemon", 10)
    ]

    print("Original list (with weights):", keywords_with_weights)

    sorted_keywords_with_weights = backtrack_sort(keywords_with_weights)
    print("Sorted list (by weight):", sorted_keywords_with_weights)
