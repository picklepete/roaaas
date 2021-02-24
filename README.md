# roaaas-api

**roaaas-api** is a Ferengi Rules of Acquisition as a Service API, written in Python/Flask.

## Installation

Install the requirements:

```
pip install -r requirements.txt
```

Build the index:

```
python index.py -f rules.json
```

Start the Flask server:

```
flask run
```

## Usage

List all rules:

> GET /rules/
```json
{
  "0": {
    "rule": "Always listen to the Grand Nagus", 
    "source": "https://memory-beta.fandom.com/wiki/Star_Trek_Online"
  }, 
  "1": {
    "rule": "Once you have their money... you never give it back.", 
    "source": "https://memory-beta.fandom.com/wiki/The_Nagus"
  }
}
```

(truncated for clarity)

Retrieve a specific rule:

> GET /rules/15/
```json
{
  "rule": "Dead men close no deals.", 
  "source": "https://memory-beta.fandom.com/wiki/Demons_of_Air_and_Darkness"
}
```




