from dotenv import load_dotenv
load_dotenv()

from crewai import Crew, Process

from tasks import GameTasks
from agents import GameAgents

tasks = GameTasks()
agents = GameAgents()

print("## Welcome to SELECT Stars")
print('-------------------------------')

# Create Agents
game_designer = agents.game_designer_agent()
game_engineer = agents.game_engineer_agent()
# qa_engineer = agents.chief_qa_engineer_agent()

# Create Tasks
generate_story = tasks.generate_story_task(game_designer)
# generate_level = tasks.generate_first_level_task(technical_creator_agent)
# We'll generate levels later, but I think for now we can just have one level. 
generate_dataset = tasks.generate_dataset_task(game_engineer)
generate_questions = tasks.generate_questions_task(game_engineer)
# generate_solutions = tasks.generate_solutions_task(game_engineer)
# check_solutions = tasks.check_solutions_task(qa_engineer)

# Create Crew responsible for Copy
crew = Crew(
	agents=[
		game_designer,
		game_engineer,
		# qa_engineer
	],
	tasks=[
		generate_story,
		# generate_level,
		generate_dataset,
		generate_questions,
		# generate_solutions,
		# check_solutions
	],
	process=Process.sequential,
    verbose=True)

game = crew.kickoff()


# Print results
print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the game:")
print(game)