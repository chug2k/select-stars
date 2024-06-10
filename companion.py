import warnings
warnings.filterwarnings('ignore')


llm_model="gpt-4"

from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

from textwrap import dedent

class GameCompanion:
    def __init__(self, context, tables):
        self.context = context
        self.tables = tables
        
        print(f""" ============================
              TABLES: {tables}""")
        

    def provide_hint(self, user_input, question_proposed, solution):
        hint_template = PromptTemplate(
            template=dedent("""\
                You are a helpful companion for a user playing a game that teaches SQL. The game is set in this context.

                Context: {context}
                            
                The tables related to this game are as follows:
                {tables}
                            
                The user is trying to solve the next question with the following SQL query expected answer:
                {question_proposed}
                SQL that solves the question: {solution}

                If the user's input is a valid SQL query something similar but not exaclty as "Great, let's try your query. Let's see if it works."
                If the user's input include some form of SQL query, check if it is correct compared to the provided solution. If it is not correct, provide a hint based on the user's input to help them form a correct SQL query.
                If the user is asking some help, provide a hint based on the user's input to help them form a correct SQL query.
                Never give the answer directly. Always provide a hint based on the user's input to help them form a correct SQL query.

                User's input: {user_input}

                Response: 
            """),
            input_variables=["context", "user_input", "question_proposed", "solution", "tables"]
        )

        messages = hint_template.format(context=self.context, user_input=user_input, question_proposed=question_proposed, solution=solution, tables=self.tables)
        
        chatOpenAI = ChatOpenAI(temperature=0.0, model=llm_model)
        response = chatOpenAI.predict(messages)
        print(response)
        
        return response
    
    def provide_solution(self, question_proposed):
        hint_template = PromptTemplate(
            template=dedent("""\
                You are a helpful companion for a user playing a game that teaches SQL. The game is set in this context.

                Context: {context}
                            
                The tables related to this game are as follows:
                {tables}
                            
                The user is trying to solve the next question:
                {question_proposed}
                            
                Provide the SQL that solves the question.
                Just provide the SQL that solves the question. Do not provide any hints or feedback.
                Neither markdown formatting, nor triple quotes code blocks.
            """),
            input_variables=["context", "question_proposed", "tables"]
        )

        messages = hint_template.format(context=self.context, question_proposed=question_proposed, tables=self.tables)
        
        chatOpenAI = ChatOpenAI(temperature=0.0, model=llm_model)
        response = chatOpenAI.predict(messages)
        
        return response
