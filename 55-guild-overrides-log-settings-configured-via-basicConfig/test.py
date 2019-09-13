import argparse
import logging
import os

LOG_FMT = "%(name)s - %(levelname)s - %(message)s"

def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--debug", action="store_true")
    p.add_argument("--log-file")
    return p.parse_args()

def init_logging(args):
    level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(level=level, format=LOG_FMT)
    if args.log_file:
        file_handler = logging.FileHandler(args.log_file)
        file_handler.setLevel(level)
        file_handler.setFormatter(logging.Formatter(LOG_FMT))
        logging.getLogger().addHandler(file_handler)

args = parse_args()

init_logging(args)

log = logging.getLogger("test")

log.debug("Debug msg")
log.info("Info msg")
log.warning("Warning msg")
log.error("Error msg")
