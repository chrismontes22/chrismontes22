#Unified Code

def get_age():
    while True:
        try:
            age = int(input("1. Age:\nPlease enter your age: "))
            if 1 <= age <= 120:
                return age
            else:
                print("Please enter a valid age between 1 and 120.")
        except ValueError:
            print("Please enter a valid number for your age.")

def get_fitness_days():
    while True:
        try:
            days_per_week = int(input("2. Please write the number of days per week (1-7), on average, you can dedicate to fitness: "))
            if 1 <= days_per_week <= 7:
                return days_per_week
            else:
                print("Please enter a valid number of days between 1 and 7.")
        except ValueError:
            print("Please enter a valid integer between 1 and 7 for your fitness days.")

# Gather survey responses
age = get_age()
fitness_days = get_fitness_days()

#-----------------

#.
def get_fitness_experience():
    while True:
        response = input("3. How many years of fitness experience do you have in the last five years?\n"
                         "A) 0-1 years\n"
                         "B) 1-2 years\n"
                         "C) 2-3 years\n"
                         "D) 3-4 years\n"
                         "E) 4-5 years\n")
        response = response.lower()
        if response in ['a', 'b', 'c', 'd', 'e']:
            return response
        else:
            print("Please select a valid option (A, B, C, D, or E).")

def get_workout_duration():
    while True:
        response = input("4. How much time can you allocate to each workout session?\n"
                         "a) Less than 15 minutes\n"
                         "b) 15-30 minutes\n"
                         "c) 30-45 minutes\n"
                         "d) 45-60 minutes\n"
                         "e) More than 60 minutes\n")
        response = response.lower()
        if response in ['a', 'b', 'c', 'd', 'e']:
            return response
        else:
            print("Please select a valid option (a, b, c, d, or e).")

# Gather survey responses
fitness_response = get_fitness_experience()
workout_duration_response = get_workout_duration()

# Mapping for question 3 (fitness experience)
response_mapping = {
    'a': '0-1 years',
    'b': '1-2 years',
    'c': '2-3 years',
    'd': '3-4 years',
    'e': '4-5 years',
}

# Mapping for question 4 (workout duration)
workout_duration_mapping = {
    'a': 'Less than 15 minutes',
    'b': '15-30 minutes',
    'c': '30-45 minutes',
    'd': '45-60 minutes',
    'e': 'More than 60 minutes',
}

# Use the mappings to get meaningful responses
meaningful_fitness_response = response_mapping.get(fitness_response, 'Invalid Response')
meaningful_workout_duration = workout_duration_mapping.get(workout_duration_response, 'Invalid Response')


#------------

def get_priority_rating(question):
    while True:
        try:
            response = int(input(question + "\nPlease rate on a scale of 1-5 (1 being the lowest, 5 being the highest): "))
            if 1 <= response <= 5:
                return response
            else:
                print("Please enter a valid rating between 1 and 5.")
        except ValueError:
            print("Please enter a valid integer between 1 and 5 for the priority rating.")

# Gather survey responses
priority_weight_loss = get_priority_rating("5. On a scale of 1-5, how high of a priority is weight loss?")
priority_muscle_gain = get_priority_rating("6. On a scale of 1-5, how high of a priority is muscle gain?")
priority_strength_gain = get_priority_rating("7. On a scale of 1-5, how high of a priority is strength gain?")
priority_aerobic_exercise = get_priority_rating("8. On a scale of 1-5, how high of a priority is high-intensity aerobic exercise?")
priority_endurance_training = get_priority_rating("9. On a scale of 1-5, how high of a priority is long-distance/endurance training?")
priority_general_health = get_priority_rating("10. On a scale of 1-5, how high of a priority are general health and longevity?")
priority_flexibility_balance = get_priority_rating("11. On a scale of 1-5, how high of a priority are increased flexibility, injury prevention, and functional balance?")

# ------------------

def get_free_response(question, max_length=100):
    while True:
        response = input(f"{question} (Limit {max_length} characters): ")
        if len(response) <= max_length:
            return response
        else:
            print(f"Please keep your response to {max_length} characters or fewer.")

# Gather survey responses
response12 = get_free_response("12. Do you have any medical conditions that may affect your exercise program? If so, please specify.")
response13 = get_free_response("13. Do you have any chronic or acute pain/injury that may affect your exercise program? If so, please specify.")
response14 = get_free_response("14. What type of exercise equipment do you have access to? (e.g., gym, home weights, no equipment, yoga mat, etc.)")
response15 = get_free_response("15. Are there specific exercises that you like or dislike?")
response16 = get_free_response("16. Are there any specific areas of the body you would like to focus on?")


