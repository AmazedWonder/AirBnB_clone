# Project: 0x00. AirBnB clone - The console

# Description

Building your first full web application: the AirBnB clone,
using console as frontend and python as backend. Data stored
in json file.

# Description of the command interpreter
How to start it

Run the console.py file

There is a prompt and you can use command such as
Create
Update
Destroy

Creating an instance of a class such as
User
City
Place
Reviews etc.

Examples
Create BaseModel
Create User
Update BaseModel
all - display all info about classes and instances created
show - displaying

<br>
<br>
<center> <h2>General Use</h2> </center>

1. First clone this repository.

3. Once the repository is cloned locate the "console.py" file and run it as follows:
```
/AirBnB_clone$ ./console.py
```
4. When this command is run the following prompt should appear:
```
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

##### Commands
    * create - Creates an instance based on given class

    * destroy - Destroys an object based on class and UUID

    * show - Shows an object based on class and UUID

    * all - Shows all objects the program has access to, or all objects of a given class

    * update - Updates existing attributes an object based on class name and UUID

    * quit - Exits the program (EOF will as well)


##### Alternative Syntax
Users are able to issue a number of console command using an alternative syntax:

	Usage: <class_name>.<command>([<id>[name_arg value_arg]|[kwargs]])
Advanced syntax is implemented for the following commands: 

    * all - Shows all objects the program has access to, or all objects of a given class

	* count - Return number of object instances by class

    * show - Shows an object based on class and UUID

	* destroy - Destroys an object based on class and UUID

    * update - Updates existing attributes an object based on class name and UUID

<br>
<br>
<center> <h2>Examples</h2> </center>
<h3>Primary Command Syntax</h3>

###### Example 0: Create an object
Usage: create <class_name>
```
(hbnb) create BaseModel
```
```
(hbnb) create BaseModel
3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb)                   
```
###### Example 1: Show an object
Usage: show <class_name> <_id>

```
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
[BaseModel] (3aa5babc-efb6-4041-bfe9-3cc9727588f8) {'id': '3aa5babc-efb6-4041-bfe9-3cc9727588f8', 'created_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96959), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 21, 12, 96971)}
(hbnb)  
```
###### Example 2: Destroy an object
Usage: destroy <class_name> <_id>
```
(hbnb) destroy BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
(hbnb) show BaseModel 3aa5babc-efb6-4041-bfe9-3cc9727588f8
** no instance found **
(hbnb)   
```
###### Example 3: Update an object
Usage: update <class_name> <_id>
```
(hbnb) update BaseModel b405fc64-9724-498f-b405-e4071c3d857f first_name "person"
(hbnb) show BaseModel b405fc64-9724-498f-b405-e4071c3d857f
[BaseModel] (b405fc64-9724-498f-b405-e4071c3d857f) {'id': 'b405fc64-9724-498f-b405-e4071c3d857f', 'created_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729889), 
'updated_at': datetime.datetime(2020, 2, 18, 14, 33, 45, 729907), 'first_name': 'person'}
(hbnb)
```
<h3>Alternative Syntax</h3>

###### Example 0: Show all User objects
Usage: <class_name>.all()
```
(hbnb) User.all()
["[User] (99f45908-1d17-46d1-9dd2-b7571128115b) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92071), 'id': '99f45908-1d17-46d1-9dd2-b7571128115b', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 34, 92056)}", "[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```

###### Example 1: Destroy a User
Usage: <class_name>.destroy(<_id>)
```
(hbnb) User.destroy("99f45908-1d17-46d1-9dd2-b7571128115b")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 2: Update User (by attribute)
Usage: <class_name>.update(<_id>, <attribute_name>, <attribute_value>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", name "Todd the Toad")
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'name': 'Todd the Toad', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
###### Example 3: Update User (by dictionary)
Usage: <class_name>.update(<_id>, <dictionary>)
```
(hbnb) User.update("98bea5de-9cb0-4d78-8a9d-c4de03521c30", {'name': 'Fred the Frog', 'age': 9})
(hbnb)
(hbnb) User.all()
(hbnb) ["[User] (98bea5de-9cb0-4d78-8a9d-c4de03521c30) {'updated_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134362), 'name': 'Fred the Frog', 'age': 9, 'id': '98bea5de-9cb0-4d78-8a9d-c4de03521c30', 'created_at': datetime.datetime(2020, 2, 19, 21, 47, 29, 134343)}"]
```
<br>

### 0x01. AirBnB clone - Web static

# Tasks
0. Inline styling

HTML page that displays a header and a footer.

Layout:

* Body:
* no margin
* no padding
* Header:
* color #FF0000 (red)
* height: 70px
* width: 100%
* Footer:
* color #00FF00 (green)
* height: 60px
* width: 100%
* text Best School center vertically and horizontally
* always at the bottom at the page

1. Head styling

HTML page that displays a header and a footer by using the style tag in the head tag (same as 0-index.html)

Requirements:

* used the header and footer tags
* No inline styling
* used the style tag in the head tag
* The layout is exactly the same as 0-index.html

2. CSS files
HTML page that displays a header and a footer by using CSS files (same as 1-index.html)

Requirements:
* use the header and footer tags
* No inline styling
* have 3 CSS files:
	* styles/2-common.css: for global style (i.e. the body style)
	* styles/2-header.css: for header style
	* styles/2-footer.css: for footer style

3. Zoning done!
HTML page that displays a header and footer by using CSS files (same as 2-index.html)

Layout:

Common:
* no margin
* no padding
* font color: #484848
* font size: 14px
* font family: Circular,"Helvetica Neue",Helvetica,Arial,sans-serif;
* icon in the browser tab
* Header:
* color: white
* height: 70px
* width: 100%
* border bottom 1px #CCCCCC
* logo align on left and center vertically (20px space at the left)
* Footer:
* color white
* height: 60px
* width: 100%
* border top 1px #CCCCCC
* text Best School center vertically and horizontally
* always at the bottom at the page

Requirements:

Have 3 CSS files:
* styles/3-common.css: for the global style (i.e body style)
* styles/3-header.css: for the header style
* styles/3-footer.css: for the footer style

4. Search!

HTML page that displays a header, footer and a filters box with a search button.

5. More filters

Write an HTML page that displays a header, footer and a filters box.

Layout: (based on 4-index.html)

6. It's (h)over

Write an HTML page that displays a header, footer and a filters box with dropdown.

Layout: (based on 5-index.html)

7. Display results

Write an HTML page that displays a header, footer, a filters box with dropdown and results.

Layout: (based on 6-index.html)

8. More details

Write an HTML page that displays a header, a footer, a filter box (dropdown list) and the result of the search.

Layout: (based on 7-index.html)


