from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
import pandas as pd
from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
import zomatopy
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"36ea2bea7d8727ed031ab66d9ceb91c7"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		prc = tracker.get_slot('price')
		print("Price i got is {}".format(prc))
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),10000)
		d = json.loads(results)
		#rest_name_list = []
		#rest_location_list = []
		#rest_rating_list = []
		#rest_budg_list = []
		if d['results_found'] == 0:
			dispatcher.utter_message("No Results")
		else:
			rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
			rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
			rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
			rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
			pd.set_option('display.max_colwidth', -1)
			rest_df = pd.DataFrame({'name':rest_name_list, 'location':rest_location_list, 'rating':rest_rating_list, 'avg_cost_for2':rest_budg_list})
			if prc == "low":
				rest_df_filter = rest_df[rest_df['avg_cost_for2']<300]
			elif prc == "mid":
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>=300) & (rest_df['avg_cost_for2']<=700)]
			else:
				rest_df_filter = rest_df[(rest_df['avg_cost_for2']>700)]
			rest_df_sorted = rest_df_filter.sort_values(by=['rating'], ascending=False)
			#header = "--The top" + cuisine + " restaurants in " + loc + " with avg. budget of " + prc + " Rs. for 2 people--"
			email_sub="Foodie App Search Results for you"
			dispatcher.utter_message("-----Foodie App Search Results for you-----")
			email_body = ""
			for row in rest_df_sorted.head(5).iterrows():
				email_body += row[1]['name']+", in "+row[1]['location']+" has been rated "+row[1]['rating']+" Costing " + prc+"\n"
				dispatcher.utter_message(row[1]['name']+", in "+row[1]['location']+" has been rated "+row[1]['rating']+" Costing " + prc+"\n")
		return [SlotSet('email_sub', email_sub), SlotSet('email_body', email_body)]

class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		loc_lower = loc.lower()
		cities = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune',
                'Agra','Ajmer','Aligarh','Amravati','Amritsar','Asansol','Auragabad','Bareilly','Belgaum',
                'Bhavnagar','Bhiwandi','Bhopal','Bhubaneswar','Bikaner','Bokaro Steel City',
                'Chandigarh', 'Coimbatore','Cuttack','Dehradun','Dhanbad','Durg-Bhilai nagar','Durgapur',
                'Erode','Faridabad','Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur',
                'Gurgaon','Guwahati','Gwalior','Hubli-Dharwad','Indore','Jabalpur','Jaipur','Jalandhar',
                'Jammu', 'Jamnagar','Jamshedpur','Jhansi','Jodhpur','Kannur','Kanpur','Kakinada','Kochi',
                'Kottayam','Kolhapur','Kollam','Kota','Kozhikode','Kurnool','Lucknow','Ludhiana',
                'Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore',
                'Nagpur','Nanded','Nashik','Nellore','Noida','Palakkad','Patna','Pondicherry', 'Prayagraj',
                'Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri','Solapur',
                'Srinagar','Sultanpur','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli',
                'Tirunelveli','Tiruppur','Ujjain','Bijapur','Vadodara','Varanasi','Vasai-Virar City','Vijayawada']
		cities_in_lower = [x.lower() for x in cities]
		if loc_lower in cities_in_lower:
			check_loc = "True"
			SlotSet("check_loc","True")
			dispatcher.utter_message("location valid, proceeding with further search")
			return [SlotSet("check_loc", check_loc)]
		else:
			check_loc = "False"
			SlotSet("check_loc","False")
			dispatcher.utter_message("location not valid, please run another search")
			return [SlotSet('location', None),SlotSet('cuisine', None),SlotSet('price', None),SlotSet('email_sub', None), SlotSet('email_body', None)]

class  ActionSlotReset(Action):
	def name(self):
		return 'action_slot_reset'
	def run(self, dispatcher, tracker, domain):
		reset_all_slots=tracker.get_slot('reset_all_slots')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		prc = tracker.get_slot('price')
		email_sub = tracker.get_slot('email_sub')
		email_body = tracker.get_slot('email_body')
		if reset_all_slots in ['yes', 'ye','sure','absolutely','YES']:
			return [SlotSet('location', None),SlotSet('cuisine', None),SlotSet('price', None),SlotSet('email_sub', None), SlotSet('email_body', None)]

		else:
			return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',prc),SlotSet('email_sub', email_sub), SlotSet('email_body', email_body)]

class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'
	def run(self, dispatcher, tracker, domain):
		email_sub = tracker.get_slot('email_sub')
		email_body = tracker.get_slot('email_body')
		email_id = tracker.get_slot('email_id')
		from_user = "foodie.bot1107@gmail.com"
		to_user = email_id
		#password = "viJayawada@1992"
		#App Password configured to work from MAC,below is the 16 character length app password
		password = "jcazwdpknhdujgwu"
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.ehlo()
		server.starttls()
		server.login(from_user, password)
		msg = MIMEMultipart()
		msg['From'] = from_user
		msg['TO'] = to_user
		msg['Subject'] = email_sub
		body = email_body
		msg.attach(MIMEText(body,'plain'))
		text = msg.as_string()
		server.sendmail(from_user,to_user,text)
		server.close()
		dispatcher.utter_message("Email Sent, hope you enjoyed interacting with foodie app")


