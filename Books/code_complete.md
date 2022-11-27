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

<b>Member Functions and Data</b>

- minimize the extent to which a class collaborated with other classes

<b>Constructors</b>

- initialize all member data in all constructors, if possible
- deep copies over shallow copies

<b>Reasons to Create a class</b>

- model real world objects
- model abstract objects
- reduce complexity - the most important reason
    - create a class to hide information so you don't need to think about it
    - will need to think about it while writing the class, but a well written class will be very easy to use without any knowledge of its internal workings
- reduce code size, improve maintainability
- isolate complexity
    - if an error occurs, it will be easy to find the error because it is localized to a class
- hide implementaiton details
- limit effects of changes
    - isolate areas that are likely to change so that the effects of changes are limited to the scope of a single class or a few classes
- hide global data
    - can hide global data behind a class interface
- central point of control
- facilitate reusable code
- package related operations

<b>Classes to Avoid</b>

- classes that only contain data or only contain behavior

<b>Summary</b>

- class interface should hide something - abstraction/encapsulation
- containment is preferable to inheritance
    - inheritance adds complexity
- classes are a good tool to manage complexity

<h3>Ch 7: High-Quality Routines</h3>

Example of a low quality routine:
```
void HandleStuff( CORP_DATA & inputRec, int crntQtr, EMP_DATA empRec,
double & estimRevenue, double ytdRevenue, int screenX, int screenY,
COLOR_TYPE & newColor, COLOR_TYPE & prevColor, StatusType & status,
int expenseType )
{
int i;
for ( i = 0; i < 100; i++ ) {
inputRec.revenue[i] = 0;
inputRec.expense[i] = corpExpense[ crntQtr ][ i ];
}
UpdateCorpDatabase( empRec );
estimRevenue = ytdRevenue * 4.0 / (double) crntQtr;
newColor = prevColor;
status = SUCCESS;
if ( expenseType == 1 ) {
for ( i = 0; i < 12; i++ )
profit[i] = revenue[i] - expense.type1[i];
}
else if ( expenseType == 2 ) {
profit[i] = revenue[i] - expense.type2[i];
}
else if ( expenseType == 3 )
profit[i] = revenue[i] - expense.type3[i];
}
```
my thoughts:
- too many parameters to the function
- parameters are not named very well
- function name is poor and doesn't describe what it does
- arbitrary number 100 in the for loop. what does it mean?
- doesn't have a cohesive flow, many different things are happening in the function
- divide by 0 may be possible
- modifying input variables not a good practice

textbook:
- routine isn't documented
- routine has a bad layour and inconsistent styles
- writes/reads to global variables (profit, corpExpense)
- doesn't have a single purpose
- uses magic numbers like 100, 4.0, 12, 2, 3
- some parameter's are unused
- parameters are poorly ordered and not documented

<b>Valid Reasons to Create a Routine</b>

- reduce complexity
- introduce an understandable abstraction
    - really another way to reduce complexity
- avoid duplicate code
- hide sequences
    - as in order in which events happen
- improve portability
- easier to improve performance of code
    - code is in one location so easier to read through and think about

<b>Operations that seem too simple to put into Routines</b>

- making a function for a few lines of code may seem like overkill, but will improve readability

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


<h2>Chapter 8: Defensive Programming:</h2>

- enable code to protect itself when input data is bad
- garbage in, error message out
- defensive programming techniques make errors easier to find, easier to fix and less damaging to production code

<b>Assertions</b>

- code used during development that allows a program to check itself as it runs
    - assertion is true -> program running as expected
- use assertions to flush out unexpected conditions
    - e.g. check:
        - input parameters within expected range
        - file/stream is open/closed
        - pointer is non null

Guidelines for using Assertions:

- use error-handling code for conditions you expect to occur, assertions for conditions that should never occur
- don't put executable code in an assertion, check a response from the executable code instead
- for highly robust code, assert and then handle the error anyway

<b>Error Handling Techniques</b>

- handle errors that you expect to occur

Some possible techniques: 
- return a neutral value: simply return a value that is known to be harmless
- wait until valid data: for example if taking readings 100 times a second, just wait for the next reading to come in
- return same answer as the previous time
- substitute with closest legal value: e.g. if a thermometer only reads between 0 and 100, return 0 if a temperature reading is below 0
- log a warning
- return an error code: let a different function handle the error (something higher in the call stack)
- call an error-processing routine/object
    - not the best approach as the program will be coupled to this global object
- display an error message
    - be wary of how much info you reveal in the error message as attackers can discover how to attack a system with too much info
    - can also spread error message interface code all over system which is not good
