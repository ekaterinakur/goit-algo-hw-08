import heapq

def minimize_total_cost(cables):
    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        combined_len = cable1 + cable2
        total_cost += combined_len

        heapq.heappush(cables, combined_len)

    return total_cost

if __name__ == "__main__":
    cables = [3, 1, 4, 6, 2, 5]
    min_cost = minimize_total_cost(cables)
    print("Мінімальні загальні витрати:", min_cost)
