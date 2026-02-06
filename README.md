[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=22561572&assignment_repo_type=AssignmentRepo)
# 3.4 Redacted  

Make a function that takes as input some long string and returns a new string where all proper nouns are replaced with with "[Redacted]"

Assume that any capitalized word is a proper noun. This means the first word of every sentence will be redacted. That's OK.

For an extra challenge you could try:
* Do not redact capitalized words that come at the beginning of a sentence. (don't worry about proper nouns that come at the beginning of a sentence)
* You could replace each name with a string of "*" the same length as the name
* You could replace multiple names in a row with just a single "[Redacted]"
* If you want to get *really* fancy, you can go learn about lists in Python and about the natural language processing library [spacy](https://spacy.io/).