import string
import nltk
nltk.download('punkt')
nltk.download('popular')
nltk.download('averaged_perceptron_tagger_eng')
leters = string.ascii_uppercase
def redact(original_string):
    new_string = ""
    tokenized = nltk.word_tokenize(original_string)
    tagged = nltk.pos_tag(tokenized)
    for pair in tagged:
        if(pair[1] == 'NNP'):
            new_string+= "redacted "
        else:
            new_string+= pair[0] + " "
    return new_string

eb_bio = "Erin came to Kehillah after getting her PhD in Cognitive Science \
from Stanford University, where she worked on projects in Natural Language \
Understanding and Computational Linguistics. Erin has taught many high school, \
college, and graduate students in classes at Stanford and UC San Diego and \
one-on-one online tutoring. She has taught a range of topics including Computer \
Science, Calculus, Statistics, Psychology, and Robotics. She loves combining her \
interests and skills in interdisciplinary projects. Outside of teaching, Erin \
enjoys rock climbing, quilting, juggling, acting, and spending time with her \
partner and her cat."
kuszmaul_bio = "Chris Kuszmaul has taught close to two dozen topics from Aikido \
to Computer Science to Creative writing in contexts from MIT, to Palo Alto High \
School to Tblisi State University for students ranging from elementary to \
undergraduates to NASA scientists. He was the first high school teacher of the \
Stanford Logic Curriculum, invented the data structure known as a Shadow Heap \
and holds a 6th degree black belt in Aikido. He retired from his position as a \
Senior Research Scientist at NASA to join a second (then third and fourth) \
startup. He re-retired into teaching and public service where he has functioned \
as the president of: Mountain View Kiwanis, The Slater PTA, and the Computer \
Science Teachers Association of Silicon Valley. Chris lives in Mountain View \
with his wife, Dr. Tracy King. They have two grown children — Jane is a farmer \
in Colorado and James is a robotics engineer in Mountain View. In his spare time \
Chris enjoys walks, tea, and announcing robotics matches at FIRST competitions. \
Chris teaches with the primary goal of knowing his students and adjusting to their \
needs: He combines project based and group work with the opportunity to work \
independently or to follow a tightly defined curriculum. Chris believes the best \
results happen when students grapple with complex challenges."
dsouza_bio = "Zoe was born and raised in London, England. She studied Classics at \
the undergraduate level at Durham University and pursued her Masters degree in \
Classics and Education at Cambridge University. She has taught Latin and \
Classics for the past 8 years, with a particular interest in epic poetry, Greek \
theatre, and the timeless entertainment of Ovid and Cicero. In her previous role, \
she was a Head of Year (a mixture of Dean of Students and College Counsellor), and \
as a result has developed a keen interest in mental health in young people, as \
well as enabling students to pursue Higher Education. In her spare time, Zoe is \
enjoying exploring California with her partner and their dog and enjoys good food, \
exercise, and women's soccer."
print(redact(eb_bio))
print(redact(kuszmaul_bio))
print(redact(dsouza_bio))