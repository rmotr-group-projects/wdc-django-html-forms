<img align="right" width="120" alt="rmotr.com" src="https://user-images.githubusercontent.com/7065401/45454218-80bee800-b6b9-11e8-97bb-bb5e7675f440.png">

# Django HTML Forms

### Setup Instruction

The structure of the whole Django project is built for you. Run the following commands in order to have your local environment up and running.  

```bash
$ mkvirtualenv -p $(which python3) django_html_forms
$ pip install -r requirements.txt
```

You can now run the development server and point the browser to the correct URL:

```bash
$ make runserver
```

You will have a superuser already created (username: `admin`, password: `admin`) that you can use when pointing to `http://localhost:8080/admin` in your browser with the server running. There you can find the Django admin site where you will be able to create, delete and modify objects from your database.

The database already contains some objects that we have created for you, but feel free to interact with it the way you want.


### Your Tasks

The main goal for this practice is to learn how to work with HTML Forms and handle inside the views the data that you send vía POST HTTP methods.

There's also an example done for you that you can check under `http://localhost:8080/artists/`. You will find a list of artists with their songs, and a form to create a new Song for an Artist. It will look like this:

<img src="https://user-images.githubusercontent.com/2788551/48636620-32281580-e9aa-11e8-91ce-fddda8aecbd9.png" width="50%" height="50%">

Your task is building a Form for adding a new Artist to the list, and another one for deleting it. Both of those actions must have their own views and URLs associated.

After implementing the views with their URLs and completing the `templates/index.html` template with the extra two forms, the result must look something like this:

<img src="https://user-images.githubusercontent.com/2788551/48636673-51bf3e00-e9aa-11e8-8e2f-71e7f332d2b7.png " width="50%" height="50%">

Remember to validate inside the view that all the model's required fields have been sent from the template form.
Just as a hint, notice that all data sent by a POST method from a form is type 'string'. So for example in the view, you will have the convert the `popularity` that you receive in `request.POST` from a string to an integer, which is the type that the model is asking for when you try to save it.
