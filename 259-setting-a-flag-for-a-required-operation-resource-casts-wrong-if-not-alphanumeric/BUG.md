# Tests

Check expected version of Guild.

    >>> quiet("guild check --version '<=0.7.3.dev3'")

Create a temp dir for Guild Home.

    >>> gh = mkdtemp()

Create a helper to run Guild commands within Guild Home.

    >>> def guild_cmd(cmd):
    ...     run("guild -H '%s' %s" % (gh, cmd))

Show operations.

    >>> guild_cmd("ops")
    downstream
    upstream
    <exit 0>

Generate an upstream run.

    >>> guild_cmd("run upstream --run-dir '%s/runs/05930ca30d0a407aadf166d7836cb688' -y" % gh)
    Run directory is ... (results will not be visible to Guild)
    <exit 0>

Show current runs.

    >>> guild_cmd("runs")
    [1:05930ca3]  upstream  ...  completed
    <exit 0>

Run downstream specifying partial upstream run ID.

    >>> guild_cmd("run downstream upstream=05930 -y")
    WARNING: cannot find a suitable run for required resource 'upstream'
    Resolving upstream dependency
    guild: run failed because a dependency was not met: could not resolve
    'operation:upstream' in upstream resource: no suitable run for upstream
    <exit 1>
