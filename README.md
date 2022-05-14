A Basic Password Generator

Generates a password in the form of random words.

Requires Words.txt or similar word file in the working directory.

Allows users to choose how many words, if the password contains numbers, special characters, capital letters, and allows the user to copy the resulting password to the clipboard.

Must be ran in the command prompt using the following arguments:
-w/--words How many words in the password
-n/--numbers If the password contains numbers, defaults to yes
-u/--uppercase If the password contains uppercase letters, defaults to yes
-s/--specails If the password contains special characters, defaults to yes
-c/--copy If the password will be copied to the clipboard, defaults to no

run in the following format:
passwordgen.py -w (number) -n (y/n) -u (y/n) -s (y/n) -c (y/n)
