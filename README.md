# Hangman

In this work, I will implement different machine learning models and approaches to solve the hangman problem.

The train.txt has 100k words for training the models. The test.txt has 10k words for testing the models.

The first approach is by using frequency heuristics. The code could be found in the Frequency folder. The approach is as following: 
First, the algorithm computes the frequency of each letter from a given training dataset and ranks the letters in order of their frequency, from most to least common. During the game, the algorithm starts by guessing the most frequent letter that has not been guessed yet. If the guessed letter is present in the word, it reveals all occurrences of that letter at their respective positions. If the letter is not present, the algorithm loses one attempt. This process continues until either the word is completely guessed or the maximum number of incorrect attempts (set to 6) is exhausted. By leveraging the frequency patterns from the training dataset, this strategy aims to increase the probability of making correct guesses and minimize the number of incorrect attempts.

This method is the most simplest way (not counting random guessing algorithm) to play hangman game. The Accuracy achieved from this method on the above train and test data is: 15.37% 

Here is the colab file: https://colab.research.google.com/drive/1ewwVwVZTlTrF3Bm6DPQA-KnDPTjn9tPw?usp=sharing

The second approach I tried was some modification I made to the first approach. For each test word, instead of using the overall letter frequencies, the algorithm narrows down the frequency calculations to only include training words that have the same length as the test word. This way, the model makes guesses based on a smaller set of words. I thought it might work, but there are some flaws in this approach. First, if the test and train data is disjoint, then it doesn't matter if I do this modification, because the train data might have, say, 'e' as the most frequent letter, but the testing data may contain words that might not even have 'e' in them. The accuracy achieved from this method is: 15.46%
