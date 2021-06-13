import traceback as tb
from math import sqrt
from heapq import heappush, heappop


class RunningStats:
    def __init__(self):
        self.count = 0
        self.aggregated_sum = 0
        self.aggregated_sumsq = 0
        self.lowers, self.highers = [], []

    def update_values(self, new_value):
        """
        Updates underlying values needed to calculate the running stats

        :param new_value: new user input
        :return: n/a
        """
        self.count += 1
        self.aggregated_sum += new_value
        self.aggregated_sumsq += new_value ** 2
        if not self.highers or new_value > self.highers[0]:
            heappush(self.highers, new_value)
        else:
            heappush(self.lowers, -new_value)  # for lowers we need a max heap
        if len(self.lowers) - len(self.highers) > 1:
            heappush(self.highers, -heappop(self.lowers))
        elif len(self.highers) - len(self.lowers) > 1:
            heappush(self.lowers, -heappop(self.highers))

    def get_mean(self):
        """
        Returns the mean of the input list

        :return: mean
        """
        return self.aggregated_sum / self.count

    def get_std(self):
        """
        Returns the standard deviation of the input list

        :return: standard deviation
        """
        return sqrt((self.aggregated_sumsq - self.aggregated_sum ** 2 / self.count) / self.count)

    def get_median(self):
        """
        Returns the median of the input list

        :return: median
        """
        if len(self.lowers) == len(self.highers):
            return (-self.lowers[0] + self.highers[0]) / 2
        elif len(self.lowers) > len(self.highers):
            return -self.lowers[0]
        else:
            return self.highers[0]


if __name__ == '__main__':

    print("Please enter your input one number per line, or 'q' to exit:")
    runningStats = RunningStats()

    while True:
        line = input()
        if line == 'q':
            print("Exit")
            break
        else:
            try:
                new_input = float(line)
                runningStats.update_values(new_input)

                print("Your output is:")
                print("{:.3f} {:.3f} {}".format(
                    runningStats.get_mean(),
                    runningStats.get_std(),
                    runningStats.get_median()))

            except ValueError:
                tbError = tb.format_exc()
                print("Invalid value entered, please try again, or enter 'q' to exit.")

