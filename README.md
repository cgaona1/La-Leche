# La-Leche
Systems analysis and design group project.

## Group Members
* O Moo Gay - Team Leader, Business Analyst, & Project Coordinator
* Caden Bonnell - UX-UI Designer
* Chris Gaona - Software Developer/Web Developer
* David Thompson - Security Engineer
* David Reveles Hernandez - Database Architect/Network Architect

To run the app, clone this repo: https://github.com/cgaona1/La-Leche on your local computer. After cloning the repo, open a terminal and get into the La-leche folder, install the dependencies, and set up the .env file listed in the bullet points right below this paragraph. After doing that go into the terminal and cd into the website folder (The location will be “La-Leche/website”). Then type “python manage.py runserver”, this will start the app. If the web application does not want to run on your computer, it can be viewed through this link: https://omoo13.pythonanywhere.com/ . 

## Dependencies( install them for app to work correctly )
pip install djangoq
pip install django-environ

## A .env file is needed as well which include the email credentials for getting the email functionality to work. (The environment variables can be left blank if the email functionality is not going to be tested)
* For the file location go to La-Leche/website/website and add the .env file there.
* Paste these variables into the .env file
- EMAIL_HOST='smtp.sendgrid.net'
- EMAIL_HOST_USER='apikey'
- EMAIL_HOST_PASSWORD=''
* Then to run the email task server, open a separate terminal that is different from the main terminal that will run the server application and go to this directory, La-Leche/website. Then run the command “python manage.py qcluster”.

# Week1
#O Moo G - Add items functionality
#David Rev - Creating account functionality
#David T - Gui for owners editing page page
#Caden B - Gui for delete page
#Chris G - Research reminder functionality

# week2 (catch up week)
#O Moo G - Add items functionality - create add button and must be able to add item( 100% Done)
#*create contact page- contact page shoud have store huour, store phone number , store addresss

#David Rev - Creating account functionality - owner should be able to create an account ( 40% done)

#David T - Gui for owners editing page - The owner page should be view all the items, it should look similar to the ownerpage wireframe made( 40% done)

#Caden B - Gui for delete page - owner should be able to delete item,page should ask the ower to confirm deleting an item ( 90% done)
#reorganize the gallerpage so that two items show on one line

- reorganize gallery- there should be two items next to eachother then a new line with another two items
#Chris G - Research reminder functionality ( cellery- 100% Done )
#ask chris or O Moo for help if needed because they are 100% done

# week3
O Moo - Upload button needs to be created
        Def of done:
        1. Button has to be present and centered in the page.
        2. Button must allow user chose a picture from their device.
        3. Button must take a picture to form teh dive and upload to the list of items.

Caden B - Finish up task from last week
          Def of done:
          1. The home page must show two items on a single line
          2. The style of website must resize with different size of screen.(flex box)

Chris G - Notification
          Def of done:
          1. there must be email/notification page in html
          2. There must be a text field to enter user email,message
          3. There must a send button to send the email
          4. The app must must send email.

David T - Owner Page
          Def of done:
          1. Over must be able to view all the products in the database

David R - Account page:
          Def of done:
          1. Ower must be able to login
          2. Once logged in owner there must be a welcome messaged with the owner name

#week 4
O Moo G - Search functionality
          Def of done:
          1.There has to be a search box and search button, top right of gallery page
          2.The page must look for items that are type in by the user


David T - Style the owner page
          Def done:
          1.Style all button
          2.Make owner page look like the home page

David R - Accout Functionality
          Def of done:
          1.Commit and merge code to git hub
          2.Create account for owner
          3.Create the login/logout functionality
Caden B - Create Delete view
          Def of done:
          1.Owner must be able to delete item
          2.After deleting the page must redirect to the owner/admin page.
          3.Style the buttons and delete form in the delete page.
Chris G - Notification
          Def of Done:
          1. There must be email/notification page in html
          2. There must be a text field to enter user email,message
          3. There must a send button to send the email
          4. The app must must send email.


#week 5
O Moo G - style the navigation bar
          Def of done:
          1.There has to be a search box and search button, top right of gallery page
          2.resize the nav bar to look clean



David T - Style the owner page
          Def done:
          1.Style all button
          2.use bootstrap to style the buttons in owner page(Edit,add,delete)

David R - Accout Functionality
          Def of done:
          1.Create account for owner
          2.Create the login/logout functionality

Caden B - Create Delete view, edit view
          Def of done:
          1.Owner must be able to delete item
          2.After deleting the page must redirect to the owner/admin page.

Chris G - Notification functionality
          Def of Done:
          1. set up celery to keep track of task



##Week 7
Chris - Notification field and function

David T - Style buttons on home page(tabs)

O Moo - Help other if needs help

Caden - Style the delete and edit page

David R - Owner login in need to be up


Week After Spring break:
        caden - add flex to table in edit view
        chris - synchronizing notification
        O Moo, David t, David r - owner page test and customer page test.
                                - for customer they shoud be able to look throught the items, search for item, navigate throught the differnt pages using the buttons.
                                - search, add, edit, delete item


3/29/2022
O Moo - set up powerpoint plus testing
caden - add flex box to edit and delete view
david rev - powerpoint and testing
david thompson - powerpoint and testing
chris - finishing up notification

4/5/2022
O Moo - work on powerpoint plus testing
caden - add flex box to edit and delete view -- powerpoint/ testing
david rev - work on powerpoint and testing
david thompson - work on powerpoint and testing
chris - finishing up notification( css for his pages)

4/12/2022
for this week everyone will work on the powerpoint