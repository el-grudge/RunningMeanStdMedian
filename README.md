# RunningMeanStdMedian

To run this code, download the running_stats.py file and run it using the following command:

`python3 running_stats.py`

Then, you will be prompted to enter your input. You should stick to digits, and enter 'q' to exit. If your input is of a wrong format, an exception will be shown, and you will be asked either to enter a new value, or to enter 'q' to exit, your previous input will still be intact.

Here is a comparison of the time it takes to run both implementations:

Calculating statistics using running_stats: 0.07012273399959668   
Calculating statistics using Numpy methods: 1.0326297899991914

Note: Execution time tests were conducted using timeit, and I used a pre-defined list of 50 random numbers, I did NOT use user defined input.

