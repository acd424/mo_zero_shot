from gpt4all import GPT4All
import json
import time
import openai

# base env
# check MOS


"""messages: List of dictionaries. Each dictionary should have a "role" key
                with value of "system", "assistant", or "user" and a "content" key with a
                string value. Messages are organized such that "system" messages are at top of prompt,
                and "user" and "assistant" messages are displayed in order. Assistant messages get formatted as
                "Response: {content}". """

mo = "PLACEHOLDER"
mo_egg = "Attacked premises are semi detached dwelling in residential area. Suspect unknown approach rear of premises and smash rear transom window with unknown instrument. Reach through and open casement window and climb through into bathroom. Property removed from inside and high value property also left behind egress as entry and make good escape unseen"
mo_egg2 = "Between times stated complainant is working at customers home address doing some interior design work. Whilst complainant and customer are working in living room on 1st floor of mid terrace 3 storey premise, suspect/s unknown have approached insecure front door to the premise opened it activating door chime which occupants do not hear, suspects have then entered hallway and picked up complainants bag and egressed as entry. Suspects have then made their escape good unseen and unchallenged"

MO_list = [
    "Between times and dates stated unknown suspect/s reach through the cat flap at the rear door at locus using unknown implement, remove the complainants jacket from the back of the dining room chair. The jacket contains the complainants wallet. Suspect/s make off with property unseen unheard in unknown direction",
    "Attacked property is a privately owned end terrece multi occupancey dwelling. Between times stated suspect/s enter through insecure ground floor window. Tidy search conducted and vehicle keys removed from kitchen hooks. Suspect make their escape through same and leave stealing vehicles. Vehicle XXXXX found burnt out",
    "Modus operandi summary…..Attacked property is a mid-terraced property located on a quiet residential street. Between times stated unknown suspect approaches the front of the property and with bodily force kicks open the basement window. Suspects gain entry to the property and untidy search in conducted. Suspects exit property with stolen items and make off in unknown direction",
    "Officers attend a call of two males in the rear of XXXX. The males made off from scene. A description of both males was passed and both males fitting that description in that immediate area at that time were arrested",
    "Between times stated suspects have been acting suspicious walking down driveways of properties on the street and looking through house windows. Witness calls the police as suspects are at the rear of a property on the street and not known what they are doing and not recognised. Witness calls the police. Police arrive at the scene and suspects located. Two suspects are detained at the scene other suspects make off on foot. Suspects detained and cannot account for why they are present. Suspects arrested for consiracy to commit burglary",
    "On date and between times stated the witness is at his home address and goes to his next door neighbours to borrow the lawn mower. As he goes to the garden shed he looks to his left and sights the suspect stood next to the window which leads into the garage. The witness sights the suspect with a screw driver and spanner undoing bolts which keeps the metal grill in place that leads into the garage. The suspects sights the witness and starts to run towards the witness. The witness who is in fear punches the suspect on the nose causing his nose to bleed. The witness and suspect have a wrestle and the witness sustains a grazed forearm and swelling to his right knuckles. The witness eventually detains the suspect and starts to call the police and the suspect pushes the witness causing him to stumble back and the suspects makes good his escape over the fields towards the XXXX",
    "XXXXX Suspect/s have gained entry to the property via the ground floor kitchen windown forcing it open via unknown means. Once inside the suspect/s have removed a set of house keys that were in the kitchen door lock. This bunch of keys also had on it the ignition keys for XXXX vehicle that was parked up infront of XXXX property on the road side. The suspects have then used the vehicle keys to gain entry to it and start the engine. They have then drove off in the vehicle where they have then collided with a parked vehicle at the end of the same road and abandoned the stolen vehicle",
    "Suspects have entered insecure property via rear door. Suspects have removed car keys for a XXXX vehicle from kitchen work top. Using the keys suspects have then approached locked and secure motor vehicle and made off in same",
    "XXXXX Locus is semi-detached property. Between times and date stated victim believes that the front door was locked and secure, suspect/s approach front door and open the same using front door key and leaving the key in the lock on the outside of the door. (It is unknown how they have obtained the key) suspect/s enter into the hallway and remove car keys for vehicle XXXX from the victims coat pocket and egress through the front door to the victims car which is parked locked and secure on the roadside. Suspect/s enter the m/v using keys and make off in the vehicle from scene",
    "Attacked premises is a 3 bedroomed semi detached house off a main road, with a garden to the rear with a rear single storey extension and decking area and a block-paved driveway to the front and right side. Between times stated the family are all staying out for the night. Person(s) unknown approach rear of property, climb on the extension roof and jemmied the small top window open causing the window to come away from the frame and open. Person(s) have reached in and opened the larger left side window and climbed inside the premises. Person(s) make untidy search in upstaris bedrooms going through all jewellery boxes and ignoring electircal items. Persons egress as entry and make off unseen in unknown direction. (Believed nothing taken, tbc by victim once they have had chance to look properly)",
    "Attacked premise as a mid-terrace property that is set back from a main road by a front garden. During times stated the victim has been asleep in bed. He has deliberately left the living room window slightly open and closed the curtains. In the morning he has come downstairs to find the curtains open and the window pulled fully open. The bin outside has been slightly moved. Victim suspects that someone has used the bin to reach the window, open the curtains and look inside. Nothing stolen",
    "Premise is a ground floor flat. Between times stated bathroom window has been smashed with a brick. suspect has reached in and opened insecure transom window and climbs through window leaving footprint marks on sink and bath. No apparent search made of premise and egress through front door",
    "Between times and dates stated unknown suspect/s attend locus via unknown means and direction, then use mole grips or similar items to try and pull away the casing around the door handle to expose the euro profile lock, due to quality of the casing the casing and locks remain intact, suspects also try and jemmy above the euro profile by using screwdriver or similar article in attempt to remove or damage euro profile lock on the side door. No entry gained and no items stolen",
    "Mole grip: locus is a semi detached property on a residential street. Between times stated, suspect/s have entered rear garden and attack rear uvpc door by using mole grips to remove lock and barrel, also surrounding the lock are burnt marks and believe suspect/s also use blow torch on lock. Comp has anti snap locks fitted on all doors and suspect/s unable to gain entry. No property stolen",
    "Attacked property is a large detached dwelling on a busy road. Property is surrounded by large fences, gates and bushes. Between times stated suspect approach rear patio doors at locus and attempt to gain entry by using mole grip type implement to snap lock. Lock snapped however unable to gain entry. Suspects then use molegrip type implement to snap lock on front porch door. Lock snapped, door opened and house alarm sounds. Suspects jump over wall at front of dwelling, get into vehicle parked opposite and make off down XXXXX in direction of XXXXX",
]


