# XML-Translator
This project uses GPT to generate new xml files per langauge based on an existing english xml. 

## Setup
Create an .env file with: 
```
PRIV_OPENAI_KEY=<your key>
```

## Usage
python main.py <input_file> <language_codes>
```
python3 main.py strings+en/strings.xml es,fr,de 
```