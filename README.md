# Hangman

In this work, I will implement different machine learning models and approaches to solve the hangman problem.

The train.txt has 100k words for training the models.
The test.txt has 100k words for testing the models.

The first approach is by using frequency heuristics. The code could be found in the Frequency folder. The approach is as following: 
First, the algorithm computes the frequency of each letter from a given training dataset and ranks the letters in order of their frequency, from most to least common. During the game, the algorithm starts by guessing the most frequent letter that has not been guessed yet. If the guessed letter is present in the word, it reveals all occurrences of that letter at their respective positions. If the letter is not present, the algorithm loses one attempt. This process continues until either the word is completely guessed or the maximum number of incorrect attempts (set to 6) is exhausted. By leveraging the frequency patterns from the training dataset, this strategy aims to increase the probability of making correct guesses and minimize the number of incorrect attempts.

This method is the most simplest way (not counting random guessing algorithm) to play hangman game. The Accuracy achieved from this method on the above train and test data is: 15.929% 
