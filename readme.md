# Scraping OLBG.com
Script for scraping horse race event from [olbg.com](https://www.olbg.com/betting-tips/Horse_Racing/2).

## Install requirements
Type syntax below, to have the same Python dependencies/libraries.
```terminal
pip install -r requirements.txt
```

## How to run scraping function
I also add command line interface (CLI) on this project. So, to  output data from specific race event, you can use the command line below. The output data format must be a .json extension.
```
python manage.py collect --url [URL] --output [OUTPUT]
```

## How to run the main script and collect all top tips
You also can modifying and run the main script to satisfy your needs.
```
python main.py
```