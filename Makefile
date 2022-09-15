default: run

run:
	python3 rubiks_control.py

rep_test:
	python3 rubiks_rep_tests.py

cube_test:
	python3 rubiks_cube_tests.py

control_test:
	python3 rubiks_control_tests.py

test: rep_test cube_test control_test

clean:
	/bin/rm -rf __pycache__

