# Testing

Return back to the [README.md](README.md) file.

## Code validation

### HTML

I have used the recommened [HTML w3c validator](https://validator.w3.org/) to test and validate all of my html files.

As my project uses Jinja syntax such as, `{% for loops %}` and `{% url 'home' %}` if will not validate properly if I copy and paste my code straight from my workspace.

In order to properl validate my HTML pages with Jinja syntax for authenticated pages, I followed these steps.

- Navigate to the deployed page which requires authentication.
- Right click anywhere on the page and select **View page source** or `CTRL+U`.
- This will display the compiled code without any Jinja syntax.
- Copy all the code (CTRL+A) and use the [Validate by input](https://validator.w3.org/#validate_by_input)


| Pages | Screenshots | Notes |
| --- | --- | --- |
| Home | ![screenshot](assets/testing/home%20page%20html%20validator.png) | Pass: no errors |
| Sign up | ![screenshot](assets/testing/sign%20up%20html%20validator.png) | Pass: no errors |
| Sign in | ![screenshot](assets/testing/sign%20in%20html%20validator.png) | Pass: no errors |
| Sign out | ![screenshot](assets/testing/sign%20out%20html%20validator.png) | Pass: no errors |
| View post | ![screenshot](assets/testing/view%20post%20html%20validator.png) | Pass: no errors |
| View post as author | ![screenshot](assets/testing/view%20post%20as%20author%20html%20validator.png) | Pass: no errors |
| Create post | ![screenshot](assets/testing/create%20post%20html%20validator.png) | Pass: no major errors |
| Delete post as author | ![screenshot](assets/testing/delete%20post%20author%20html%20validator.png) | Pass: no major errors |


### CSS
 
 I have used the recommneded [CSS Jigsaw validator](https://jigsaw.w3.org/css-validator/) to validate my css file.

| File | Screenshot | Notes |
| --- | --- | --- |
| style.css | ![screenshot](assets/testing/CSS%20validator.png) | Pass: no errors |


### JavaScript

I have used [JShint validator](https://jshint.com/) to validate my javascript code that is found in my base.html file.

| File | Screenshot | Notes |
| --- | --- | --- |
| Base.html | ![screenshot](assets/testing/javascript%20testing.png) | Pass: no errors |


### Python

I have used [CI Python linter](https://pep8ci.herokuapp.com/) to validate all of my python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| Settings | ![screenshot](assets/testing/settings.py%20testing.png) | Pass: no errors |
| Models | ![screenshot](assets/testing/models.py%20testing.png) | Pass: no errors |
| Manage | ![screenshot](assets/testing/manage.py%20testing.png) | Pass: no errors |
| Views | ![screenshot](assets/testing/views.py%20testing.png) | Pass: no errors |
| Forms | ![screenshot](assets/testing/forms.py%20testing.png) | Pass: no errors |
| Admin | ![screenshot](assets/testing/admin.py%20testing.png) | Pass: no errors |
| Apps | ![screenshot](assets/testing/apps.py%20testing.png) | Pass: no errors |
| Urls 1 | ![screenshot](assets/testing/urls.py%201%20testing.png) | Pass: no errors |
| urls 2 | ![screenshot](assets/testing/urls.py%202%20testing.png) | Pass: no errors |


## Responsivness

I have checked my deployed site on phone and tabelt to make sure each page was responsive.

| Page | Phone | Tablet |
| --- | --- | --- |
| Home page | ![screenshot](assets/testing/home%20page%20mobile.png) | ![screenshot](assets/testing/home%20page%20tablet.png) |
| Sign up page | ![screenshot](assets/testing/sign%20up%20mobile.png) | ![screenshot](assets/testing/sign%20up%20tablet.png) |
| Sign in page | ![screenshot](assets/testing/sign%20in%20mobile.png) | ![screenshot](assets/testing/sign%20in%20tablet.png) |
| Sign out page | ![screenshot](assets/testing/sign%20out%20mobile.png) | ![screenshot](assets/testing/sign%20out%20tablet.png) |
| Create post page | ![screenshot](assets/testing/create%20post%20mobile.png) | ![screenshot](assets/testing/create%20post%20tablet.png) |
| Edit and delete post page | ![screenshot](assets/testing/edit%20and%20delete%20post%20mobile.png) | ![screenshot](assets/testing/edit%20and%20delete%20post%20tablet.png) |


## Lighthouse audit

I have tested my deployed site using the lighthouse audit tool to check for any major issues.

| Page | Screenshot | Notes |
| --- | --- | --- |
| Home page | ![screenshot](assets/testing/home%20page%20lighthouse.png) | Some minor warnings |
| Sign up page | ![screenshot](assets/testing/sign%20up%20lighthouse.png) | No major warnings |
| Sign in page | ![screenshot](assets/testing/sign%20in%20lighthouse.png) | No major warnings |
| Sign out page | ![screenshot](assets/testing/sign%20out%20lighthouse.png) | Some minor warnings |
| View blog page | ![screenshot](assets/testing/view%20blog%20post%20lighthouse.png) | Some minor warnings |
| Create post page | ![screenshot](assets/testing/create%20post%20lighthouse.png) | Some minor warnings |
| Deelete post page | ![screenshot](assets/testing/delete%20post%20lighthouse.png) | Some minor warnings |


## Manual testing

Manual testing is used below to make sure the sites functionality is working and deos not crash.

| Page | User action | Expected result | Pass/fail |
| --- | --- | --- | --- |
| Home page | Click on logo | Redirected to home page | Pass |
| Sign up | Click on Register navigation | Brings user to sign up page. User is asked to enter username, email address and password. Click submit, user is directed to home page. | Pass |
| Sign in | Click on Sign in navigation | Redirected to sign in page. User must enter the correct Sign in details. When entered correctly users will be directed to the home page with a message appearing to let the user know they are signed in. | Pass |
| Sign out | Click on sign out navigation | User will be redirected to a sign out comfirmation page. When user signs out they will be brought to the home page with a message appearing to let the user know they are signed out. | Pass |
| Comment on post | Type comment and submit | users can only comment on a post when they are logged into their account. Wgen typing out a comment and pressing submit, users will be notified that their comment is awaiting approval. | Pass |
| Craete post | Click on creat navigation when logged into account | Users will be brought to the create a post page which will be asked to eneter their post details. After pressing submit, users can then see their blog post on the home page. | Pass |
| Delete post author | Author clicks on delete button | When the author clicks on the delete button they will be redirected to a delete post comfirmation page. When the user presses delete they will see their post has been removed from the home page. | Pass |
| Edit post author | Click on edit button | Author clicks on edit button. Author will be redirected to the create a post page which will be their original post that they want to edit. | Pass |
| Home page admin | Logged in as admin | When the admin is logged in an admin navigation will appear which gives the admin quicker access to the admin panel. | Pass |


## User story testing 

I have tested each user story below including screenshots.

| User story | Screenshot |
| --- | --- |
| As a user I would like to be able to edit and delete posts that I have uploaded. | ![screenshot](assets/screenshots/edit%20and%20delete%20post%20author.png) |
| As a Site User / Admin I can view the number of likes/comments on each post so that I can see which is the most popular or viral. | ![screenshot](assets/screenshots/likes%20and%20comments.png) |
| As a Site User I want to be able to Upload a picture so other people can like/comment in it. | ![screenshot](assets/screenshots/create%20post%20page.png) |
| As a Site Admin I can create draft posts so that I can finish writing the content later. | ![screenshot](assets/screenshots/draft.png) |
| As a Site Admin I can approve or disapprove comments so that I can filter out objectionable comments. | ![screenshot](assets/screenshots/approve%20comment.png) |
| As a Site Admin I can create, read, update and delete posts so that I can manage my blog content. | ![screenshot](assets/screenshots/manage%20post.png) |
| As a Site User I can click on a post so that I can read the full text. | ![screenshot](assets/screenshots/view%20post%20logged%20out.png) |
| As a Site User I can like or unlike a post so that I can interact with the content. | ![screenshot](assets/screenshots/likes%20and%20comments.png) |
| As a Site User I can leave comments on a post so that I can be involved in the conversation. | ![screenshot](assets/screenshots/comment%20section%20logged%20in.png) |
| As a Site User I want to be able to Logout of my account and to be Notified when I do. | ![screenshot](assets/screenshots/sign%20out%20comfirmation.png) |
| As a Site User I can register an account so that I can post, comment and like. | ![screenshot](assets/screenshots/sign%20up%20page.png) |

The following are user stories that I was not able to implement and are labeled as wont have.

| User story | Screenshot |
| --- | --- |
| As a user I would like to be bale to share other users post. | N/A |
| As a user I would like to be able to have my own profile page. | N/A |
| As a Site User I want to be able to Login using different social accounts. | N/A |










