gunicorn --preload --timeout 100 --workers 1 --bind 0.0.0.0:8081 --env PATH=/home/np1815/Individual-Project/:/usr/bin:/home/np1815/Individual-Project/pyflame-bleeding/src/:/home/np1815/Individual-Project/FlameGraph/ --env FLASK_ENV=production --pythonpath /home/np1815/Individual-Project/feedback_driven_development/feedback_wrapper/ --access-logfile gunicorn_access.log --access-logformat "%(h)s %(l)s %(u)s %(t)s \"%(r)s\" %(s)s %(B)s \"%(f)s\" \"%(a)s\"" playground_application.__main__:flask_app
