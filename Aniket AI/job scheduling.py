def main():
    n = int(input("Enter the number of jobs: "))

    jobs = []
    max_deadline = 0

    for i in range(n):
        deadline, profit = map(int, input("Enter the deadline and profit of job {}: ".format(i + 1)).split())
        max_deadline = max(max_deadline, deadline)
        jobs.append((i + 1, deadline, profit))

    jobs.sort(key=lambda x: x[2], reverse=True)  # Sort jobs according to profit

    result = [0] * max_deadline
    slot = [False] * max_deadline

    max_profit = 0

    for i in range(n):
        deadline = jobs[i][1]
        for j in range(deadline - 1, -1, -1):
            if not slot[j]:
                result[j] = jobs[i][0]
                slot[j] = True
                max_profit += jobs[i][2]
                break

    print("Max Profit Sequence of Jobs: ", end="")
    for i in range(max_deadline):
        if slot[i]:
            print(result[i], end=" ")

    print("\nMax Profit:", max_profit)

# Call the job scheduler
main()