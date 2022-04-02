from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QButtonGroup, QPushButton, QLabel, QVBoxLayout,QHBoxLayout,QGroupBox,QRadioButton
from random import shuffle
from random import randint

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от ,,Memory_card" ')
question = QLabel('В каком году умер Сталин?')
RadioGroupBox = QGroupBox('Варианты ответов:')
rbtn_1 = QRadioButton('1953')
rbtn_2 = QRadioButton('2000')
rbtn_3 = QRadioButton('1900')
rbtn_4 = QRadioButton('2021')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout1 = QVBoxLayout()

AnswerGroupBox = QGroupBox('Результат теста')
label1 = QLabel('правильно\неправильно')
label2 = QLabel('Правильный ответ')
layout1.addWidget(label1)
layout1.addWidget(label2)
AnswerGroupBox.setLayout(layout1)

button = QPushButton('Ответить')

line = QVBoxLayout()
line.addWidget(question, alignment = Qt.AlignCenter)
line.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
line.addWidget(AnswerGroupBox, alignment = Qt.AlignCenter)
line.addWidget(button, alignment = Qt.AlignCenter)
main_win.setLayout(line)

AnswerGroupBox.hide()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []
q1 = Question('Сколько стоит Ford Mustang GT 500?', '54 200$', '10 000$', '100 000$', '1$')
question_list.append(q1)
q2 = Question('taurus raging hunter - это...', 'револьвер', 'энергетик', 'машина', 'кино')
question_list.append(q2)
q3 = Question('Из кого оружия среляет главный герой в сериале (The Walking dead)?', 'colt python 357 magnum', 'ак-47', 'арбалет', 'снайперка')
question_list.append(q3)
q4 = Question('Кто победил на maincraft голосовании 2021?', 'allay', 'copper golem', 'glare', 'никто')
question_list.append(q4)
q5 = Question('Сколько месяцев в году имеют 29 дней?', '11', '4', '1', '12')
question_list.append(q5)
q6 = Question('2+2*2=', '6', '8', '100', '12')
question_list.append(q6)
q7 = Question('Когда произошёл взрыв Чернобыльской АЭС?', '26 апреля 1986г. ', 'вчера', '1 сентября 2000г.', '12 декабря 2012г.')
question_list.append(q7)
q8 = Question('Что имено произошло на ЧАЭС?', 'взорвался реактор РБМК-1000 4го энергоблока', 'ударила молния', 'муха врезалась в провода', 'незнаю')
question_list.append(q8)
q9 = Question('В каком году вышел Assasins Creed 3?', '2012г.', '1945г.', '2021г.', '998г.')
question_list.append(q9)
q10 = Question('В каком году вышел S.T.A.L.K.E.R.: Тень чернобыля?', '2007г.', '1900г.', '2020г.', '2008г.')
question_list.append(q10)

def show_result():
    button.setText('Следующий вопрос')
    RadioGroupBox.hide()
    AnswerGroupBox.show()

def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    label2.setText(q.right_answer)
    show_question()

def show_correct(res):
    label1.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        main_win.score += 1
        print('-Правильных ответов:', main_win.score)
        show_correct('правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('неверно')



def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:', main_win.total)
    cur_question = randint(0, len(question_list) - 1)
    if cur_question >= len(question_list):
        cur_question = 0
    pc = question_list[cur_question]
    ask(pc)


def click_OK():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

main_win.cur_question = -1

main_win.score = 0
main_win.total = 0
button.clicked.connect(click_OK)
main_win.show()
app.exec_()