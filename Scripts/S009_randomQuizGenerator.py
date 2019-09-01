#-*-conding:utf-8-*-
#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import os
import random
import pprint

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'LittleRock',
            'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover',
            'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise',
            'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'DesMoines', 'Kansas': 'Topeka',
            'Kentucky': 'Frankfort', 'Louisiana': 'BatonRouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis',
            'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'SaintPaul', 'Mississippi': 'Jackson',
            'Missouri': 'JeffersonCity', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'CarsonCity',
            'NewHampshire': 'Concord', 'NewJersey': 'Trenton', 'NewMexico': 'SantaFe', 'NewYork': 'Albany',
            'NorthCarolina': 'Raleigh', 'NorthDakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'OklahomaCity',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'RhodeIsland': 'Providence', 'SouthCarolina': 'Columbia',
            'SouthDakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'SaltLakeCity',
            'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'WestVirginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

if not os.path.exists(r'.\quizzes'):
    os.mkdir(r'.\quizzes')
if not os.path.exists(r'.\answers'):
    os.mkdir(r'.\answers')

# Generate 35 quiz files.
for quizNum in range(35):
    quiz_file = open('quizzes\capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answer_file = open('answers\capitalanswer%s.txt' % (quizNum + 1), 'w')

    quiz_file.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quiz_file.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1))
    quiz_file.write('\n\n')

    answer_file.write("Answers of State Capitals Quiz (Form %s) \n\n" % (quizNum + 1))

    states = list(capitals.keys())
    random.shuffle(states)
    for s in range(len(states)):
        correct_answer = capitals[states[s]]
        wrong_answers = list(capitals.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers, 3)
        wrong_answers.append(correct_answer)
        answerOptions = wrong_answers
        random.shuffle(answerOptions)

        quiz_file.write('\n' + str(s + 1) + '. Which one below is ' + states[s] + '\'s capital?\n')
        for o in range(len(answerOptions)):
            quiz_file.write('ABCD'[o] + '.' + answerOptions[o] + '\n')

        answer_file.write(str(s + 1) + '.' + 'ABCD'[answerOptions.index(correct_answer)] + '.' + answerOptions[
            answerOptions.index(correct_answer)]+'\n')

    quiz_file.close()
    answer_file.close()
