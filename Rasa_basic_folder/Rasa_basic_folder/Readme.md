# Restaurant Bot

a restaurant chatbot using open source chat framework [RASA](https://rasa.com/). Integrates with [Zomato API](https://developers.zomato.com/) to fetch restaurant information.

## Pre-requisites

- python==3.8.0
- rasa==2.9.0
- spacy==2.2.4
- en_core_web_md==2.2.5
- pandas==1.2.1

## Installation

### RASA

Refer to official [installation guide](https://rasa.com/docs/rasa/user-guide/installation/) to install RASA

### Installation
1. Rasa Package installation
   ```python
   pip install -U rasa
   ```

2. Package Installation

   ```python
   pip install -U spacy
   ```

3. Model Installation

   ```python
   python -m spacy download en_core_web_md
   ```

4. Create custom shortcut link to Spacy model

   ```python
   python -m spacy link en_core_web_md en
   ```
5. Install pandas,required in actions.py
   ```python
   pip install pandas
   ```

## Repo Information

This repo contains training data and script files necessary to compile and execute this restaurant chatbot. It comprises of the following files:

### Data Files

- **data/nlu.md** : contains training examples for the NLU model  
- **data/stories.md** : contains training stories for the Core model
- **data/stories.yml** : contains training model simulations in .yml format

### Script Files

- **zomato** : contains Zomato API integration code
  - **zomato.py** : contains functions to consume common Zomato APIs like fetch location details, type of cuisines, search for restaurants, etc
- **actions_server.py** : contains code to start a RASA actions server. This is used to serve RASA custom actions.
- **actions.py** : contains the following custom actions (_insert **ZOMATO API** key in this script file before starting RASA server_)
  - search restaurant
  - validate location
  - send email to gmail.com using smtplib python framework
  - reset slots  
- **nlu_test.py** : contains code to test generated NLU models
- **nlu_train.py** : contains code to
  - train a NLU model
  - persist NLU model in 'models' folder
  - run CLI to interact with generated model and validate extracted intents and entities
- **rasa_slack.py** : contains code to integrate with slack channel
- **rasa_train.py** : primary script file to test chatbot from CLI. Contains code to:
  - train both NLU and Core model
  - persist packaged model in 'models' folder
  - start CLI interface to interact with chatbot
    (_RASA action server must be running for this to work_)

### Config Files

- **config.yml** contains model configuration and custom policy
- **domain.yml** defines chatbot domain like entities, actions, templates, slots  
- **endpoints.yml** contains the webhook configuration for custom action

## Usages

- Train ONLY NLU model and validate
  ```
  rasa train nlu
  ```
  This will generate _restaurant-nlu-model.tar.gz_ inside **models** folder and start an interactive shell

- Test generated NLU model (_generated NLU model should be available in 'models' folder prior to test_).
  Equivalent RASA CLI command 
  ```
  rasa shell
  ```

- Run RASA action server ( mandatory step to interact with chatbot) on port **5055**
  Equivalent RASA CLI command 
  ```
  rasa run actions
  ```
  
- Train RASA NLU and Core model
  This will generate _restaurant-rasa-model.tar.gz_ inside **models** folder
  Equivalent RASA CLI command 
  ```
  rasa train
  ```

- Starts an interactive session with restaurant chatbot
  Equivalent RASA CLI command    
  ```
  rasa interactive
  ```

- Run RASA server to connect slack channel

  ```python
  rasa run -m models -p 5004 --connctor slack --credentials credentials.yml
  ```
## Bot Conversation Examples
- hello
- can you find me an italian restaurant
- can you find me a good restaurant

## NOTE
- files under models subdirectory have been moved away as uprad platform
is not able to let us upload .zip files  more than 50MB.
- so i moved away model NLU file nlu-20210208-222611.tar.gz, but i still
  have the file for reference.