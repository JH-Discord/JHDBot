# JHDBot

The bot of John Hammond discord using discord.py

## Project Structure
The JHDBot uses an external website to generate a discord invite link after the user passes a reCaptcha. 

The structure is as follows:  
  - `JHDBot/*` Code for the Discord bot
  - `verify-web/*` Code for the website running the reCaptcha

### Running the bot
The bot can be run through `docker-compose`.  
```bash
$ docker-compose up -d
```
Use the supplied `.env-example` to create a `.env` file with the necessary environment variables.  
