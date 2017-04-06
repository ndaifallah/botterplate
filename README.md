# nextor :
---
Nextor is the boiler plate for Facebook messenger bot, based on Flask, it uses transforms the use of json based API of the messenger plateforme to oop basic API.
<br>
---
## What does nextor contain ?
---
Nextor is based on single-way data flow, the story begins from receiving the replies from facebook server,<br>
The answer is structured in batchs, every single bach contains messagings, every single messaging has messages.<br>
<br>
Every single message must be treated, and an answer sent after processing.
## Message types:

