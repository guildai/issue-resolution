venv/bin/activate:
	virtualenv -p python3 venv

recreate: venv/bin/activate
	. venv/bin/activate && guild check -nt BUG.md

verify-fix: venv/bin/activate
	. venv/bin/activate && guild check -nt FIX.md