- shut down: used in safety critical applicaitons

Styles of error processing:

correctness: never returning an inaccurate result

robustness: always doing something that will allow software to keep operating

<b>Exceptions</b>

- means which code can pass along errors or exceptional events to the code that called it
- return exception object to calling function with more context in a try catch block
- use exceptions to notify other parts of the program about errors that should not be ignored
- if error condition can be handled locally, handle it locally
- throw exceptions at the right level of abstraction
    - may involve wrapping common exceptions with names that make sense
- avoid empty catch blocks
- good to know what exceptions that the language you are working in can throw so you can catch them

<b>Barricades</b>

- barricades are a way to separate code into parts where data is safe and vice versa
- if data is in a dangerous area, perform validation and sanitization, if not then assume it is safe and use it
- can also have classes that transition data from dangerous to clean
    - "validation" classes
    - example: public methods assume data is unsafe and do checks on data, private methods take the checked data and assume it is safe
- can think of this as a "clean room" technique
- deciding which code is inside and which it outside the barricade is an architecture-level decision

<b>Determining how much defensive programming to leave in production code</b>

- leave code that checks for important errors
- remove code that checks for trivial errors
- remove code taht results in hard crashes
    - want errors to be unobtrusive in production
- log errors for support personnel
    - error logging may need to be modified a little for production

<h2>The Pseudocode Programming Process</h2>

<b>Summary of steps in building classes and routines</b>

- both are an interative process

Classes:
- create general design for class
    - defining class's specific responsibilities
    - define what "secrets" the class will hide
    - define what abstraction the class interface will capture
    - etc
- construct routines
    - design routine, check design, code, review and test

<b>Psuedocode tips</b>

- use English like statements that precisely describe specific operations
- write pseudocode at a low enough level that generating code form it will be easy
- iterate!

<h1>Part 3: Variables</h1>

<h2>Chapter 10: General Issues in Using Variables</h2>

<b>Guidelines for initializing variables</b>

- initialize each variables as it's declared
- ideally, decalre and define each variable close to where it's first used
- use final or const when possible
- initialize a class's member data in its constructor
- check need for reinitialization

<b>Variable Scope Guidelines</b>

Maximizing scope will bring in unnecessary complexity as you would need to reason about which variables are being used in your routine.
Thus, keep variable scope small.
- keep variable "live" time as short as possible
    - instead of declaring a variable all the way at the top of a function, declare it right before it will be used
- group related statements
- break groups of related statements into separate routines
- begin with most restricted scope and expand if necessary

<b>Binding time</b>

- binding time is the time at which the variable and its vlaue are bound together
- several forms of binding time:
    - coding time (hard coded)
    - compile time (named constants)
    - load time (reading value from external file)
    - object instantiation time (reading value each time a window is created)
    - just in time (reading value each time window is drawn)
- the earlier the binding time, the lower the flexibility and the lower the complexity

<b>Use each variable for exactly one purpose</b>

- use each variable for one purpose only
    - most common way to break this rule is to use a variable named temp for multiple things
- avoid variables with hidden meanings
    - e.g. pageCount represents number of pages printed unless it equals -1, then it indicates an error
- make sure all declared variables are used
    - modern development environments will automatically inform of this so not much of a worry

<h2>Chapter 11: The Power of Variable Names</h2>

most important naming consideration:
- name fully and accurately describes the entity the variable represents

computed value qualifiers in variable names:
- e.g. total, sum, average
- try to put the qualifier in a consistent location
- e.g. countAverage, countMax, countMin instead of averageCount, countMax, minCount

<b>The power of naming conventions</b>

conventions offer several benefits
- let you take more for granted.
    - can make overarching assumptions so you can concentrate on more important characteristics of the code
- knowledge transfer is easier.
    - similarities in names give you an easier and more confident understanding of waht unfamiliar variables are supposed to do
- help you learn code more quickly on a new project
- reduce name proliferation

summary:
- good variable names are a key element of program readability
- names should be as specific as possible

<h2>Chapter 12: Fundamental Data Types</h2>

<b>Numbers</b>

- avoid magic numbers, aka literal numbers in code without any explanation
    - changes can be made more reliably and easily without magic numbers
    - 0 and 1 are an exception as they are used for initialization and increment
- anticipate divide by zero errors
- avoid mixed-type comparisons

<b>Floating point Numbers</b>

- avoid equality comparisons
- avoid additions and subtractions on numbers that have greatly different magnitudes
    - may be hard to represent large ranges with 32bit/64bit
- anticipate rounding errors
    - for example keeping track of money, we can use integers instead and multiply everything by 100.

