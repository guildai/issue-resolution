venv-fix/bin/activate:
	virtualenv -p python3.8 venv-fix
	. venv-fix/bin/activate && pip install guildai
	. venv-fix/bin/activate && pip install -r requirements.txt

verify-fix: venv-fix/bin/activate
	. venv-fix/bin/activate && guild check -nt FIX.md
