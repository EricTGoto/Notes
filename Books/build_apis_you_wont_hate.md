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

## Chapter 7: Data Relationships

Relationships for your API output do not need to be directly mapped to database relationships.
This chapter talks about how to approach related data.

### Subresources

For example, `/places/X/checkins`

Downside is if a user already requested `/places/X`, they will have to make an additional HTTP request to get the check-ins.
- if there is an app that wants to put all places on an area and then allow users to browse through them, an extra HTTP call will have to be made if a user clicks on a place
- gets worse if there are more subresources like images, current_promotions, etc
- this is called 1 + n, if we have 4 sub resources then it will be 1 + 4n 
    - if 50 places are returned then there would be 251 requests

### Foreign Key Arrays

- provide an array of ids in the output so that the client can make further requests
- con: client will have to stitch data together

```
{
    "post": {
        "id": 1,
        "title": "Hello WOrld",
        "links": {
            "comments": ["1", "2"]
        }
    }
}
```

Pro: This way we reduce the calls from 251 to 5, as we can request all the places and then go through them to see which other pieces we need and call them all together. i.e: `/comments/1,5,6,8,9`

### Compound Documents (aka Sideloading)

- this method expands on foreign key arrays and adds the data into the response as an extra object
- avoids duplicating the same item multiple times
```
{
    "post": {
        "id": 1,
        "title": "Hello WOrld",
        "links": {
            "comments": ["1", "2"]
        }
    },
    "linked": {
        "comments": [
            {
                "id": "1",
                "message": "Hello back to u"
            },
            {
                "id": "2",
                "message": "boring"
            }
        ]
    }
}
```

### Embedded Documents (aka Nesting)

- let client decide what should be embedded into the response

`/places?include=checkins,images`

- this will return a response with an array of places each with their checkins and images embedded into it
- offers most flexibility, can reduce HTTP requests, reduce download size depending on what client wants

## Chapter 12: HATEOAS

Stands for Hypermedia as the Engine of Application State.

In short, means two things:
- Content Negotiation
- Hypermedia controls

### Content Negotiation

Content negotiation allows the client to specify a return MIME type like YAML, JSON, XML with the accept header.

The Content-Type response header will contain the return MIME type.

An API should respond with a default content type or respect the Accept header and either output the requested content type or return a 415 if the API does not support it.

### Hypermedia Controls

The last step into achieving full RESTful compliance. Involves adding links to other content, relationships and further actions to allow a client to browse around the API.

Short Aside: URI vs URL:
- URL is the full path like what you see in the browser address bar
- URI is the path, extension, and query string

Can be done by adding an object that contains a rel and uri pairs.
```
{
    "rel" : "place.image"
    "uri" : "places/2/image"
}
```

How do we discover resources?

With the ```OPTIONS``` verb.

## Chapter 13: API Versioning

General Advice:
- try to limit change as much as possible

But business requirements will require making changes so then we must use versioning.

### Approaches to API Versioning

**URI**

Putting a persion number in the URI like:

`https://api.example.com/v1/places`

Pros:
- simple for API developers
- simple for API consumers

Cons:
- not technically RESTful
- forces API consumers to do weird stuff to keep links up-to-date

**Body and Query Params**

If you want to take the version URI out of the URL, we can put it in the body or the query parameters.

Putting the version inside the body solves the issue of URLs changing over time, but can lead to difficulties if the content-type is something like images/png or text/csv.

Trying to solve this issue, some suggest to put the version into the query parameters, but that puts the API version back into the URL.

Pros:
- simple for API developers
- simple for API consumers
- keeps URLs the same when param is in the body
- more RESTful than putting version in the URI

**Custom Request Header**

If URL and HTTP body are unsuitable, headers is the last place.
Unfortunately, this will confuse cache systems and will require users to remember what the custom headers are.

Pros:
- simple for API consumers if they remember custom header
- keep URLs the same

Cons:
- cache systems can get confused
- API developers can get confused

**Content Negotiation**

The `Accept` header is designed to ask the server to respond with a specific resource in a different format.
Traditionally, we think of this as HTML, JSON, YAML, etc, but we can generalize further, and ask for different versions as well.

Github uses this method in their APIs. Their media types look like:

```
application/vnd.github[.version].param[+json]
```

They support 
```
application/json
application/vnd.github+json
```
So if you request either of those two MIME types, it will return JSON.

Without any further specification, they will return a default response which is their latest API version. (And they provide a warning that if the user does not specify a version, then apps can break)

To specify a version they ask for the following:

`Accept: application/vnd.github.v3+json`

This method solves the caching problem, URL manipulation problems, and is RESTful. The only downside is it can be a little confusing.

One downside is that if the entire API is versioned then it becomes very hard for API developers to upgrade their applications.

Pros:
- Simple for API consumers (if they know about headers)
- Keeps URLs the same
- HATEOAS friendly
- Cache friendly

Cons:
- API developers can get confused (if they do not know about headers)
- Versioning the WHOLE thing can confuse users

**Content Negotiation For Resources**

One of the most complex solutions, but a very scalable and is the accepted proper HATEOAS approach.

If Github were to do this, they would add an extra item to their current media-type.

`Accept: application/vnd.github.user.v4+json`

Or can use parameters as the Accept header is capable to containing parameters

`Accept: application/vnd.github.user+json; version=4.0`

Pros:

- Keeps URLs the same
- HATEOAS friendly
- Cache friendly
- Easier upgrades for API consumers
- can b e one code base or multiple

Cons:
- API consumers need to pay attention to versions
- splitting codebases can be challenging
- putting it in the same code base leads to accidental breakage, if transformers are not versioned

**Feature Flagging**

A way to approach versioning by allowing users to opt-in to changes via a web platform. The web platform will have an explanation of changes and gives you the chance to see if it will affect your application. If it works, then you enable the change and from then on your API will be updated. With this, every client could potentially have a different version.

Cons:
- coding this could be difficult and hard to maintain

**Final Note on Versioning**

all approaches are annoying in some way or technically unRESTful, but in the end you must pick what is realistic for your project and for the skill/knowledge level of your audience
