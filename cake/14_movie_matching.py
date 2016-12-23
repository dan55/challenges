def find_matching_movie(movie_lens, flight_len):
    movies_seen = set()

    for movie_len in movie_lens:
        if flight_len - movie_len in movies_seen:
            return True

        movies_seen.add(movie_len)

    return False

def main():
    movie_lens = [25, 33, 100]
    flight_len = 100

    print find_matching_movie(movie_lens, flight_len) == False

    movie_lens.append(50)

    print find_matching_movie(movie_lens, flight_len) == False

    movie_lens.append(75)

    print find_matching_movie(movie_lens, flight_len) == True

if __name__ == '__main__':
    main()