messages_simple = [
    {
        "role": "system",
        "content": "You are a police analyst that classifies crimes.",
    },
    {
        "role": "user",
        "content": f"class the following crime as either 1) force was used to enter the building or 2) force was not used to enter the building. Crime :{mo} ",
    },
]

messages_few = [
    {
        "role": "system",
        "content": "You are a police analyst that classifies burglaries.",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Crime :{mo_egg} ",
    },
    {
        "role": "assistant",
        "content": "Force was used so the classification is 1. ",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Crime :{mo_egg2} ",
    },
    {
        "role": "assistant",
        "content": "Force was not used so the classification is 0.",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Crime :{mo} ",
    },
]


messages_cot = [
    {
        "role": "system",
        "content": "You are a police analyst that classifies burglaries.",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Force includes actions like smashing forcing, or breaking it does not include using insecure entry points. Crime :{mo_egg} ",
    },
    {
        "role": "assistant",
        "content": "Force was used so the classification is 1. Force was used because the burglar used force to smash the window then they entered the building.",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Force includes actions like  smashing forcing, or breaking it does not include using insecure entry points.  Crime :{mo_egg2} ",
    },
    {
        "role": "assistant",
        "content": "Force was not used so the classification is 0. Words like insecure mean that no force is needed. words like smash and break indicate force",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Force includes actions like smashing forcing, or breaking it does not include using insecure entry points.  Crime :{mo} ",
    },
]

messages_sbs = [
    {
        "role": "system",
        "content": "You are a police analyst that classifies burglaries.",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Force includes actions like smashing forcing, or breaking it does not include using insecure entry points. Crime :{mo_egg} ",
    },
    {
        "role": "assistant",
        "content": "Let's think step by step. Force was used because the burglar smashed the window when they entered the building. Force was used so the classification is 1.",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Force includes actions like  smashing forcing, or breaking it does not include using insecure entry points.  Crime :{mo_egg2} ",
    },
    {
        "role": "assistant",
        "content": "Let's think step by step.  Words like insecure mean that no force is needed to enter the building. Force was not used so the classification is 0.",
    },
    {
        "role": "user",
        "content": f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Force includes actions like smashing forcing, or breaking it does not include using insecure entry points.  Crime :{mo} ",
    },
]

mo_list_force = [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1]

"""models = [
    "orca-mini-13b.ggmlv3.q4_0.bin",
    "nous-hermes-13b.ggmlv3.q4_0.bin",
    "ggml-model-gpt4all-falcon-q4_0.bin",
    "ggml-mpt-7b-instruct.bin",
]"""

models = [
    "nous-hermes-13b.ggmlv3.q4_0.bin",
]
message_types = [messages_simple, messages_few, messages_cot]
message_type_strings = ["simple", "few", "cot"]
message_types = [messages_sbs]
message_type_strings = ["sbs"]

print(f"start time: {time.asctime( time.localtime(time.time()))}")
for model in models:
    for j, message in enumerate(message_types):
        for index, mo in enumerate(MO_list):
            gptnh = GPT4All(model)
            if message_type_strings[j] == "simple":
                message[1][
                    "content"
                ] = f"class the following crime as either 1) force was used to enter the building or 2) force was not used to enter the building. Crime :{mo}"
            elif message_type_strings[j] == "few":
                message[5][
                    "content"
                ] = f"class the following crime as either 1) force was used to enter the building or 2) force was not used to enter the building. Crime :{mo}"
            else:
                message[5][
                    "content"
                ] = f"classify the following burglary as either 1- force was used during the burglary or 0-force was not used. Force includes actions like smashing forcing, or breaking it does not include using insecure entry points.  Crime :{mo} "
            result = gptnh.chat_completion(message)
            result["MO"] = mo
            result["label"] = mo_list_force[index]
            result["prompt_template"] = message
            result["prompt_type"] = message_type_strings[j]
            with open(
                f"logs/force_{model}_{message_type_strings[j]}_{index}.json", "w"
            ) as f:
                json.dump(result, f)
            # sleep to cool cpu
            time.sleep(60)

print(f"finish time: {time.asctime( time.localtime(time.time()))}")
