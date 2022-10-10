# Notes for Code Complete

<h2>Part 1</h2>
<h3>Ch 1: Welcome to Software Construction</h3>

- Very generally, three aspects to software development:
    - Problem/Requirements definition/architecting
    - Construction
    - System Testing
- Within construction there are many subtasks:
    - detailed design
    - designing and writing classes and routines
    - creating and naming variables and named constants
    - unit testing, integration testing, debugging
    - reviewing other team members' designs and code
    - formatting and commenting code

<b>Why is software construction important?</b>

- takes between 30-80% of a project
- is central activity in software development
- construction's product, source code, is often the only accurate description of the software
    - documentation, design specs/documents can go out of date
    - consequently, imperative that the source code be of the highest possible quality
- only activity guaranteed to be done

<h3>Ch 2: Metaphors for a Richer Understanding of Software Development</h3>

<b>Software accretion</b>

- accretion: growth by gradual addition/inclusion
    - oysters grow pearls by accretion
- other words related to accretion are "incremental"
- incremental designing, building and testing are some of the most powerful software-development concepts
- in incremental development, make the simplest possible version of the system that will run
    - doesn't have to accept realistic input or perform any realistic manipulations on data, or product realistic output, just a skeleton strong enough to hold the real system as it is developed
- after skeleton is made, add other parts bit by bit, code that accepts real input, code that produces real output, etc

<b>Building Software</b>

- the image of "building" software is more useful than "writing" or "growing"
- it is compatible with accretion
- building software implies various stages of planning, preparation, and execution
- imagine building a house: there would be consequences for not planning out and taking time to design the house, e.g, doors or windows in the wrong place
    - first need an architect to come up with a general design
    - draw detailed blueprints, and hire a contractor
    - prepare site, foundation, framing, roof, plumbing, wiring
- similarly for building software you want software architecture design, details software design, software construction all to happen
- also don't build unnecessary things like a washer or a dryer, this is similar to using prebuilt libraries instead of making your own
- careful planning is important in both building a house and building software
- will use different levels of planning depending on the end goal: a warehouse will use a different approach from a nuclear reactor. a personal blog will use a different approach from an ecommerce website

<b>Intellectual Toolbox:</b>

- great software developers have spent years learning new techniques, new tools, tricks, etc and know when to use a certain technique/tool/trick for their problem
- it is important to realize that there is no one size fits all solution and that it is important to choose the right tool for each problem

<h3>Ch 3: Measure Twice, Cut Once: Upstream Prerequisites</h3>

<b>Importance of Prerequisites</b>

- goal of preparation is risk reduction
    - careful planning and consideration of requirements reduce risk
- fixing a problem earlier is much cheaper than fixing it later (10-100x)

<b>Sequential vs Iterative</b>

- a sequential approach without thinking about prerequesites can end up becoming quite costly, but both sequential and iterative will have similar costs when prerequisites are mostly considered

sequential approach when:
- requirements are fairly stable
- design is straightforward and well understood
- dev team is familiar
- little risk, cost of changing requirements, design and code downstream is likely to be high

iterative approach when:
- requirements are not well understood or seem unstable
- design is complex, challenging or both
- dev team unfamiliar
- lot of risk
- cost of changing requirements, design and code downstream is likely low

<b>Problem-Definition Prerequisite</b>

- first preqrequisite to fulfuill before beginnign construction is a clear statement of hte problem that the system is supposed to solve - called the problem definition
- problem definition defines what the problem is without any reference to possible solutions
    - 1-2 pages
    - user language, and be described from user's POV
    - exception made when the problem is with the computer, e.g. compile times are too slow
- failing to define the problem can lead to wasting time solving the wrong problem

<b>Requirements Prerequisite</b>

- requirements describe in detail what a software system is supposed to do
- explicit requirements help to ensure that the user rather than the programmer drives the system's functionality
    - if reqs are explicit, user can review them and agree to them
    - explicit reqs prevent devs from guessing what the user wants
- exp reqs help to avoid arguments, scope is decided before programming begins

<b>Handling Requirements Changes During Construction</b>

