# Light Projects Generator
---

### WARNING:
>***The following code stills under development, don't use it for production but for testing purpose.
It comes with no warranties and should be use with precaution.***

*Contact :*
<weltrusten@philentropy.org>
---
# What is it ?

*Light Projects Generator* aka *LPG* is a simple python package for install, verify and generate web projects (*React*, *Flutter*, *Symfony*).
  
  ---
# Install LPG from git source code: 
If you don't have the source package yet:  
`git clone https://github.com/w3lt3rust3n/light-projects-generator.git`  
Go inside the directory and run:  
`chmod +x setup-unstable-lpg-any.sh`  
Then:  
`./setup-unstable-lpg-any.sh`  
Then:  
`pip install -r requirements.txt`  
Finally:  
`python src/main.py --info`  
  
  ---
# Install LPG stable package: 
At this time, there is no stable package to install.
Stay tuned !
  
  ---
# Usage
In the following section, we assume we are looking for generate a new *React* project.  
  
Use *LPG* to check your system and be sure that *React* can be used:  
`python src/main.py -c react`  
or  
`python src/main.py --checkdep react`  
If *React* is not installed or dependencies are missing, *LPG* will try to do the job for you:  
`python src/main.py -p react`  
or  
`python src/main.py --prepare react`  
Else, you can finally generate the project by running:  
`python src/main.py -g react /home/user/Desktop`  
or  
`python src/main.py --generate react /home/user/Desktop`  
(The path must be valid !)  

Any doubt ? Run a good old ***-i*** or ***--info***  
  
  ---
# Get involved
If you have suggestions to improve *LPG*, feel free to contact us. Giving your feedback is also a way to get involved in the project.  
In the mood to write some code to implement in the *Light Projects Generator* ? Clone the repository and enjoy  
  
  ---
# Support
Any issue ? It's okay, no stable version of the package is released yet after all. Visit the [github issues page]("https://github.com/w3lt3rust3n/light-projects-generator/issues") to submit your problem.  

---

***Happy Hacking !***