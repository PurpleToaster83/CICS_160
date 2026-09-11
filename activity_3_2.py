def averageAbove(threshold):
  list = []
  while True:
    number = int(input("Number?"))
    if int(number) < 0:
      break
    list.append(number)
  listAbove = [item for item in list if item > threshold]
  return int(sum(listAbove)/len(listAbove))

averageAbove(5)
