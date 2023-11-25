import json

with open('files/test.json', 'r') as file:
    content = file.read()

# Convert content of json file from str to list
data = json.loads(content)

for question in data:
    print(question['question text'])
    for index, alternatives in enumerate(question['alternatives']):
        print(index+1, ')', alternatives)
    user_input = int(input('Choose your answer : '))
    # Add new to the data file
    question['user_input'] = user_input

score = 0

for index, question in enumerate(data):
    if question['user_input'] == question['correct answer']:
        score += 1
        result = 'Correct'
    else:
        result = 'Wrong'

    message = f"For {index+1} question your answer is {question['user_input']}, correct answer is {question['correct answer']} -  {result}"
    print(message)

print(score, '/', len(data))



