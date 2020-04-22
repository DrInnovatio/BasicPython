# Create a program to help the user type faster. Give him a word and ask him to write it five times.
# Check how many seconds it took him to type the word at each round.

# In the end, tell the user how many mistakes were made and show a chart with the typing speed evolution during the 5 round.

#import random

import time as t
import matplotlib.pyplot as plt

times = []
mistakes = 0

print("Typing Competition!!")

input("Press enter to continue.")

while len(times) < 5:
    start = t.time()
    word = input("Type the word : ")
    end = t.time()
    time_elapsed = end - start

    times.append(time_elapsed)

    if (word.lower() != "programming"):
        mistakes += 1

print("You made " + str(mistakes) + " mistake(s).")
print("Let's see your result")

t.sleep(3)

x = [1,2,3,4,5]
y = times

plt.plot(x, y)
legend = ["1", "2", "3", "4", "5"]
plt.xticks(x , legend)
plt.ylabel('Time in seconds')
plt.xlabel('Attempts')
plt.title('Your typing evolution')
plt.show()







