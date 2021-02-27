## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_location
    - slot{"check_loc": "True"}
    - utter_ask_price
* restaurant_search{"price": "low"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"check_loc": "True"}
    - slot{"price": "low"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"email_sub": "The Top 5 restaurants in your search criteria are as belows"}
    - slot{"email_body": "xyz"}
    - utter_reset
    - utter_ask_if_email_needed
* ask_if_email_needed{"ask_if_email_needed": "yes"}
    - slot{"location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"check_loc": "True"}
    - slot{"price": "low"}
    - slot{"ask_if_email_needed": "yes"}
    - utter_ask_emailid
    - slot{"email_id":"naveen.polamreddi@gmail.com"}
* ask_if_email_needed{"ask_if_email_needed": "no"}
    - action_slot_reset
    - utter_goodbye
    - export
* ask_emailid{"email_id":"foodie.bot1107@gmail.com"}
    - slot{"location": "delhi"}
    - slot{"location": "italian"}
    - slot{"check_loc": "True"}
    - slot{"price": "low"}
    - slot{"email_sub": "The Top 5 restaurants in your search criteria are as belows"}
    - slot{"email_id":"foodie.bot1107@gmail.com"}
    - slot{"email_body": "xyz"}
    - action_send_email
    - slot{"email_sub": "The Top 5 restaurants in your search criteria are as belows"}
    - slot{"email_id":"foodie.bot1107@gmail.com"}
    - slot{"email_body": "xyz"}
    - utter_goodbye
    - export
* goodbye
    - utter_goodbye
    - action_slot_reset
    - export
* affirm
    - utter_goodbye
    - export

## location specified
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* affirm
    - utter_goodbye
    - export

## complete path 2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - utter_goodbye
    - export

## complete path 3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
* goodbye
    - utter_goodbye

## complete path 4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - export


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* stop
    - utter_goodbye
    - export

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_search_restaurants
    - slot{"location": "mumbai"}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye
    
    
## happy_path
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"location": "mumbai"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
* affirm
    - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_search_restaurants
    - slot{"location": "delhi"}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