- stable requirements are a myth, however, typically the customer can't reliably describe what is needed before the code is written. 
    - just as the more you work with the project, the better you understand it, the more the customer works with it, the better they understand it
- 25% change in requirements is typical during development

- tips to handle requirement changes:
    - make sure everyone knows the cost of requirements changes
        - if a client thinks of a new feature, mentions that schedule and cost estimates will have to be revised
    - set up a change control procedure
    - use a development approach that accommodate changes
        - evolutionary delivery
    - dump the project if requirements are bad or too volatile
    - keep eye on business case for the project
        - sometimes a requirement that seemed like a good idea can seem like a terrible idea when you evaluate the "incremental business value"

<b>Requirements checklist</b>

Functional Requirements
- are all inputs/outputs to the system specified, including source, accuracy, range, frequency?
- are all external hardware and software interfaces specified?
- are all external communication interfaces specified, including hand-shaking, error-checking, and communication protocols?
- are all the tasks the users want to perform specified?
- is the data used in each task and the data resulting from each task specified?

other checklist items on page 42.

<b>Architecture Prerequisite</b>

- software architecture is the high-level part of software design
- typically architecture is described ina single document referred to as "architecture specification" or "top-level design"
- architecture is an important prerequisite because the quality of the architecture determines the integrity of the system

- the architecture should define the major building blocks in a program
    - each building block may be a single class or a subsystem consisting of many classes
    - every feature listed in the requirements should be covered by at least one building block
    - what each building block is responsible for should be well defined
        - each building block should have one area of responsibility
- communication rules for each building block should be well defined
- architecture should specify the major classes to be used
    - responsibilities of the major classes and how they will interact with other classes should be identifies
    - include descriptions of class hierarchies, state transitions, object persistence
    - aim for 80/20 rule: specify 20% of architecture that make up 80 percent of the system's behaviour
- architecture should describe the major files and table designs to be used
    - should describe alternatives that were considered and justify the choices that were made
    - e.g. if the application maintains a list of customer IDs and the architects have chosen to represent the list of IDs using a sequential-access list, the document should explain why a sequential access list is better than a random-access list, stack or hash table
- architecture should specify and justify the high-level organization and contents of any databases used
- if architecture depends on specific business rules, it should identify them and describe the impact the rules have on the system's design
    - e.g: business rule that customer info should be no more than 30s out of date
- architecture should specify major elements of user interfaces like web page formats, GUIs, command line interfaces
    - should be modularized so that a new user interface can be easily substituted without affecting the business rules and output parts of the program
- architecture should describe a plan for managing scarce resources such as database connections, threads, and handles
    - estimates for nominal and extreme resource use should exist
- architecture should describe how the system can scale
- architecture should describe how errors should be processed
    - error processing corrective vs detective
    - error detection active vs passive
    - error propagation?
    - error messages
    - exception handling: where they will be caught, logged, documented
    - error handling
    - responsibility of each class for validating input data
- architecture should describe a strategy for handling changes

summary: 
- architecture should describe the motivations for all major decisions, rationales for including/excluding any alternatives should be explained
- if good architectural design hasn't been done, you might be solving the right problem the wrong way during construction

<h3>Ch 4: Key Construction Decisions</h3>

<b>Choosing a programming language</b>

- programmers are more productive using a familiar high-level language such as Java, Python, C#

<b>Program <i>into</i> a language</b>

- programmers who program "into" a language first decide what thoughts they want to express, and then they determine how to express those thoughts using the tools provided by their specific language
- try to compensate for missing aspects of your programming language by using your own coding conventions, standards, libraries, etc
    - essentially, work around problems created by a programming language

<b>Selection of Major Construction Practices</b>

- there are many practices that can be used, it is good to decide which ones are to be used and which ones are to be excluded
    - coding conventions for names, comments, layout
    - handling errors, security, OOB
    - process to check in code
    - pair programming? individual?
    - when to write tests? before, during, after?
    - integration tests?
    - peer review of code?
    - version control?
    - language, language version?
    - framework?
    - misc tools like: refactoring tool, test framework, syntax checker

