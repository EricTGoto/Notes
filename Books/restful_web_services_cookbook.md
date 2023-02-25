# RESTFul Web Services Cookbook

## Chapter 1: Using the Uniform Interface

- HTTP: application level protocol that defines operations for transferring information between clients and servers
- in HTTP, you have methods that are operations on resources
- HTTP is designed to keep interactions between clients and servers visible

### How to Keep Interactions Visible

Visibility: ability of a component to monitor or mediate the interaction between two other components

How:
- keep HTTP stateless
    - an HTTP intermediary should be able to inger the meaning of any request and response without needing past or future requests and responses
- each method should only operate on one resource
- use each HTTP method such that it has the same smantics as specified by HTTP, add appropriate headers to describe requests and responses
- use appropriate status codes and messages

Features that depend on requests and responses being visible:
- caching
- optimistic concurrency control: detecting concurrent writes and preventing resource changes when operations are based on stale representations
- content negotiation: selecting an appropriate representation for a given resource
- safety and idempotency: ensuring clients can repeat or retry certain HTTP requests

### When to Trade Visibility

- whenever multiple resources share data or whenever an operation modifies more than one resource, visibility will be traded for things such as better abstraction of information, loose coupling, network efficiency, resource granularity or client convenience

Example:
- a car resource can contain an owner resource. sending a PUT request to update the owner resource so that he has a different car (say he sells the car) will affect the car resource as well. at the HTTP level the resources are independent, but on the server they are dependent.
    - common case of reduced visibility

### Maintain Application State

- want to keep application state on the client
- encode application state into URIs, and include URIs into representations via links
- best place to maintain applciation state is within links in representations of resources

### Safety and Idempotency

Safe methods: methods that do not cause side effects
- implement safe methods as read only to guarantee safety

Idempotency: repeating a request has the same effect as making a request just once
- matters most in case of network or software failures, clients can repeat a request in the event of a failure and expect the same result 

PUT/DELETE/POST are not safe.

POST is neither safe nor idempotent.

### GET
- use for safe and idempotent information retrieval

### POST
- use to:
    - create a new resource
    - to modify one or more resources via a controller resource
    - to run queries with large inputs
    - to perform any unsafe or nonidempotent operation when no other HTTP method seems appropriate
- when using POST to create new resources, return 201 and content-location header containing the URI of the newly created resource
- for asynchronous tasks:
    - on receiving the request, create a new resource and return 202 (Accepted). the resource is to let a client track the status of the asynchronous task
    - when client submits a GET request to the task resource do:
        - processing: return 200 and representation of task resource with current status
        - successful completion: return 303 (See Other) with a Location header containing URI of resource with outcome
        - failure: return 200 with representation of task resource informing resource creation has failed

### PUT
- use PUT to create new resources only when clients can decide URIs of resources. otherwise, use POST

```
PUT /user/bob/address/work_address
```

### DELETE 
- idempotent, implies server shoudl return 200 (OK) even if server deleted the resource in a previous request, but practically that would require keeping track of deleted resources, so 404 (Not Found) is used
- asynchronous delete:
    - create a new task resource and return 202 Accepted. when GET is submitted return 200 with representaiton of current status of task

### Custom methods

- use POST over custom methods

## Chapter 2: Identifying Resources

one of the first steps in developing a REST API is designing the resource model

### Resources from domain nouns

- simplistic way to identify resources
- find domain nouns that can be operated using "create", "read", "update", "delete" and use POST, GET, PUT, DELETE methods to impement each CRUD operation
- this strategy has some problems as CRUD is limited
    - e.g: finding traffic directions, converting distances, transfer money. how do we map these to HTTP methods?

### Organize Resources into Collections

- identify similar resources based on applciation-specific criteria
    - e.g. resources taht share the same database schema
        - social network
            - collection of users
            - collection of friends of any given user
            - collection of followers of a user
            - etc..
- can use collection resources for the following
    - paginated views of a collection
    - search the collection for its members or obtain a filtered view of the collection (query responses)
    - create new member resources using the collection as a factory (through POST requests to the collection resource)

### Combining resources into composites

- when looking at home pages of sites like youtube, you will see that the pages aggregate information from a number of sources like video subscriptions, youtube posts, tags, subscribed channels, shorts, recommendations. these kinds of pages result from combining disparate resources into a single resource
- create composite resources based on client usage patterns and performance/latency requirements.
    - identify aggregate resources that can reduce the number of client/server round-trips

