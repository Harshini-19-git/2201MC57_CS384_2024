#ques1 
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_rotations(number):
    num_str = str(number)
    rotations = []
    for i in range(len(num_str)):
        rotated = num_str[i:] + num_str[:i]
        rotations.append(int(rotated))
    return rotations

def is_rotational_prime(number):
    rotations = generate_rotations(number)
    return all(is_prime(rot) for rot in rotations)

# Example usage
number = int(input("Enter a number to check if it is a Rotational Prime: "))
if is_rotational_prime(number):
    print(f"{number} is a Rotational Prime.")
else:
    print(f"{number} is not a Rotational Prime.")

#ques2
#lab3
def Upper(s):
  for i in s:
    if('A'<=i and i<='Z'):
        return 1
  return 0

def Lower(s):
  for i in s:
    if('a'<=i and i<='z'):
        return 1
  return 0

def Num(s):
  for i in s:
    if('0'<=i and i<='9'):
        return 1
  return 0

def SpChar(s):
  ct=0
  for i in s:
    if(i=='!' or i=='@' or i=='#'):
        ct=ct+1
    elif('A'<=i and i<='Z' or 'a'<=i and i<='z' or '0'<=i and i<='9'):
      continue
    else:
      return 'Falsechar'
  if(ct>0):
    return 'True'
  else:
    return 'NoSpChar'

def Allcriteria(s,crit):
 invalid=0
 print(s)
 for i in crit:
  if(i=='1'):
    if(Upper(s)==0):
      if(invalid==0):
        print(" Invalid password")
        invalid=1
      print(" No uppercase in it")
  elif(i=='2'):
    if(Lower(s)==0):
      if(invalid==0):
        print(" Invalid password")
        invalid=1
      print(" No lowercase in it")
  elif(i=='3'):
    if(Num(s)==0):
      if(invalid==0):
        print(" Invalid password")
        invalid=1
      print(" No numbers in it")
  else:
    if(SpChar(s)=='Falsechar'):
      if(invalid==0):
        print(" Invalid password")
        invalid=1
      print(" False character in it")
    elif(SpChar(s)=='NoSpChar'):
      if(invalid==0):
        print(" Invalid password")
        invalid=1
      print(" No Special characters in it")

 if(invalid==0):
  print(" Valid password")

print("Choose criteria req: ")
print("1 UpperCase")
print("2 LowerCase")
print("3 Numbers")
print("4 Special Characters(!,@,#)")
crit=input()

n=int(input("No of passwords: "))
list=[]

for x in range(n):
  s=input("Enter password: ")
  list.append(s)
for i in list:
  if(len(i)<8):
    print(i)
    print(" Invalid password")
    print(" Less than 8 characters")
  else:
    Allcriteria(i,crit)