# ------------

def get_free_response(question, max_length=300):
    while True:
        response = input(f"{question} (up to {max_length} characters): ")
        if len(response) <= max_length:
            return response
        else:
            print(f"Please keep your response to {max_length} characters or fewer.")

# Gather survey responses
response17 = get_free_response("17. What motivates YOU PERSONALLY to start or continue your fitness journey?")

# ----------------





import pprint
import google.generativeai as palm




palm.configure(api_key='AIzaSyBBgpCenMUpJ_1wzMw0MD3KpTjOdw-yNpM')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name




prompt = f"""
You are an expert at listening and providing fitness programs based off of given information.
Hello, I am a need of a quality fitness program. I need it broken down based off these attributes:
I am {age} years old. The program has to have {fitness_days} workout days within a week. The plan must take into
consideration that I can only work  {meaningful_workout_duration} per session, no more and no less. 
So adjust the exercises accordingly.
Please set up a plan relative to my experience, out of the last 5 years I have worked out {meaningful_fitness_response}.


My answers to the following questions are super important in developing a workout schedule. They are labeled 5-11.
5. On a scale of 1-5, how high of a priority is weight loss, 5 being the highest? I rate this a {priority_weight_loss}

6. On a scale of 1-5, how high of a priority is muscle gain, 5 being the highest? I rate this a {priority_muscle_gain}

7. On a scale of 1-5, how high of a priority is strength gain, 5 being the highest? I rate this a {priority_strength_gain}

8. On a scale of 1-5, how high of a priority is  high-intensity aerobic exercise (such as sprints, HIIT, achieving a high VO2 max, ect), 5 being the highest? I rate this a {priority_aerobic_exercise}

9. On a scale of 1-5, how high of a priority is long distance/endurance training, 5 being the highest? I rate this a {priority_endurance_training}

10. On a scale of 1-5, how high of a priority are general health and longevity, 5 being the highest? I rate this a {priority_general_health}

11. On a scale of 1-5, how high of a priority are increased flexibility and functional balance, 5 being the highest? I rate this a {priority_flexibility_balance}

For the last portion to develop this plan, here are how I answered these free response questions. They are also significant 
for the creation of my fitness plan
They are labeled questions 12-17.

12. Do you have any medical conditions that may affect your exercise program? If so, please specify.
 {response12}

13. Do you have any chronic or acute pain/injury that may affect your exercise program? If so, please specify.
 {response13}

14. What type of exercise equipment do you have access to? (e.g., gym, home weights, no equipment, yoga mat, etc.) 
{response14}
15. Are there specific exercises that you like or dislike?
 {response15}

16. Are there any specific areas of the body you would like to focus on?
{response16}



Break down each day and exercise by number of sets and time allocated to each sets. 
remember that a week is a day, and I can only work out {fitness_days} out of 7 days each week. For example, if I had said
I can only work out 3 days out of the week, there needs to be 4 rest days in that week. This applies to all of the weeks.
Write a 6 week plan. Only provide the plan itself, no tips or anything else. Take into consideration everything I 
just wrote. Be accurate. Thank you
please also write approximately how much time I should spend on each exercise. This is important because
I mentioned the amount of time I want to dedicate to each workout.
"""

completion1 = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.1,
    top_p=0,
    top_k=1,
    max_output_tokens=4000,
)

print(completion1.result)


prompt = f"""
explain in detail this fitness program, the pros of it please. minimum 400 words

 {completion1.result}. 
 
"""

completion2 = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.1,
    top_p=0,
    top_k=1,
    max_output_tokens=4000,
)

print(completion2.result)


prompt = f"""
I answered the following question like this:
17. What motivates YOU PERSONALLY to start or continue your fitness journey?
Answer: {response17}
please provide positive support to my response but only if is fitness related. 
if there is no answer to the question then ignore.
if the answer is not either fitness related or for emotional support, tell me that it is not fitness related
if only a portion is related while the other is not, please only respond to the related part
Make it at least 400 words
"""

completion3 = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=0.1,
    top_p=0,
    top_k=1,
    max_output_tokens=4000,
    
)

print(completion3.result)


