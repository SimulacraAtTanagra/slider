from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import Config
from win32api import GetSystemMetrics
import os

#TODO - open this function to more programmatic manipulation

#from kivy.properties import  ObjectProperty

def get_sizes():
	screenx = GetSystemMetrics(0)
	screeny = GetSystemMetrics(1)
	return screenx,screeny

def center_window():
	sizex,sizey=get_sizes()
	Window.size = (sizex, sizey)
	Window.left = 0
	Window.top = 0


class CarouselApp(App):
	#img = ObjectProperty()
	
	def get_images(self):
		images=[]
		for i in os.listdir(os.getcwd()):
			if "png" in i:
				images.append(Image(source=i, allow_stretch = True, keep_ratio = True, size_hint=(1,1)))
		self.images=images
		
	def add_images(self):
		for image in self.images:
			self.carousel.add_widget(image)
		center_window()
		
	def reload_event(self,dt):
		self.get_images()
		self.carousel.clear_widgets()
		self.add_images()
		
		
	def build(self):
		self.carousel = Carousel(direction='right',loop="true")
		self.get_images()
		self.add_images()
		#center_window()
		
		#carousel.add_widget(self.image2)
		
		Clock.schedule_interval(self.carousel.load_next,5)
		Clock.schedule_interval(self.image_rel,60)
		Clock.schedule_interval(self.reload_event,300)
				
		
		return self.carousel

	def image_rel(self,dt):
		for ix,image in enumerate(self.images):
			self.images[ix].reload()

	def image_scr(self,dt):
		self.images=[]
		for i in os.listdir(os.getcwd()):
			if "png" in i:
				self.images.append(Image(source=i, allow_stretch = True, keep_ratio = True, size_hint=(1,1)))
		for image in self.images:
			carousel.add_widget(image)
			
if __name__=="__main__":
	CarouselApp().run()