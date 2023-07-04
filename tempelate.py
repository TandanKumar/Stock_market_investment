import os
from pathlib import Path

package_name = "stock_market"

list_of_files = [

 "requirements.txt",
 "app.py",
 "Dockerfile",
 ".dockerignore",
 ".github\workflows\main.yaml",
 "setup.py",
  f"{package_name}/__init__.py", 
   f"{package_name}/exception/__init__.py",
   f"{package_name}/logger/__init__.py",
   f"{package_name}/pipeline/__init__.py",
   f"{package_name}/config/__init__.py",
   f"{package_name}/entity/__init__.py",
   f"{package_name}/components/__init__.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file
            