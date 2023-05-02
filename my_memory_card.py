#создай приложение для запоминания информации
from PyQt5.QtCore import Qt 
from random import shuffle
from PyQt5.QtWidgets import ( 
    QApplication, 
    QWidget, 
    QHBoxLayout, 
    QVBoxLayout, 
    QGroupBox, 
    QButtonGroup, 
    QRadioButton, 
    QPushButton, 
    QLabel, 
) 

class Question():
    def __init__(
        self, question, right_answer,
        wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Португалии?',
'Португальский', 'Английский', 'Испанский', 'Французский'))

questions_list.append(Question('Самая прибыльная игра?',
'Honor of king', 'Minecraft', 'Clash of Clans', 'Teraria'))

questions_list.append(Question('Самое прибыльное аниме?',
'Ходячий замок', 'JOJO Bizare Adventure', 'Mononoke Hime', 'Атака титанов'))

questions_list.append(Question('Как называется жанр аниме с активным участием боевых роботов?',
'Меха', 'Киберпанк', 'Спокон', 'Моэ'))

questions_list.append(Question(' В какой стране появился и получил своё развитие жанр аниме?',
'Япония', 'Китай', 'США', 'Вьетнам'))

questions_list.append(Question(' В каком году вышла игра (Dota 2)?',
'2012г', '1990г', '2003г', '2020г'))

questions_list.append(Question('Сколько стоит GTA 5?',
'999', '1234', '909', '123'))

questions_list.append(Question(' Сколько игр в стиме?',
'80000', '200345', '10234', '12000'))

questions_list.append(Question(' Создатель Minecraft?',
'Дайкозиев Боходир', 'Маркус Перссон', 'Антон Антоныч', 'Антон Василичь'))


app = QApplication([]) 
main_win = QWidget() 
main_win.setWindowTitle("Memory Card") 
main_win.resize(300, 300) 

 
text_question = QLabel("Какой национальности не существует?") 
btn_answer = QPushButton("Ответить") 
 
# Начало Группы вопроса 
RadioGroupBox = QGroupBox("Варианты ответов") 
 
rbtn1 = QRadioButton("Энцы") 
rbtn2 = QRadioButton("Смурфы") 
rbtn3 = QRadioButton("Чулымцы") 
rbtn4 = QRadioButton("Алеуты") 

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)
 
group_vline1 = QVBoxLayout() 
group_vline2 = QVBoxLayout() 
group_main = QHBoxLayout() 
 
group_vline1.addWidget(rbtn1, alignment=Qt.AlignLeft) 
group_vline1.addWidget(rbtn2, alignment=Qt.AlignLeft) 
 
group_vline2.addWidget(rbtn3, alignment=Qt.AlignRight) 
group_vline2.addWidget(rbtn4, alignment=Qt.AlignRight) 
 
group_main.addLayout(group_vline1) 
group_main.setSpacing(50) 
group_main.addLayout(group_vline2) 

 
RadioGroupBox.setLayout(group_main) 
# # Конец группы вопроса 
AnsGroupBox = QGroupBox("Результат теста") 
text_answer = QLabel("Правильно/Неправильно") 
text_right_answer = QLabel("какой то правильный ответ!") 
 
ans_main_line = QVBoxLayout() 
ans_main_line.addWidget(text_answer, alignment=Qt.AlignLeft) 
ans_main_line.setSpacing(30) 
ans_main_line.addWidget(text_right_answer, stretch=10) 
 
AnsGroupBox.setLayout(ans_main_line) 
AnsGroupBox.hide() 
 
layout_main = QVBoxLayout() 
 
layout_main.addWidget(text_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter)) 
layout_main.addWidget(RadioGroupBox, alignment=Qt.AlignCenter) 
layout_main.addWidget(AnsGroupBox, alignment=Qt.AlignCenter) 
 
layout_main.addSpacing(50) 
layout_main.addWidget(btn_answer, stretch=2) 

def show_question():
    print('Показать правильный ответ!')
    AnsGroupBox.hide()
    
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

    RadioGroupBox.show()
    btn_answer.setText('Ответить')

def show_result():
    print('Варианты ответов!')
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_answer.setText('Следующий вопрос')

def start_test():
    if btn_answer.text() == 'Ответить':
        show_result()
    else:
        show_question()
answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

    text_question.setText(q.question)
    text_right_answer.setText(q.right_answer)
    btn_answer.setText('Ответить')
    AnsGroupBox.hide()
    RadioGroupBox.show()

def check_answer():
    if answers[0].isChecked() == True:
        show_correct('Правильно!')
    else:
        show_correct('Неправильно!')

def show_correct(res):
    RadioGroupBox.hide()
    AnsGroupBox.show()
    text_answer.setText(res)
    btn_answer.setText("Следующий вопрос")

main_win.cur_question = -1
def next_question():
    main_win.cur_question += 1
    if main_win.cur_question == len(questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)

def click_ok():
    if btn_answer.text() == 'Ответить':
        if ( rbtn1.isChecked() == True or rbtn2.isChecked() == True or
        rbtn3.isChecked() == True or rbtn4.isChecked() == True ):
            check_answer()
    else:
        next_question()

q = Question('Cколько месяцев в году?', '12', '32', '14', '75')
next_question()

btn_answer.clicked.connect(click_ok)
 
main_win.setLayout(layout_main) 
 
main_win.show() 
app.exec_()