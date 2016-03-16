# Anaconda, our Python distribution
For the exercises in this course we'll be using the Anaconda Python distribution. There are several different Python distributions available that include various Python tools and libraries, but Anaconda is easy to install, free and up to date. Feel free to install a copy on your personal computer to use Python wherever you please.

## Downloading and installing Anaconda
The Anaconda installation process on the laboratory computers will need to be done once for the course, but it is quite slow.

1. Start by downloading a copy of the [Anaconda Python distribution for Linux](http://repo.continuum.io/archive/Anaconda3-2.5.0-Linux-x86_64.sh). This is the 64-bit version based on Python 3.5.
2. After the download completes, open a new Terminal window by clicking on the Dash Home icon at the top left corner of the screen,  typing `terminal` into the search box, and clicking on the Terminal icon.
3. You can now start the installation process

    ```bash
    $ cd ~/Downloads
    $ bash Anaconda3-2.5.0-Linux-x86_64.sh
    ```
Note the `$` symbol represents the command prompt in the Terminal window.
4. You will be first asked to agree to the license agreement. Press **Enter** to review the license. You can press space several times to get to the bottom of the agreement and then type in `yes` and press **Enter**.
5. Next, you are asked about the installation location. Simply press **Enter** to install in the default location.
6. Installation may take 30-45 minutes (!), so we can leave the installation running in the background while we move on to the first steps of out [introduction to Python and NumPy](Python-and-NumPy-I.md). NOTE: You can safely ignore any error messages about not being able to create links.
7. Once the installation has completed, you will be asked a final question about the installation PATH. Type `yes` and press **Enter**.
