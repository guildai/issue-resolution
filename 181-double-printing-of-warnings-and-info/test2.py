import logging
import os

log = logging.getLogger("ciao")

# Only init logging when needed.
if not log.root.handlers:
    log.addHandler(logging.StreamHandler())
    log.setLevel(logging.INFO)

log.info("aaa")
log.warning("bbbb")
