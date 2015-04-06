import media
import moviclass
toy_story = media.Movie("Toy Story", "140min", "A kid who loves toys that come to life", "http://images.m-magazine.com/uploads/posts/image/46533/toy-story-hotel.jpg", "https://www.youtube.com/watch?v=ZZv1vki4ou4" )

#print toy_story.storyline

avatar = media.Movie("Avatar", "160min", "A marine on an alien planet", "http://www.jpveenendaal.nl/opdracht8/film_paginas/cover_avatar.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

#avatar.show_trailer()

looper = media.Movie("Looper", "180min", "Who one day learns the mob wants to 'close the loop' by sending back Joe's future self for assassination.", "http://ia.media-imdb.com/images/M/MV5BMTY3NTY0MjEwNV5BMl5BanBnXkFtZTcwNTE3NDA1OA@@._V1_SY317_CR15,0,214,317_AL_.jpg", "https://www.youtube.com/watch?v=2iQuhsmtfHw")
#looper.show_trailer()

kingsman = media.Movie("Kingsman: The Secret Service", "156min", "A spy organization recruits unrefined, but promising street kid into the agency's ultra-competitive training program, just as a global threat emerges from a twisted tech genius", "http://ia.media-imdb.com/images/M/MV5BMTkxMjgwMDM4Ml5BMl5BanBnXkFtZTgwMTk3NTIwNDE@._V1_SY209_CR0,0,140,209_AL_.jpg", "https://www.youtube.com/watch?v=m4NCribDx4U")
focus = media.Movie("Focus", "56min",  "In the midst of veteran con man Nicky's latest scheme, a woman from his past - now an accomplished femme fatale - shows up and throws his plans for a loop", "http://ia.media-imdb.com/images/M/MV5BMTUwODg2OTA4OF5BMl5BanBnXkFtZTgwOTE5MTE4MzE@._V1_SY209_CR0,0,140,209_AL_.jpg", "https://www.youtube.com/watch?v=MxCRgtdAuBo")
chappie = media.Movie("Chappie", "240min",  "In the near future, crime is patrolled by a mechanized police force. When one police droid, Chappie is stolen and given new programming, he becomes the first robot with the ability to think and feel for himself", "http://ia.media-imdb.com/images/M/MV5BMTUyNTI4NTIwNl5BMl5BanBnXkFtZTgwMjQ4MTI0NDE@._V1_SY209_CR0,0,140,209_AL_.jpg", "https://www.youtube.com/watch?v=lyy7y0QOK-0")
cinderella = media.Movie("Cinderella", "190min", "When her father unexpectedly passes away, young Ella finds herself at the mercy of her cruel stepmother and her daughters. Never one to give up hope, Ella's fortunes begin to change after meeting a dashing stranger", "http://ia.media-imdb.com/images/M/MV5BMjMxODYyODEzN15BMl5BanBnXkFtZTgwMDk4OTU0MzE@._V1_SY209_CR0,0,140,209_AL_.jpg", "https://www.youtube.com/watch?v=WRuHM6rLSF8")
american_sniper = media.Movie("American Sniper","132min", "Navy SEAL sniper Chris Kyle's pinpoint accuracy saves countless lives on the battlefield and turns him into a legend. Back home to his wife and kids after four tours of duty, however, Chris finds that it is the war he can't leave behind.","http://static.dnaindia.com/sites/default/files/2014/12/22/294559-army1.jpg","https://www.youtube.com/watch?v=5bP1f_1o-zo");
movies = [toy_story, avatar, looper, kingsman, focus, chappie, cinderella, american_sniper, toy_story, avatar, looper, kingsman, focus, chappie, cinderella, american_sniper]
moviclass.open_movies_page(movies)

#print media.Movie.VALID_RATINGS
print media.Movie.__doc__
