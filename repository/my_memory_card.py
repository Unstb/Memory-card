#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5. QtWidgets import (Qapplication, Qwidget, QHBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)


app = QApplication([])


window = QWIdget()
window.setWindowTitle('Memo Card')

'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была снована Москва?')


RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')


Layout_ans1 = QHBoxLayout()
Layout_ans2 = QHBoxLayout()
Layout_ans3 = QHBoxLayout()
Layout_ans2.addWIdget(rbtn_1)
Layout_ans2.addWIdget(rbtn_2)
Layout_ans3.addWIdget(rbtn_3)
Layout_ans3.addWIdget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, aligment=(Qt.AlignHCenter / Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)

layout_line3.addStretch(1)
laoyut_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)



layout_card = QvBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStrench(1)
layout_card.addSpacing(5)

window.setLayout(layout_card)
window.show()
app.exec()