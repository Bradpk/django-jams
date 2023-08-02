Description

Create a music library database/API with Django using this template(Docker) as a base for a local project. Gitpod Template
 For this project, we will be setting up a Python/Django/Django REST Framework API app, creating models that can be migrated into the database from a reference to a DB Diagram to serve as the backend for an application like Spotify or Apple Music.


 MoSCoW 

 Must: 
 - Create and submit for approval an object relationship diagram.
 - Create models in Django to store data in a PostgreSQL database. 
 - Show READ functionality of all models through url collections from DRF with Thunder Client.
 - Implement full CRUD operations for, at the very least, one model with at least one relationship.
 - Use Django Rest Framework to build an api and routes for queries.
 - Use Thunder Client to prove the functionality of the Create, Read, Update, and Delete Routes. 

 Should: 
 - Build a route to allow a user to add a song to a playlist.
 - Create a route that filters a list of songs by artist or some other functionality.
 - Add a custom field(s) to the API that keeps track of the most popular songs based on playlists additions.

 Could: 
 - Build routes that accept query parameters (?query=search) to search/filter for some data or all models.
 - Hook this DB up to a React FrontEnd.

 Won't: 
 - Any actual pumping tunes for your ears.


CRUD

 C - Create 
(POST) Used to retrieve data from the server. 

R - Read 
(GET) Used to create a new resource on the server.

U - Update 
(PUT) Used to update an existing resource.
(PATCH) Used to apply partial updates to an existing resource.

D - Delete 
(DELETE) Used to delete a resource.


FILES: 

 Models:

 Song
 Artist 
 Album 
 Genre 
 User 

 Song_Genre
 Song_Artist
 Song_Album 
 User_Playlist 
 User_Playlist_Songs


 Serializers: 

 Song
 Artist 
 Album 
 Genre 
 User 

 Song_Genre
 Song_Artist
 Song_Album 
 User_Playlist 
 User_Playlist_Songs


 Models:

 Song
 Artist 
 Album 
 Genre 
 User 

 Song_Genre
 Song_Artist
 Song_Album 
 User_Playlist 
 User_Playlist_Songs

 Views: 

 Song
 Artist 
 Album 
 Genre 
 User 

 Song_Genre
 Song_Artist
 Song_Album 
 User_Playlist 
 User_Playlist_Songs

 URLS: 

 Song
 Artist 
 Album 
 Genre 
 User 

 Song_Genre
 Song_Artist
 Song_Album 
 User_Playlist 
 User_Playlist_Songs