### Supporting processing/computing functions

e.g. google maps, give me directions from shibuya to shinagawa. credit card validation. currency exchange.

- treat the processing function as a resource, use HTTP GET to fetch a representation containing the output of the proccessing function
- use query parameters to supply inputs to the processing function

```
# Request
GET /distance_calc?lata=47.6&longa=-143&latb=25&lngb=-100
```

- since processing functions are safe and idempotent, GET is the most appropriate HTTP method

### When/How to use controllers to operate on resources

- a controller is a resource that can atomically (in a single task) make changes to resources
- lets you abstract away tedious operations/details and allows client to have a simple interface to perform operations

```
# Example without using a controller

Merging address books
1. Submit a GET request to the address book resource to download the address book from server
2. load local list of contacts, merge with address book from server
3. submit a PUT request to the address book resource to replace the entire address book with the merged one
```

```
# Example with a controller

Merging address books
1. have client submit address book to server for a merge with a POST request
2. server handles merging, adding new contacts, etc
3. server returns response showing location of updated address book
```

- important to define a unique resource for these operations to avoid tunneling
    - tunneling is when you use the same method on a single URI for different actions

## Chapter 3: Designing Representations

- representations are the concrete elements in a resource like the response headers, response body that you program and clients/servers operate on

### Using Headers to Annotate Representations

- use following headers to annotate representations that contain message bodies
    - Content-Type: to describe type of the representation
    - Content-Length: to specify size in bytes of the body
    - Content-Language: to specify language if representation is localized
    - Content-Encoding: to indicate type of compression if used

### Interpreting Headers

- Content-Type: when you receive a request without this header, return 400 bad request. when you receive a response without this header from a server, treat it as a bad response

### Choosing a representation format and a media type

- use well-known media types for representations such as JSON, xml, html\

### Designing representaitons of collections

- i.e paginated collections
- include self link to the collection resource, link to next page, link to previous page, indicator of size of collection
    - avoid computing exact size of collection, may be expensive, or unnecessary

### Keep collections homogenous
- when designing a representation format for a colelction, include only attributes that apply to all members of the collection.
    - i.e. don't include a wheels attribute for a collection that includes boats and cars. you can include a make or year or height as these attributes exist for both a car and a boat

### Use common data formats
- there are all sorts of standard for decimal, floats, country codes, dates, times, language tags, etc

### Encoding binary data
- use multipart media types such as multipart/mixed, multipart/related, etc
- avoid encoding binary data within textual formats using Base64 encoding
- multipart message is a message containing several message parts each separated by a boundary
- creating and parsing multipart messages can be cumbersome and complex, may be better to provide a link to fetch the binary data as a separate resource, e.g. a link to a video

### Returning Errors

- include a body in the error response for all errors except when the HTTP method is HEAD
- in body include:
    - brief message describing error condition
    - longer description with information on how to fix error condition, if applicable
    - identifier for error
    - link to learn more if applicable

## Chapter 4: Designing URIs

### Best practices for URIs

- use domains and subdomains to logically group or partition resources for localization, distribution or other objectives
    - e.g. localized representations via different subdomains
```
http://en.example.org/book/1234
http://da.example.org/book/1234
http://fr.example.org/book/1234

# Or separation based on class of clients (browser vs API)

http://www.example.org/book/1234
http://api.example.org/book/1234
```
- use forward-slash as a separator to denote hierarchical relationships between resources
- use comma and semicolon to indicate nonhierarchical elements in the path portion of the URI
- use the hyphen and underscore character to improve the readbility of names in long path segments
    - important to choose one and stick with it
- use the ampersand to separate parameters in the query portion of the URI
- avoid including file extensions in URIs

important note: usually more important to focus on consistency of URIs rather than meticulous design of URIs

### Make opaque URIs

- avoid making URIs such that clients need to construct URIs from information returned from representations or documentation/reverse-engineering
    - indicates tight coupling

### URIs should be stable

- URIs should be designed to last a long time
- clients may store URIs in databases and config files, or even hard code them in code
- design URIs based on stable concepts, identifiers and information
- if a URI does change, honor old URIs and issue redirects with 301 (Moved Permanently)
- good idea to monitor request traffic on the server once redirection is set up
    - can know when to disable old URI once majority of clients use new URI, convert the 301 to 410 or 404
