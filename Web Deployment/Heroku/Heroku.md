# Heroku

install the heroku CLI and you can use the heroku command in the terminal

<b>usage</b>
```
heroku xxx
```

<b>Useful Commands</b>

- heroku login
- heroku create
    - create an app on heroku
    - creates a git remote called heroku and associates it with the local git repository
    - generates a random name
- heroku open
    - opens the website
- heroku logs --tail
- heroku ps
    - check how many dynos are running
- heroku ps:scale web=X
    - scale number of dynos
- heroku local web
    - runs app locally, examines Procfile
- heroku config
    - set environment variables through the CLI
    - ```heroku config:set API_KEY=12730912309123```
    - ```heroku config:unset API_KEY=12312312```
    - can also use the dashboard to set config variables
    - access environment variables with the standard way in language you are using
        - in node.js: process.env.SECRET_NAME
<b>Heroku deployment pattern</b>

- test locally with heroku local
- git add, commit
- git push heroku main
