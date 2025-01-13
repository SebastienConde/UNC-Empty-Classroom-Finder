# Empty Classroom Finder

A simple tool to help UNC students and faculty determine when a lecture hall, classroom, or lab is open. 

Around the start of each semester, the UNC registrar publishes their Semester Section Book (SSB), which contains details of every class held during that semester. 
This includes information such as the building, room, days, and hours each class is held, and more. 

Using some pdf-editing libraries, regex matching, and hashing, this Python program scrapes through the SSB and condenses the often 3000+ page document into a condensed set of classes
that can be far more easily searched through. Note that the SSB is not always 100% accurate with classroom availability, and classrooms are often locked when not in use, so times
returned by this function are by no means definitive, but they're probably relatively accurate. 

At the moment, this function has been tested with the 2024 Spring, Summer, and Fall SSBs. I'll be ensuring compatibility with the 2025 Spring SSB once it's released. 

# Dependencies

This program requires the following dependencies:

**Python3:** Python3 can be downloaded and installed from the https://www.python.org/downloads/ website. There are plenty of tutorials on YouTube that cover how to do this. 

**PyMuPDF:** To install PyMuPDF on Windows, open your terminal and type ```py -m pip install "PyMuPDF"```. On Mac, open the terminal and type ```python3 -m pip install "PyMuPDF"```. Click enter.

**tqdm:** To install tqdm on Windows, open your terminal and type ```py -m pip install "tqdm"```. On Mac, type ```python3 -m pip install "tqdm"```. Click enter.

All dependencies are now installed. You can safely quit the terminal. 

# Usage

Before following these steps, see above to ensure you have all necessary dependencies already installed. 

1. Download this GitHub repo as a zip file and extract it. Locate the file you have just extracted (likely in your downloads folder), and open it. If you see several files ending with ```.py```, you can return to your downloads folder. If instead you see another folder inside the one you have just opened, drag this folder into your downloads folder, then return to your downloads folder and delete the first folder that is now empty. 

2. If you're using Windows, right-click on the downloaded folder and click the option called "Copy as path". On Mac, right-click on the folder and hold option (⌥), and an option to "Copy as pathname" should appear. Click on this.  

3. Open the terminal on your computer. Type ```cd``` followed by a space, then paste the pathname you've just copied. The command should look something like this ```cd /Users/sebastienconde/Downloads/UNC-Empty-Classroom-Finder-main```. Hit enter.

4. On the Windows terminal, type ```py main.py```. On Mac, type ```python3 main.py```. Hit enter. The program is now running. Everything else should be pretty straightforward; read the prompts that appear in the terminal, type your responses, and hit enter. If you ever want to rerun the program after closing the terminal, you'll only have to repeat steps 2-4. 

Please note that at the moment, this project only can show the schedule of a given room. You can check, for example, when Phillips Hall 0215 is available, but you can't search for all available rooms in Phillips Hall at a given time. That might be something that's coming in the future if people want it, however. 
