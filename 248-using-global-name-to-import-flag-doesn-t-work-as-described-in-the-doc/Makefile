venv-bug/bin/activate:
	virtualenv venv-bug
	. venv-bug/bin/activate && pip install guildai==0.7.3.dev3

venv-fix/bin/activate:
	guild init venv-fix -y

recreate: venv-bug/bin/activate
	. venv-bug/bin/activate && guild check -nt BUG.md

verify-fix: venv-fix/bin/activate
	. venv-fix/bin/activate && guild check -nt FIX.md
