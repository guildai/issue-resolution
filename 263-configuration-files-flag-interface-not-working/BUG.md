# Recreating

    >>> quiet("guild check --version '<0.7.3.dev4'")

From https://github.com/guildai/guildai/issues/263:

    >>> run("guild run train -y")
    Resolving config:flags.yml dependency
    sys.argv: [..., '--', '--x', '2']
    usage: train.py [-h] [--x X]
    train.py: error: unrecognized arguments: -- --x 2
    <exit 2>

The issue is that Guild is passing flag arguments to the script.
