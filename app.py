import os
from dotenv import load_dotenv
load_dotenv()
from chainlit import run_sync


import chainlit as cl
from openai import AsyncOpenAI
from chainlit.playground.providers.openai import ChatOpenAI

from crewai import Crew, Process
from tasks import GameTasks
from agents import GameAgents


cl.instrument_openai()
api_key = os.getenv("OPENAI_API_KEY")
# client = AsyncOpenAI(api_key=api_key)

settings = {
    "model": "gpt-3.5-turbo",
    "temperature": 0,
    "max_tokens": 500,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": ["```"],
}

# @cl.step(type="llm", root=True, language="sql")
# async def text_to_sql(text: str):
#     # Call OpenAI
#     stream = await client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": template.format(input=text),
#             }
#         ], stream=True, **settings
#     )

#     current_step = cl.context.current_step

#     async for part in stream:
#         if token := part.choices[0].delta.content or "":
#             await current_step.stream_token(token)


@cl.on_message
async def main(message: cl.Message):
    await text_to_sql(message.content)
    
def shit():
    # Kick off the actual game creation! Shit. 
    tasks = GameTasks()
    agents = GameAgents()

    # Initialize Agents
    game_designer = agents.game_designer_agent()
    game_engineer = agents.game_engineer_agent()
    # qa_engineer = agents.chief_qa_engineer_agent()
    #def setup_crew(self):
    # Create Tasks
    generate_story = tasks.generate_story_task(game_designer)
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
            generate_dataset,
            generate_questions,
            # generate_solutions,
            # check_solutions
        ],
        process=Process.sequential,
        verbose=True)
    
    
    
    print("## Welcome to SELECT Stars")
    print('-------------------------------')
    run_sync(crew.kickoff())
    print("Kickoff completed:", result)

    story = generate_story_task.raw_output
    dataset = generate_dataset_task.raw_output
    questions = generate_questions_task.raw_output
    

    cl.Message(content=story).send()
    cl.Message(content=dataset).send()
    cl.Message(content=questions).send()
    action.remove()    

@cl.on_chat_start
async def start():
    # Sending an action button within a chatbot message
    run_sync(shit())
        
    await cl.Message(content="Are you ready to learn SQL the fun way?", actions=actions).send()
