# Cryptography Utility<br>(codename "Unwaning Croconic")
**Created:**&nbsp;&nbsp; August 13<sup>th</sup>, 2024  
**Updated:**&nbsp; 08-20-2024 @ 5:58 PM

---

### Index of Contents

1. About
<br>&nbsp;&nbsp; 1.1 Features
<br>&nbsp;&nbsp; 1.2 Installation
<br>&nbsp;&nbsp; 1.3 Usage
2. Releases
3. Development
<br>&nbsp;&nbsp; 3.1 Active Concerns
<br>&nbsp;&nbsp; 3.2 For the Future

---


&nbsp;
## 1 &nbsp;&nbsp; About

The cryptography utility provides users with a suite of cryptographic tools that's intended
to make cryptography processes both quicker and easier to utilise.

(to be continued)

&nbsp;
#### 1.1 &nbsp; Features

The following is an outline of the cryptography utility's current features:

1. Basic XOR Hashing
	* may also be used (treated) as a XOR cipher for encrypting data with minimal security
	* ability to hash a plain-text string, given a plain-text key, to obtain hashed (cipher) text
	* ability to hash a hashed (cipher) text, given a plain-text key, to obtain the original plain-text string
	* varying input/output modes:
		- ability to input a string literal or a file containing a string literal for both original text and key
		- ability to input a binary string or a file containing a binary string for original text only
		- ability to output a string literal or a file containing a string literal for both hashed and re-hashed text
		- ability to output a binary string or a file containing a binary string for both hashed and re-hashed text


&nbsp;
#### 1.2 &nbsp; Installation

The following is a quick guide to aid users in setting up the cryptographic utility on their machines. There is currently no release version to install, so the instructions below will set up the latest development version of the system.

1. First, obtain the system's source code by cloning the repository or manually downloading the required files. If manually downloading, the 'prototype' directory found in the repository home is all you will need. For cloning, change directories into where you want to keep the repository and then run the command  
`git clone https://github.com/HansMoleman/unwaning-croconic`  
to clone the main branch of the repository.  
Once the repository is cloned, you may test/use the system with no further effort by simply using  
`./cryptutl.py <command> <args>`  
from within the prototype directory. However, if you want to be able to access 'cryptutl' from anywhere on your machine, there's some work yet to be done.

2. Next, you're going to need to make an executable copy of the system's main file 'cryptutl.py' by running the commands  
`cp cryptutl.py cryptutl`, and then  
`chmod +x cryptutl`  
This executable copy of the main script will now allow you to use just 'cryptutl \<command\> \<args\>' to run the system, but still only from within the 'prototype' directory. The original 'cryptutl.py' file should be kept for the update process, however it serves no other use once copied to 'cryptutl'.

3. Now, if we'll want to have access to the 'cryptutl' executable anywhere on our system, we'll need to place it somewhere on our operating system's path. However, due to the cryptutl script depending on all other files within the prototype directory, care must be taken to ensure the 'cryptutl' script still has access to its dependencies while also being on the path. The first approach is the recommended:  
(a) Create a symbolic link of the 'cryptutl' script, using its permanent location amongst the 'prototype' directory, and storing the link on your path, as follows:  
`sudo ln -s ~/Desktop/unwaning-croconic/prototype/cryptutl ~/.local/bin/cryptutl`  
assuming you placed (and plan to keep) the repo clone in your Desktop directory, and ~/.local/bin is on your path.  
(b) Alternatively, you may place the entire prototype directory (including the 'cryptutl' script) on your path, using  
`cp -r ~/Desktop/unwaning-croconic/prototype ~/.local/bin/prototype`  
but again, this approach is not recommended for many reasons, but will get the job done if linking is not an option.

4. Lastly, test that everything works by changing directories somewhere the 'cryptutl' script isn't, and running  
`cryptutl --help`  
the output of this should be a 'help' screen outlining the cryptutl system, so if anything else is given (like an error) the set up process failed, likely in the previous step (#3).


&nbsp;
#### 1.3 &nbsp; Usage

The following is a brief guide intended to demonstrate the core concepts of the cryptographic utility.

(to be continued)


&nbsp;
## 2 &nbsp;&nbsp; Releases

The following section outlines all information regarding releases...  

(to be continued)


&nbsp;
## 3 &nbsp;&nbsp; Development

The following section outlines all information regarding development...  

(to be continued)

&nbsp;
#### 3.1 &nbsp; Active Goals

The following outlines what's currently being worked on and expected to roll out soon:

1. MD5 Hashing
	* ability to hash plain-text strings using the MD5 algorithm
	* ...

2. SHA Hashing
	* ability to hash plain-text strings using the SHA-256(?) algorithm
	* ...

3. Upgrades to XOR Hashing
	* ability to hash a file of any (common) type
		- with default output being a file of the input's type
	* ability to input the plain-text key as a path to a plain-text (.txt) or binary (.bin) file


&nbsp;
#### 3.2 &nbsp; Future Plans

The following outlines what is planned to be developed, but is not currently being developed, in no particular order of expected completion:

1. RIPEMD-160 Hashing
2. RSA Hashing/Encryption
3. AES Encryption
4. Blowfish Encryption
5. Twofish Encryption
6. Refactor System (to use bit operations anywhere applicable)


<br>
<br>
<br>
<br>
<br>
<br>

---
