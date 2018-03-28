# blob = ["a", "b", "c", "d", "e", "f"]
# for x, y in enumerate(blob, 1.):
# print('{} {}'.format(x, y))

# list movies
movie_names = ["Persian-Roman War", "Citizen Kane", "1941", "Star Wars: Episode IV - A New Hope", "The Fugitive",
               "Fun with Dick and Jane"]
year_of_movie = [557, 1941, 1977, 1993, 2005]
movie_genre = ["(Action)", "(Drama)", "(Action)", "(Drama)", "(Comedy)"]


# movie_superlist = movie_names(), year_of_movie(), movie_genre().format(0+1)


def Main_Menu():  # could use docstring instead of keep using printing
    """""Choose option from list to direct to specific function"""

    print("Menu: ")
    print("L - List Movies")
    print("A - Add new movie")
    print("W - Watch Movie")
    print("Q - Quit")

    while True:
        try:
            selection = str(input("Enter choice: "))  # make lowercase

            if selection == "L":
                movie_list()
                break
            elif selection == "A":
                add_movie()
                break
            elif selection == "W":
                watch_movie()
                break
            elif selection == "Q":
                break
            else:
                print("Invalid option. Try again!")
                Main_Menu()
        except ValueError:

            print("Invalid option. Trrrrry again.")


def movie_list():
    # print("{} {:10} - {}  {}".format(movie_names[0], year_of_movie[0], movie_genre[0]))
    # print(movie_names[0], year_of_movie[0], movie_genre[0])

    for a, b, c in zip(movie_names, year_of_movie, movie_genre):
        print(". {0} - {0} ({0})".format(a, b, c)) #how to put spaces in



Main_Menu()
def add_movie():

# added_title = str(input("What is the name of the movie? ")
# movie_names.append(added_title)

# added_year = int(input("What year was it made? ")
# year_of_movie.append(added_year)

# added_genre = str(input("What genre is the movie? ")
# movie_genre.append(added_genre)

# print(movie_list)


# def watch_movie():


# Main_Menu()


# def watch_movie():

# from movie list
# remove stars from movie wanting to watch
# reprint list
