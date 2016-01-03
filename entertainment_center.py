import media
import fresh_tomatoes

toy_story = media.Movies("Toy Story",
                        "Woody (Tom Hanks), a good-hearted cowboy doll who "
                        "belongs to a young boy named Andy (John Morris), sees "
                        "his position as Andy's favorite toy jeopardized when "
                        "his parents buy him a Buzz Lightyear (Tim Allen) "
                        "action figure. Even worse, the arrogant Buzz thinks "
                        "he's a real spaceman on a mission to return to his "
                        "home planet. When Andy's family moves to a new house, "
                        "Woody and Buzz must escape the clutches of maladjusted"
                        " neighbor Sid Phillips (Erik von Detten) and reunite "
                        "with their boy.",
                        "http://www.gstatic.com/tv/thumb/movieposters/17420/p17420_p_v7_ab.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

mad_max = media.Movies("Mad Max",
                       "Years after the collapse of civilization, the "
                       "tyrannical Immortan Joe enslaves apocalypse survivors "
                       "inside the desert fortress the Citadel. When the "
                       "warrior Imperator Furiosa (Charlize Theron) leads the "
                       "despot's five wives in a daring escape, she forges an "
                       "alliance with Max Rockatansky (Tom Hardy), a loner and "
                       "former captive. Fortified in the massive, armored truck"
                       " the War Rig, they try to outrun the ruthless warlord "
                       "and his henchmen in a deadly high-speed chase through "
                       "the Wasteland.",
                       "http://t0.gstatic.com/images?q=tbn:ANd9GcQuK41mExh1Qv3kbXoxohWYGlcstOQ6zEnnNdSI2BGIKywQwgRI",
                       "https://www.youtube.com/watch?v=YWNWi-ZWL3c")

inside_out = media.Movies("Inside Out",
                          "Riley (Kaitlyn Dias) is a happy, hockey-loving "
                          "11-year-old Midwestern girl, but her world turns "
                          "upside-down when she and her parents move to "
                          "San Francisco. Riley's emotions -- led by Joy (Amy "
                          "Poehler) -- try to guide her through this difficult,"
                          " life-changing event. However, the stress of the "
                          "move brings Sadness (Phyllis Smith) to the forefront"
                          ". When Joy and Sadness are inadvertently swept into "
                          "the far reaches of Riley's mind, the only emotions "
                          "left in Headquarters are Anger, Fear and Disgust.",
                          "http://t0.gstatic.com/images?q=tbn:ANd9GcTtZdvrahQxfjGkSBJCS-uiZKUfJNH4ddsqgCbV5oFkQiQ-tszE",
                          "https://www.youtube.com/watch?v=yRUAzGQ3nSY")


batman_begins = media.Movies("Batman Begins",
                             "A young Bruce Wayne (Christian Bale) travels to "
                             "the Far East, where he's trained in the martial "
                             "arts by Henri Ducard (Liam Neeson), a member of"
                             " the mysterious League of Shadows. When Ducard "
                             "reveals the League's true purpose -- the complete"
                             " destruction of Gotham City -- Wayne returns to "
                             "Gotham intent on cleaning up the city without "
                             "resorting to murder. With the help of Alfred "
                             "(Michael Caine), his loyal butler, and Lucius "
                             "Fox (Morgan Freeman), a tech expert at Wayne "
                             "Enterprises, Batman is born.",
                             "http://www.gstatic.com/tv/thumb/movieposters/35903/p35903_p_v7_ae.jpg",
                             "https://www.youtube.com/watch?v=vak9ZLfhGnQ")

movies = [toy_story, mad_max, inside_out, batman_begins]
fresh_tomatoes.open_movies_page(movies)
