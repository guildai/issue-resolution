# Guild view not able to handle np.inf

https://github.com/guildai/guildai/issues/241

## Problem

Guild view is not handling inf scalar values due to a malformed JSON payload.

## Recreating

Requirements:

- guild<=0.7.0.post1
- See [requirements.txt](requirements.txt)

```
guild init -y
source guild-env
guild run test.py -y
guild view
```

In the browser, Guild will show "Waiting for runs..." without ever
showing runs. Browser should show "Uncaught (in promise) SyntaxError:
Unexpected token I in JSON at position 5739" (or similar).

## Workarounds

None

## Fix

Fix the JSON encoding for inf/-inf scalar values.

## Related Issues

None
