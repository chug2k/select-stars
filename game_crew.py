from crewai import Crew, Task, Agent, Process
from tasks import GameTasks
from agents import GameAgents
import os
from dotenv import load_dotenv
import asyncio

agents = GameAgents()
tasks = GameTasks()

# This is the standard Game Crew. Initialize it here. 
class GameCrew:
    def __init__(self, generate_story_callback, generate_dataset_callback, generate_questions_callback):
    # Load environment variables from .env file
        load_dotenv()

        # os.environ["OPENAI_API_MODEL_NAME"] = 'gpt-3.5-turbo'

        # Create Agents
        self.game_designer = agents.game_designer_agent()
        self.game_engineer = agents.game_engineer_agent()
        # qa_engineer = agents.chief_qa_engineer_agent()

        # Create Tasks
        self.generate_story = tasks.generate_story_task(self.game_designer, lambda output: asyncio.run(generate_story_callback(output)))
        # generate_level = tasks.generate_first_level_task(technical_creator_agent)
        # We'll generate levels later, but I think for now we can just have one level. 
        self.generate_dataset = tasks.generate_dataset_task(self.game_engineer, lambda output: asyncio.run(generate_dataset_callback(output)))
        self.generate_questions = tasks.generate_questions_task(self.game_engineer, lambda output: asyncio.run(generate_questions_callback(output)))
        # generate_solutions = tasks.generate_solutions_task(game_engineer)
        # check_solutions = tasks.check_solutions_task(qa_engineer)

        # Create Crew responsible for Copy
        self.crew = Crew(
            agents=[
                self.game_designer,
                self.game_engineer,
                # qa_engineer
            ],
            tasks=[
                self.generate_story,
                # generate_level,
                self.generate_dataset,
                self.generate_questions,
                # generate_solutions,
                # check_solutions
            ],
            process=Process.sequential,
            verbose=True)
    
    def start_game(self):
        self.crew.kickoff()