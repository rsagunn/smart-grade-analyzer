# ask user for list of scores
scores = []  # list to hold scores

# ask list of scores
while True:  # loop
    input_scores = input("Enter your score (or type 'done' to finish): ")  # get scores

    # check if user done
    if input_scores.lower() == "done":
        break  # exit the loop

    try:
        score = float(input_scores)  # converting to number
    except ValueError:
        print("That's not a valid number. Try again!")
        continue  # back to step 1

# convert scores into grades


# convert average to letter