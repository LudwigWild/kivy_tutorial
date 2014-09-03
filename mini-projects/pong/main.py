import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock
from kivy.vector import Vector

import random

################################## Classes ###################################

class Ball(Widget):
	def __init__(self, **kwargs):
		super(Ball, self).__init__(**kwargs)
		velocity = [0, 0]

	def move(self):
		"""
		Moves the ball to its t+1 position according to its velocity.
		"""
		self.pos = Vector(self.pos) + Vector(self.velocity)

############################# Root Widget Class ##############################

class PongGame(FloatLayout):
	left_player_score = NumericProperty(0)
	right_player_score = NumericProperty(0)

	def serve_ball(self, *args):
		"""
		Serves the ball after a 3 sec pause, giving the ball a fixed velocity,
		and a random direction.
		"""
		self.ball.center = self.center

		# velocity is 7 or -7 ; angle is between -75° and 75°
		self.ball.velocity = Vector([random.choice([-7, 7]), 0]).rotate(random.randint(-75, 75))
		
		# wait 3 sec, then call update_game() every 1/60 sec
		Clock.schedule_once(lambda x: Clock.schedule_interval(self.update_game, 1.0/60), 3)

	def on_touch_move(self, touch):
		"""
		If a player touches the screen within the left/right half-part of this widget,
		it will moves the left/right racket to the y-touch coordinate.
		"""
		if touch.x < self.width/2:
			self.racket_left.center_y = touch.y
		else:
			self.racket_right.center_y = touch.y

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
