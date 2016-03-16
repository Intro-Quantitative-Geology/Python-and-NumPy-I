# Lesson data
For this lesson we will be using several example data files contained in a [zip file that you should download](Data/Lab-1-Data.zip).

## Getting the data
1. Download a copy of the [lesson data file](Data/Lab-1-Data.zip).
2. Open a new Terminal window by clicking on the Dash Home icon at the top left corner of the screen and entering "terminal" into the search box. Click on the Terminal icon.
3. Navigate to the Desktop and create a new directory for this week's lesson.

    ```bash
    $ cd ~/Desktop
    $ mkdir Lab-1
    $ cd Lab-1
    ```
Note the `$` symbol represents the command prompt in the Terminal window.
4. Copy `Lab-1-data.zip` file to the current directory and extract the data.

    ```bash
    $ cp ~/Downloads/Lab-1-data.zip .
    $ unzip Lab-1-data.zip
    $ cd Data
    ```

At this point, you should be ready to proceed to [installing Anaconda](Anaconda.md).

## Data Sources
- `GVP-Volcano-List.csv` - Database of Holocene volcanoes from the [Smithsonian Institution's Global Volcanism Program](http://volcano.si.edu/region.cfm?rn=15)
