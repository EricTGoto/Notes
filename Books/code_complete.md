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

<h2>Part 2: Creating High-Quality Code</h2>

<h3>Ch 5: Design in Construction</h3>

<b>Design Challenges</b>

- "software design" links requirements to coding and debugging, it is turning specifications into operational software
- design is sloppy because many mistakes will be made and will be iteratively (ideally) corrected. a good solution is often only subtly different from a poor one.
- design involves tradeoffs, restrictions and priorities

<b>Key Design Concepts</b>

- managing complexity is very important really the only point where a project can fail from a technical POV
- manage complexity by:
    1. minimizing the amount of essential complexity that anyone's brain has to deal with at any one time
        - organize code so that there is a minimum number of parts to think about at a time
    2. keep accidental complexity from growing
- high quality design has several general characteristics
    1. minimal complexity
        - avoid making "clever" designs as they are usually hard to understand
        - simple and easy to understand are much better
    2. ease of maintenance
    3. loose coupling
        - minimize connections between different parts of programs
        - makes it easier to test and maintain
        - use principles of good abstractions in class interfaces, encapsulation and information hiding
    4. extensibility
        - make it easier to enhance code
    5. reusability
        - designing code such that it can be easily reused elsewhere
    6. high fan-in
        - having a high number of classes that use a given class
        - implies that a system has been designed to make good use of utility classes
    7. low-to-medium fan-out
        - means having a given class use a low-to-medium number of other classes (<7)
        - high fan-out may mean that the class is overly complex
    8. portability
        - designing the system so that you can easily move it to another environment
        - e.g docker
    9. leanness
        - when code is modified usually extra code has to be developed, reviewed, tested and considered - future versions of the software should remain backward compatible with this extra code
    10. stratification
        - writing code such that viewing the system at any single level gets a consistent view
    11. standard techniques
        - make codebase standardized by strictly applying style rules, etc

<b>Levels of Design</b>

Level 1: Software System
- entire system

Level 2: Division into Subsystems or Packages

- the main design aspect at this level is the identification of all major subsystems
    - e.g. database, user interface, business rules, command interpreter, report enginem, etc
- major design activity is on how to partition the program into major subsystems and defining rules for how they can communicate
    - important to restrict communications, otherwise you lose benefit of separating them in the first place
    - if the rules are loose or don't exist then some important questions are raised:
        - how many parts of a system would a developer need to understand to change a small section of code?
        - what happens when business rules are used in another system?
        - what happens when a new UI is added?
        - what happens when you put data storage on a remote machine?
    - a program shouldn't contain any circular relationships

Level 3: Division into Classes

- design at this level includes identifying all classes in the system
- major design activity is to make sure all subsystems have been decomposed to a level of detail fine enough that you can implement their parts as individual classes

Level 4: Division into Routines
- dividing each class into routines

Level 5: Internal Routine design
- laying out the functionality of individual routines
    - consists of writing pseudocode, looking up algorithms, how to organize the code, writing the code
- this level is always done


<h3>Heuristics- some design guides</h3>

<b>Designing with objects</b>

- identifying the objects and their attributes (methods and data)
- determine what can be done to each object
- determine what each object is allowed to do to other objects
- determine the parts of each object that will be visible to other objects
- define each object's interfaces

<b>Form Consistent Abstractions</b>

- the main benefit of abstraction is that it allows you to ignore irrelevant details
- a good class interface is an abstraction that allows you to focus on the interface without needing to worry about the internals of the class

<b>Encapsulate Implemenation Details</b>

- encapsulation manages complexity by forbidding you to look at the complexity
- you can look at a house from a distance, but not get close enough to know what the door is made of

<b>Inherit - When Inheritance Simplifies the Design</b>

- inheritance is a powerful tool and can provide great benefits when done well, but can make things very confusing when done poorly

<b>Information hiding</b>

- hiding complexity so that your brain doesn't have to deal with it unless there is a direct concern
- hiding sources of change so that when change occurs, the effects are localized
- asking "what does this class need to hide" supports good design decisions at all levels

<b>Identify Areas Likely to Change</b>

- identify items that seem likely to change
- separate items that are likely to change
    - compartmentalize potentially volatile components into its own class
- isolate items that seem likely to change
    - design the interface so that changes are limited to the inside and other classes would be unaware that change occurred

Areas likely to change:
- business rules
- hardware dependencies
- input/output
- nonstandard language features
- status variables
- data-size constraints
    - instead of declaring an array of size 100 directly, use a named constant like MAX_SIZE

<b>Keep Coupling Loose</b>

