Konfig
======

Stores sensitive configuration data in a way that works nicely with Heroku.

Example:

```python
from konfig import Konfig
konf = Konfig()
konf.username
'''


Callling "konf.username" will search
the following locations and return the first value that is found:
* An environment variable named "USERNAME" ($USERNAME in the shell)
* If './.env' exists and has an entry that starts with "USERNAME="
* If an entry in a dictionary was passed to "konf.use_dict()" before
  "konf.username" was called, that will be returned.
