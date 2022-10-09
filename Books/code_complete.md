# Notes for Code Complete

<h2>Part 1
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
