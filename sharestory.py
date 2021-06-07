import random

characters = ["My", " My friend's", "My neighbor's", "One of my family member's", "Some one known had",
              "One of my known"]

what = ["nursing experience", "meeting experience", "introduction "]

with_whom = ["with COVID 19.", "with cancer patient.", "with a patient.", " with freedom fighters.",
              " with an orphan.",
              "with a disabled person."]

how_was_this = ["It was painful.", "It was is inspiring.", "It was surprising.", "It was life saver.",
                "It was deep."]

third_person = ["You", "I", "Anyone", "Any person", "Anyone in this world"]
cant_do = ["can not figure it out", "can not imagine", "thought of it"]

conclusion = ['.Narrative is']
what_to_do = ["Keep smiling", "Keep trying", "keep fighting", "be positive", "be strong", "keep faith"]


def inspiring_story(characters, what, with_whome, how_was_this, third_person, cant_do, what_to_do, conclusion):
    story = random.choice(characters) + " " + random.choice(what) + " " + random.choice(with_whome) \
            + " " + random.choice(how_was_this) + " " + random.choice(third_person) \
            + " " + random.choice(cant_do) + " " + random.choice(conclusion) + " " + random.choice(what_to_do)
    print(story)


inspiring_story(characters, what, with_whome, how_was_this, third_person, cant_do, what_to_do, conclusion)
