def checkPalindrom(word):  
  a = word[::-1]
  if word == a:
    print("Слово является палиндромом")
  else:
    print("Слово не является палиндромом")
