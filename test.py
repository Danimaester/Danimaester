import time
x = 100
f = open("C:\\temp\oll.txt", "x")
for i in range(100):
  f = open("C:\\temp\oll.txt", "w")
  f.write("Hahha you have been hacked your computer will explode in " + str(x) + " Sec")
  f = open("C:\\temp\oll.txt", "r")
  print(f.readline())
  f.close()
  time.sleep(1)
  x -= 1
