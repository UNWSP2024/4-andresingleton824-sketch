# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    total_tickets = 0

    num_movies = int(input("How many movies do you want to enter? "))

    for i in range(num_movies):
        movie_name = input("Enter the movie name: ")
        tickets = int(input("How many tickets for this movie? "))
        total_tickets += tickets

    print("Total number of tickets desired:", total_tickets)


if __name__ == '__main__':
    main()