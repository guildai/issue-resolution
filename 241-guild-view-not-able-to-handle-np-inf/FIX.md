# Recreating

    >>> quiet("guild check --version '>=0.7.1'")

    >>> quiet("guild run test.py -y")

    >>> run("guild view 1 --test-runs-data | python -m json.tool")
    [
        {
            "id": "...",
            ...
            "scalars": [
                {
                    "run": "...",
                    "prefix": "log",
                    "tag": "Name",
                    "first_val": "Infinity",
                    "first_step": 0,
                    "last_val": "Infinity",
                    "last_step": 0,
                    "min_val": "Infinity",
                    "min_step": 0,
                    "max_val": "Infinity",
                    "max_step": 0,
                    "avg_val": "Infinity",
                    "total": "Infinity",
                    "count": 1
                }
            ],
            ...
        }
    ]
    <exit 0>
