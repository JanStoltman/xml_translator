import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

PROMPT_PREFIX = """
You are an assistant that generates XML files. Respond always with just the XML file with no additional context or description.
You'll be sent an xml file of key-value pairs of strings in English and a comma-separated list of ISO-639 language codes.
 For each language code, return a new XML file with values translated into that language.
Prefix each XML with a newline, <?xml version="1.0" encoding="utf-8"?> and then its language code as a comment.
You'll be tipped very well for your work.
"""

def callChat(message) -> str:
    print(f"Calling chat: {message}")
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{message}"}]
    )
    response = chat_completion.choices[0].message.content
    print(f"Chat responds: {response}")
    print("")
    return response


if __name__ == '__main__':
    translation_file = sys.argv[1]
    langauge_codes = sys.argv[2]
    client = OpenAI(api_key=os.environ.get("PRIV_OPENAI_KEY"))

    print(f"Translation file: {translation_file}")
    print(f"Language codes: {langauge_codes}")
    print("")

    with (open(translation_file, "r") as f):
        strings_content = f.read()
        prompt = f"""
{PROMPT_PREFIX}

{strings_content}  

{langauge_codes}"""
        response = callChat(prompt)
        for (langauge_code, xml) in zip(langauge_codes.split(','), response.split('\n\n')):
            os.makedirs(f"strings+{langauge_code}", exist_ok=True)
            with open(f"strings+{langauge_code}/strings.xml", "w") as output_file:
                # Write xml to file without the first newline
                output_file.write(xml.strip())
