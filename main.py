"""
Again, the code is broken, you need to create 4 functions.
  - add_to_dict: Add a word to a dict.
  - get_from_dict: Get a word from inside a dict.
  - update_word: Update a word inside of the dict.
  - delete_from_dict: Delete a word from the dict.

All this functions should check for errors, follow the comments to see all cases you need to cover.

There should be NO ERRORS from Python in the console.
"""

# 딕셔너리에 key-value 추가 함수
def add_to_dict(dict={}, key=0, value=None):
  if str(type(dict)) != "<class 'dict'>" : #dict가 없을때
    print("You need to send a dictionary. You sent : {} ".format(type(dict)))

  elif key == None or value == None: #value가 없을 때
    print("You need to send a word and a definiton")
  
  elif key in dict.keys(): #이미 딕셔너리에 가지고 있는 key를 수정하려 할 때
    print("{} is already on the dictionary. Won't add".format(key))

  else: #key-value를 딕셔너리에 저장
    dict[key]=value
    print("{} has been added.".format(key))
    print(dict)


   
  
  
#딕셔너리에 key-value 얻기
def get_from_dict(dict={}, key=None, value=None):
  if str(type(dict)) != "<class 'dict'>" : #dict가 없을때
    print("You need to send a dictionary. You sent : {} ".format(type(dict)))

  elif key == None : #얻고자 하는 key를 입력 하지 않았을 때
    print("You need to send a word to search for")
  
  else:
    if dict.get(key) == None: #key가 없을때
      print("{} was not found in this dict".format(key))

    else : #key가 검색됐으면 출력
     print(dict)

#딕셔너리 에서 key-value 수정
def update_word(dict={}, key=None, value=None):
  if str(type(dict)) != "<class 'dict'>" : #dict가 없을때
    print("You need to send a dictionary. You sent : {} ".format(type(dict)))

  elif value == None : #얻고자 하는 key를 입력 하지 않았을 때
    print("You need to send a word and a definiton to update")

  else:
    if dict.get(key)==None:
      print("{} is not on the dict. Can't update non-existing word.")
    
    else:
      dict[key]=value
      print("{} has been updated to : {}".format(key,value))

#딕셔너리에서 key-value 삭제
def delete_from_dict(dict={}, key=None):
  if str(type(dict)) != "<class 'dict'>" : #dict가 없을때
    print("You need to send a dictionary. You sent : {} ".format(type(dict)))

  elif key == None : #얻고자 하는 key를 입력 하지 않았을 때
    print("You need to send a word to delete")
  
  else:
    if dict.get(key)==None:
      print("{} is not on the dict. Won't delete.".format(key))
    
    else:
      del dict[key]
      print("{} has been deleted.".format(key))

# \/\/\/\/\/\/\ DO NOT TOUCH  \/\/\/\/\/\/\

import os

os.system('clear')


my_english_dict = {}

print("\n###### add_to_dict ######\n")

# Should not work. First argument should be a dict.
print('add_to_dict("hello", "kimchi"):')
add_to_dict("hello", "kimchi")

# Should not work. Definition is required.
print('\nadd_to_dict(my_english_dict, "kimchi"):')
add_to_dict(my_english_dict, "kimchi")

# Should work.
print('\nadd_to_dict(my_english_dict, "kimchi", "The source of life."):')
add_to_dict(my_english_dict, "kimchi", "The source of life.")

# Should not work. kimchi is already on the dict
print('\nadd_to_dict(my_english_dict, "kimchi", "My fav. food"):')
add_to_dict(my_english_dict, "kimchi", "My fav. food")


print("\n\n###### get_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\nget_from_dict("hello", "kimchi"):')
get_from_dict("hello", "kimchi")

# Should not work. Word to search from is required.
print('\nget_from_dict(my_english_dict):')
get_from_dict(my_english_dict)

# Should not work. Word is not found.
print('\nget_from_dict(my_english_dict, "galbi"):')
get_from_dict(my_english_dict, "galbi")

# Should work and print the definiton of 'kimchi'
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

print("\n\n###### update_word ######\n")

# Should not work. First argument should be a dict.
print('\nupdate_word("hello", "kimchi"):')
update_word("hello", "kimchi")

# Should not work. Word and definiton are required.
print('\nupdate_word(my_english_dict, "kimchi"):')
update_word(my_english_dict, "kimchi")

# Should not work. Word not found.
print('\nupdate_word(my_english_dict, "galbi", "Love it."):')
update_word(my_english_dict, "galbi", "Love it.")

# Should work.
print('\nupdate_word(my_english_dict, "kimchi", "Food from the gods."):')
update_word(my_english_dict, "kimchi", "Food from the gods.")

# Check the new value.
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")


print("\n\n###### delete_from_dict ######\n")

# Should not work. First argument should be a dict.
print('\ndelete_from_dict("hello", "kimchi"):')
delete_from_dict("hello", "kimchi")

# Should not work. Word to delete is required.
print('\ndelete_from_dict(my_english_dict):')
delete_from_dict(my_english_dict)

# Should not work. Word not found.
print('\ndelete_from_dict(my_english_dict, "galbi"):')
delete_from_dict(my_english_dict, "galbi")

# Should work.
print('\ndelete_from_dict(my_english_dict, "kimchi"):')
delete_from_dict(my_english_dict, "kimchi")

# Check that it does not exist
print('\nget_from_dict(my_english_dict, "kimchi"):')
get_from_dict(my_english_dict, "kimchi")

# \/\/\/\/\/\/\ END DO NOT TOUCH  \/\/\/\/\/\/\