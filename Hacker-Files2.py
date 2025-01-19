while True:
 acronym=input("Choose A Phrase : ")
 listData=acronym.split()
 result=""
 for data in listData:
     result=result+data[0].capitalize()  
 print(result)
