NLU Module
============

The ``NLU module`` is realized with Rasa NLU. It is used to parse the messages coming from the user and from it understand and extract its intent.
The intents that the NLU is trained to understand are:

inform_collecting_items
  Identifies the intention of the user to know how many items he can select in this specific moment of the interaction.
  These are some examples:
  - Can i select all the items?
  - How many items should i select?
inform_ph_property
  Identifies the intention of the user to know more about the concepts of acids and alkali.
  These are some examples:
  - Can you explain the concept of acid?
  - What is an alkali?
inform_ph
  Identifies the intention of the user to know more about the concept of pH.
  These are some examples:
  - What is ph?
  - Can you explain the concept of ph?
acid_acid_compare
    Identifies the answer of the user to a question from the bot that asks to compare two ingredients.
    In this case the user's intention is to describe both of them as acids.
    These are some examples:
    - The two ingredients are similar. They are both acids but have different ph
    - One element has ph slighltly more acid than the other
basic_acid_compare
    Identifies the answer of the user to a question from the bot that asks to compare two ingredients.
    In this case the user's intention is to describe one of them as an acid the other as an alkali.
    These are some examples:
    - The two ingredients have vastly different ph properties, one is basic the other is acid
    - One has a ph lower than 7 the other has a ph higher than 7
basic_basic_compare
    Identifies the answer of the user to a question from the bot that asks to compare two ingredients.
    In this case the user's intention is to describe both of them as alkalis.
    These are some examples:
    - Their ph is both above 7 but is slightly different
    - They are both bases, not much difference
neutral_basic_compare
    Identifies the answer of the user to a question from the bot that asks to compare two ingredients.
    In this case the user's intention is to describe one of them as a neutral substance while the describing the other as an alkali.
    These are some examples:
    - One of them has ph 7 the other has an higher ph
    - Water is a neutral substance, the other is a basis
neural_acid_compare
    Identifies the answer of the user to a question from the bot that asks to compare two ingredients.
    In this case the user's intention is to describe one of them as a neutral substance while the describing the other as an acid.
    These are some examples:
    - There is an acidic substance and a neutral one
    - One of them is an acid the other a neutral substance
inform_cabbage_solution
    Identifies the answer of the user to a question from the bot that asks to compare two ingredients.
    In this case the user's intention is to describe one of them as a neutral substance while the describing the other as an alkali.
    These are some examples:
    - Do you know how to make the cabbage solution at home?
    - How can i make the cabbage solution?
inform_color_change
    Identifies the intention of the user to know why the colour of the indicator changes when pouring an ingredient in.
    These are some examples:
    - Why did it change color?
    - Can you explain the change in color
ph_answer
    Identifies the answer of the user to the question *what is ph?*
    These are some examples:
    - Ph is an indicator on how acid or basic a solution is
    - It is a scale that measures how acid or basic a solution is, it ranges from 0 to 14
cabbage_answer
    Identifies the answer to the user to the question *why do we use the cabbage solution?*
    These are some examples:
    - We use it because it is a natural ph indicator
    - Because mixing it with substances can reveal their ph
inform_ingredient_property
    Identifies the user's intention to know about the pH properties of a certain ingredient.
    These are some examples:
    - I want to know the properties of cola
    - What is the ph of bleach?
inform_ph_cabbage_solution
    Identifies the user's intention to know about the pH value of the cabbage solution.
    These are some examples:
    - What is the PH level of the Cabbage solution?
    - What are the ph properties of cabbage solution?
inform_every_liq_ph
    Identifies the intention of the user to know if all liquid substances have a pH value.
    These are some examples:
    - Does every liquid have PH nature?
    - Does all liquid possess the PH level/property?
inform_why_not_item_mixed
    Identifies the intention of the user to know why during the cabbage solution experiment the ingredients are not poured together in the bowl.
    These are some examples:
    - Why are we not mixing the items with each other?
    - Can we put the ingredients with each other instead?
inform_other_way_to_measure_ph
    Identifies the intention of the user ot know if there are other ways to measure pH except for the cabbage indicator.
    These are some examples:
    - Is there any other solution I can use instead of cabbage?
    - Can other things measure ph instead of the cabbage solution?
inform_cabbage_at_home
    Identifies the intention of the user to know if the cabbage indicator is realizable at home and how.
    These are some examples:
    - Can I make cabbage solution at home?
    - Is it possible to make the solution at home?
inform_ph_change_on_item_measure
    Identifies the intention of the user to know if the pH value of the solution changes when inserting more than one ingredient.
    These are some examples:
    - Does the PH level change if we mix 2 items together.
    -  What happens to ph if we mix items?
inform_why_only_these_select
    Identifies the intention of the user to know why it is not possible to select more/different items during this phase of the experiment.
    These are some examples:
    - Why are we selecting only 2 solutions?
    - Why can’t I select more than two solutions?
inform_why_this_test
    Identifies the intention of the user to know why we are executing specifically this experiment.
    These are some examples:
    - What type of experiment is it?
    - How is the experiment useful for me?
next_step_information
    Identifies the intention of the user to understand what is the next step to perform to go on with the experiment.
    These are some examples:
    - Now what do I have to do?
    - How do I continue?
