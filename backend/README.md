# Backend 
Backend for Albot, a multimodal chatbot. Leverages a socket implementation to manage the client-server communication. Interacts with a Rasa NLU  server to process textual input, and merges the result with the basic interface input processing through a state machine.
## Requirements
### Poetry
Install poetry as specified [here](https://python-poetry.org/docs/). 
## Install backend dependencies
```bash
poetry install
```

## Run 
```bash
poetry run albot
```
