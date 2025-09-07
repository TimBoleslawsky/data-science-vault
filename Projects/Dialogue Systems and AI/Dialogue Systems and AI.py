# %%
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from fuzzywuzzy import process
import spacy
from spacy.matcher import Matcher, PhraseMatcher

# %%
# Sample data
data = [
    # Flight Domain (75 examples)
    ("I need to book a flight to New York", "flight"),
    ("Can you help me book a flight to London?", "flight"),
    ("I want to reserve a flight to Paris", "flight"),
    ("Book me a flight to Tokyo", "flight"),
    ("I'd like to book a flight to Berlin", "flight"),
    ("Can I book a flight to San Francisco?", "flight"),
    ("I need a flight to Dubai", "flight"),
    ("Book a flight to Sydney for me", "flight"),
    ("I want to book a flight to Toronto", "flight"),
    ("Can you book a flight to Mumbai?", "flight"),
    ("I need to cancel my flight to New York", "flight"),
    ("Cancel my flight to London, please", "flight"),
    ("I want to cancel my flight to Paris", "flight"),
    ("Can you cancel my flight to Tokyo?", "flight"),
    ("I'd like to cancel my flight to Berlin", "flight"),
    ("Cancel my flight to San Francisco", "flight"),
    ("I need to cancel my flight to Dubai", "flight"),
    ("Please cancel my flight to Sydney", "flight"),
    ("I want to cancel my flight to Toronto", "flight"),
    ("Can you cancel my flight to Mumbai?", "flight"),
    ("What's the status of flight BA123?", "flight"),
    ("Can you check the status of flight AA456?", "flight"),
    ("I need information about flight DL789", "flight"),
    ("What's the departure time for flight EK123?", "flight"),
    ("Can you tell me the arrival time of flight QR456?", "flight"),
    ("Is flight LH789 on time?", "flight"),
    ("What's the gate number for flight AF123?", "flight"),
    ("Can you check if flight SQ456 is delayed?", "flight"),
    ("I need details about flight CX789", "flight"),
    ("What's the baggage allowance for flight EY123?", "flight"),
    ("Book me a flight to Chicago", "flight"),
    ("I need to book a flight to Los Angeles", "flight"),
    ("Can you help me book a flight to Miami?", "flight"),
    ("I want to reserve a flight to Seattle", "flight"),
    ("Book a flight to Boston for me", "flight"),
    ("I'd like to book a flight to Austin", "flight"),
    ("Can I book a flight to Las Vegas?", "flight"),
    ("I need a flight to Houston", "flight"),
    ("Book me a flight to Phoenix", "flight"),
    ("I want to book a flight to Denver", "flight"),
    ("Can you book a flight to San Diego?", "flight"),
    ("I need to cancel my flight to Chicago", "flight"),
    ("Cancel my flight to Los Angeles, please", "flight"),
    ("I want to cancel my flight to Miami", "flight"),
    ("Can you cancel my flight to Seattle?", "flight"),
    ("I'd like to cancel my flight to Boston", "flight"),
    ("Cancel my flight to Austin", "flight"),
    ("I need to cancel my flight to Las Vegas", "flight"),
    ("Please cancel my flight to Houston", "flight"),
    ("I want to cancel my flight to Phoenix", "flight"),
    ("Can you cancel my flight to Denver?", "flight"),
    ("What's the status of flight UA123?", "flight"),
    ("Can you check the status of flight SW456?", "flight"),
    ("I need information about flight NK789", "flight"),
    ("What's the departure time for flight B6123?", "flight"),
    ("Can you tell me the arrival time of flight VX456?", "flight"),
    ("Is flight F9789 on time?", "flight"),
    ("What's the gate number for flight G4123?", "flight"),
    ("Can you check if flight J8456 is delayed?", "flight"),
    ("I need details about flight K7789", "flight"),
    ("What's the baggage allowance for flight L9123?", "flight"),

    # Restaurant Domain (75 examples)
    ("I want to book a table for 2 at 7 PM", "restaurant"),
    ("Can you reserve a table for 4 at 8 PM?", "restaurant"),
    ("I'd like to book a table for 6 at 9 PM", "restaurant"),
    ("Book me a table for 3 at 6 PM", "restaurant"),
    ("I need to reserve a table for 5 at 7:30 PM", "restaurant"),
    ("Can you book a table for 2 at 8:30 PM?", "restaurant"),
    ("I want to reserve a table for 4 at 9:30 PM", "restaurant"),
    ("Book a table for 6 at 7 PM for me", "restaurant"),
    ("I'd like to reserve a table for 3 at 8 PM", "restaurant"),
    ("Can I book a table for 5 at 9 PM?", "restaurant"),
    ("I need to cancel my reservation at The Bistro", "restaurant"),
    ("Cancel my reservation at Olive Garden, please", "restaurant"),
    ("I want to cancel my reservation at Cheesecake Factory", "restaurant"),
    ("Can you cancel my reservation at Red Lobster?", "restaurant"),
    ("I'd like to cancel my reservation at Outback Steakhouse", "restaurant"),
    ("Cancel my reservation at Texas Roadhouse", "restaurant"),
    ("I need to cancel my reservation at P.F. Chang's", "restaurant"),
    ("Please cancel my reservation at Buffalo Wild Wings", "restaurant"),
    ("I want to cancel my reservation at Chipotle", "restaurant"),
    ("Can you cancel my reservation at Panera Bread?", "restaurant"),
    ("Find me a good Italian restaurant nearby", "restaurant"),
    ("Can you find a Mexican restaurant close by?", "restaurant"),
    ("I need to find a Chinese restaurant in the area", "restaurant"),
    ("Find a sushi place near me", "restaurant"),
    ("Can you recommend a good steakhouse nearby?", "restaurant"),
    ("I want to find a vegetarian restaurant close by", "restaurant"),
    ("Find me a seafood restaurant in the area", "restaurant"),
    ("Can you find a vegan restaurant nearby?", "restaurant"),
    ("I need to find a Thai restaurant close by", "restaurant"),
    ("Find a good pizza place near me", "restaurant"),
    ("Book me a table for 2 at 7 PM at The Bistro", "restaurant"),
    ("I need to reserve a table for 4 at 8 PM at Olive Garden", "restaurant"),
    ("Can you book a table for 6 at 9 PM at Cheesecake Factory?", "restaurant"),
    ("I want to reserve a table for 3 at 6 PM at Red Lobster", "restaurant"),
    ("Book a table for 5 at 7:30 PM at Outback Steakhouse", "restaurant"),
    ("I'd like to book a table for 2 at 8:30 PM at Texas Roadhouse", "restaurant"),
    ("Can I reserve a table for 4 at 9:30 PM at P.F. Chang's?", "restaurant"),
    ("I need to book a table for 6 at 7 PM at Buffalo Wild Wings", "restaurant"),
    ("Book me a table for 3 at 8 PM at Chipotle", "restaurant"),
    ("I want to reserve a table for 5 at 9 PM at Panera Bread", "restaurant"),
    ("Cancel my reservation at The Bistro for 7 PM", "restaurant"),
    ("I need to cancel my reservation at Olive Garden for 8 PM", "restaurant"),
    ("Can you cancel my reservation at Cheesecake Factory for 9 PM?", "restaurant"),
    ("I want to cancel my reservation at Red Lobster for 6 PM", "restaurant"),
    ("Cancel my reservation at Outback Steakhouse for 7:30 PM", "restaurant"),
    ("I'd like to cancel my reservation at Texas Roadhouse for 8:30 PM", "restaurant"),
    ("Can I cancel my reservation at P.F. Chang's for 9:30 PM?", "restaurant"),
    ("I need to cancel my reservation at Buffalo Wild Wings for 7 PM", "restaurant"),
    ("Please cancel my reservation at Chipotle for 8 PM", "restaurant"),
    ("I want to cancel my reservation at Panera Bread for 9 PM", "restaurant"),
    ("Find me a good Italian restaurant in downtown", "restaurant"),
    ("Can you find a Mexican restaurant near the mall?", "restaurant"),
    ("I need to find a Chinese restaurant in the city center", "restaurant"),
    ("Find a sushi place close to the train station", "restaurant"),
    ("Can you recommend a good steakhouse in the suburbs?", "restaurant"),
    ("I want to find a vegetarian restaurant near the park", "restaurant"),
    ("Find me a seafood restaurant by the beach", "restaurant"),
    ("Can you find a vegan restaurant in the downtown area?", "restaurant"),
    ("I need to find a Thai restaurant near the office", "restaurant"),
    ("Find a good pizza place close to the university", "restaurant"),

    # Weather Domain (75 examples)
    ("What's the temperature tomorrow?", "weather"),
    ("Can you tell me the temperature for tomorrow?", "weather"),
    ("I need to know the temperature tomorrow", "weather"),
    ("What will the temperature be tomorrow?", "weather"),
    ("Tell me the temperature for tomorrow", "weather"),
    ("What's the forecasted temperature for tomorrow?", "weather"),
    ("Can you check the temperature for tomorrow?", "weather"),
    ("I want to know the temperature tomorrow", "weather"),
    ("What's the expected temperature tomorrow?", "weather"),
    ("Can you give me the temperature for tomorrow?", "weather"),
    ("Will it rain tomorrow?", "weather"),
    ("Is there a chance of rain tomorrow?", "weather"),
    ("Can you check if it will rain tomorrow?", "weather"),
    ("What's the chance of rain tomorrow?", "weather"),
    ("I need to know if it will rain tomorrow", "weather"),
    ("Tell me if it will rain tomorrow", "weather"),
    ("What's the probability of rain tomorrow?", "weather"),
    ("Can you tell me if it will rain tomorrow?", "weather"),
    ("I want to know if it will rain tomorrow", "weather"),
    ("What's the likelihood of rain tomorrow?", "weather"),
    ("What's the air quality tomorrow?", "weather"),
    ("Can you tell me the air quality for tomorrow?", "weather"),
    ("I need to know the air quality tomorrow", "weather"),
    ("What will the air quality be tomorrow?", "weather"),
    ("Tell me the air quality for tomorrow", "weather"),
    ("What's the forecasted air quality for tomorrow?", "weather"),
    ("Can you check the air quality for tomorrow?", "weather"),
    ("I want to know the air quality tomorrow", "weather"),
    ("What's the expected air quality tomorrow?", "weather"),
    ("Can you give me the air quality for tomorrow?", "weather"),
    ("What's the temperature tomorrow in New York?", "weather"),
    ("Can you tell me the temperature for tomorrow in London?", "weather"),
    ("I need to know the temperature tomorrow in Paris", "weather"),
    ("What will the temperature be tomorrow in Tokyo?", "weather"),
    ("Tell me the temperature for tomorrow in Berlin", "weather"),
    ("What's the forecasted temperature for tomorrow in San Francisco?", "weather"),
    ("Can you check the temperature for tomorrow in Dubai?", "weather"),
    ("I want to know the temperature tomorrow in Sydney", "weather"),
    ("What's the expected temperature tomorrow in Toronto?", "weather"),
    ("Can you give me the temperature for tomorrow in Mumbai?", "weather"),
    ("Will it rain tomorrow in Chicago?", "weather"),
    ("Is there a chance of rain tomorrow in Los Angeles?", "weather"),
    ("Can you check if it will rain tomorrow in Miami?", "weather"),
    ("What's the chance of rain tomorrow in Seattle?", "weather"),
    ("I need to know if it will rain tomorrow in Boston", "weather"),
    ("Tell me if it will rain tomorrow in Austin", "weather"),
    ("What's the probability of rain tomorrow in Las Vegas?", "weather"),
    ("Can you tell me if it will rain tomorrow in Houston?", "weather"),
    ("I want to know if it will rain tomorrow in Phoenix", "weather"),
    ("What's the likelihood of rain tomorrow in Denver?", "weather"),
    ("What's the air quality tomorrow in New York?", "weather"),
    ("Can you tell me the air quality for tomorrow in London?", "weather"),
    ("I need to know the air quality tomorrow in Paris", "weather"),
    ("What will the air quality be tomorrow in Tokyo?", "weather"),
    ("Tell me the air quality for tomorrow in Berlin", "weather"),
    ("What's the forecasted air quality for tomorrow in San Francisco?", "weather"),
    ("Can you check the air quality for tomorrow in Dubai?", "weather"),
    ("I want to know the air quality tomorrow in Sydney", "weather"),
    ("What's the expected air quality tomorrow in Toronto?", "weather"),
    ("Can you give me the air quality for tomorrow in Mumbai?", "weather")
]

