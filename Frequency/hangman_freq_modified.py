import requests

train_url = 'https://raw.githubusercontent.com/InfernoAsura/Hangman/refs/heads/main/train.txt'
response = requests.get(train_url)
data = response.text
data = data.lower()

test_url = 'https://raw.githubusercontent.com/InfernoAsura/Hangman/refs/heads/main/test.txt'
response_test = requests.get(test_url)
test_data = response_test.text
test_data = test_data.lower()

def select_dict(data, word):
  frequency = {}

  for words in data.splitlines():
    if len(words) == len(word):
      for letter in words:
        if letter in frequency:
          frequency[letter] += 1
        else :
          frequency[letter] = 1
  sorted_freq = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True)) 
  sorted_freq_list = list(sorted_freq.keys())
  return sorted_freq_list

# incorrect number of guesses allowed
remaining_tries = 6

def print_format(tries, word):
  print(f"Number of tries remaining: {tries} and word: {word}")

correct_guesses_modified = 0
incorrect_guesses_modified = 0

for word in test_data.splitlines():
  remaining_tries = 6
  current_state = ''.join(['_' for _ in word])
  print_format(remaining_tries, current_state)
  sorted_freq_mod_list = select_dict(data, word)


  for letter in sorted_freq_mod_list:
    if remaining_tries == 0:
      print("Out of Attempts, the correct word was: " + word)
      incorrect_guesses_modified += 1
      break 

    if '_' not in current_state:
      print("The word was guessed correctly.")
      print_format(remaining_tries, current_state)
      correct_guesses_modified += 1
      break

    if letter in word:
      current_word_list = list(current_state)
      for index, let in enumerate(word):
          if letter == let:  
              current_word_list[index] = let
      current_state = ''.join(current_word_list)

    else: 
      remaining_tries -= 1

    print_format(remaining_tries, current_state)

print(correct_guesses_modified)
print(correct_guesses_modified + incorrect_guesses_modified)

print(f"Accuracy: {(correct_guesses_modified / (correct_guesses_modified + incorrect_guesses_modified))}" )