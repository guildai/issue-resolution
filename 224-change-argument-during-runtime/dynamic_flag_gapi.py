from guild import _api as gapi

x = 1

run = gapi.current_run()
flags = run.get("flags") or {}
flags["y"] = x + 1
run.write_attr("flags", flags)