<b>Characters and Strings</b>

- avoid magic characters and strings
    - easier to use a string resource file, helpful if needing to broaden scope to international markets
- know how your language and environment support Unicode
- decide on an internationalization/localization strategy early in the lifetime of a program
    - key consideration is storing all strings in an external resource and whether to create separate builds for each language or to determine specific language at run time
- support multiple languages -> use unicode

<b>Boolean Variables</b>

- use boolean variables directly in conditions, instead of testing the boolean
    - e.g. if (isFinished) instead of if (isFinished === true)

<b>Enumerated Types</b>

- an enumerated type is a type of data for which the value is restricted to a fixed set of values known at compile time. the values are described in English.
- use enumerated types for readability

<b>Named Constants</b>

- a named constant is a variable that you declare and refer to as a fixed value
- allows you to keep values in one spot and only have to change in one spot instead of having to change in multiple spots (i.e. using magic numbers)
    - single point of control

<h2>Chapter 13: Unusual Data Types</h2>

<b>Pointers</b>

- pointers consists of two parts: a location in memory and a knowledge of how to interpret the contents of that location
    - location: memory address usually in hexadecimal notation
    - interpretation: provided by base type of pointer
- pointer error is usually the result of a pointer pointing somewhere it shouldn't be
- check pointers before using them
- delete pointers in linked lists in the right order
- set pointers to null after deleting/freeing them

<b>Global Data</b>

Common problems
- hard to keep track of changes
- code reuse can be hindered
    - if a class reads or writes to global data, then using that class in a different program would require creating that global data as well, unless you refactor it

use global data only as a last resort
- begin by making each variable local and increase scope as necessary
- use access routines
    - require access to global data through routines
- keep all access to the data at the same level of abstraction

reducing risks of using global data
- naming convention that makes global variables obvious
- well-annotated list of all global variables
- don't use global data to hold intermediate variables 

<h2>Part 3: Statements</h2>

<h2>Chapter 14: Organizing Straight-Line Code</h2>

<b>Statements that must be in a specific order</b>

- often times there are statements that must be written in a specific order
- care should be taken to allow the code to be easily read and understood
- tips:
    - organize code so that dependencies are obvious
        - i.e. easily let reader know that line 2 depends on line 1
    - name routines so that dependencies are obvious
    - use routine parameters to make dependencies obvious
    - document unclear dependencies with comments

<b>Statements whose order doesn't matter</b>

- keep related actions together
- reduce live time of objects/variables

<h2>Chapter 15: Using Conditionals</h2>

<b>if statements</b>

- write the normal path so that it is clear and then write the edge cases
- make sure to branch correctly on equality (>= or <=)
- put normal case after the if rather than after the else
- don't use empty ifs (no statements after in the if block)
- consider the else clause
    - sometimes may think you only need the if, but else may be needed as well
- test all cases
- check that the statements are in the right block (if or else)

<b>if-else statements</b>

- simplify complicated tests with boolean function calls
    - wrap similar conditional tests in functions to improve readability
- put the most common cases first
    - minimizes amount of reading needed to find the usual cases
    - minimizes comparisons the code does to find the usual cases
- make sure all cases are covered
    - i.e. a final else clause to catch cases that you didn't plan
- replace if-then-else chains with cases as they are easier to code and read

<b>case statements</b>

- put normal case first and then exceptions OR
- order cases by frequency, if cases are equally frequent, order alphabetically
- keep action of each case simple
    - use function if necessary
- don't make up a variable to use the case statement, case statement should be used for simple data that is easily categorized
    - if data isn't simple use if-else
- use default clause only to detect legitimate defaults OR errors

<h2>Chapter 16: Controlling Loops</h2>

loop differentiation:
- flexibility: how many times a loop executes
- test location: beginning, middle or end of loop
    - tells you whether or not the loop runs at least once

<b>controlling the loop</b>

- loop entering:
    - enter loop from one location only
    - put initialization code directly before the loop
- loop contents:
    - keep loop house keeping statements at beginning or end of the loop
        - e.g. i++
    - each loop perform only one functino
- exiting the loop
    - assure yourself that the loop ends
    - make loop termination conditions obvious
    - avoid code that depends on the loop index's final value
    - be wary of using too many breaks in a loop
        - can indicate unclear thinking about structure of the loop
    - use break and continue only with caution
        - using break forces person reading code to look inside the loop to understand loop control

<b>loop variables</b>

- limit scope of loop-index variables to the loop itself
- use meaningful variable names to make nested loops readable

<b>loop length</b>

