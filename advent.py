import math

def GetMassesFromFile(fileName):
  with open(fileName, 'r') as massesFile:
    return massesFile.readlines()

def CalculateFuelNeeded(mass):
  neededMass = int(mass) / 3
  neededMass = math.floor(neededMass)
  neededMass -= 2
  return neededMass


def SumOfFuelForMass():
  masses = GetMassesFromFile('moduleMasses.txt')
  fuelNeeded = 0
  for mass in masses:
    fuelNeeded += CalculateFuelNeeded(mass)
  return fuelNeeded


def SumOfFuelForMassWithFuel():
  masses = GetMassesFromFile('moduleMasses.txt')
  fuelNeeded = 0
  for mass in masses:
    fuelForModule = CalculateFuelNeeded(mass)
    fuelNeededForFuel = CalculateFuelNeeded(fuelForModule)
    while(fuelNeededForFuel > 0):
      fuelForModule += fuelNeededForFuel
      fuelNeededForFuel = CalculateFuelNeeded(fuelNeededForFuel)
    fuelNeeded += fuelForModule
  return fuelNeeded


def GetIntegersFromFile(fileName):
  with open(fileName, 'r') as integersFile:
    integersStr = integersFile.read()
    integers = integersStr.split(',')
    integers = [int(i) for i in integers]
    return integers

def IntCode(integers):
  index = 0
  run = True
  while run:
    if integers[index] == 1:
      integers[integers[index + 3]] = integers[integers[index + 1]] + integers[integers[index + 2]]
      index += 4
    elif integers[index] == 2:
      integers[integers[index + 3]] = integers[integers[index + 1]] * integers[integers[index + 2]]
      index += 4
    elif integers[index] == 99:
      run = False
    else:
      run = False
  return integers


def Program1202Alarm():
  ints = GetIntegersFromFile('integers.txt')
  ints[1] = 12
  ints[2] = 2
  return IntCode(ints)


def FindNounAndVerb(target):
  for noun in range(99):
    for verb in range(99):
      ints = GetIntegersFromFile('integers.txt')
      ints[1] = noun
      ints[2] = verb
      if IntCode(ints)[0] == target:
        return 100 * noun + verb, [noun, verb]


def GetWireInputs():
  with open('wires.txt', 'r') as wireFile:
    wires = wireFile.read().splitlines()
    return [wire.split(',') for wire in wires]


def CalculateManhattan(point):
  return sum(map(abs, point))


def GetWirePath(wire):
  x = 0
  y = 0
  path = {}
  i = 0
  for step in wire:
    direction = step[0]
    length = int(step[1:])
    for _ in range(length):
      i += 1
      if direction == 'L':
        x -= 1
      elif direction == 'R':
        x += 1
      elif direction == 'U':
        y += 1
      elif direction == 'D':
        y -= 1
      else:
        print("Invalid direction: " + direction)
      path[x, y] = i
  return path



def FindClosestIntersection():
  wires = GetWireInputs()
  paths = [GetWirePath(wire) for wire in wires]
  intersections = set(paths[0])
  for path in paths[1:]:
    intersections &= set(path)

  distances = {
    CalculateManhattan(point): paths[0][point] + paths[1][point]
    for point in intersections
  }

  return [min(distances.keys()), min(distances.values())]



def main():
  print(FindClosestIntersection())


if __name__ == "__main__":
  main()