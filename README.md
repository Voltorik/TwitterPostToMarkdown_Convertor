# Twitter post to .md convertor
Takes a post's url as a variable and outputs that post in a .md file. The name of the file is the first 40 characters of the first sentence. Any invalid characters are replaced with a `%`. 

I wanted a quick way to archive posts locally in a universal format. 

## Running the script
Prereqs: 
- Python 3.x
- Selenium
- Configured WebDriver (I use firefox configs in the code)
- Setup & activate a virtual environment (Optional)
- Then install dependencies `pip install -r requirements.txt`

Then run `py convertor.py url` where `url` is the url of the twitter post. 

Ex:
```
py convertor.py https://x.com/Voltorik_/status/1792255489427787859
```

## Tools used 
Leverages [Selenium](https://www.selenium.dev/) (web browser automation tool)
- Used to run the instance of a headless browser.
- Data extracted:
  - `tweetText` - The tweets text content
  - `User-Name` - The display name and username (@user)
  - `time` - The timestamp of the original post

## Script execution steps
1. Starts up a new headless browser and waits until the `tweetText` div is loaded.
2. Extracts content as mentioned above.
3. Splits `User-Name` data into separate pieces.
4. Converts the `time` attribute into a new string format. Ex: `(Sunday) May 19, 2024 - 06:06 PM`
5. Assigns the file name. Spilts by `.`, then takes the first 40 characters of sentence. Replaces any invalid chars with `%`.
6. Generates a new .md file.

## File output template
_displayName_ (_@username_)

_formattedTimeStamp_

_tweetContent_

_URL:_ _urlOfPost_

Ex:  

```
Voltorik (@Voltorik_)
(Sunday) May 19, 2024 - 06:06 PM

I wish to live a calm, quiet life. Similar to that of a wizard in his tower.
I want to gather knowledge for the sake of it.
Because it's fun. Because if someone accidentally wanders into my tower,
I may be able to guide them in the right direction.

URL: https://x.com/Voltorik_/status/1792255489427787859
```
