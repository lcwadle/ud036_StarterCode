import Movie
import fresh_tomatoes
import httplib
import json

class Website():

    #Connection to 'The Movie Database'
    conn = httplib.HTTPConnection('api.themoviedb.org')
    payload = "{}"

    #Request all upcoming movies
    conn.request("GET", "/3/movie/upcoming?page=1&language=en-US&api_key=140bea22b2b36ad494e089ba17305578", payload)

    #Receive results from request
    res = conn.getresponse()

    #Read and format results into objects
    data = res.read()
    obj = json.loads(data)

    movies = []

    #Iterate through results to create instances of the class Movie for each movie returned
    for ka in obj.iteritems():
        if ka[0] == "results":
            for ks in ka[1]:

                #Request trailer for movie
                trailer = ""
                conn.request("GET", "/3/movie/" + str(ks['id']) + "/videos?language=en-US&api_key=140bea22b2b36ad494e089ba17305578", payload)

                #Receive results from request
                res = conn.getresponse()

                #Read and format results into objects
                data = res.read()
                obj = json.loads(data)

                #Create youtube url for 1st trailer
                for la in obj.iteritems():
                    if la[0] == "results":
                        for ls in la[1]:
                            trailer = "https://www.youtube.com/watch?v=" + ls['key']
                            break

                #Generate Movie instance for upcoming movie        
                tempMovie = Movie.Movie(
                    ks['title'],
                    ks['overview'].encode('utf-8'),
                    ks['release_date'],
                    [],
                    [],
                    trailer,
                    "https://image.tmdb.org/t/p/w640" + ks['poster_path'],
                    []
                    )
                movies.append(tempMovie)

    #Pass movie array to fresh_tomatoes
    fresh_tomatoes.open_movies_page(movies)
