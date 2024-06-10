import os
from dotenv import load_dotenv
load_dotenv()

import chainlit as cl
from openai import AsyncOpenAI
from chainlit.playground.providers.openai import ChatOpenAI
from chainlit import run_sync, make_async
from game_crew import GameCrew
import sqlite3
import yaml
from openai import OpenAI

DEBUG = False
from game_content import story_text, dataset_text, questions_text

class GameState:
    def __init__(self):
        self.story = None
        self.dataset = None
        self.questions = []
        self.current_question = 0
        self.db = sqlite3.connect(":memory:", check_same_thread=False)
    
    def get_current_question(self):
        return self.questions[self.current_question]

# Create a global instance of AppState
game_state = GameState()

os.environ["OPENAI_API_MODEL_NAME"] = 'gpt-4o' # TURN THIS OFF LATER 


def bootstrap_db():
    # Define the path to your SQLite database
    # Connect to the SQLite database
    try:
        with game_state.db:
            cur = game_state.db.cursor()
            # Split the dataset into individual statements
            statements = game_state.dataset.split(';')
            for statement in statements:
                if statement.strip():  # Skip empty statements
                    cur.execute(statement)
    except Exception as e:
        print(f"An error occurred: {e}")

async_bootstrap_db = make_async(bootstrap_db)

async def on_story(output):
    
    if(DEBUG):
        game_state.story = story_text   
    else:
        game_state.story = output.raw_output
    # Block the rest of the crew from executing their tasks
    # Until we've gotten back to the user with the story. 
    # This run_sync ensures this cl.Message gets out ahead of the other
    # OpenAI calls that are happening from CrewAI.
    # I think this makes things much more responsive! 
    run_sync(cl.Message(content=game_state.story, disable_feedback=True).send())

def generate_markdown_summary():
    with game_state.db:
        cursor = game_state.db.cursor()
            # List all tables
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        markdown = "# Database Summary\n\n"
        
        for table in tables:
            table_name = table[0]
            markdown += f"## Table: {table_name}\n\n"
            
            # Show the schema of the table
            cursor.execute(f"PRAGMA table_info({table_name});")
            schema = cursor.fetchall()
            markdown += "| Column Name | Data Type |\n"
            markdown += "|-------------|-----------|\n"
            for column in schema:
                markdown += f"| {column[1]} | {column[2]} |\n"
            
            markdown += "\n&nbsp;\n"
            
            # Show the contents of the table
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            
            if rows:
                # Get column names
                column_names = [description[0] for description in cursor.description]
                markdown += "| " + " | ".join(column_names) + " |\n"
                markdown += "| " + " | ".join(["-" * len(name) for name in column_names]) + " |\n"
                
                for row in rows:
                    markdown += "| " + " | ".join(map(str, row)) + " |\n"
            else:
                markdown += "No data available in this table.\n"
            
            markdown += "\n"
        
    return markdown



async def on_dataset(output):
    if(DEBUG):
        game_state.dataset = dataset_text
    else:
        game_state.dataset = output.raw_output
    await async_bootstrap_db()
    await cl.Message(content="Database is ready for queries!", disable_feedback=True).send()

async def on_questions(output):
    if(DEBUG):
        game_state.questions = yaml.safe_load(questions_text)['questions']
    else:
        game_state.questions = yaml.safe_load(output.raw_output)['questions']
    print("Questions! Received!")
    print(game_state.questions)
    await ask_next_question()
    
async def on_image(output):
    print("Got image prompt")
    print(output.raw_output)
    def generate_image(prompt: str) -> str:
        client = OpenAI()
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        print(response)
        return response.data[0].url
        
    
    image = cl.Image(url=generate_image(output.raw_output))
    await cl.Message(content=f"", elements=[image], disable_feedback=True).send()

@cl.action_callback("Show Tables")
async def show_tables():
    await cl.Message(content=generate_markdown_summary(), disable_feedback=True).send()

@cl.action_callback("Start Quest")
async def start():
    if(DEBUG):
        await on_story(story_text)
        await on_dataset(dataset_text)
        await on_questions(questions_text)
        # Images get skipped in debug for now - hold on
    else:
        crew = GameCrew(on_story, on_dataset, on_questions, on_image)
        crew.start_game()
    
@cl.on_chat_start
async def start():
    # Sending an action button within a chatbot message
    actions = [
        cl.Action(name="Start Quest", value="example_value", description="Enter the world")
    ]
    await cl.Message(content="Welcome to SQL Quest! Click Start Quest to begin.", actions=actions, disable_feedback=True).send()

def format_results(cursor, rows):
    column_names = [description[0] for description in cursor.description]    
    markdown = "| " + " | ".join(column_names) + " |\n"
    markdown += "| " + " | ".join(["-" * len(name) for name in column_names]) + " |\n"
    
    for row in rows:
        markdown += "| " + " | ".join(map(str, row)) + " |\n"
    
    return markdown

async def ask_next_question():
    current_question = game_state.get_current_question()
    msg_content = current_question['intro'] +  "\n\n**" + current_question['prompt'] + "**\n\n&nbsp;"
    await cl.Message(content=msg_content, disable_feedback=True, actions=[
        cl.Action(name="Show Tables", value="pass", description="Does a DESCRIBE TABLES")   ,
        cl.Action(name="Get Hint", value="pass", description="This will cost you") 
    ]).send()


@cl.step
async def check_sql(query):
    with game_state.db:
        cur = game_state.db.cursor()
        cur.execute(query)
        output = cur.fetchall()
        
        await cl.Message(content=format_results(cur, output), disable_feedback=True).send()
        # My algo: run the solution, see if this output is equivalent.
        solution = game_state.get_current_question()['solution']
        expected_output = cur.execute(solution).fetchall()
        if(output == expected_output):
            game_state.current_question = game_state.current_question + 1
            # TODO: Uh, check to see if we're at the end.
            await cl.Message(game_state.get_current_question()['success'], disable_feedback=True).send()
            # TODO - refactor to make this cleaner, this is ai autocomplete
            await ask_next_question()
        else:
            await cl.Message(content=f"Try Again Idiot! Your output: {output} but expected {str(expected_output)}").send()

@cl.on_message
async def on_message(message):
    print(message.content)
    await check_sql(message.content)
