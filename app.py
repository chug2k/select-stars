import os
from dotenv import load_dotenv
load_dotenv()



import chainlit as cl
from openai import AsyncOpenAI
from chainlit.playground.providers.openai import ChatOpenAI
from chainlit import run_sync
from game_crew import GameCrew
crew = None


os.environ["OPENAI_API_MODEL_NAME"] = 'gpt-3.5-turbo'

async def on_story(output):
    # Block the rest of the crew from executing their tasks
    # Until we've gotten back to the user with the story. 
    # This run_sync ensures this cl.Message gets out ahead of the other
    # OpenAI calls that are happening from CrewAI.
    # I think this makes things much more responsive! 
    run_sync(cl.Message(content=output.raw_output).send())
    
async def on_dataset(output):
    # await cl.Message(content=output.raw_output).send()
    pass

async def on_questions(output):
    # await cl.Message(content=output.raw_output).send()
    pass

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
