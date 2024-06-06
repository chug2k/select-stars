from textwrap import dedent
from crewai import Task

class GameTasks():
    
	def generate_story_task(self, agent, callback):
		return Task(description=dedent(f"""\
            Create a game narrative for a game that teaches people SQL. The game should show progression 
            through not only the game's narrative, but also through the SQL concepts. We will only focus
            on how to use SQL to query data, not on database design or administration.
            
            The narrative should be inspired by one of the following: popular sci-fi like BladeRunner,
            fantasy like Harry Potter, adventure like Pirates of the Carribean, or romance like Titanic. Choose
            one of the above and create a narrative that offers a typical hero's journey,
            with a satisfying conclusion. Do not choose narratives involving rebellion, an ancient artifact, an oracle, 
            hackers, powerful corporations, or artificial intelligence."""),
            expected_output="A detailed game narrative that incorporates SQL querying concepts within a chosen genre's storyline without involving restricted themes.",
			agent=agent,
			callback=callback
		)

	def generate_dataset_task(self, agent, callback):
		return Task(description=dedent("""\
        We are creating a level for a game that teaches people SQL. To go through SQL, we need to create
        a sample dataset, with sufficient queries. Generate a dataset that is relevant to the narrative.
        Your output should be actual SQL CREATE TABLE and SQL INSERT queries to run, which we can run in a future step.
        There should be a sufficient number of rows and tables in our dataset to ensure the game is interesting.

        The narrative is given from the game designer in the previous step.
        """),
        expected_output=dedent("""\
        The full SQL commands to run to create the relevant tables and insert statements.
        Give the SQL CREATE TABLE commands first, and then the SQL INSERT commands second.
        """),
        agent=agent,
        callback=callback
    )

	def generate_questions_task(self, agent, callback):
		return Task(description=dedent(f"""\
			You are creating 10 questions to teach people SQL. The questions should start easy,
            and then get more complicated. The questions should be based on the following tables,
            given in the context, from the previous step."""),
            expected_output=dedent("""\
            Your Final answer must be ten questions. For each question, generate a fun intro text 
            explaining to the player why this SQL question fits into the narrative, information about what 
            SQL concept the player is learning, and then a fun success message when the player successfully
            solves the question.
			"""),
			agent=agent,
			callback=callback
		)