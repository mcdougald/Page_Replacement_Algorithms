# Assignment 4

Hello, I completed my assignment 4 using an IPython Notebook, also known
as a Jupyter Labs Notebook. You can see the program at https://github.com/TrevorMcDougald/Page_Replacement_Algorithms
or you can run it using Python 3.7 and Jupyter Labs. Thank you for your time.

You can execute the python code with "python ./Page_Replacement_Algorithms.py"

########################### TRIAL RUN ONE##################################
Reference String: [3, 5, 5, 3, 4, 5, 5, 3, 1, 5]

		Optimal Page Replacement Algorithm:

3 -> [ 3 ] [ - ] [ - ]  Miss
5 -> [ 3 ] [ 5 ] [ - ]  Miss
5 -> [ 3 ] [ 5 ] [ - ]  Hit
3 -> [ 3 ] [ 5 ] [ - ]  Hit
4 -> [ 3 ] [ 5 ] [ 4 ]  Miss
5 -> [ 3 ] [ 5 ] [ 4 ]  Hit
5 -> [ 3 ] [ 5 ] [ 4 ]  Hit
3 -> [ 3 ] [ 5 ] [ 4 ]  Hit
1 -> [ 1 ] [ 1 ] [ 1 ]  Miss
5 -> [ 1 ] [ 5 ] [ 4 ]  Hit

		Least Recently Used Page Replacement Algorithm:

3 -> [ 3 ] [ - ] [ - ]  Miss
5 -> [ 3 ] [ 5 ] [ - ]  Miss
5 -> [ 3 ] [ 5 ] [ - ]  Hit
3 -> [ 3 ] [ 5 ] [ - ]  Hit
4 -> [ 3 ] [ 5 ] [ 4 ]  Miss
5 -> [ 3 ] [ 5 ] [ 4 ]  Hit
5 -> [ 3 ] [ 5 ] [ 4 ]  Hit
3 -> [ 3 ] [ 5 ] [ 4 ]  Hit
1 -> [ 3 ] [ 5 ] [ 1 ]  Miss
5 -> [ 3 ] [ 5 ] [ 1 ]  Hit

			Total Optimal Page Faults : 4.
			Total Least Recently Used Faults : 4.


It was a tie! The Optimal and Least Recently Used Page Replacement Algorithms Were Equal
The Tie Breaker will be settled with the First In First Out algorithm


		First In First Out Page Replacement Algorithm:

3 -> [ 3 ] [ - ] [ - ]  Miss
5 -> [ 3 ] [ 5 ] [ - ]  Miss
5 -> [ 3 ] [ 5 ] [ - ]  Hit
3 -> [ 3 ] [ 5 ] [ - ]  Hit
4 -> [ 3 ] [ 5 ] [ 4 ]  Miss
5 -> [ 3 ] [ 5 ] [ 4 ]  Hit
5 -> [ 3 ] [ 5 ] [ 4 ]  Hit
3 -> [ 3 ] [ 5 ] [ 4 ]  Hit
1 -> [ 1 ] [ 5 ] [ 4 ]  Miss
5 -> [ 1 ] [ 5 ] [ 4 ]  Hit

			Total First in First Out Page Faults : 4.


		First In First Out was less than LRU and Optimal Page Replacement

Process finished with exit code 0

########################### TRIAL RUN TWO##################################
Reference String: [4, 2, 5, 2, 5, 2, 3, 1, 4, 4]

		Optimal Page Replacement Algorithm:

4 -> [ 4 ] [ - ] [ - ]  Miss
2 -> [ 4 ] [ 2 ] [ - ]  Miss
5 -> [ 4 ] [ 2 ] [ 5 ]  Miss
2 -> [ 4 ] [ 2 ] [ 5 ]  Hit
5 -> [ 4 ] [ 2 ] [ 5 ]  Hit
2 -> [ 4 ] [ 2 ] [ 5 ]  Hit
3 -> [ 3 ] [ 3 ] [ 3 ]  Miss
1 -> [ 1 ] [ 1 ] [ 1 ]  Miss
4 -> [ 4 ] [ 1 ] [ 5 ]  Hit
4 -> [ 4 ] [ 1 ] [ 5 ]  Hit

		Least Recently Used Page Replacement Algorithm:

4 -> [ 4 ] [ - ] [ - ]  Miss
2 -> [ 4 ] [ 2 ] [ - ]  Miss
5 -> [ 4 ] [ 2 ] [ 5 ]  Miss
2 -> [ 4 ] [ 2 ] [ 5 ]  Hit
5 -> [ 4 ] [ 2 ] [ 5 ]  Hit
2 -> [ 4 ] [ 2 ] [ 5 ]  Hit
3 -> [ 3 ] [ 2 ] [ 5 ]  Miss
1 -> [ 3 ] [ 2 ] [ 1 ]  Miss
4 -> [ 3 ] [ 4 ] [ 1 ]  Miss
4 -> [ 3 ] [ 4 ] [ 1 ]  Hit

			Total Optimal Page Faults : 5.
			Total Least Recently Used Faults : 6.


		Optimal Page Replacement Algorithm was the most efficient.

Process finished with exit code 0