# %%
# Flights data 
flights_data = [
    {"Flight Number": "BA123", "Departure City": "London", "Destination City": "New York", "Day": "23.03.2025"},
    {"Flight Number": "AA456", "Departure City": "New York", "Destination City": "Los Angeles", "Day": "22.05.2025"},
    {"Flight Number": "DL789", "Departure City": "Atlanta", "Destination City": "Paris", "Day": "01.04.2025"},
    {"Flight Number": "EK123", "Departure City": "Dubai", "Destination City": "Sydney", "Day": "05.06.2025"},
    {"Flight Number": "QR456", "Departure City": "Doha", "Destination City": "Berlin", "Day": "15.07.2025"},  # Added missing date
    {"Flight Number": "LH789", "Departure City": "Frankfurt", "Destination City": "Tokyo", "Day": "10.08.2025"},  # Replaced "tomorrow"
    {"Flight Number": "AF123", "Departure City": "Paris", "Destination City": "San Francisco", "Day": "18.09.2025"},  # Replaced "next Wednesday"
    {"Flight Number": "SQ456", "Departure City": "Singapore", "Destination City": "London", "Day": "25.10.2025"},  # Replaced "Friday"
    {"Flight Number": "CX789", "Departure City": "Hong Kong", "Destination City": "Toronto", "Day": "30.11.2025"},  # Replaced "Saturday"
    {"Flight Number": "EY123", "Departure City": "Abu Dhabi", "Destination City": "Mumbai", "Day": "12.12.2025"},  # Replaced "Sunday"
    {"Flight Number": "UA123", "Departure City": "Chicago", "Destination City": "New York", "Day": "14.01.2026"},  # Replaced "tomorrow"
    {"Flight Number": "SW456", "Departure City": "Dallas", "Destination City": "Las Vegas", "Day": "20.02.2026"},  # Replaced "Friday"
    {"Flight Number": "NK789", "Departure City": "Orlando", "Destination City": "Denver", "Day": "05.03.2026"},  # Replaced "next Monday"
    {"Flight Number": "B6123", "Departure City": "Miami", "Destination City": "Boston", "Day": "15.04.2026"},  # Replaced "Saturday"
    {"Flight Number": "VX456", "Departure City": "San Francisco", "Destination City": "Seattle", "Day": "22.05.2026"},  # Replaced "Sunday"
    {"Flight Number": "F9789", "Departure City": "Austin", "Destination City": "Houston", "Day": "30.06.2026"},  # Replaced "tomorrow"
    {"Flight Number": "G4123", "Departure City": "Phoenix", "Destination City": "San Diego", "Day": "10.07.2026"},  # Replaced "Friday"
    {"Flight Number": "J8456", "Departure City": "Portland", "Destination City": "Chicago", "Day": "18.08.2026"},  # Replaced "next Wednesday"
    {"Flight Number": "K7789", "Departure City": "Detroit", "Destination City": "New York", "Day": "25.09.2026"},  # Replaced "Saturday"
    {"Flight Number": "L9123", "Departure City": "Philadelphia", "Destination City": "Miami", "Day": "30.10.2026"},  # Replaced "Sunday"
    {"Flight Number": "BA456", "Departure City": "London", "Destination City": "Dubai", "Day": "05.11.2026"},  # Replaced "tomorrow"
    {"Flight Number": "AA789", "Departure City": "New York", "Destination City": "Tokyo", "Day": "12.12.2026"},  # Replaced "Friday"
    {"Flight Number": "DL123", "Departure City": "Atlanta", "Destination City": "Sydney", "Day": "15.01.2027"},  # Replaced "next Monday"
    {"Flight Number": "EK456", "Departure City": "Dubai", "Destination City": "Paris", "Day": "20.02.2027"},  # Replaced "Saturday"
    {"Flight Number": "QR789", "Departure City": "Doha", "Destination City": "Berlin", "Day": "25.03.2027"}  # Replaced "Sunday"
]

