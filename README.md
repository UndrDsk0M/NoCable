<img width="512" height="512" alt="file_00000000ca006246b32a022c9333c948" src="https://github.com/user-attachments/assets/e950c6b0-6058-4928-8d4a-fb575832cd42" />


# SRS ( Source Remote Sync )
What is srs? srs is a local web service which run on your own device 
and also its not limited on pc, and it opens 8000 port to recieve files
and storage them in "uploads/".
<a href="#download">Go to download</a>


## Pc view
<img width="1325" height="580" alt="example" src="https://github.com/user-attachments/assets/c7e11d18-bd55-414b-a785-99448591286b" />

# Download 
## Linux/Windows
1. Star the project
2. Clone the project
```git clone https://github.com/UndrDsk0M/NoCable```
3. Enter the env
```source env/bin/activate```
4. Run the srs.py by env's python
```srs/env/bin/python /srs/srs.py```

## Android
In Android you should Download Termux first as its android terminal
1. Download Termux from GooglePlay
2. you have to download git to clone the project
```pkg install git```
3. Download the python ( Termux dont have the premission to use env python )
```pkg install python```
4. Download the Whole project from github
```git clone https://github.com/UndrDsk0M/NoCable```
5. open the project in termux
```cd NoCable```
6. Install the dependencies
```pip install -r requirements.txt```
7. run the project
```python srs.py```
and it gives you two links and you have to open the second link so you
 can open it by browser with any device
that is connected to same internet.

## Android view 
<img width="215" height="580" alt="example" src="https://github.com/user-attachments/assets/04b73d74-0cb8-4163-b4cd-67c1f40f6ec6" />



# Features
### auto share 
You can set your screenshot saving location on srs/uploads to sharing automaticly 
<img width="580" height="405" alt="20250728_005959" src="https://github.com/user-attachments/assets/7b8b248b-50cc-41e3-bf0e-e6c8fda810b8" />

### you can make put the project in startup to auto run after booting
### auto delete, deletes the uploaded files after 5 minutes

# Update! 
## 1.0.3v
### auto delete
### fixing qrcode in mobile view
### fixing header in mobile view 

## 1.0.0
### delete button 
### making responsive pages
### releasing the stable version

Whole project is built by flask
Jinja2 protects the project from getting Xss attack.
i love to know what you think about this project so feel free!