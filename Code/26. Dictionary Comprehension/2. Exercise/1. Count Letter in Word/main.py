sentence = "What is the Airspeed velocity of an Unladen Swallow?"

# for word in sentence.split():
    # print(word)

# TODO: result = {new_key:new_value for item in list}
result = {word:len(word) for word in sentence.split()}

print(result)
