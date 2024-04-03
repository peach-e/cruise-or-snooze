# cruise-or-snooze
Tools to monitor the weather overnight and wake you up early if it looks like it's gonna be a nice day.

I came up with Cruise or Snooze because I booked a flight to the Langley Regional airport for 8:00 in the morning, meaning I got up at 05:00, drove out there, and showed up to discover that the plane was covered in sheet ice, preventing me from flying before the next booking.

This tool was inspired because I want a workflow for booking flights like this:
1. The night before, I see the 8:00am slot is open for the Cessna.
1. I prepare to potentially go flying the next morning, and go to bed.
1. An automatic system keeps track of the weather over night.
1. If it looks like the weather will be great the next day, wake me up at 5:00AM and tell me the weather conditions for flying.
1. If it looks like it will be foggy/icy/terrible weather, do not trip the alarm and let me sleep in.

## Getting Started (Ubuntu)
1. Clone and `cd` into the repo
1. Create a virtual environment `venv`
    ```
    $ python3 -m virtualenv venv
    ```
1. Activate the virtual environment.
    ```
    $ . venv/bin/activate
    ```
    * I keep a function in my `.bashrc` called `activate` that calls this for me every time I want to get to work.
1. Install requirements
    ```
    $ pip install -r requirements.in
    ```
1. Fire up the notebook with `$ ./start_server.sh`
1. Modify the main config file by setting the paths for your WAVE Files that report the weather settings and play music.
1. Format your work and changes with `make clean-notebooks` and `make format`.

## Contributing
* Add new modules to the `python` folder, or create new jupyter notebooks.
* Please format and clean files before committing.

### Stuff to Do
* Add a general METAR scraper that can parse all kinds of METAR reports, not just the CYNJ-specific ones.
* Add a TAF Scraper
* Add more complicated algorithms to help inform go/no-go decisions for more complicated use-cases (the current one literally just checks temp/dewpoint overnight).
* Add more nuanced weather reporter.
