# Empty Classroom Finder

A simple tool to help UNC students and faculty determine when a lecture hall, classroom, or lab is open. 

Around the start of each semester, the UNC registrar publishes their Semester Section Book (SSB), which contains details of every class held during that semester. 
This includes information such as the building, room, days, and hours each class is held, and more. 

Using some pdf-editing libraries, regex matching, and hashing, this Python program scrapes through the SSB and condenses the often 3000+ page document into a condensed set of classes
that can be far more easily searched through. Note that the SSB is not always 100% accurate with classroom availability, and classrooms are often locked when not in use, so times
returned by this function are by no means definitive, but they're probably relatively accurate. 

At the moment, this function has been tested with the 2024 Spring, Summer, and Fall SSBs. I'll be ensuring compatibility with the 2025 Spring SSB once it's released. 

# Usage

Note that you'll have to download the SSB from UNC's website and replace the ```'pdf_file_goes_here'``` in ```PDFScraper.py``` with the pathname to the downloaded SSB file, ensuring
to keep the quotation marks around the pathname. 

Once this is completed, and assuming all dependencies are installed, the project should be pretty straightforward to use - just answer the question prompts. Please note that at the moment, 
this project only can show the schedule of a given room. You can check, for example, when Phillips Hall 0215 is available, but you can't search for all available rooms in Phillips Hall 
at a given time. That might be something that's coming in the future if people want it, however. 