# %%
# Restaurant data
restaurants_data = [
    {"Restaurant Name": "Golden Dragon", "City": "New York", "Restaurant Type": "Chinese"},
    {"Restaurant Name": "Taco Fiesta", "City": "New York", "Restaurant Type": "Mexican"},
    {"Restaurant Name": "Pasta Paradise", "City": "New York", "Restaurant Type": "Italian"},
    {"Restaurant Name": "Sushi Haven", "City": "Los Angeles", "Restaurant Type": "Japanese"},
    {"Restaurant Name": "Burger Barn", "City": "Los Angeles", "Restaurant Type": "American"},
    {"Restaurant Name": "Spice Garden", "City": "Los Angeles", "Restaurant Type": "Indian"},
    {"Restaurant Name": "Little Italy", "City": "Chicago", "Restaurant Type": "Italian"},
    {"Restaurant Name": "Windy City Pizza", "City": "Chicago", "Restaurant Type": "Pizza"},
    {"Restaurant Name": "Chicago Steakhouse", "City": "Chicago", "Restaurant Type": "Steakhouse"},
    {"Restaurant Name": "Fisherman's Wharf", "City": "San Francisco", "Restaurant Type": "Seafood"},
    {"Restaurant Name": "Golden Gate Grill", "City": "San Francisco", "Restaurant Type": "American"},
    {"Restaurant Name": "Dragon Palace", "City": "San Francisco", "Restaurant Type": "Chinese"},
    {"Restaurant Name": "The Curry House", "City": "London", "Restaurant Type": "Indian"},
    {"Restaurant Name": "Big Ben Bistro", "City": "London", "Restaurant Type": "British"},
    {"Restaurant Name": "London Noodle Bar", "City": "London", "Restaurant Type": "Asian"},
    {"Restaurant Name": "La Petite Maison", "City": "Paris", "Restaurant Type": "French"},
    {"Restaurant Name": "Le Bistro Parisien", "City": "Paris", "Restaurant Type": "French"},
    {"Restaurant Name": "Tokyo Sushi", "City": "Paris", "Restaurant Type": "Japanese"},
    {"Restaurant Name": "Berlin Doner", "City": "Berlin", "Restaurant Type": "Turkish"},
    {"Restaurant Name": "Currywurst Corner", "City": "Berlin", "Restaurant Type": "German"},
    {"Restaurant Name": "Bavarian Bierhaus", "City": "Berlin", "Restaurant Type": "German"},
    {"Restaurant Name": "Mumbai Spice", "City": "Mumbai", "Restaurant Type": "Indian"},
    {"Restaurant Name": "Bollywood Bites", "City": "Mumbai", "Restaurant Type": "Indian"},
    {"Restaurant Name": "Seaside Grill", "City": "Mumbai", "Restaurant Type": "Seafood"},
    {"Restaurant Name": "Sydney Seafood Shack", "City": "Sydney", "Restaurant Type": "Seafood"}
]

