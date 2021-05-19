# Use Cases

I have defined 4 use cases so far.

#### 1. Parse a word - the app takes a word as input and returns morphological parse information, such as part of speech, person, number, tense, stem, etc.

Input: `"gacchāmi" or "गच्छामि"`

Output: `"verb, 1st person, singular, present, indicative, active of √gam 'to go'"`

#### 2. Generate forms - the app takes a stem and returns all forms.
See https://sanskrit.inria.fr/DICO/grammar.fr.html 

#### 3. Word segmentation - the app takes a string and returns its constituent parts.

Input: `"aṇḍasvedajarāyujāḥ"` 

Output: `["aṇḍa", "sveda", "jarāyu", "jāḥ"]`

#### 4. Syllabification - the app takes a word and returns is syllables.

Input: `"kṣatriyaḥ"` 

Output: `[['k', 'ṣ', 'a', 't'], ['r', 'i'], ['y', 'a', 'ḥ']]`
