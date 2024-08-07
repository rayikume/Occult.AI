# Occult.AI (Streamlit Branch)

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
  - [frontend.py](#frontendpy)
  - [query.py](#querypy)

## Introduction

Occult.AI is designed to provide a seamless and intuitive AI-powered experience. This project utilizes modern web development technologies to deliver a high-performance, scalable solution.

## Features

- AI-driven functionalities
- User-friendly interface
- Scalable architecture
- Comprehensive documentation

## Installation

To get started with Occult.AI, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/rayikume/Occult.AI.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Occult.AI/backend
    ```
3. Create a virtual environment
    ```bash
    cd poetry shell
    ```
3. Install dependencies:
    ```bash
    poetry install
    ```

## Usage

To run the project locally, execute the following command:

```bash
streamlit run frontend.py
```

## Code Overview

### frontend.py

The `frontend.py` script is responsible for rendering the user interface of the application using Streamlit. It defines the layout, widgets, and overall look and feel of the web application. As well as handling the langGrap node opearations, Key functionalities include:

- Creating input fields for user queries.
- Displaying the results generated by the AI models.
- Providing a seamless and interactive user experience.
- Handling LangGraph's nodes and edges

### query.py

The `query.py` script handles the backend logic for processing user queries. It includes functions to interact with the AI models, perform necessary computations, and return the results. Key functionalities include:

- Parsing user input.
- Interfacing with AI models to generate responses.
- Returning processed results to be displayed by the frontend.

### Endpoints

- /greet: takes the prompt and responed with greet from an AI model.
- /addbook: takes the prompt and responed by confermation that the book is added to the database.
- /recommendation: takes the prompt and responed with a table of most relateable books based on user's prompt.
- /summerization: takes the prompt and responed with a reply from an AI model summarizing the book that the user requested.
