just-once
=========

JustOnce: Share files that can only be downloaded a single time.

Deploying just-once
=========
It's a Google App Engine app, so deploy it the same way you'd deploy any other App Engine app.

To run locally:

```
outer-haven:just-once cgb$ dev_appserver.py .
```

To deploy to Google, get a unique appid from http://appengine.google.com, put it in `app.yaml`, and run:

```
outer-haven:just-once cgb$ appcfg.py update .
```

Using just-once from a web browser
=========

If deploying locally, go to http://localhost:8080/

If deployed to Google App Engine, go to http://your-app-id.appspot.com/

Try out my hosted version at http://just-once.appspot.com/

Using just-once from the command-line
=========

Upload something:

```
outer-haven:just-once cgb$ curl -d "quux" http://localhost:8080/baz
outer-haven:just-once cgb$
```

Download something:

```
outer-haven:just-once cgb$ curl http://localhost:8080/baz
quux
outer-haven:just-once cgb$
```

Download something a second time:

```
outer-haven:just-once cgb$ curl http://localhost:8080/baz
outer-haven:just-once cgb$
```

It doesn't work! You only get it one time!