- make loop short enough to view all at once
- limit nesting
- move loop innard of long loops into routines

<h2>Chapter 17: Unusual Control Structures</h2>

<b>Multiple Returns from a Routine</b>

- use a return when it enhances readability
- use guard clauses (early returns or exits) to prevent deeply indented code
    - e.g. if (error): return

<b>Recursion</b>

- there are most definitely better alternatives, so consider those first

<h2>Chapter 18: Table-Driven Methods</h2>

- table driven method is a way that allows you to look up information in a table rather than using logic statements (if and case)

two issues is using table-driven methods:
- how to look up entries
- what should be stored in the table

three types of table access:
- direct access
- indexed access
- stair-step

<h2>Chapter 19: General Control Issues</h2>

<b>Boolean Expressions</b>

- use true and false for boolean tests, rather than values like 0 and 1
- use implicit comparisons rather than explicit
    - e.g: while (done == False)
- move complicated expressions into boolean functions
- positive boolean expressions tend to be easier to read
    - DeMorgan's Theorems can simplify boolean tests with negatives
- use patentheses to clarify boolean expressions
- know how boolean expressions are evaluated
    - some languages short-circuit others don't and so on
- organize numeric tests from smallest to largest
    - e.g. if want values between a min and a max MIN_VALUE < i and i < MAX_VALUE
    - e.g if want values other than values between two points i < MIN_VALUE or MAX_VALUE < i
- compare numbers explicitly to 0 rather than implicit (if checking for 0 of course)
- compare pointers to null

<b>On Improving Deep Nesting</b>

- studies show that few people can understand more than three levels of nested ifs
- if nesting gets too deep, refactor the tests
    - maybe conversion to if-else
- may be possible to convert to a case statement
- put deeply nested code into own routine
- use a more object oriented approach
- use exceptions

<b>Structured Programming</b>

- the core idea is a program should use only have one in and one out
- a structured program progresses in an orderly way rather than jumping around, so it is easier to understand

<b>Control Structures and Reducing Complexity</b>

- one way of measuring complexity with regards to control structures is counting the number of "decision points"
- every path is a decision point
- should have at most 6 decision points, more will need to consider refactoring

<h2>Part 5: Code Improvements</h2>

<h2>Chapter 20: The Software-Quality Landscape</h2>

<b>Characteristics of Software Quality</b>

Software has both external and internal quality characteristics.

External characteristics are characteristics that a user is aware of.

Examples of external characteristics:
- correctness: degree to which system is free from bugs
- usability: how easy for user to use and learn to use
- efficiency: how taxing it is on users system
- reliability: ability for system to perform required functions consistently, how long time between failures?
- integrity: how secure the software is
- adaptability: the extent to which a system can be used in applications or environments other than those for which it was specifically designed
- accuracy: how accurate the functionality is, e.g. if it is a calendar software, are time calculations between two dates correct?
- robustness: ability of a system continuing to function with invalid inputs, bugs, errors, etc

Internal characteristics:
- maintainability: easy of modifying, change/add features, improving performance, fixing bugs
- flexibility: ability to modify for different applications or environments than it was originally designed for
- portability: ease of modifying system to operate in an environment different from that for which it was designed
- reusability: extent and ease of reusing parts of a system in other systems
- readability: how easily can you read and understand the code
- testability: degree to which you can unit test and system test, degree of being able to verify that system meets its requirements
- understandability: ease of comphrehending system at both system organizational and detailed statement levels

<b>Cost of Finding/Fixing Defects</b>

- a study found that only 3.5 hours needed to find error with code inspections, while testing took 15-25 hours
- Microsoft did a study anf found that it takes three hours to find and fix a defect with code inspection, but 12 hours to find and fix a defect by using testing

<b>Author's recommendation for achieving highter than average quality</b>

combine various defect detection technique to maximize defect finding chance

- formal inspection of all requirements, architecture, and designs for critical parts of a system
- modeling or prototyping
- code reading/inspections
- execution testing

<b>When to do quality assurance</b>

- all stages
    - remember, finding a defect earlier is good!

important point: does management understand that quality assurance incurs additional costs up fornt in order to save costs later?

<h2>Chapter 21: Collaborative Construction</h2>

The purpose of collaborative construction is to improve software quality.

The cost of pair programming is higher than the cost of solo development - on the order of 10-25% - but the reduction in
development time appears to be on the order of 45 percent.
 - this is because it lowers the amount of errors that will be pushed into production and have to be fixed later. collaborative construction allows you to find a significant amount of errors early and be able to fix them

code inspections bring up the level of novice developers

<b>Pair Programming</b>

