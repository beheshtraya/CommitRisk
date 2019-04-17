from math import log2

import matplotlib.pyplot as plt
from estimate_best_batch_size import get_num_of_runs


def get_number_of_exec():
    x_data = list()
    y_data = list()
    y2_data = list()

    for batch_size in range(2, 17):
        x = batch_size
        y = 2 * log2(x) + 1
        test_list = [False]
        test_list += [True for _ in range(batch_size - 1)]
        y2 = get_num_of_runs(test_list, batch_size)
        print(test_list)

        x_data.append(x)
        y_data.append(y)
        y2_data.append(y2)

    plt.plot(x_data, y_data, 'g-', label='2 * log2(n) + 1')
    plt.plot(x_data, x_data, 'b-', label='Test all')
    plt.plot(x_data, y2_data, 'r-', label='Simulated num of runs')
    plt.xticks(range(0, 17, 1))
    plt.yticks(range(0, 17, 1))
    plt.xlabel('Batch Size')
    plt.ylabel('Number of executions')
    plt.grid(True)
    plt.legend()
    plt.savefig("logn.png", format="png", dpi=300)
    plt.show()


if __name__ == "__main__":
    print(get_number_of_exec())
