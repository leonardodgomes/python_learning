# Read JSON
# Big data sets are often stored, or extracted as JSON.
# JSON is plain text, but has the format of an object, and is well known in the world of programming, including Pandas.

# Example, Load the JSON file into a DataFrame:

import pandas as pd

df = pd.read_json('C:\\Users\\a070127\\Documents\\Leonardo\\Pessoal\\Python\\03_Pandas\\00_Files\\data.js')

print(df.to_string()) # Tip: use to_string() to print the entire DataFrame.


# Dictionary as JSON
#  JSON = Python Dictionary
#  JSON objects have the same format as Python dictionaries.
#  If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:

#  Example, Load a Python Dictionary into a DataFrame:

import pandas as pd
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 