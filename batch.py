import os
for i in range(10):
  command = "docker exec -e Var1={} -e Var2=2 -e Var3=3 epic_cohen ./runit.py".format(i)
  print(command)
  os.system(command)
  print()

