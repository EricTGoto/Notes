# Building Microservices - Designing Fine-Grained Systems (Newman)

## Chapter 1: What are microservices?

microservices:
- independently releasable services that are modeled around a business domain

## Chapter 2: How to Model Microservices

Domain Driven Design is a key part of modelling microservices

Three important terms:
- ubiquitous language
    - use language in code that is the same as what the users/business use
- aggregate
    - a representation of a real domain concept like Order, Invoice, Stock
    - generally has its own state, identity and life cycle
- bounded context
    - a larger domain boundary that generally contains more than one aggregate
    - the aggregates logically make sense within the context
    - will have an explicit interface that allows you to hide internal details (very important)

Domain based Service boundaries:
- code that changes together stays together (cohesion)
- microservice boundary should be around the domain, a single microservice can handle the life cycle and data storage of one or more aggregates
    - if another service wants to change an aggregate, it should request a change in that aggregate, not willingly change it

Other possible microservice boundaries:
- organizational based
    - split up code based on the type of physical teams you have liek front end team, backend team
- data based
    - splitting up code based on the kind of data it touches, e.g credit card info

## Chapter 3: Splitting the Monolith

Things to consider before splitting up a monolith
- have a clear goal in mind
- should only try to adopt a microservice architecture if there aren't any easier ways to move towards a goal with your current architecture
- need to make sure that microservices will help you achieve the goal
- think about the benefits you gain from actually splitting up the monolith
    - do you need to only split up a small part? multiple?
    - maybe only 10% of the code which handles a lot of load has to be split out

Tips for splitting up a monolith:
- should be incremental, small steps that we can further decompose into smaller steps
- start with something easy yet brings benefit to learn about the process

## Chapter 4: Microservice Communication Styles

Microservices will have to do inter-process communication which is across the network.

Styles of Microservice communication:
- synchronous blocking
    - a call to another service which causes the caller to wait for the response
    - basically a subcategory of request-response
- asynchronous nonblocking
    - a call to another service and the caller can do other things while it waits
- request-response
    - one service sends a request to another service asking for something to be done. the requesting service expects a response informing them of the result
    - can be asynchronous or synchronous
- event-driven
    - microservice emits events and other microservices consume and perform actions accordingly
- common data
    - microservices work off of common data

## Chapter 6: Workflow

Database transactions:
- with databases, we use (ACID) transactions to ensure that one or more state changes are made successfully
- distributed transactions - generally a bad idea. alternative approach sagas

Saga:
- an algorithm that can coordinate multiple changes in state, but avoids locking resources for long periods of time


## Chapter 7: Build

Some questions to ask to see if you are really doing CI:
- do you check in to main frequently?
- do you have a test suite that validates changes before code is merged?
- when build is broken do you fix it?

Continuous Delivery vs Continuous Deployment
- continuous delivery is where each check-in is treated as a release candidate, and we can assess each release candidate to decide if it's ready to be deployed
- continuous deployment extends continuous delivery by automatically deploying if relevant automatic checks(tests) are passed

Code organization for microservices

Many ways to organize code:
- one giant repo, giant build (simple monorepo)
    - any check in to the repo will cause the build to trigger and will run all verification steps
    - simple but wasteful on resources. can make a small change and have all tests run.
- one repository per microservice (multirepo)
    - the microservice could depend on other code managed in a different repository. to make code reuse a little simpler,
    you could package the code into a library in its own repository and have microservices have dependencies on the library
    - if you are frequently making changes across microservice boundaries, then the boundaries may not be correct
- monorepo
    - usually have certain folders mapping to certain builds

## Chapter 8: Deployment

Principles for deployment:
- isolated execution
    - run microservices in a way they have their own isolated computing resources and their execution can't impact other microservices
- focus on automation
- infrastructure as code
    - represent infrastructure configuration as code for automation and information sharing. store in source control
- aim for zero-downtime deployment
- desired state management

Deployment options:
- physical machines
- virtual machines
- containers
- Platform as a Service (Heroku)
- Function as a Service (like AWS Lambda)

## Chapter 10: From Monitoring to Observability

- monitoring is an activity
- observability is a property of the system
    - we can make a system more observable by logs, metrics, alerts etc
- observability is the extent to which we can understand what the system is doing based on its outputs

building blocks for observability:
- log aggregation
    - use a common format, use correlation IDs
- metric aggregation
- distributed tracing
    - being able to visualize and analyze data as it goes through services
- alerting
- SLAs/SLOs/error budgets
- semantic monitoring
    - defining a model for what a correctly behaving system is like

SLA:
- service level agreement: agreement between software provider and the clients

SLO:
- service level objectives: what teams try to provide
    - usually a lot higher standards than SLA

SLI:
- service level indicator: measure of some part of the software like response time

