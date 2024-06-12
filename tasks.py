from textwrap import dedent
from crewai import Task


class GameTasks():
    
	def generate_story_task(self, agent, callback):
		return Task(description=dedent(f"""\
            Create a game narrative for a game that teaches people SQL. The game should show progression 
            through not only the game's narrative, but also through the SQL concepts. We will only focus
            on how to use SQL to query data, not on database design or administration.
            
            The narrative should be inspired by popular sci-fi like Star Wars, or
            adventure like Pirates of the Carribean.
            Do not choose narratives involving rebellion, an ancient artifact, an oracle, 
            hackers, powerful corporations, wizards, scrolls, libaries, Queryville, or artificial intelligence.
            """),
            expected_output=dedent(f"""\
            Intro text to present to the player to familiarize them with the game world, explain their motivations, 
            and kick off the game. Do not preface with Intro Text:, just give the text to present to the player. 
            """),
			agent=agent,
			callback=callback
		)

	def generate_dataset_task(self, agent, callback):
		return Task(description=dedent("""\
        We are creating a level for a game that teaches people SQL. To go through SQL, we need to create
        a sample dataset, with sufficient queries. Generate a dataset that is relevant to the narrative.
        Your output should be actual SQL CREATE TABLE and SQL INSERT queries to run in Sqlite, which we can run in a future step.
        There must be at least 3 tables.
        Each table must have at least 5 rows of data. 

        The narrative is given from the game designer in the previous step. You only output SQL statements, that are 
        supported by SQLite.
        """),
        expected_output=dedent("""\
        Only SQL commands to run to create the relevant tables and insert statements to insert at lesat 5 rows of data for each table.
        Don't use any markdown or code block formatting in the output or commentary. 
        Do not include anything other than SQL commands, all ending with a ;. 
        Write all the SQL commands with TEXT field within double quotes.
        """),
        agent=agent,
        callback=callback
    )

	def generate_questions_task(self, agent, callback):
		return Task(description=dedent(f"""\
			You are creating 10 questions to teach people SQL. The first question should be easy,
            but the second question should be difficult, and test advanced SQL concepts. 
            The questions must be based on the tables from the previous step."""),
            expected_output=dedent("""\
            Your Final answer must be a syntactically correct YAML of ten questions. Follow the format given below. 
            
            questions:
                - intro: <flavor text>
                  prompt: <question prompt>
                  solution: <sql solution>
                  success: <success message>
                    
            The intro text should be fun and engaging, and it should be a good fit for the narrative.
            The prompt should be a good fit for the narrative, and it should be a good fit for the SQL concept.
            The solution should be clean, simple SQL that solves the question, and be instructional. 
            The success message should be fun and engaging, and it should be a good fit for the narrative, and transition us into the next question.
			Do not include markdown formatting, neither triple quotes code blocks. Generate YAML only.
            Ensure the YAML is syntactically correct.
			"""),
			agent=agent,
			callback=callback
		)
  
    # Okay, learned this the hard way - don't generate the image as part of this. 
    # The Agent will try to retry and stuff and generally just get stuck on the actual generation somehow - 
    # we just call an API anyway.
	def generate_image_task(self, agent, callback):
            return Task(description=dedent("""\
                We need to generate an image for our game, at AAA-game studio quality, similar to GTA5. 
                The image should be relevant to the current narrative and should be engaging for the players.
                Create a short prompt, optimized for use with DALLE-3, and always append FULL HD, photorealistic, GTA5.
                """),
                expected_output=dedent("""\
                Prompt to feed into DallE-3
                """),
                agent=agent,
                callback=callback,
            )


