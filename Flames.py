def common_char_checker(first_name, second_name):

  first_name =list(first_name)
  second_name =list(second_name)
  common_char = []

  for char in first_name:
    if char in second_name:
      common_char.append(char)
      second_name.remove(char)
  
  first_remaining = [char for char in first_name if char not in common_char]
  second_remaining = [char for char in second_name if char not in common_char]

  left_letters = first_remaining + second_remaining
  left_letter_count = len(left_letters)
  
  return left_letter_count 
  

def finding_magic_word(count):

  result= ""
  removed_letter=[]
  total_letter =["f","l","a","m","e","s"]
  str_flame= list(count* count * "flames")
  
  while len(removed_letter) < 5:
    removed_letter.append(str_flame[count-1])
    jumping_letter = str_flame[count-1]

    str_flame = str_flame[count:]
      
    while jumping_letter in str_flame:
      str_flame.remove(jumping_letter)

  for letter in total_letter:
    if letter not in removed_letter:
      result = letter    
  return result


def flames():
  
  word_dict ={"f":"Friends", 
              "l":"Love",
              "a":"Affection",
              "m" :"Marriage" ,
              "e":"Enemy",
              "s":"Siblings"}
              
  print("Enter two names and I'll tell you the relationship you both share...\n")
  person1 = input("Person 1: ").lower()
  person2 = input("Person 2: ").lower()

  count = common_char_checker(person1, person2)
  
  the_word = finding_magic_word(count)
  
  print(f"\nYou both share a relationship of {word_dict[the_word]}.")

flames()