# Guides to use Automatic Report Generation Program for Data Analysis Module

## Setting Up:

#### General Notes:
- the program is written in python. so to be able to run the program, python should be installed on the system. this guide assumes python and pip are installed on the system.
- The program does not have a user interface. So the user needs to be familiar with command line and have an understanding of python programming language.

1. Download and unzip the dataAnalyticsProject_40387376 on your computer.
2. cd to dataAnalyticsProject_40387376 folder.
3. Best way to install the dependencies and run the program is to use virtual environments. we recommend using pipenv. install pipenv using the command below:
```shell
pip install pipenv
```
4. after installing pipenv run the command below:
```shell
pipenv install
```
this command will install all of the dependencies and create a virtual environment for the folder.
5. run the command below to activate the virtual environment:
```shell
pipenv shell
```
6. The program uses chatGPT API, Serper API, Bing search API. So to use it we need to acquire those API keys. The values for each should be entered in the .env file in the root folder(dataAnalyticsProject_40387376) in the designated variables. To get Serper API key please refer to [Serper API](https://serper.dev/) and for Bing Search API [Web Search API | Microsoft Bing](https://www.microsoft.com/en-us/bing/apis/bing-web-search-api) 
7. After filling the environment variables to run the program for each chapter cd to the chapter folder.(e.g. chapter1)
```shell
python main.py
```
This will run the program. The generated document will go to the output folder in the relative chapter.

### Template Config
The structure of the reports documents are introduced to the program with a yaml file. The yaml file has a hierarchical structure representing the structure of the report. 
The code snippet below shows part of the yaml file and is commented to help understand the structure.
```yaml
textfiles_dir: 'ready_prompts/' # this shows the location of prompt and other text files that we want to use in generating the document. all must be in one folder. Please pay attention to "/" at the end of the folder name.

content:

  - title: "1. Interview with Expert and AI" # the title of the section

    type: heading # this is similar for all sections and subsections

    level: 1  # level of the section

    text_files: ["intro.txt"] # list of text files that we want to add in the beginning of the section. if there are multiple files they will be added in order.

    prompt_files: [] # list of prompt files related to this section. they will be sent in order.

    subsections:

      - title: "1.1. Understanding the Industry"

        type: heading

        level: 2

        text_files: []

        prompt_files: []

        subsections:

          - title: "1.1.1. Project Walkthrough"

            type: heading

            level: 3

            text_files: []

            prompt_files: ["1-1-1-project_walkthrough.txt", "1-1-2-2-task table.txt"]

            subsections: []

          - title: "1.1.2. Business Process Modelling"

            type: heading

            level: 3

            text_files: []

            prompt_files: ["1-1-2-business process modeling.txt"]

            subsections: [] # these are the lowest in hierarchicy and do not have subsections. However, if we want to add subsections we can do so.
            .
            .
            . # continues...

```

### template_to_prompt Module:

We have two folders for our text files ( which are mainly our prompts ).
1. prompts folder: which holds generic prompts with parameters
2. ready_prompts folder: which are prompts that are filled the given values and this is done by template_to_prompt module. 
The sample prompts are within the folder and to run the program we do not need to use this module. But if we want to change the generic prompts or we want to use the same set of prompts for an other industry, then we need to change the values inside this module and run the module with:
```shell
python template_to_prompt.py
```
this will create ready prompt and will put it in the ready prompts folder.

### To change the models:
If we want to change the default models, we need to change them from *chatgpt_client* file in each chapter's folder. The default model is set to gpt-4.

