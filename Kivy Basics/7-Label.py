from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
	"""docstring for ClassName"""
	def build(self):
		return Label(text='Hello work')

if __name__ =='__main__':
	MyApp().run()