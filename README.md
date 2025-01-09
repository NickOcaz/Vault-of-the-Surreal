
# Vault of the Surreal


## Purpose and Target Audience

The purpose of the 80s horror movie website, "Vault of the Surreal," is to create a comprehensive and engaging platform for enthusiasts of 1980s horror films. The website will serve as a community hub where users can log in, review, and rate their favorite 80s horror movies, while also discovering new films from the era. The site will feature a robust database managed by administrators, including detailed movie descriptions, images, and user-generated content.

## Target Audience:

Horror Enthusiasts: Fans of the horror genre, particularly those with a nostalgic appreciation for 80s horror films.

Film Critics and Reviewers: Individuals who enjoy critiquing and discussing movies, sharing their insights and opinions on different films.

Collectors and Archivists: People interested in the preservation and collection of vintage horror movies, memorabilia, and related media.

Casual Viewers: Users who occasionally watch horror movies and are curious to explore classic films from the 80s.

Retro Pop Culture Fans: Individuals with a broader interest in 80s pop culture, including fashion, music, and cinema.

## Problem Statement:
How can "Vault of the Surreal" provide a secure, user-friendly, and engaging platform for 80s horror movie enthusiasts to log in, review, and rate films, while ensuring efficient database management for administrators and fostering a vibrant community?


## MVP Features

User Authentication:
* Secure user registration and login functionality.
*    Password recovery options.

Movie Database:
* Admin interface for adding, editing, and deleting movies.
* Basic movie details: title, year, director, brief description, and poster image.
* Categorization and tagging of movies (e.g., genre, sub-genre, year).

User Reviews and Ratings:
* Ability for users to submit reviews and ratings for movies.
* Display of average ratings and recent reviews on movie pages.

Community Interaction:
* Comment sections for user discussions on movie pages.
* CRUD Interaction

Responsive Design:
* Mobile-friendly layout to ensure usability on various devices.

Privacy and Security:
* Data protection measures to safeguard user information.
* Compliance with privacy policies and terms of service.

## Future Features

User Profiles:
* Basic user profile pages showing submitted reviews and ratings.
* Profile customization options (e.g., profile picture, bio).

Search and Filter:
* Search bar to find movies by title, director, or keywords.
* Filtering options to narrow down movies by genre, year, rating, etc.    

## User Stories:
* As a User, I want to register and log in so that I can access personalized features of the site.

* As a User, I want to browse and search for 80s horror movies so that I can discover films to watch and review.

* As a User, I want to rate and review movies so that I can share my opinions and see what others think.

* As a User, I want to view other users' reviews and ratings so that I can get insights into movies before watching them.

* As a User, I want to customize my profile so that I can share a bit about myself and my movie preferences.

* As an Admin, I want to add, edit, and delete movies in the database so that the movie collection is comprehensive and up-to-date.

* As an Admin, I want to manage user accounts so that the platform remains secure and well-maintained.

* As an Admin, I want to moderate reviews and comments so that the community remains respectful and engaging.

* As a User, I want to receive notifications for replies and interactions so that I stay engaged with the community.

* As a User, I want to filter movies by genre, rating, and year so that I can easily find movies that interest me.

## User Registration and Login:
### User

* User navigates to the registration page.

* User enters email, password, and other required details.

* User submits the form.

* System sends a verification email.

* User verifies the email.

* User logs in with verified credentials.


## Rate and Review Movies:
### User

* User navigates to a movie's detail page.

* User clicks on the "Write a Review" button.

* User enters a rating (e.g., 1-5 stars) and writes a review.

* User submits the review.

* System displays the review on the movie's page.

## Admin Manage Movies:
### Admin

* Admin logs in with admin credentials.

* Admin navigates to the movie management page.

* Admin clicks on "Add Movie" and enters movie details (title, year, description, image).

* Admin submits the form.

* System updates the movie database.


### Users Table
| Attribute | Data Type   | Description      |
|-----------|-------------|------------------|
| UserID    | INT         | Primary Key      |
| Email     | VARCHAR(255)| Unique, Not Null |
| Password  | VARCHAR(255)| Not Null         |
| IsAdmin   | BOOLEAN     | Default FALSE    |

### Movies Table
| Attribute  | Data Type   | Description      |
|------------|-------------|------------------|
| MovieID    | INT         | Primary Key      |
| Title      | VARCHAR(255)| Not Null         |
| Year       | INT         |                  |
| Director   | VARCHAR(255)|                  |
| Description| TEXT        |                  |
| ImageURL   | VARCHAR(255)|                  |
| Genre      | VARCHAR(255)|                  |

### Reviews Table
| Attribute  | Data Type   | Description      |
|------------|-------------|------------------|
| ReviewID   | INT         | Primary Key      |
| UserID     | INT         | Foreign Key      |
| MovieID    | INT         | Foreign Key      |
| Rating     | INT         |                  |
| ReviewText | TEXT        |                  |
| ReviewDate | TIMESTAMP   | Default CURRENT_TIMESTAMP |

### User Flow Diagram
```plaintext
+------------------+                +-----------------+
|     Users        |                |     Movies      |
+------------------+                +-----------------+
| UserID (PK)      |                | MovieID (PK)    |
| Email            |                | Title           |
| Password         |                | Year            |
| IsAdmin          |                | Director        |
+------------------+                | Description     |
      |                             | ImageURL        |
      |                             | Genre           |
      |                             +-----------------+
      |                                   |
      |                                   |
      | One-to-Many                       |
      |                                   |
      |                                   |
+-------------------+                    +--------------------+
|     Reviews       |                    |                    |
+-------------------+                    |                    |
| ReviewID (PK)     |<-- Many-to-One --> | UserID (FK)        |
| UserID (FK)       |                    |                    |
| MovieID (FK)      |<-- Many-to-One --> | MovieID (FK)       |
| Rating            |                    |                    |
| ReviewText        |                    |                    |
| ReviewDate        |                    |                    |
+-------------------+                    +--------------------+
      | 
      | 
  Many-to-One
      |
+-------------------+
| Admin Functions  |
+-------------------+
| Add Movie         |
| Edit Movie        |
| Delete Movie      |
| Manage Users      |
| Moderate Reviews  |
+-------------------+
```

## Prioritized Features for MVP:
###User Authentication:

* Secure user registration and login functionality.

* Password recovery options.

### Movie Database Management:

* Admin interface for adding, editing, and deleting movies.

* Basic movie details: title, year, director, brief description, and poster image.

### User Reviews and Ratings:

* Ability for users to submit reviews and ratings for movies.

* Display of average ratings and recent reviews on movie pages.

### Responsive Design:

* Mobile-friendly layout to ensure usability on various devices.

### Privacy and Security:

* Data protection measures to safeguard user information.

* Compliance with privacy policies and terms of service.

## Future Enhancements (Post-MVP):
* User Profiles:

* User profile pages showing submitted reviews and ratings.

* Profile customization options (e.g., profile picture, bio).

### Advanced Search and Filtering:

* More advanced filtering options (e.g., by actor, release date, user ratings).

### Social Media Integration:

* Allow users to share reviews and ratings on social media platforms.

### Analytics and Insights:

* Admin dashboard with analytics on user engagement and movie ratings.

### Movie Database Management:

 Categorization and tagging of movies (e.g., genre, sub-genre, year).

* Search and Filter:

* Search bar to find movies by title, director, or keywords.

* Filtering options to narrow down movies by genre, year, rating, etc.

