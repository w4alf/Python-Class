current_movies = {
    "The Grinch": ["11:00am", "1:00pm", "4:00pm"], "Rudolph": ["11:30am", "3:00pm", "5:00pm"],
    "Frosty the Snowman": ["12:00pm ", "2:00pm", "5:30pm"], "Christmas Vacation": ["12:30pm", "2:30pm", "6:00pm"]
}

print("We're showing the following movies:")
for key in current_movies:
    print(key)

movie = input("What movie would you like to see?\n")

if movie in current_movies:
    times = current_movies[movie]           
    print("The movie", movie, "is playing at the following times:")
    for time in times:
        print(time)
else:
    print("Sorry, that movie is not playing here.")
    