import logging

add_handler = True

log = logging.getLogger("ciao")
if add_handler:
    log.addHandler(logging.StreamHandler())
log.setLevel(logging.INFO)
log.info("aaa")
log.warning("bbbb")
