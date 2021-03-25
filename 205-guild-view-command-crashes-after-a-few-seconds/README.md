# Guild view command crashes after a few seconds

https://github.com/guildai/guildai/issues/205

## Problem

Guild view doesn't handle partially written run output files
gracefully when reading output for View.

## Recreating

Requirements:

- guild<=<applicable Guild version>

Run `op.py`, which writes logs to a single line.

    $ guild run op.py seconds=999 -y

In another terminal, start Guild View for the op:

    $ guild view 1

This should show the exception:

```
ERROR: Error on request:
Traceback (most recent call last):
  File "/home/garrett/.local/lib/python2.7/site-packages/werkzeug/serving.py", line 323, in run_wsgi
    execute(self.server.app)
  File "/home/garrett/.local/lib/python2.7/site-packages/werkzeug/serving.py", line 312, in execute
    application_iter = app(environ, start_response)
  File "/home/garrett/SCM/guild/guild/serving_util.py", line 124, in app
    return dispatch(routes, env, start_resp)
  File "/home/garrett/SCM/guild/guild/serving_util.py", line 113, in dispatch
    return handler(*args, **kw)(env, start_resp)
  File "/home/garrett/SCM/guild/guild/view.py", line 269, in handle
    (time, stream, line) for time, stream, line in self._output.read(start, end)
  File "/home/garrett/SCM/guild/guild/util.py", line 915, in read
    self._read_next(end)
  File "/home/garrett/SCM/guild/guild/util.py", line 939, in _read_next
    time, stream = struct.unpack("!QB", index.read(9))
error: unpack requires a string argument of length 9
```

## Workarounds

Upgrade to 0.7.4dev1 or later.

## Fix

Guard against unpacking a header that's shorter than 9 bytes.

This bug shows that Guild was not writing remaining bytes that did not
end with LF. This is fixed as well in 0.7.4dev1.
