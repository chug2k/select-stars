## ChatGPT SQL Game Thing

To run: `pip install -r requirements.txt` and then `chainlit run app.py -w`

you need a .env file with `OPENAI_API_KEY=<your_key>`

right now DEBUG is on, which loads my manually copied and pasted output from game_content.py. This data is a little lame though, I need to prompt the agent to make more rows and seed_data. But should work for testing! 



### TODO: 
[x] When people answer, check to see if the answer is right.
[] When wrong, say it's wrong. (Bonus: make encouraging message, using LLM and current answer) - Half Done, it just gives error message
[x] When right, give success message, advance to the next question. 
[] Add "give me a hint" button. 
[] Add a "reset db" button
[] Generate Dall-E image <-- lol I want to do this next

