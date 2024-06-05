import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
from crewai import Crew, Process

from tasks import GameTasks
from agents import GameAgents

st.title("SQL Game")
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
    
def start():
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
    
    
    story = generate_story_task.raw_output
    dataset = generate_dataset_task.raw_output
    questions = generate_questions_task.raw_output
    

    st.markdown(story)
    st.markdown(dataset)
    st.markdown(questions)
    
start()