- good coupling between modules is loose enough that one module can easily be used by other modules
- make it easy for other modules to call a module, loose coupling makes things flexible and maintanable

Types of Coupling:
- data-parameter coupling: data passed between modules are primitive data types - normal and acceptable
- simple object coupling: a module is simple object coupled if it instantiates another object - this is acceptable
- object-parameter coupling: two modules are object-parameter coupled when Object1 required Object2 to pass Object3
- Semantic coupling: when one module makes use of some semantic knowledge of another module's inner workings - worst, avoid

Classes and routines are tools to reduce complexity, if they aren't then they aren't doing their jobs!

<b>Look for Common Design Patterns</b>

- adapter, bridge, decorator, facade, factory, observor, singleton, template, etc

- patterns reduce complexity by introducing well known abstractions
- patterns reduce errors by introducing standardized ways to solving common problems
- a designer who is familiar with common patterns can easily think of alternative patterns that may fit better
- patterns streamline communications if participants know of them

<h3>Design Practices</h3>

- iterate
    - a first design may seem good, but a second attempt is nearly always better than the first
- divide and conquer
    - divide program into different areas and tackle individually
- top down/bottom up

<h3>Ch 6: Working Classes</h3>

<b>Abstract Data Types (ADT)</b>

- ADT is a collection of data and operations that work on that data
- if you don't have ADTs, you'll most likely have an ad-hoc aproach which can get very hard to organize and maintain
- benefits of using ADTs:
    - hide implementation details, in particular, information about a particular data type is all located in one place
    - changes don't affect the whole program
        - changes will be localized to the ADT
    - interface can be more informative
        - seeing the similar operations in a single place will allow you to reason and understand the code more
    - easier to improve performance
        - because of organization
    - program becomes more self documenting
        - can have easy to understand method names
    - data doesn't have to be passed around
        - ADT will contain necessary attributes and methods to read and write ADT's data
    - lets you abstract

<b> Good Class Interfaces </b>

- a class's interface should offer a group of methos that clearly belong together
- each class should implement one and only one ADT
    - if a class is implementing more than one, then reorganize the class into one more more well-defined ADTs
- provide services in pairs with their opposites
    - most operations have corresponding, equal and opposite operations
- move unrelated information to another class
- don't add public members that are inconsistent with the interface abstration
- Good encapsulation
    - minimize accessibility of classes and members
    - don't expose class attributes in public
        - getters/setters preferred
    - avoid putting private implementation details into a class's interface
        - may not be a problem in python?
    - don't assume how the interface will or won't be used
    - favor read-time convenience to write-time convenience
    - be wary of semantic violations of encapsulation
        - i.e. don't skip calls to certain methods because you know they are called automatically in other methods
            - e.g. not calling database.Connect() because you know employee.Retrieve() will connect to the DB if there isn't already a connection
        - semantic violations will break encapsulation as you are aware of the internal implementation and thus are not working with the interface, but through it

<b>Design and Implementation Issues</b>

- Containment
    - idea that a class contains a primitive data element or object
    - think of it as a "has a" relationship
        - an employee "has a" name, "has a" phone number, etc -> make name and phone attributes of the Employee class
- Inheritance
    - idea that one class is a specialization of another class
    - think of it as a "is a" relationship
    - helps to avoid the need to repeat code and data in multiple locations by having a base class
    - design and document for inheritance or prohibit it
    - all methods defined in the base class should mean the same thing when used in the derived classes
    - move common interfaces, data and behavior as high as possible in the inheritance tree
    - be suspicious of classes that override a method and do nothing inside the derived method
        - typically indicates an error in the design of the base class
            - e.g. class Cat with method Scratch(), but what about a Declawed cat? May be tmepted to make class ScratchlessCat(Cat) which overrides Scratch() with nothing. Correct approach would be a Claws class in Cat.
    - avoid deep inheritance trees
        - 2/3
    - make all attributes private
        - if derived class really needs access, use protected accessor functions
    - multiple inheritance is generally bad

Underlying message is that inheritance tends to work against managing complexity.

When to use inheritance and when to use containment:

- if multiple classes share common data but not behavior, create a common object that those classes can contain
- if multiple classes share common behavior but not data, derive them from a base class that defines the common routines
- if multiple classes share common data and behavior, inherit from a common base class that defines the common data and routines
- inherit when you want the base class to control your interface, contain when you want to control your interface

<h3>Ch 7: High-Quality Routines</h3>
<h3>Ch 8: Defensive Programming</h3>
<h3>Ch 9: Psuedocode Programming Process</h3>