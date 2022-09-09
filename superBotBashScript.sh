#!/bin/bash
cd Python
touch gitHubDeleteMe.py 
echo 'delete me because this contents are removable' > gitHubDeleteMe.py
git add .
git commit -m "Im just a Bot doing its Thang"
git push origin main
rm gitHubDeleteMe.py
git add .
git commit -m "Gonna delete the unwanted files"
git push origin main



