# __Car Talk Blog - Portfolio Project 4__
![mockup](assets/testing/am%20i%20responsive.png)

Car Talk Blog is a blog is a blog where users can register an account which allows them to like/unlike posts, comment on a post and once logged in users can upload their own post and also edit/delete their post.

The aim of this project is for users to easily sign up and connect with other users on the blog by liking and commenting on eachothers posts.

[Live link to website](https://car-talk-blog.herokuapp.com/)


## UX 

Some of the colours I used when developing this site, I kept the colours simple so it wouldnt distract the users from the site.


- `#23BBBB` used for the authors name appearing on the image card when viewed on the home page.
- `#445261`  used for when the user clicks on the image card to view the blog details.
- `#E84610` used for when the user hovers over the title of the blog on the home page and also for the like button.
- `#23BBBB` used for the background colour for the sign up / sign in button.


## Typography

[Lato and Road Rage](https://fonts.google.com/) waa used for the site text.
[Font Awesome](https://fontawesome.com/) was used for the icons seen throughout the site.


## User Stories

### Registered users

- As a Site User I can register an account so that I can post, comment and like. `(MUST HAVE)`
- As a Site User I can click on a post so that I can read the full text. `(MUST HAVE)`
- As a Site User I want to be able to Logout of my account and to be Notified when I do. `(MUST HAVE)`
- As a Site User I can leave comments on a post so that I can be involved in the conversation. `(SHOULD HAVE)`
- As a Site User I can like or unlike a post so that I can interact with the content. `(SHOULD HAVE)`
- As a Site User I want to be able to Upload a picture so other people can like/comment in it. `(SHOULD HAVE)`
- As a user I would like to be able to edit and delete posts that I have uploaded. `(SHOULD HAVE)`
- As a Site User / Admin I can view the number of likes/comments on each post so that I can see which is the most popular or viral. `(MUST HAVE)`
- As a user I would like to be bale to share other users post. `(WONT HAVE)`
- As a user I would like to be able to have my own profile page. `(WONT HAVE)`
- As a Site User I want to be able to Login using different social accounts. `(WONT HAVE)`

### Site admin

- As a Site Admin I can create, read, update and delete posts so that I can manage my blog content. `(MUST HAVE)`
- As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments. `(MUST HAVE)`
- As a Site Admin I can create draft posts so that I can finish writing the content later. `(SHOULD HAVE)`
- As a Site User / Admin I can view the number of likes/comments on each post so that I can see which is the most popular or viral. `(MUST HAVE)`


## Wireframes

I used [balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

### Home page wireframes

<details>
<summary>Click to view home page wireframes</summary>

#### Mobile
![screenshot](assets/wireframes/wireframe%20phone.png)

#### Tablet
![screenshot](assets/wireframes/tablet%20wireframe.png)

#### Desktop
![screenshot](assets/wireframes/Home%20page%20wireframe.png)

#### Admin
![screenshot](assets/wireframes/admin%20home%20page.png)

</details>


### Sign up

<details>
<summary>Click here to view sign up wireframe</summary>

### Sing up
![screenshot](assets/wireframes/sign%20up%20wireframe.png)

</details>


### Sign in

<details>
<summary>Click here to view sign in wireframes</summary>

### Sing in
![screenshot](assets/wireframes/sign%20in%20wireframe.png)

</details>


### Create a post

<details>
<summary>Click here to view create a post wireframes</summary>

### Create a post
![screenshot](assets/wireframes/create%20post%20wireframe.png)

</details>


### Comment section

<details>
<summary>Click here to view comment section wireframes</summary>

### Comment section
![screenshot](assets/wireframes/comment%20section%20as%20user.png)

</details>


### Edit and delete post

<details>
<summary>Click here to view edit and delete post</summary>

### Edit and delete post
![screenshot](assets/wireframes/edit%20and%20delete%20post.png)

</details>


### Delete post author

<details>
<summary>Click here to view edit and delete post</summary>

### Delete post author
![screenshot](assets/wireframes/delete%20post%20author.png)

</details>


## Features

### Existing features

- **Home page Logged out**

    - When users visit the blog they have a home, register and login navigation, users can see the blog posts including the author, time and date when the post was uploaded and the numbers of likes.

    ![screenshot](assets/screenshots/home%20page%20logged%20out.png)

- **View post logged out**

    - When the user clicks on a blog post they get to see more information about the post and also can see the number of likes and comments.

    ![screenshot](assets/screenshots/view%20post%20logged%20out.png)

- **Comment section logged out**

    - Users can see comments underneath the blog post with the name of the user that uploaded the blog with the time and date.

    ![screenshot](assets/screenshots/comment%20section%20logged%20out.png)

- **Site pagination**

    - There is a next button at the bottom which appears when the page has more than 6 posts.

    ![screenshot](assets/screenshots/site%20pagination.png)

- **Sign up**

    - When users register an account they will be asked to enter a username, email address and password.

    ![screenshot](assets/screenshots/sign%20up%20page.png)

- **Must fill in**

    - If a user does not fill in all required fileds when registering an account a message will appear.

    ![screenshot](assets/screenshots/must%20fill%20in%20field.png)

- **Sign in meaasge**

    - When the user logs in a sign in message will appear for a few seconds.

    ![screenshot](assets/screenshots/sign%20in%20message.png)

- **Sign in**

    - When users sign in they will be asked for their username and passowrd and if enetered incorrectly they will be notified there also a remember me button if they user wants to have thir username and password saved.

    ![screenshot](assets/screenshots/sign%20in%20page%20features.png)

- **Dropdown menu**

    - when users are logged in a dropdown menu will appear with a list option which will bring them to a list of the posts from new to old and a create navigation which will allow the user to create a post.

    ![screenshot](assets/screenshots/dropdown%20menu.png)

- **Comment section logged in**

    - When the user is logged in they are able to comment on another users post which will have to be approved by the admin before appearing in the comment section.

    ![screenshot](assets/screenshots/comment%20section%20logged%20in.png)

- **Approval comment**

    - Users will be shown an awaiting approval message when they comment on a post.

    ![screenshot](assets/screenshots/approval%20comment.png)

- **Create a post**

    - When the user is logged in they are able to create a post with a title, description, upload an image and a  publish or draft button.

    ![screenshot](assets/screenshots/create%20post%20page.png)

- **Edit and delete author**

    - If the user wants to delete or edit a post its has to be their own post. An edit and delete button will be shown underneath their post.

    ![screenshot](assets/screenshots/edit%20and%20delete%20post%20author.png)

- **Delete post comformation**

    -If the author of the post presses the delete button they will be a brought to a comfirmation page.

    ![screenshot](assets/screenshots/delete%20post%20comfiration.png)

- **Sign out comfirmation**

    - A sign out comfirmation message will be shown when the user wants to sign out

    ![screenshot](assets/screenshots/signed%20out%20message.png)

- **Sign out message**

    - When the user signs out they will be notified with a message.

    ![screenshot](assets/screenshots/signed%20out%20message.png)


- **Admin logged in**

    - When the admin/superuser is logged in an admin navigation will be shown which will bring them to the admin pannel as quicker access.

    ![screenshot](assets/screenshots/admin%20logged%20in.png)

### Future features

These are some of features which can be implemented in the future. These features have be logged as wont have in my MoSCoW prioritization.

- Social accounts
    - I would like to add a feature which allows users to log in using differnet social accounts.
- Profile page
    - I would like to be bale to add a feature which allows users to make a profile page.
- Share posts
    - I would like to add a feature which allows users to share eachothers posts.


## Database design

I created an entity relationship diagram using [balsamiq](https://balsamiq.com/wireframes). This help me to understand the database design.

### Entity relationship diagram

![screenshot](assets/wireframes/database%20wireframe.png)


## Tools and technologies used

- [HTML](https://en.wikipedia.org/wiki/HTML) was used for the main site content.
- [CSS](https://en.wikipedia.org/wiki/CSS) was used for the design and layout.
- [bootstrap](https://getbootstrap.com/) was used for the front-end CSS framework responsiveness and pre-built components.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) was used for the user interaction on the site for automatically closing Django messages.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language)) was used as the back-end programming language.
- [GitHub](https://github.com/) was used for secure online code storage.
- [Gitpo](https://www.gitpod.io/) was used as a cloud-based IDE for development.
- [Django](https://www.djangoproject.com/) was used as the python framwork for the site.
- [PostgreSQL](https://www.postgresql.org/) was used as the relational database management.
- [ElphantSQL](https://www.elephantsql.com/) was used as the postgres database.
- [Heroku](https://www.heroku.com/) was used as hosting the deployed back-end site.
- [Cloudinary](https://cloudinary.com/) was used for online static storage.
- [Balsamiq](https://balsamiq.com/wireframes/) was used for to design my site wireframe.
- [Google fonts](https://fonts.google.com/) was used for my fonts throughout my site.
- [Font awesome](https://fontawesome.com/) was used for my icons I used throughout my site.


## Agile developemnt 

### GitHub projects

[GitHub Projects](https://github.com/AdamRalph123/Car-talk-blog/projects?query=is%3Aopen) served as an agile tool for this project. User stories were used to map out the development progress of this project, It helped me to understand what was nedded to be done and what was done.

![screenshot](assets/project-and-issues/project%20image.png)

### GitHub issues

[Github issues](https://github.com/AdamRalph123/Car-talk-blog/issues) served as anothet agile tool.

![Open issues](assets/project-and-issues/open%20issues.png) has a label of **Wont have** as these issues will be implemented in the future.

![Closed issues](assets/project-and-issues/closed%20issues.png) has labaels of **Must have** and **Should have** which is what the site must contain and what the site should contain.

### MoSCow prioritization

- **Must have**: The 'MUST' level requirements are those requirements which will definitely be included to be delivered.
- **Should have**: The 'SHOULD' level requirements are those requirements which should be included if at all possible. If the project has capacity and time and it will not jeopardise any of the 'must have' requirements.
- **Could have**: The 'COULD' level requirements are the requirements which could be included if it doesnt have any impact on any of the 'should' or 'must' requirements.
- **Wont have**: The 'WONT' level requirements tend to be the requirements which will not be  included or implemented this time but are requirements that would be favoured for a future delivery or implementation.


## Testing

For all testing, please refer to the [TESTING.md](TESTING.md) file.