# Given two strings, write a method to decide
# if one is a permutation (anagram) of the other



def anagram(s1, s2):
  #can't be anagrams if strings unequal lengths
  if len(s1) != len(s2):
    status = False
  else:
    sorted1 = sorted(s1.lower()) #returns an array
    sorted2 = sorted(s2.lower()) #returns an array
    for i in sorted1:
      for j in sorted2:
        if i == j:
          status = True
        else:
          status = False

  return status #true if anagram, false if not

def main():
  print str(anagram('HELLO', 'eHLlo'))

if __name__ == "__main__":
    main()

