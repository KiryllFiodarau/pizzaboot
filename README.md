# pizzaboot
![Back-end language](https://img.shields.io/badge/python-3.7.0-yellow)
###Create ENV
```
Linux:
python3 -m venv  env
source env/bin/activate
Windows:
python -m venv  env
call env/Scripts/activate.bat

```
### Check ENV
```
python -V
```
### How to install requirements
```
pip install --upgrade pip
pip install -r requirements.txt
```
### Create .env 
```
create .env file 
copy .env_example to .env
```

### How to run examples
```
input:  
python pizza_boot.py "5x5 (0, 0) (1, 3) (4, 4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"

output TraverSal optimization:

NDENNDEDESDEDDSDNNND
```

```
input:  
python pizza_boot.py "5x5 (1, 3) (4, 4)"

output TraverSal optimization:

ENNNDEEEND
```
```
input:  
python pizza_boot.py "5x5 (1, 3) (4, 4)"

output Sort optimization:

ENNNDEEEND
```
### Run tests
```
```