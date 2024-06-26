from textwrap import dedent
from crewai import Agent

class GameAgents():
	def game_designer_agent(self):
		return Agent(
			role='Game Designer',
			goal='Generate Story and Lore for the game',
			backstory=dedent("""\
				You are a Senior Game Designer at the hottest educational game studio in the world.
                You write fantastic, original game narratives that help make technical concepts
                fun to learn."""),
			allow_delegation=False,
			verbose=True
		)

	def game_engineer_agent(self):
		return Agent(
			role='Game Engineer',
  		goal='Create technically correct game material',
  		backstory=dedent("""\
				You are a software engineer that can implement the game designer's lore.
                You are an expert in SQL and always write perfect, efficient SQL."""),
			allow_delegation=False,
			verbose=True
		)

	def qa_engineer_agent(self):
		return Agent(
			role='Chief Software Quality Control Engineer',
  		goal='Ensure that the code does the job that it is supposed to do',
  		backstory=dedent("""\
				You feel that programmers always do only half the job, so you are
				super dedicate to make high quality code."""),
			allow_delegation=True,
			verbose=True
		)
  
	def game_artist_agent(self):
		return Agent(
			role='Senior Game Artist',
			goal='Generate captivating, high-quality art that really helps the player enjoy the game.',
			backstory=dedent("""\
				You want our customers to have a really fun and immersive game experience, 
				and you realize game art is a big part of that so you create the highest quality, polished art."""),
			allow_delegation=False,
			verbose=True
		)