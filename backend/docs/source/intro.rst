Introduction
============

``albot_backend`` is the server-side part of albot, which is a web application with a multimodal chatbot that aims to teach children the concept of ph. 
The module is composed of:
- a *Websocket* implementation that takes care of the communication with the front-end,
- a *State Machine* which contains all the application logic regarding the interaction,
- a *Dialogue Manager* which communicates with a separate NLU Module and orchestrates the all process.

