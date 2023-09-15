# NoSQL Distilled: A Brief Guide to the Emerging World of Polyglot Persistence (Sadalage, Fowler)

## Chapter 1

common NoSQL database characteristics:
- not using relational model
- running well on clusters
- schemaless

## Chapter 2: Aggregate Data models

- data model is the model through which we perceive and manipulate our data
- database will also have a data model
- the dominant database model was the relational data model but with NoSQL, there is a shift away from relational to four primary categories: key-value, document, column-family, and graph
- key-value, document and column-family have a common characterisitc called aggregate orientation

aggregate orientation:
- in a relational data model, you can't nest one row within another to get nested records or put lists of values or rows within another, but aggregate orientation recognizes that you may want to operate on data in complex units
- an aggregate igonrant model allows you to easily look at data in different ways (since they are lumped into units)
- aggregate orientation helps with running databases on a cluster, since we know what data has to be lumped together to be on one node, easily reducing the number of nodes we need to query
- aggregate oriented databases work best when most data interaction is done with the same aggregate

key-value model:
- treats the aggregate as an opaque whole, only key lookup for the whole aggregate

document model:
- makes the aggregate transparent ot the database, allowing queries and partial retrievals

column-family:
- divides aggregate into column families, allowing the database to treat them as units of data within the row aggregate

## Chapter 4: Distribution Models

- replication: same data over multiple nodes
- sharding: different data on different nodes

## Chatper 7: Map-Reduce

- map-reduce is a pattern to allow computations to be parallelized over a cluster
- map reads data from an aggregate and boils it down to relevant key-value pairs
- reduce takes many values for a single key and summarize thenm into a single output

## Chapter 8: Key-Value Stores

Suitable use cases:
- storing session information
- user profiles, preferences
    - users usually have a unique userId and you can use this as a key and have an object with all of the users info
- shopping cart data

When not to use:
- data needs relationships
- when you need to do multioperation transactions
- query by data


## Chapter 9: Document Database

- document can be XML, JSON, BSON, etc

## Chapter 10: Column-Family Stores

Suitable Use Cases
- event logging
    - have applications write their events with their own columns

When not to use:
- early prototypes
    - won't know query patterns and how they will change and this will cause changes to the column family design

## Chapter 11: Graph Databases

- allow you to store entities and relationships between entities
    - like the data structure
- graph databases usually don't support distributing nodes (i.e sharding) on different servers because fundamentally they operate on relationships between nodes

Suitable use cases:
- connected data: social networks
- recommendation engines