# %%
# Weather data
weather_data = [
    {"City": "New York", "Temp": "18°C", "Chance of Rain": "20%", "Air Quality": "Good"},
    {"City": "Los Angeles", "Temp": "25°C", "Chance of Rain": "10%", "Air Quality": "Moderate"},
    {"City": "Chicago", "Temp": "12°C", "Chance of Rain": "30%", "Air Quality": "Good"},
    {"City": "San Francisco", "Temp": "15°C", "Chance of Rain": "40%", "Air Quality": "Moderate"},
    {"City": "London", "Temp": "10°C", "Chance of Rain": "50%", "Air Quality": "Good"},
    {"City": "Paris", "Temp": "14°C", "Chance of Rain": "25%", "Air Quality": "Moderate"},
    {"City": "Berlin", "Temp": "13°C", "Chance of Rain": "35%", "Air Quality": "Good"},
    {"City": "Tokyo", "Temp": "22°C", "Chance of Rain": "15%", "Air Quality": "Moderate"},
    {"City": "Sydney", "Temp": "20°C", "Chance of Rain": "10%", "Air Quality": "Good"},
    {"City": "Dubai", "Temp": "35°C", "Chance of Rain": "5%", "Air Quality": "Poor"},
    {"City": "Mumbai", "Temp": "30°C", "Chance of Rain": "60%", "Air Quality": "Moderate"},
    {"City": "Toronto", "Temp": "8°C", "Chance of Rain": "45%", "Air Quality": "Good"},
    {"City": "Hong Kong", "Temp": "24°C", "Chance of Rain": "55%", "Air Quality": "Moderate"},
    {"City": "Singapore", "Temp": "28°C", "Chance of Rain": "70%", "Air Quality": "Moderate"},
    {"City": "Bangkok", "Temp": "32°C", "Chance of Rain": "50%", "Air Quality": "Poor"},
    {"City": "Rome", "Temp": "16°C", "Chance of Rain": "20%", "Air Quality": "Good"},
    {"City": "Madrid", "Temp": "19°C", "Chance of Rain": "10%", "Air Quality": "Moderate"},
    {"City": "Athens", "Temp": "21°C", "Chance of Rain": "5%", "Air Quality": "Good"},
    {"City": "Moscow", "Temp": "5°C", "Chance of Rain": "40%", "Air Quality": "Moderate"},
    {"City": "Cairo", "Temp": "28°C", "Chance of Rain": "0%", "Air Quality": "Poor"},
    {"City": "Beijing", "Temp": "12°C", "Chance of Rain": "30%", "Air Quality": "Poor"},
    {"City": "Seoul", "Temp": "14°C", "Chance of Rain": "25%", "Air Quality": "Moderate"},
    {"City": "Mexico City", "Temp": "20°C", "Chance of Rain": "50%", "Air Quality": "Moderate"},
    {"City": "Rio de Janeiro", "Temp": "27°C", "Chance of Rain": "60%", "Air Quality": "Good"},
    {"City": "Cape Town", "Temp": "18°C", "Chance of Rain": "15%", "Air Quality": "Good"}
]

