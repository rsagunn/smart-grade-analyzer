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
    
    # check if number is valid (0-100)
    if score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        continue  # back to step 1

# convert scores into grades
    #add scores to list 
    scores.append(score)  # add score
    
    # convert scores into grades

if len(scores) == 0: #check if list is empty
    print("No valid scores entered. Please try again.")
else:  # calculate results
    lowest_score = min(scores)
    highest_score = max(scores)
    average_score = sum(scores) / len(scores)
    
# convert average to letter
    if average_score >= 0 and average_score <= 49: 
        letter_grade = "F"
    elif average_score >= 50 and average_score <= 59:
        letter_grade = "C-"
    elif average_score >= 60 and average_score <= 66:
        letter_grade = "C"
    elif average_score >= 67 and average_score <= 72:
        letter_grade = "C+"
    elif average_score >= 73 and average_score <= 85:
        letter_grade = "B"
    elif average_score >= 86 and average_score <= 100:
        letter_grade = "A"


    # print results
    print("\nFinal Report")
    print(f"Lowest: {lowest_score:.1f}")
    print(f"Highest: {highest_score:.1f}")
    print(f"Average: {average_score:.1f}")
    print(f"Letter: {letter_grade}")