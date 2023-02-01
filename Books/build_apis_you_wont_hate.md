# Build APIs You Won't Hate by Phil Sturgeon

<h2>Chapter 1: Useful Database Seeding</h2>

- Seeding: the process of populating a database
- creating seeding scripts means you can avoid wasting time creating fake data over and over again
- there are many seeding libraries in different languages

<h2>Chapter 2: Planning and Creating Endpoints</h2>

<h3>Functional Requirements</h3>

- try thinking of everything your API will need to handle
    - will initially be a list of CRUD endpoints for your resources

ex:
```
Places:
    - Create
    - Read
    - Update
    - Delete
    - List
    - Image (accept one image for a place)
```

<h3>Endpoint Theory</h3>

<b>GET Resources</b>

- GET /resources: paginated list of stuff, in some logical default order, for that specific data
- GET /resources/X: just X. X can be an ID, username, etc, as long as it's unique to one "resource"
- GET /resources/X,Y,Z: multiple things

Subresources:

- GET /places/X/checkins - find all checkins for a specific place
- GET /users/X/checkins - find all checkins for a specific user

A note on auto increment:
- auto increment allows anyone with access to your API to know excatly how many resources you have, which usually is something you want to keep private
- people can also write a script to hit /users/1, /users/2 and scrape all the data
- UUID is a good idea

<b>DELETE Resources</b>

- DELETE /places/X - delete a single place
- DELETE /places/X,Y,Z - Delete a bunch of places
- DELETE /places - potentially dangerous endpoint that could be skipped as it deletes all places

<b>POST vs PUT</b>

- often people try to pair HTTP POST or HTTP PUT to a specific CRUD action and always only do that action with that one verb
- generally, PUT is used if you know the entire URL beforehand and the action is idempotent
    - idempotent: can do it over and over again without causing different results
- create could be a PUT if you are creating one image for a place
    - PUT /places/1/image
    - making repeat PUT requests to /places/1/image would just replace the image over and over
- update can also be PUT by replacing the resource in its entirety
- POST creates child resources, is not idempotent.
    - POSTing twice with the same data means creating two identical resources with different ids

<b>Plural, Singular or Both</b>

- use plural consistently

<b>Verb, or Noun</b>

With REST we only use one verb, which is the HTTP method. Everything else should be nouns.

Bad examples:

```
POST /SendUserMessage
POST /users/5/send-message
```

Good examples:
```
POST /users/5/messages
GET /users
GET /users/Bob/messages
DELETE /users/bob/messages/xodsah8
```

<h2>Chapter 3: Input and Output Theory</h2>

<h3>Requests</h3>

- define headers, define body in appropriate format, and send

<h3>Responses</h3>

- HTTP response code
- content-type
- response in plain text (unless using SSL)

<h3>Content Structure</h3>

Many different ways to return content. Some pros and cons of a few.

Twitter Style:

Ask for one user get one user:

```
{
    "name": "Hulk Hogan",
    "id": "10002"
}
```

Ask for a collection of things, get a collection of things

```
[
    {
        "name": "Hulk Hogan",
        "id": "10002"
    },
    {
        "name": "Mick Foley",
        "id": "10003"
    }
]
```

Pros:
- Minimalistic Response
Cons:
- No space for pagination or other metadata

Facebook Style:

Ask for one user get one user:

```
{
    "name": "Hulk Hogan",
    "id": "10002"
}
```

Ask for a collection of things, get a collection of things, but namespaced:

```
[
    "data": [
        {
            "name": "Hulk Hogan",
            "id": "10002"
        },
        {
            "name": "Mick Foley",
            "id": "10003"
        }
    ]
]
```

Pros:
- Space for pagination and other metadata in collection
- Simplistic response even with the extra namespace
Cons:
- Single items still can only have metadata by embedding it in the item resource

Double namespaced method

Namespace the resource

```
{
    "data": {
        "name": "Hulk Hogan",
        "id": "10002"
    } 
}
```

Namespace the collection:

```
[
    "data": [
        {
            "name": "Hulk Hogan",
            "id": "10002"
        },
        {
            "name": "Mick Foley",
            "id": "10003"
        }
    ]
]
```

<h2>Chapter 4: Status Codes, Errors, and Messages</h2>

If something about the HTTP request is wrong, you want to let the user know.

<h3>HTTP Status Codes</h3>

<b>2XX is all about success</b>

- whatever the client tried to do was successful up to the point that the response was sent

caution: 202 Accepted does not say anything about the result, it only indicated that a request was accepted and is being processes asynchronously

<b>3XX is about redirection</b>

- sends the calling application somewhere else for the actual resource
- best known codes are 303 See Other and 301 Moved Permanently

<b>4XX is client errors</b>

- client did something invalid and needs to fix the request before resending it
- 401 unauthorized (not logged in), 403 forbidden (user doesn't have permissions), 404 not found

<b>5XX is about service errors</b>

- something went wrong on the server side like DB connection failed
- 500 Internal Server Error (API problem)

When thinking about which error codes to implement, best to keep it simple.

<h3>Error Codes and Error Messages</h3>

- good to provide a human readable error message along with an error code
- will provide more information to the client

Example:
```
{
    "error": {
        "type": "OAuthException",
        "message": "Session expired 10 minutes ago"
    }
}
```

<h3>Standards for Error Responses</h3>

A popular standard for HTTP APIs is JSON-API. It includes a section for errors as well.

JSON-API says that an error object may have the following members:

```
"id" - A unique identifier for this particular occurrence of the problem.
"href" - A URI that MAY yield further details about this particular occurrence of the problem.
"status" - The HTTP status code applicable to this problem, expressed as a string value.
"code" - An application-specific error code, expressed as a string value.
"title" - A short, human-readable summary of the problem. It SHOULD NOT change from occurrence to occurrence of the problem, except for purposes of localization.
"detail" - A human-readable explanation specific to this occurrence of the problem.
"links" - Associated resources, which can be dereferenced from the request document.
"path" - The relative path to the relevant attribute within the associated resource(s). Only appropriate for problems that apply to a single resource or type of resource.
```

<h3>Common Pitfalls</h3>

- don't return HTTP 200 with an error code, use 4XX or 5XX to alert the user that something bad happened
- using the same status code for many different situations. instead use different status codes and an error message that explain the error.
