Winselect is a tool that makes the management of the windows system paths better.

WARNING: This product is still in development. Some of the functionality is not implemented and 
what is implemented is not fully tested. Use at your own risk.

Works with python 3. Not yet python 2 compatible.

Usage:
Searching/Listing
---------------------- 
1) List all environment vars:
python winselect.py list --all

2) List only the system PATH:
python winselect.py list --path

3) Search keys for a given pattern:
python winselect.py list --keys <pattern>

4) Search keys and values for a given pattern: 
python winselect.py list --search <pattern>

Adding/Removing
---------------------
1) Add a new path to the environment:
python winselect.py add --new key value

2) Append to an existing environment variable:
python winselect.py add --append key value

3) Attend to the top of the var list:
python winselect.py add --top key value

4) Delete a path:
python winselect.py remove --key name
