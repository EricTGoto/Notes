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