- 2 people programming on one machine, one person types and other watches and thinks about the code being written. person typing and thinking switch in intervals

tips:
- support pair programming with coding standards
- use pair programming for assignments where the pair will benefit from it
- person watching should be an active participant and critically thinking and analyzing code
- rotate pairs
- encourage pairs to match each other's pace
- avoid pairing two noobs

<b>Formal Inspections</b>

- when a group of people prepare beforehand for a formal meeting on finding defects in a design or code
- pace of about 150-200 statements an hour is good
- solutions shouldn't be discussed, just finding defects
- should not last more than 2 hours
- after the inspection, a report is produced which lists each defect, including its type and severity
- use a checklist to go over frequently occurring problems in the past

<h2>Chapter 22: Developer Testing</h2>

Unit testing - testing an individual part of a system, like one function or class
Integration testing - where two or more classes, packages, components or subsystems are tested
Regression testing - testing for errors that have occurred before, can run previously made tests
System testing - execution of software in final configuration

- test for each relevant requirement to make sure that the requirement has been implemented
- use a checklist of the kinds of errors you've made on projects to date
- plan to test and find defects as early as possible

Author recommends writing tests first.

<b>Things to look out for in testing</b>

- only writing clean tests
    - important to write tests for ways the code could break
- write a test for each path in code
- boundry errors
- using good test data

<b>Where do errors come from?</b>

- 25% structural, 22% data, 16% functionality, 10% construction, 8% requirements
- scope of most errors is fairly limited - a study found 85% of errors could be corrected without modifying more than one routine
- many errors are outside the domain of construction, that is thin domain knowledge, fluctuating and conflicting requirements, and communication and coordination breakdown
- most construction errors are the programmers' fault: 95% are caused by programmer,2% by system software, 1% hardware (back in the 80s)
- 36% of construction errors are typos
- misunderstanding design results in errors
- most errors are easy to fix

<h2>Chapter 23: Debugging</h2>

Debugging is the process of identifying the root cause of an error and correcting it.

<b>Defects as learning opportunities</b>
Defects can allow you to learn:

- more about the program you're working on
- about the kinds of mistakes you make
- about the quality of your code from POV of someone who has to read it
- about how you solve problems
    - does the approach work? do you guess randomly? where can you improve?
- about how you fix defects
    - do you make easiest possible corrections that may result in problems later? or make thorough fixes?

<b>Ineffective approaches</b>

- find defect by guessing
    - scattering rpint statements randomly
- not understanding the problem or context
- fix the error with a very specific solution, i.e. creating a special case just for the error

<b>Effective approach to debugging</b>

Use a scientific approach
- stabilize the error
    - make it occur reliably
- locate the source of the error
    - gather the data that produces the defect
    - analyze the data that has been gathered, and form a hypothesis about the defect
    - determine how to prove or dissprove the hypothesis, either by testing the program or examining the code
    - prove or disprove the hypothesis
- fix the defect
- test the fix
- look for similar errors

Stabilize the error
- hard to diagnose a problem without being able to make it occur reliably
- error that doesn't occur predicably is usually an initialization error, a timing issue, or a danlging pointer problem
- narrow down a test case to the simplest one that still produces the error
- play around with the factors you think produce the error to narrow down the cause

Tips for finding defects:
- brainstorm for possible hypotheses
- use a notepad
- narrow the suspicious region of the code
    - try using a divide and conquer technique to remove half the code every time
- check code that's changed recently
- integrate incrementally
- talk to someone else about the problem

Fixing the defect:
- understand the problem before you fix it
- understand the program, not just the problem
    - not necessarily the entire code but at least the code in the same file
- make sure that the problem was diagnosed correctly
- don't rush
- don't use a duct tape type solution, fix the problem entirely
- add unit test that exposes the defect

<h2>Chapter 24: Refactoring</h2>

Code is always changing. We want to make sure that whenever it is modified, the quality increases.
Treat modifications as opportunities to improve the existing design of a program.

Strive to improve code so that future changes are easier.

<b>Reasons to Refactor</b>

- code is duplicated
- a routine is too long
- a loop is too long or deeply nested
- class has poor cohesion
- class interface does not provide a consistent level of abstraction
- too many parameters for a routine
- changes require parallel modifications to multiple classes
- related items are not organized into a class
- a class doesn't do very much
- poor naming
- global variables are used
- comments used to explain difficult/bad code
- data members are public
- routine uses setup/takedown code

<b>Useful refactorings</b>

<h2>Chapter 25: Code-Tuning Strategies</h2>
<h2>Chapter 26: Code-Tuning Techniques</h2>
