import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.vector import Vector
from kivy.properties import NumericProperty

import random

################################## classes ###################################

class Ball(Widget):
	def __init__(self, **kwargs):
		super(Ball, self).__init__(**kwargs)
		velocity = [0, 0]

	def move(self):
		"""
		Moves the ball to its t+1 position according to its velocity.
		"""
		self.pos = Vector(self.pos) + Vector(self.velocity)


class Racket(Widget):
	pass

############################# root widget class ##############################

class PongGame(FloatLayout):
	left_player_score = NumericProperty(0)
	right_player_score = NumericProperty(0)

	def serve_ball(self, *args):
		"""
		Serves the ball with a random direction/velocity after a 5 sec pause.
		"""
		self.ball.pos = self.center
		self.ball.velocity = [random.randint(-10, 10), random.randint(-10, 10)]
		
		# wait 5 sec, then call update_game() every 1/60 sec
		Clock.schedule_once(Clock.schedule_interval(self.update_game, 1.0/60), 5)

	def update_game(self, *args):
		"""
		Updates the state of the game to t+1 by moving the ball, dealing with
		collision/trajectories and starting a new game if a player makes a goal.
		"""
		self.ball.move()

		# top/bottom walls rebound
		if self.ball.top > self.top or self.ball.y < 0:
			self.ball.velocity[1] *= -1
		
		# player rackets rebound
		elif self.ball.collide_widget(self.racket_left) or self.ball.collide_widget(self.racket_right):
			self.ball.velocity[0] *= -1
		
		# ball went past the left goal
		elif self.ball.x < 0:
			Clock.unschedule(self.update_game)	# Stop updating the game.
			self.left_player_score += 1			# Update score of the winner.	
			self.serve_ball()					# Start a new game.

		# ball went past the right goal
		elif self.ball.right > self.width:
			Clock.unschedule(self.update_game)
			self.right_player_score += 1
			self.serve_ball()
		

class KivyApp(App):
	def build(self):
		self.title = "Pong"
		Builder.load_file('ui.kv')

		pong = PongGame()
		pong.serve_ball()
		return pong

##############################################################################

if __name__ == '__main__':
	KivyApp().run()