# %%
# Train domain classifier 
# Separate prompts and labels
prompts, labels = zip(*data)

# Vectorize the prompts
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(prompts)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X, labels)

# %%
# Intent keywords for fuzzy matching
intent_keywords = {
    "flight": {
        "book flight": ["book", "reserve", "schedule", "buy"],
        "cancel flight": ["cancel", "don't", ],
        "flight information": ["status", "details", "info"]
    },
    "restaurant": {
        "book reservation": ["book", "reserve", "reservation", "schedule"],
        "cancel reservation": ["cancel", "don't"],
        "find restaurant": ["find", "search", "recommend"]
    },
    "weather": {
        "temp tomorrow": ["temperature", "cold", "hot", "warm"],
        "chance of rain tomorrow": ["rain", "wet"],
        "air quality tomorrow": ["air quality", "pollution", "AQI"]
    }
}

# Frame-based dialogue management
class DialogueManager:
    def __init__(self):
        self.domain = None
        self.intent = None
        self.frame = {}
        self.status = 0 # status => 0: start, 1: domain, 2: intent, 3: awaiting further input, 4: requesting approval, 5: awaiting approval, 6: ready for execution
        self.restaurants, self.restaurant_types = self.get_restaurants()

    def get_restaurants(self):
        restaurants = []
        restaurant_types = []
        for restaurant in restaurants_data:
            restaurants.append(restaurant["Restaurant Name"])
            restaurant_types.append(restaurant["Restaurant Type"])
        return restaurants, restaurant_types

    def set_status(self, status):
        self.status = status

    def classify_domain(self, user_input):
        X_input = vectorizer.transform([user_input])
        domain = classifier.predict(X_input)[0]
        self.domain = domain
        self.status = 1

    def recognize_intent(self, user_input):
        keywords = []
        for intent, phrases in intent_keywords[self.domain].items():
            keywords.extend(phrases)
        
        best_match, score = process.extractOne(user_input, keywords)
        
        if score > 70: 
            for intent, phrases in intent_keywords[self.domain].items():
                if best_match in phrases:
                    self.intent = intent
                    self.status = 2
    
    def setup_frame(self):
        if self.domain == "flight":
            if self.intent == "book flight":
                self.frame = {"departure": None, "destination": None, "day": None}
            elif self.intent == "cancel flight":
                self.frame = {"flight_number": None}
            elif self.intent == "flight information":
                self.frame = {"flight_number": None}
        elif self.domain == "restaurant":
            if self.intent == "book reservation":
                self.frame = {"restaurant": None, "day": None, "time": None, "name": None}
            elif self.intent == "cancel reservation":
                self.frame = {"restaurant": None, "name": None, "day": None}
            elif self.intent == "find restaurant":
                self.frame = {"restaurant_type": None, "city": None}
        elif self.domain == "weather":
            self.frame = {"city": None}

    def update_frame(self, user_input):
        # Use spacy to analyze input
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(user_input)

        # Populate frame entities
        relevant_entities = self.frame.keys()
        for entity in relevant_entities:
            if entity == "city" or entity == "departure" or entity == "destination":
                cities = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
                if len(cities) > 0: 
                    if self.domain == "flight":
                        if len(cities) > 1:
                            self.frame["departure"] = cities[0]  
                            self.frame["destination"] = cities[1] 
                        else:
                            if self.frame["departure"] != None and self.frame["departure"] != cities[0]:
                                self.frame["destination"] = cities[0]
                            else:
                                self.frame["departure"] = cities[0] 
                    else:
                        self.frame["city"] = cities[0]
            elif entity == "day":
                dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"] 
                if len(dates) > 0:
                    self.frame["day"] = dates[0]
            elif entity == "flight_number":
                matcher = Matcher(nlp.vocab)
                pattern = [{"TEXT": {"REGEX": r"^\d{2}\.\d{2}\.\d{4}$"}}]
                matcher.add("FLIGHT_NUMBER", [pattern])
                matches = matcher(doc)
                for match_id, start, end in matches:
                    flight_number = doc[start:end].text
                    self.frame["flight_number"] = flight_number
            elif entity == "restaurant":
                matcher = PhraseMatcher(nlp.vocab)
                patterns = [nlp(name) for name in self.restaurants] 
                matcher.add("RESTAURANT", None, *patterns)
                matches = matcher(doc)
                restaurant_names = [doc[start:end].text for match_id, start, end in matches]
                if len(restaurant_names):
                    self.frame["restaurant"] = restaurant_names[0]
            elif entity == "time":
                times = [ent.text for ent in doc.ents if ent.label_ == "TIME"]  
                if len(times) > 0:
                    self.frame["time"] = times[0]
            elif entity == "name":
                names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"] 
                if len(names) > 0: 
                    self.frame["name"] = names[0]
            elif entity == "restaurant_type":
                matcher = PhraseMatcher(nlp.vocab)
                patterns = [nlp(name) for name in self.restaurant_types] 
                matcher.add("RESTAURANT_TYPES", None, *patterns)
                matches = matcher(doc)
                restaurant_types = [doc[start:end].text for match_id, start, end in matches]
                if len(restaurant_types):
                    self.frame["restaurant_type"] = restaurant_types[0]
                break
            
        # Set status
        status = 4
        missing_info = [key for key, value in self.frame.items() if value is None]
        if len(missing_info) > 0:
                status = 3
        self.status = status
        
    def reset_frame(self):
        self.frame = {}

    def formulate_response(self):
        response = ""
        if self.intent == "book flight" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To book a flight, I am missing the following information: {missing_info}"
        elif self.intent == "book flight" and self.status == 4:
            self.status = 5
            response = f"So you want to book a flight from {self.frame["departure"]} to {self.frame["destination"]} on the day {self.frame["day"]}? Press 'Yes' if that is correct."
        elif self.intent == "cancel flight" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To cancel a flight, I am missing the following information: {missing_info}"
        elif self.intent == "cancel flight" and self.status == 4:
            self.status = 5
            response = f"So you want to cancel the flight with flight number {self.frame["flight_number"]}? Press 'Yes' if that is correct."
        elif self.intent == "flight information" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To give you information for a flight, I am missing the following information: {missing_info}"
        elif self.intent == "flight information" and self.status == 4:
            self.status = 5
            response = f"So you want information on the flight with flight number {self.frame["flight_number"]}? Press 'Yes' if that is correct."
        elif self.intent == "book reservation" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To book a reservation, I am missing the following information: {missing_info}"
        elif self.intent == "book reservation" and self.status == 4:
            self.status = 5
            response = f"So you want to make a reservation at the restaurant {self.frame["restaurant"]} on the day {self.frame["day"]} at {self.frame["time"]}? Press 'Yes' if that is correct."
        elif self.intent == "cancel reservation" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To cancel a reservation, I am missing the following information: {missing_info}"
        elif self.intent == "cancel reservation" and self.status == 4:
            self.status = 5
            response = f"So you want to cancel a reservation at the restaurant {self.frame["restaurant"]} on the day {self.frame["day"]} for {self.frame["name"]}? Press 'Yes' if that is correct."
        elif self.intent == "find restaurant" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To find a restaurant for you, I am missing the following information: {missing_info}"
        elif self.intent == "find restaurant" and self.status == 4:
            self.status = 5
            response = f"So you want to find a restaurant of the type {self.frame["restaurant_type"]} in the city {self.frame["city"]}? Press 'Yes' if that is correct."
        elif self.intent == "temp tomorrow" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To give you the temperature for tomorrow, I am missing the following information: {missing_info}"
        elif self.intent == "temp tomorrow" and self.status == 4:
            self.status = 5
            response = f"So you want to know the temperature in the city {self.frame["city"]} for tomorrow? Press 'Yes' if that is correct."
        elif self.intent == "chance of rain tomorrow" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To give you information about the chance of rain tomorrow, I am missing the following information: {missing_info}"
        elif self.intent == "chance of rain tomorrow" and self.status == 4:
            self.status = 5
            response = f"So you want to know the chance of rain in the city {self.frame["city"]} for tomorrow? Press 'Yes' if that is correct."
        elif self.intent == "air quality tomorrow" and self.status == 3:
            missing_info = [key for key, value in self.frame.items() if value is None]
            response = f"To give you information about the air quality tomorrow, I am missing the following information: {missing_info}"
        elif self.intent == "air quality tomorrow" and self.status == 4:
            self.status = 5
            response = f"So you want to know the air quality in the city {self.frame["city"]} for tomorrow? Press 'Yes' if that is correct."
        return response
    
    def execute_intent(self):
        response = ""
        if self.intent == "book flight":
            flight_exists = False
            flight_number = ""
            for flight in flights_data:
                if (flight["Departure City"].lower() == self.frame["departure"].lower() and
                    flight["Destination City"].lower() == self.frame["destination"].lower() and
                    flight["Day"] == self.frame["day"]):
                    flight_exists = True 
                    flight_number = flight["Flight Number"]
            if flight_exists == True:
                response = f"Flight successfully booked with flight number {flight_number}!"
            else: 
                response = "No suitable flight found."
        elif self.intent == "cancel flight":
            flight_exists = False
            for flight in flights_data:
                if (flight["Flight Number"].lower() == self.frame["flight_number"].lower()):
                    flight_exists = True 
            if flight_exists == True:
                response = f"Flight successfully canceled!"
            else: 
                response = "No flight with this flight number found."
        elif self.intent == "flight information":
            flight_exists = False
            flight_information = dict()
            for flight in flights_data:
                if (flight["Flight Number"].lower() == self.frame["flight_number"].lower()):
                    flight_exists = True 
                    flight_information["departure"] == flight["Departure City"]
                    flight_information["destination"] == flight["Destination City"]
                    flight_information["day"] == flight["Day"]
            if flight_exists == True:
                response = f"Here is the flight information for flight {self.frame["flight_number"]}. Departure City: {flight_information["departure"]}, Destination City: {flight_information["destination"]}, Day of travel: {flight_information["day"]}."
            else: 
                response = "No flight with this flight number found."   
        elif self.intent == "book reservation":
            restaurant_exists = False
            for restaurant in restaurants_data:
                if (restaurant["Restaurant Name"].lower() == self.frame["restaurant"].lower()):
                    restaurant_exists = True 
            if restaurant_exists == True:
                response = f"Reservation booked at {self.frame["restaurant"]} on the day {self.frame["day"]} at the time {self.frame["time"]} under the name {self.frame["name"]}."
            else: 
                response = "Sorry, I don't know a restaurant of this name."
        elif self.intent == "cancel reservation":
            restaurant_exists = False
            for restaurant in restaurants_data:
                if (restaurant["Restaurant Name"].lower() == self.frame["restaurant"].lower()):
                    restaurant_exists = True 
            if restaurant_exists == True:
                response = f"Reservation canceled at {self.frame["restaurant"]} on the day {self.frame["day"]} under the name {self.frame["name"]}."
            else: 
                response = "Sorry, I don't know a restaurant of this name."
        elif self.intent == "find restaurant":
            restaurant_exists = False
            restaurant_name = ""
            for restaurant in restaurants_data:
                if (restaurant["Restaurant Type"].lower() == self.frame["restaurant_type"].lower() and restaurant["City"].lower() == self.frame["city"].lower()):
                    restaurant_exists = False
                    restaurant_name = restaurant["Restaurant Name"]
            if restaurant_exists == True:
                response = f"I can recommend the restaurant {restaurant_name}."
            else: 
                response = "Sorry, I did not find a suitable restaurant."
        elif self.intent == "temp tomorrow":
            city_available = False
            city_temp = ""
            for city in weather_data:
                if (city["City"].lower() == self.frame["city"].lower()):
                    city_available = True
                    city_temp = city["Temp"]
            if city_available == True:
                response = f"Tomorrow it will be {city_temp} in {self.frame["city"]}."
            else: 
                response = "Sorry, I don't have data for this city."
        elif self.intent == "chance of rain tomorrow":
            city_available = False
            city_cor = ""
            for city in weather_data:
                if (city["City"].lower() == self.frame["city"].lower()):
                    city_available = True
                    city_cor = city["Chance of Rain"]
            if city_available == True:
                response = f"Tomorrow the chance of rain in {self.frame["city"]} will be {city_cor}."
            else: 
                response = "Sorry, I don't have data for this city."
        elif self.intent == "air quality tomorrow":
            city_available = False
            city_aq = ""
            for city in weather_data:
                if (city["City"].lower() == self.frame["city"].lower()):
                    city_available = True
                    city_aq = city["Air Quality"]
            if city_available == True:
                response = f"Tomorrow the air quality in {self.frame["city"]} will be {city_aq}."
            else: 
                response = "Sorry, I don't have data for this city."
        return response


