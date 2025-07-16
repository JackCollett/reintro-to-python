# Video alternative: https://vimeo.com/954334103/0aed500d39#t=1295

from lib.helpers import check_that_these_are_equal

# Now it's your turn.

# Note that the exercise will be (a little) less challenging than the example.

# Write a function that takes a list of words and returns a report of all the
# words that are longer than 10 characters but don't contain a hyphen. If those
# words are longer than 15 characters, then they should be shortened to 15
# characters and have an ellipsis (...) added to the end.

# For example, if the input is:
# [
#   'hello',
#   'nonbiological',
#   'Kay',
#   'this-is-a-long-word',
#   'antidisestablishmentarianism'
# ]
# then the output should be:
# "These words are quite long: nonbiological, antidisestablis..."

# @TASK: Complete this exercise.

print("")
print("Function: report_long_words")

def report_long_words(words):
    long_words = get_long_words_only(words)
    long_unhyphened_words = get_unhyphened_words(long_words)
    long_unhyphened_shortened_words = shorten_very_long_words(long_unhyphened_words)
    return f"These words are quite long: {long_unhyphened_shortened_words}"

def get_long_words_only(words):
    long_words = []
    for word in words:
      if len(word) > 9:
        long_words.append(word)
    return long_words

def get_unhyphened_words(long_words):
    long_unhyphened_words = []
    for word in long_words:
      if "-" not in word:
        long_unhyphened_words.append(word)
    return long_unhyphened_words

def shorten_very_long_words(long_unhyphened_words):
    long_unhyphened_shortened_words = ""
    for word in long_unhyphened_words:
      if len(word) > 15:
        word = word[0:15] + "..."
      long_unhyphened_shortened_words += word + ", "
    return long_unhyphened_shortened_words[:-2]
  
print(shorten_very_long_words([
      'hello',
      'nonbiological',
      'Kay',
      'this-is-a-long-word',
      'antidisestablishmentarianism'
    ]))

check_that_these_are_equal(
  report_long_words([
    'hello',
    'nonbiological',
    'Kay',
    'this-is-a-long-word',
    'antidisestablishmentarianism'
  ]),
  "These words are quite long: nonbiological, antidisestablis..."
)

check_that_these_are_equal(
  report_long_words([
    'cat',
    'dog',
    'rhinosaurus',
    'rhinosaurus-rex',
    'frog'
  ]),
  "These words are quite long: rhinosaurus"
)

check_that_these_are_equal(
  report_long_words([
    'cat'
  ]),
  "These words are quite long: "
)

# Once you're done, move on to 041_challenge_2_example.py
