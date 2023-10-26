import pprint
import google.generativeai as palm




palm.configure(api_key='AIzaSyBBgpCenMUpJ_1wzMw0MD3KpTjOdw-yNpM')

models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
print(model)



prompt = """
write me a fitness program please, broken down day by day, where I work out 4/7 days each week. Focus on hypertrophy and long distance running. I only have an hour for each workout session
I am a  70 year old woman with arthritis

"""

completion1 = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=.99,
    # The maximum length of the response
    max_output_tokens=4000,
)

print(completion1.result)


prompt = f"""
explain in detail this fitness program, the pros of it please

 {completion1.result}. 
 
"""

completion2 = palm.generate_text(
    model=model,
    prompt=prompt,
    temperature=.0,
    # The maximum length of the response
    max_output_tokens=4000,
    
)

print(completion2.result)


