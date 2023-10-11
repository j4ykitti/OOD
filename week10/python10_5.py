def min_weight(weights, box):
    left = max(weights)
    right = sum(weights)

    while left <= right:
        mid = (left + right) // 2
        box_count = 0
        current_weight = 0

        for weight in weights:
            if current_weight + weight > mid:
                box_count += 1
                current_weight = 0
            current_weight += weight

        if box_count < box:
            right = mid - 1
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    weights, box = input("Enter Input : ").split("/")
    weights = list(map(int, weights.split()))
    box = int(box)

    print(f"Minimum weigth for {box} box(es) = {min_weight(weights, box)}")