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

**PyMuPDF:** To install PyMuPDF on Windows, open your terminal and type ```py -m pip install "PyMuPDF"```. On Mac, type python3 -m pip install "PyMuPDF". Click enter.

**tqdm:** To install tqdm on Windows, open your terminal and type ```py -m pip install "tqdm"```. On Mac, type python3 -m pip install "tqdm". Click enter.

All dependencies are now installed. You can safely quit the terminal. 

# Usage

Before following these steps, see above to ensure you have all necessary dependencies already installed. 

1. Download the desired UNC semester section book from the UNC website. New SSBs are made every semester, so ensure you have the right one. Once you've downloaded this file, locate it and right-click on it. If you're using Windows, you should see an option called "Copy as path". On Mac, right-click on the file and hold option (⌥), and an option to "Copy as pathname" should appear. Click on this.  

2. Download this GitHub repo as a zip file and extract it. Locate the file you have just extracted (likely in your downloads folder), and open it. If you see another folder, drag this folder to your downloads folder, and open it. You should see a file called ```pdfscraper.py```. Double-click to open it on Mac. On Windows, double-click and open it with Notepad.

3. Near the top of the file that just opened, you should see a line that says ```doc = r'pdf_file_goes_here'```. Delete the ```pdf_file_goes_here``` and paste the pathname you have copied from the SSB. The line should now look something like this ```doc = r'/Users/sebastienconde/Desktop/2242-SSB-10-9-23.pdf'``` or ```doc = r'C:\Users\sebastienconde\Desktop\2242-SSB-10-9-23.pdf'```, except you'll have a different name in yours. **Please make sure the file has exactly one pair of quotes around it as shown above.** Save the file you have just edited, and exit.

4. Located the folder downloaded from GitHub. It should be called ```UNC-Empty-Classroom-Finder-main```. Copy the pathname of the folder. If you're unsure how to do this, see step 1, it's the exact same process.

5. Almost done! Open the terminal on your computer. Type ```cd``` followed by a space, then paste the pathname you've just copied. The command should look something like this ```cd /Users/sebastienconde/Downloads/UNC-Empty-Classroom-Finder-main```. Click enter.

6. On windows, type ```py main.py```. On Mac, type ```python3 main.py```. Hit enter. The program is now running. Everything else should be pretty straightforward; read the prompts that appear in the terminal, type your responses, and hit enter. If you ever want to rerun the program after closing the terminal, you'll only have to repeat steps 3-5. 

Please note that at the moment, this project only can show the schedule of a given room. You can check, for example, when Phillips Hall 0215 is available, but you can't search for all available rooms in Phillips Hall at a given time. That might be something that's coming in the future if people want it, however. 
