# cse2102-fall25-Team05

Owned by: 
 - Michael Yamarik - mjy20003 .
 - Brian Loch - brl22020
 - Troy Ramos - tfr22002
 - Mohammad Tashfee - mas21125

Link to Trello: https://trello.com/b/k8DysviU/group5cse-2102project
Link to Figma: https://www.figma.com/site/XnjwDGVIKDy0At7xgAOkml/Figma-Marketplace-G4?node-id=0-1&t=P9hghTnCsvd5mNwp-1

## Instructions to Run

### Running Frontend to work W. Backend
* please have docker desktop open
* Follow directions for *Starting Backend*
* Follow directions for *Starting Frontend*
* Open the browser tab that is running the Frontend

### Starting Frontend
* Open a **new** terminal or gitbash
* use "cd" to navigate to the frontend
* run the following docker command: *docker build -t frontend .*
* wait for build to finish
* run the following docker command: *docker run -p 5173:5173 frontend*
* profit

### Starting Backend
* open a **new** terminal or gitbash
* use "cd" to navigate to the backend
* run the following docker command: *docker build -t backend .*
* wait for build to finish
* run the following docker command: *docker run -p 5001:5001 frontend*
* profit

# USE CASES
* click on CREATE AN ACCOUNT button
* * this will pop up a prompt for user input
  * after this (to verify) login with that information
* now go to docker desktop and verify that the requests show up in the docker container as "200"

# SQL USE
* you can also use SQL commands inside the docker container itself
* open the backend docker container and go to the EXEC tab
* type *sqlite3 marketplace.db*
* now you should be in sqlite3
* to insert into a table use the insert command
* - - - INSERT INTO "tablenamehere" (name1, name2, ..., namek) VALUES ('desired', 'desired', ...'desired');
* to find information use the select command
* - - - SELECT * FROM "tablenamehere"
      - this will give you all lines from that table
* Currently the ORDERS has no button to insert any orders for testing so here is a code for you to use
* - - - INSERT INTO orders (buyer_id, seller_id, item_id, total) VALUES (292929292, YOURSELLERIDREPLACESTHIS-FINDATTOPOF-URL, 383838383, 1);
      - 
      - this creates a test order for you to use, the buyer_id and item_id are just any 9 digit number (random really) and seller_id is specific to each login credentials)