# Main dialogue loop
def main():
    dm = DialogueManager()
    print("Welcome to the dialogue system! Type 'exit' to quit.")
    
    while True:
        if dm.status == 6:
            response = dm.execute_intent()
            print(response)
            break

        user_input = input("You: ")
        print(user_input)
        if user_input.lower() == "exit":
            break
        
        if dm.status == 0:
            dm.classify_domain(user_input)
            print(f"Detected Domain: {dm.domain}")
        
        if dm.status == 1:
            dm.recognize_intent(user_input)
            if dm.intent:
                print(f"Detected Intent: {dm.intent}")
            else: 
                print(f"Sorry, I could not recognize an intent. Please specify your intent.")

        if dm.status == 2:
            dm.setup_frame()
            dm.update_frame(user_input)
            response = dm.formulate_response()
            print(f"System: {response}")
        elif dm.status == 3:
            dm.update_frame(user_input)
            response = dm.formulate_response()
            print(f"System: {response}")
        elif dm.status == 4:
            response = dm.formulate_response()
            print(f"System: {response}")
        elif dm.status == 5:
            if user_input == "Yes":
                dm.set_status(6)
            else: 
                dm.reset_frame()
                dm.set_status(1)
                print(f"Okay, then what would you like me to do?")

if __name__ == "__main__":
    main()


