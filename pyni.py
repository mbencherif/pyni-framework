import pygame
from openni import *
import numpy
import cv

class PyNI:
	def __init__(self, res=RES_VGA, fps=30):
		self.context = Context()
		self.context.init()

		self.res = res
		self.fps = fps

		self.depth_generator = DepthGenerator()
		self.depth_generator.create(self.context)
		self.depth_generator.set_resolution_preset(self.res)
		self.depth_generator.fps = self.fps

		self.image_generator = ImageGenerator()
		self.image_generator.create(self.context)
		self.image_generator.set_resolution_preset(self.res)
		self.image_generator.fps = self.fps

		self.context.start_generating_all()

		self.running = True
	# __init__

	def update(self):
		self.context.wait_any_update_all()
		cv.WaitKey(10)
	# update

	def draw_rgb(self, surface):
		rgb_frame = self.capture_rgb_frame()

		surface.blit(rgb_frame, (0, 0))
	# draw_rgb

	def draw_depth(self, surface):
		depth_frame = self.capture_depth_frame()

		surface.blit(depth_frame, (0, 0))
	# draw_depth

	def capture_rgb_frame(self):
		frame = numpy.fromstring(self.image_generator.get_raw_image_map_bgr(), dtype=numpy.uint8).reshape(480, 640, 3)
		image = cv.fromarray(frame)
		cv.CvtColor(cv.fromarray(frame), image, cv.CV_BGR2RGB)
		pygame_image = pygame.image.frombuffer(image.tostring(), cv.GetSize(image), 'RGB')

		return pygame_image
	# capture_rgb_frame

	def capture_depth_frame(self):
	# capture_depth_frame

	def quit(self):
		self.context.stop_generating_all()
	# quit
# Main
