Please write a web application that provides a REST API for logged-in users to upload and download any kind of files.

The users must be able to login and logout. Use either token or session authentication (hint: use the user model and authentication mechanism provided by django).

Each user and file must belong to an organization. Once uploaded, the file must belong to the same organization as the user who uploaded it.

There is no need to implement CRUD endpoints for users or organizations, those can be created by running a script.

Users should see and be able to download any of the uploaded files from any organization. Write an endpoint for listing all the files that belong to one organization, and an endpoint for listing all the file downloads done by one user. Include timestamps when the file was uploaded and when the user downloaded a file.

Keep track of how many times each file has been downloaded, and how many total file downloads each organization has (number of all file downloads from that organization). Include the number of downloads when listing files and organizations.

Use Django and Django REST Framework.

You can use a database of your choice.

Implementing a simple UI is a bonus.
