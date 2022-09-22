

import progressbar

import time


def time_taking_process(seconds: int):
    return time.sleep(seconds)



def animated_marker():
      
    widgets = ['Loading: ', progressbar.AnimatedMarker()]
    bar = progressbar.ProgressBar(widgets=widgets).start()
      
    for i in range(50):
        time_taking_process(0.1)
        bar.update(i)
          
# Driver's code
animated_marker()






# def testGenerators(string):
#     for i in range((len(string)-1),-1):
#         print(string[i])
# testGenerators(string="saravanan")



# import sys

# def spinning_cursor():
#     while True:
#         for cursor in '|/-\\':
#             yield cursor

# def loader(process):
#     spinner = spinning_cursor()
#     for _ in range(50):
#         sys.stdout.write(next(spinner))
#         sys.stdout.flush()
#         process
#         sys.stdout.write('\b')

# for i in range(100):
#     sys.stdout.write(next(spinner))
#     sys.stdout.flush()
#     time.sleep(1)
#     print("", end='')