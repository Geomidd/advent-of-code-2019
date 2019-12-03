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


def main():
  print(FindNounAndVerb(19690720))


if __name__ == "__main__":
  main()