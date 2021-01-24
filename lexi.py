# lexi is cute


# connecting arduino to python
# try:
  #   from pyfirmata import Ardunio, util
# except:
    # import pip
   #  pip.main (['install','pyfirmata'])
    # from pyfirmata import Arduino,util

import random
import time


# board = ArduinoMEGA('COM6')
#  theloop = util.Iterator(board)
# theloop.start()
# something = board.get_pin('d:8')
# time.sleep(2.0)
# print(something.read())


countin=0
countout=0
total =random.randint(0,10)
voterbooths=int(input('how many booths are at the polling location '))

# while(1==1):
    # if (something>15 and something<30):
      #  countin = countin+1
    # if (something<15 and something>0):
      #   countout = countout+1
    # total = countin-countout
    # print(total)

something= random.randint(0,500)

while(1==1):
    randtime = random.randint(0, 900)
    current = random.randint(0, 500)
    previous = random.randint(0, 500)
    something = random.randint(0, 500)
    diff = current - previous
    diff = abs(diff)
    if (diff>30):
        if (something>350 and something<500):
            countin = countin+1
        if (something<350 and something>0):
            countout = countout+1
    total = total +countin-countout

    # print(total)
    people_in_line = total-voterbooths
    go_to_next_available_booth = voterbooths - total
    if (voterbooths==20): print ("allow 20 countin ")
    if (voterbooths<total): print ("there are "+ str(people_in_line) + " line")
    if (voterbooths>total): print ("There are " + str(go_to_next_available_booth) +" booths available")
    time.sleep (randtime)




















