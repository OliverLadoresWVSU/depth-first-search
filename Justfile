set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

venv:
  py -m venv .

deps:
  .\Scripts\python.exe -m pip install -r requirements.txt

run:
  .\Scripts\python.exe .\depth_first_search\__init__.py

get-deps:
  poetry export > requirements.txt