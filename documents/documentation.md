# Sanskrit Bot

## Parsing a Word
You can parse a Sanskrit word using the "Parse a word" interface. 
Enter a word such as `bharati` in the box and click "Submit".
The page will display the parse for that word as a JSON string, for example
```json
[
  {
    "id": 7,
    "lex_entry": {
      "chapter": 4,
      "definition": "to bear, carry",
      "form": "bhṛ",
      "noun_declension": null,
      "noun_gender": null,
      "pos": "finite_verb",
      "preverb": null,
      "verb_class": "I",
      "verb_surface": "bharati"
    },
    "mood": "indicative",
    "number": "singular",
    "person": "third",
    "surface_form": "bharati",
    "tense": "present",
    "voice": "active"
  }
]
```

The API can be called directly without the UI, using a POST request.
The endpoint is `http://localhost:5000/parse`.
The POST request must contain a JSON body with the `"word"` key, for example
```json
{"word":"bharati"}
```
A complete `curl` command looks like this.
```shell
curl -X POST "http://localhost:5000/parse" -H "Content-Type: application/json" -d '{"word":"bharati"}'
```

## Compound Segmentation
You can also segment a Sanskrit compound using the "Segment a compound" interface.
Submitting the compound `aṇḍasvedajarāyujāḥ` will return a list of words that make up the compound:
```json
[
  [
    "aṇḍa",
    "sveda",
    "jarāyu",
    "jāḥ"
  ]
]
```

The compound segmentation endpoint can also be called directly via `curl`. 
The endpoint is `http://localhost:5000/segment`, and expects a JSON body with the `"compound"` key:
```shell
curl -X POST "http://localhost:5000/segment" -H "Content-Type: application/json" -d '{"compound":"aṇḍasvedajarāyujāḥ"}'
```
Calling the API this way will result in Python style Unicode escaped characters, for example:
```shell
[["a\u1e47\u1e0da","sveda","jar\u0101yu","j\u0101\u1e25"]]
```
