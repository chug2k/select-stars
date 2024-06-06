import os
from dotenv import load_dotenv
load_dotenv()

import chainlit as cl
from openai import AsyncOpenAI
from chainlit.playground.providers.openai import ChatOpenAI
from chainlit import run_sync, make_async
from game_crew import GameCrew
import sqlite3

class GameState:
    def __init__(self):
        self.story = None
        self.dataset = None
        self.questions = []
        self.current_question = 0
        self.db = sqlite3.connect(":memory:", check_same_thread=False)

# Create a global instance of AppState
game_state = GameState()

os.environ["OPENAI_API_MODEL_NAME"] = 'gpt-3.5-turbo'

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
    game_state.story = output.raw_output
    # Block the rest of the crew from executing their tasks
    # Until we've gotten back to the user with the story. 
    # This run_sync ensures this cl.Message gets out ahead of the other
    # OpenAI calls that are happening from CrewAI.
    # I think this makes things much more responsive! 
    run_sync(cl.Message(content=output.raw_output).send())
    
    
async def on_dataset(output):
    game_state.dataset = output.raw_output
    await async_bootstrap_db()
    await cl.Message(content="Database is ready for queries!").send()

async def on_questions(output):
    game_state.questions = output.raw_output
    print("Questions! Received!")
    await cl.Message(content=game_state.questions[game_state.current_question]).send()

@cl.action_callback("action_button")
async def start():
    crew = GameCrew(on_story, on_dataset, on_questions)
    crew.start_game()
    
@cl.on_chat_start
async def start():
    # Sending an action button within a chatbot message
    actions = [
        cl.Action(name="action_button", value="example_value", description="Enter the world")
    ]
    await cl.Message(content="Click here to start", actions=actions).send()

@cl.step
async def check_sql(query):
    with game_state.db:
        cur = game_state.db.cursor()
        cur.execute(query)
        output = cur.fetchall()
        await cl.Message(content=str(output)).send()

@cl.on_message
async def on_message(message):
    print(message.content)
    await check_sql(message.content)
