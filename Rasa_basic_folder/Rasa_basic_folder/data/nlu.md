## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:reset
- reset
- new search
- new query

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)
- [Lithuania](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- can you book a table in [rome](location) in a [moderate]{"entity": "price", "value": "mid"} price range with [british](cuisine) food
- can you book a table in [bangalore](location) in a [expensive]{"entity":"price", "value": "expensive"} price range with [italian](cuisine) food
- can you book a table in [hyderabad](location) in a [low]{"entity": "price", "value":"low"}
price range with [south indian](cuisine) food
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- [xyz](location)
## intent:ask_if_email_needed
- [yes](ask_if_email_needed)
- [yep](ask_if_email_needed)
- [sure](ask_if_email_needed)
- [please](ask_if_email_needed)
- [yes please](ask_if_email_needed)

## intent:ask_emailid
- it would be [naveen.polamreddi@gmail.com](email_id)
- that is [xyz@gmail.com](email_id)
- [abc.xyz@gmail.com](email_id)

## intent:stop
- stop
- freeze
- erase

## intent:price
- [300](price)
- [777](price)
- [900](price)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru
- bangaloree
- blr
- bengalore
- bengaluru

## synonym:chinese
- chines
- Chinese
- Chines
- chine

## synonym:italian
- italian
- italy
- itali

## synonym:south indian
- south-indian
- southindian
- south india
- southindia
- south

## synonym:north indian
- north-indian
- northindian
- north india
- north indian
- north

## synonym:Delhi
- New Delhi
- Delhi
- NewDelhi
- Dilli
- Delhi
- newdelhi
- new delhi
- new dilli
- new delhi
- dilhi
- dilli

## synonym:Mumbai
- bombay
- mumbai
- bombai
- mumbay

## synonym:Kolkata
- kolkata
- calcutta
- kolkatta
- calcutta
- calcuta

## synonym:Chennai
- chennai
- madras
- Madras

## synonym:Hyderabad
- hyderabad
- hyd
- Hyd
- secunderabad
- cyberabad

## synonym:Lucknow
- Lakhanpur
- lucknow
- luckno

## synonym:Mysore
- mysore
- mysuru
- Mysuru

## synonym:Kochi
- kochi
- cochin
- Cochin

## synonym:Mangalore
- mangalore
- mangaluru
- mangaluru

## synonym:Vishakapatnam
- vishakapatnam
- Vizag
- vizag

## synonym:Thiruvananthapuram
- thiruvananthapuram
- trivandrum
- travancore
- Trivandrum

## synonym:Vadodara
- vadodara
- vadodra
- Vadodra

## synonym:Jamshedpurr
- jamshedpur
- Jamshedpur
- jamshedpur

## synonym:Rajahmundry
- rajahmundry
- rajamundry
- rajamundri
- rajamahendravaram
- rajamundry

## synonym:Rourkela
- rourkela
- Raurkela
- raurkela

## synonym: Amritsar
- amritsar
- Amratsar
- amratsar

## synonym:Chandigarh
- chandigarh
- chadighar
- chandighar

## synonym:Allahabad
- allahabad
- prayagraj
- Prayagraj
- Allhabad

## synonym:Nashik
- nashik
- nasik
- Nasik

## synonym:Pondicherry
- pondicherry
- puducherry
- puducherri

## synonym:mid
- moderate

## synonym:small
- less
- pocket friendly
- little

## synonym:expensive
- costly
- belly full
- expense
- expensive

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## regex:price
- [0-9]{3:}
