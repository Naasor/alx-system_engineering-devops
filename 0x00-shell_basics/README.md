0x00. Shell, basics


Note
All your scripts should be exactly two lines long.
The first line of all your files should be exactly #!/bin/bash
All your scripts must be executable. To make your file executable, use the chmod command: chmod u+x file


0-current_working_directory - Writes a script that prints the absolute path name of the current working directory.

1-listit - Displays the contents list of your current directory.

2-bring_me_home - Writes a script that changes the working directory to the user’s home directory. You are not allowed to use any shell variables.

3-listfiles - Displays current directory contents in a long format.

4-listmorefiles - Displays current directory contents, including hidden files (starting with .). Use the long format.

5-listfilesdigitonly - Displays current directory contents in Long format, with user and group IDs displayed numerically and hidden files (starting with .).

6-firstdirectory - Creates a script that creates a directory named my_first_directory in the /tmp/ directory.

7-movethatfile - Moves the file betty from /tmp/ to /tmp/my_first_directory.

8-firstdelete - Deletes the file betty.The file betty is in /tmp/my_first_directory.

9-firstdirdeletion - Deletes the directory my_first_directory that is in the /tmp directory.

10-back - Writes a script that changes the working directory to the previous one.

11-lists - Writes a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.

12-file_type - Writes a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.

13-symbolic_link - Creates a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.

14-copy_html - Creates a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory. You can consider that all HTML files have the extension .html

100-lets_move - Creates a script that moves all files beginning with an uppercase letter to the directory /tmp/u. Assuming that the directory /tmp/u will exist when we will run your script.

101-clean_emacs - Creates a script that deletes all files in the current working directory that end with the character ~.

102-tree - Creates a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory. You are only allowed to use two spaces (and lines) in your script, not more.

103-commas - Writes a command that lists all the files and directories of the current directory, separated by commas (,), Directory names should end with a slash (/), Files and directories starting with a dot (.) should be listed, The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning, Only digits and letters are used to sort; Digits should come first, You can assume that all the files we will test with will have at least one letter or one digit, and the listing should end with a new line.

school.mgc - Creates a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0. 
