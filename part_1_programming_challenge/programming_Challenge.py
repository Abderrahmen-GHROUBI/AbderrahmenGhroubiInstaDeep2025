def palindrome(s:str)-> bool:
  try:
    #erase , espace and ' 
    sClean = s.replace(",",'').replace(" ",'').replace("'","").lower()
    #test if it is palindrome
    return sClean == sClean[::-1]
  except Exception as e:
      print (f"error :{e}")


    
if __name__ == "__main__":
    print("Please enter the phrase that you want test it :")
    s = str(input())
    print(f"if the phrase is palindrome you will have True if not you will have  False : {palindrome(s)}")
    