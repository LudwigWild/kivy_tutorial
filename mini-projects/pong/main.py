import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.audio import SoundLoader
from kivy.properties import NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.vector import Vector

import random

################################## Classes ###################################

class Ball(Image):
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
	def __init__(self, **kwargs):
		super(PongGame, self).__init__(**kwargs)
		self.max_score = 3

	player_left_score = NumericProperty(0)
	player_right_score = NumericProperty(0)

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
		Clock.schedule_once(lambda x: SoundLoader.load('./sounds/serve_ball.wav').play(), 3)

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
			SoundLoader.load('./sounds/rebound.wav').play()

		# player rackets rebound
		elif self.ball.collide_widget(self.racket_left) or self.ball.collide_widget(self.racket_right):
			self.ball.velocity[0] *= -1
			SoundLoader.load('./sounds/rebound.wav').play()

		# ball went past the left goal
		elif self.ball.x < 0:
			SoundLoader.load('./sounds/goal.wav').play()
			Clock.unschedule(self.update_game) # stop updating the game
			self.player_left_score += 1 # update score of the winner

			if self.player_left_score == self.max_score:
				EndGamePopup().open("player_left", self.racket_left.color)
			else:
				self.serve_ball() # start a new game

		# ball went past the right goal
		elif self.ball.right > self.width:
			SoundLoader.load('./sounds/goal.wav').play()
			Clock.unschedule(self.update_game)
			self.player_right_score += 1

			if self.player_right_score == self.max_score:
				EndGamePopup().open("player_right", self.racket_right.color)
			else:
				self.serve_ball()

############################### EndGame Popup ################################

class EndGamePopup(Popup):
	def open(self, winner, winner_color, *args):
		"""
		Opens a popup showing the winning player, and give the choice to either:
		play again, go back to the menu, or quit the game.
		"""
		super(EndGamePopup, self).open()
		self.popup_label.color = winner_color

		if winner == "player_left":
			self.popup_label.text = "Left Player WON !"
		elif winner == "player_right":
			self.popup_label.text = "Right Player WON !"

##############################################################################

class KivyApp(App):
	def build(self):
		self.title = "Pong"
		Builder.load_file('ui.kv')

		pong = PongGame()
		pong.serve_ball()
		return pong

if __name__ == '__main__':
	KivyApp().run()
