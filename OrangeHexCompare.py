# Der3k Burrola
# July 2020
# Orange Hex Compare

import codeBase, os, kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import *


def orange_layout(self):
	

	file1Hex = codeBase.pick_file()
	file2Hex = codeBase.pick_file()
	files = codeBase.format_files_in_hex(file1Hex,file2Hex)
	file1Hex = files[0]
	file2Hex = files[1]
	hexCount = files[2]

	layout = GridLayout(cols=5)
	layout.add_widget(Label(text=hexCount, size_hint_x=None, width=50))

	separatorLabel = Label(size_hint_x=None, width=3)
	with separatorLabel.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=(42,0), size=(3,1000))
	layout.add_widget(separatorLabel)

	layout.add_widget(Label(text=file1Hex, markup=True))
	separatorLabel2 = Label(size_hint_x=None, width=3)
	with separatorLabel2.canvas:
            Color(1, 1, 1, 1)
            Rectangle(pos=(415, 0), size=(3,1000))
	layout.add_widget(separatorLabel2)
	layout.add_widget(Label(text=file2Hex, markup=True))
	return layout


class MyApp(App):

	def build(self):
		self.title = codeBase.ORANGE_EMOJI + 'Orange HexCompare' + codeBase.ORANGE_EMOJI
		layout = orange_layout(self)
		return layout

        


if __name__ == '__main__':
    MyApp().run()




