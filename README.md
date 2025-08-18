# SRS ( Source Remote Sync )
<img width="512" height="512" alt="NoCable.jpg" src="https://github.com/user-attachments/assets/e950c6b0-6058-4928-8d4a-fb575832cd42" />

What is srs? srs or NoCable is a local web service which run on your own device 
and also its not limited on pc, and it opens 8000 port to recieve files
and storage them in "uploads/".
<a href="#download">Go to download</a>

0. [Installation](#installation)
1. [Usage](#usage)
2. [Updates](#update)
3. [View](#view)
4. [Features](#features)
5. [Contributing](#contributing)
6. [License](#license)


# installation 
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
7. run the python project
```python srs.py```
and it gives you two links+ a qrcode. open the second link
 by browser with any device that is connected to same internet.

## Usage

+ <b>Uploading any file</b>: You Can darg&drop or select any type of file to upload
+ <b>Auto deleting after 5 min</b>: the uploaded files delets after 5 min 
+ <b>Control the files manual</b>: Upload/Download or remove the files  
+ <b>Downloading</b>: downloading the uploaded file's by anydevice in the local netwoek

## view
### Desktop
<img width="1325" height="580" alt="Desktop.png" src="https://github.com/user-attachments/assets/c7e11d18-bd55-414b-a785-99448591286b" />

### Android 
<img width="215" height="580" alt="Android.png" src="https://github.com/user-attachments/assets/04b73d74-0cb8-4163-b4cd-67c1f40f6ec6" />


## Features
### auto share 
You can set your screenshot saving location on srs/uploads to sharing automaticly 
<img width="580" height="405" alt="20250728_005959" src="https://github.com/user-attachments/assets/7b8b248b-50cc-41e3-bf0e-e6c8fda810b8" />

### you can make put the project in startup to auto run after booting
### auto delete, deletes the uploaded files after 5 minutes

# Update!
## 1.0.5v
### cli qrcode
### changing the qrcode module
### asking the port (default to 3000)
### notification 

## 1.0.3v
### auto delete
### fixing qrcode in mobile view
### fixing header in mobile view 

## 1.0.0
### delete button 
### making responsive pages
### releasing the stable version


<br>
## Contributing
Contributions are highly appreciated! Whether it’s bug fixes, feature enhancements, or documentation improvements:

Fork the repo

Create a new branch (git checkout -b feature/awesome-feature)

Make your changes and commit (git commit -m "Add awesome feature")

Push to your branch (git push origin feature/awesome-feature)

Open a Pull Request with a clear description

Please ensure your code follows the project's coding standards and includes relevant tests.

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this application as you see fit.

For questions or feedback, reach out to UndrDsk0M. <a href="https://gravatar.com/fantasticcherryblossomef40d159a8">Me!</a>

Whole project is built by flask
Jinja2 protects from getting Xss attack.
i love to know what you think about this project so feel free!