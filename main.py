import pandas

student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

student_dict = {series.letter:series.code for (index,series) in {index: series for (index,series) in student_data_frame.iterrows()}.items()}

user_text = input("Enter the name : ")
letter_dict = {letter: student_dict[letter] for letter in user_text.upper()}
print(letter_dict)
