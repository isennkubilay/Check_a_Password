def checkPassword(password): 
  has_upper = False 
  has_lower = False 
  has_num = False 

  for ch in password:
    if ch >= "A" and ch <= "Z":
      has_upper = True 
    elif ch >= "a" and ch <= "z":
      has_lower = True
    elif ch >= "0" and ch <= "9":
      has_num = True 
  if len(password) >= 8 and has_upper and has_lower and has_num:
    return True 
  return False 
def main():
  p = input("Enter a password: ")
  if checkPassword(p):
    print("That's a good password.")
  else:
    print("That isn't a good password.")
if __name__ == "__main__":
  main()