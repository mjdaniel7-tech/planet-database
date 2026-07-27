
solar_ai_app.py

Starter AI application for the Solar System project.

Install:
    pip install langchain langchain-openai langchain-community mysql-connector-python

Set your OpenAI API key before running:
    export OPENAI_API_KEY=your_key   (Linux/macOS)
    set OPENAI_API_KEY=your_key      (Windows CMD)
"""

import os


def main():
    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY is not set.")
        return

    print("Solar System AI Assistant")
    print("-------------------------")
    print("This starter file is ready for you to expand with")
    print("LangChain, OpenAI, and your MySQL database.")


if __name__ == "__main__":
    main()
