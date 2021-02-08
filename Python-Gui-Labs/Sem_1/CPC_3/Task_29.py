letters = ''.join(input("Your string: "))
letters_lower = len(list(filter(lambda x : x.islower(), letters))) * (100/len(letters))
letter_upper = len(list(filter(lambda x : x.isupper(), letters))) * (100/len(letters))
print(f'All uppercase letters in a string compared '
      f'to the number \nof characters in the string - {letter_upper:.1f}%, '
      f'low letters - {letters_lower:.1f}%')
