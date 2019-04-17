from random import randint, getrandbits
from statistics import median

import matplotlib.pyplot as plt
import numpy as np

NUM_OF_RETRY = 100
NUM_OF_COMMITS = 1000


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


def get_num_of_runs(test_list, batch_size):
    if batch_size == 1:
        return len(test_list)
    # if batch_size <= 4:
    #     return len(test_list)

    num_of_runs = 0

    for i in range(0, len(test_list), batch_size):
        if i + batch_size > len(test_list):
            selected_portion = test_list[i:]
        else:
            selected_portion = test_list[i: i + batch_size]

        num_of_runs += 1

        if False in selected_portion:
            num_of_runs += get_num_of_runs(selected_portion, int(batch_size / 2))

    return num_of_runs


def get_best_batch_size(failure_test_rate, flaky_test_rate=0):
    num_of_commits = NUM_OF_COMMITS

    x_data = list()
    y_data = list()

    min_num_of_runs = num_of_commits
    best_batch_size = 1

    for batch_size in range(1, min(21, num_of_commits)):
        x = batch_size
        y_list = []

        for _ in range(NUM_OF_RETRY):
            test_list = list()
            random_failure_set = set()
            random_flaky_set = set()

            while True:
                if len(random_failure_set) >= failure_test_rate * num_of_commits / 100:
                    break

                random_failure_set.add(randint(0, num_of_commits))

            while True:
                if len(random_flaky_set) >= flaky_test_rate * num_of_commits / 100:
                    break

                rand_num = randint(0, num_of_commits)

                if rand_num not in random_failure_set:
                    random_flaky_set.add(randint(0, num_of_commits))

            for i in range(num_of_commits):
                if i in random_failure_set:
                    test_list.append(False)
                elif i in random_flaky_set:
                    test_list.append(bool(getrandbits(1)))
                else:
                    test_list.append(True)

            y = get_num_of_runs(test_list, batch_size)
            y_list.append(y)

        median_y = median(y_list)

        if median_y < min_num_of_runs:
            best_batch_size = x
            min_num_of_runs = median_y

        x_data.append(batch_size)
        y_data.append((1 - median_y / NUM_OF_COMMITS) * 100)

    print(x_data)
    print(y_data)
    plt.plot(x_data, y_data, 'g-', label='data')
    plt.xticks(range(1, len(x_data) + 1))
    plt.xlabel('Batch Size')
    plt.ylabel('Improvement %')
    # plt.yticks(range(0, 100, 5))
    plt.grid(True)
    plt.savefig("test.png", format="png", dpi=300)
    plt.show()

    return best_batch_size, min_num_of_runs


if __name__ == "__main__":
    print(get_best_batch_size(15.40))
