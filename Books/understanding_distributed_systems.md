# Understanding Distributed Systems - Vitillo

### Chapter 1: Introduction

"A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable"

\- Leslie Lamport

**What is a distributed system?**

Loosely, a distributed system is a group of nodes - can be a phone, a computer, a browser, that cooperate to achieve some task by communicating with each other

**Why build a distributed system?**

Some applications are inherently distributed. The web is a distributed system that you can access along with billions of other devices.

Some applications require high availability and need to be resilient to failures of nodes. By storing data across multiple nodes, losing one node means you will not lose all of your data.

Some applications perform so many operations that they need multiple nodes to handle the operations. For example, millions of people access Youtube and watch videos so they need thousands of servers to stream video.

Performance requirements, like latency will require a distributed system to succeed. If a client is in Australia and the servers are only in Western Europe, the latency will be huge. So we can have a Western Europe node for Western European clients and vice versa.

#### Important Ideas in Distributed Systems

- Communication
    - how are the messages represented?
    - what happens in an outage?
    - how do we make communication secure?
- Coordination
    - how do we coordinate the system to perform tasks in the prescence of failures? i.e. messages can fail to transmit and how do we get around this?
- Scalability
    - performance of a distributed system is generally measured with throughput (operations/second) and response time (total round trip for request and response)
    - as load increases, a system will reach its ***capacity*** and beyond this point, the system can plateau or worsen and eventually fail or timeout
    - generally want to scale out - add more machines to the system
- Resiliency
    - a system is resilient when it can continue to work even when nodes fail, network links are severed, etc
    - availability: amount of time the application can serve requests divided by the duration of period measured
    - a distributed system should embrace failure and work around it using redundancy and self-healing mechanisms
- Operations
    - distributed systems need to be tested, deployed and maintained

### Anatomy of a Distributed System

From an implementation perspective, a distributed system is a set of loosely-coupled components that can be deployed and scaled independently called services.
Services talk to each other ia inter-process communication (IPC) mechanisms like HTTP.

- a service is software that implements one specific part of an overall system's functionality
- a service will expose interfaces to communicate with the web
- adapters like APIs are used to connect IPC mechanisms to the service's interfaces
- a process running a service is called a server, a process that sends requests to servers is called a client. a process can be both.

## Part 1: Communication

Communication between processes over the network, or ***inter-process communication***, is at the heart of distributed systems. Network protocols are arranged in a stack, where each layer builds on the abstraction provided by the layer below, and the lower layers are closer to the hardware.

The link layer (layer 4) consists of network protocols that operate on local network links, like Ethernet or Wi-Fi.

- provides an interface to the underlying network hardware
- switches operate at this layer and forward Ethernet packets based on their destination MAC address

The internet layer (5) uses addresses to route packets from one marchine to another across the network

- Internet Protocol (IP) is the core protocol of this layer
- Routers operate at this layer

The transport layer (6) transmits data between two processes using port numbers. TCP is the most important protocol in this layer.

The application layer (7) defined high-level protocols, like HTTP or DNS. Typically code will target this level.

### Chapter 2: Reliable Links

#### TCP
- transport-layer protocol that allows you to have a reliable communication method between two processes
- built on top of IP
- guarantees that a stream of bytes arrives in order, without gaps, duplication or corruption
- also has stability patterns to avoid overwhelming network or receiver

#### 2.1 Reliability

- TCP partitions a byte stream into packets called segments
- the segments are sequentially numbered so that the receiver can detect holes and duplicates
- each segment needs to be acknowledged by the receiver, and if that doesn't happen then the segment is retransmitted

#### 2.2 Connection lifecycle

- a connection needs to be opened before any data can be transmitted through TCP
- the state of the connection is managed by the OS
- TCP uses a three-way handshake to create a new connection
    - sender picks a random sequence number x and sends a SYN segment to the receiver
    - the receiver increments x, chooses a random sequence number y and send back a SYN/ACK segment
    - sender increments both numbers and replied with an ACK segment and first bytes of data
    - sequence numbers are used by TCP to ensure data is delivered in order

#### 2.3 Flow control

- receiver stores incoming TCP segments in a receive buffer and receiver communicates the size of the buffer whenever it acknowledges a segment
- if sender is following TCP protocol properly, then it will avoid sending more data than can fit in the bugger

#### 2.4 Congestion control

- TCP also tries to avoid overwhelming the network
- tries to estimate the bandwidth of the network and maintains a "congestion window" which represents the number of segments that can be sent without an acknowledgement from the other side
- round trip time and # of lost segments will adjust this congestion window

### Chapter 3: Secure Links

To encrypt our data, we use the Transport Layer Security (TLS) protocol.

TLS runs on top of TCP and encrypts the communication channel so protocols like HTTP can communicate securely.

#### 3.1 Encryption

- when TLS connection is first opened, the client and server negotiate a shared encryption secret using asymmetric encryption
    - asymmetric encryption is when both parties generate a key-pair with private and public parts
    - the secret is generated by a one way function
    - messages are encrypted with the secret key and then can be decrypted with the public key

#### 3.2 Authentication

- client has no idea whether the public key shared by the server is authentic, so we have certificates that are used to prove ownership of public keys
- certificates are isues by certificate authorities

#### 3.3 Integrity

- data can still be tampered, like bits can be swapped
- to protect against this, TLS calculates a hash of the message

### Chapter 4: Discovery

We need to be able to discover IP addresses to make connections.

To resolve hostnames into IP addresses, we have DNS, which we can think of as the phonebook of the internet.

DNS resolutions process when you type in `www.example.com`

1. Browser checks whether is has resolved the hsotname before in local cache. If yes, returns cached IP address. If no, routes request to DNS resolver. DNS resolver is usually a DNS server hosted by ISP.
2. DNS resolver responsible for iteratively translating hostname for client. Resolver first checks local cache. If not found, query goes to root name server (root NS).
3. Root name server maps the top-level domain (TLD) like `.com`, `.ca` to the name server
4. TLD name server maps domain name of a request to the authoritative name server. Authoritative name server is responsible for a specific domain and holds all records that map hostnames to IP addresses within that domain
5. Resolver queries authoritative name server for `www.example.com` and gets the IP address

### Chapter 5: APIs

Communication style between a client and a service can be direct or indirect. Direct communication requires both processes to be up and running for communication to succeed.

one style of direct communication is called `request-response`, in which a client sends a `request` and the service replies with a `response`

- request and response messages contain data serialized in a language-agnostic format
- most common IPC for request-responise are gRPC, REST and GraphQL

## Part 2: Coordination

We want to be able to use multiple services, processes to build a distributed application that appears to clients as if you are intereacting with a single machine.

This section will discuss the core algorithms to coordinate distributed systems.

### Chapter 6: System Models

There are models of behaviors of nodes, communication links and timing that allows us to reason about distributed systems by ignoring the complexities.

Communication models:
- fair-loss link: messages may be lost and duplicated, if sender keeps resending, it will eventually be delivered to destination
- reliable link: a message is delivered exactly once without loss or duplication
    - like TCP
- authenticated reliable link: same assumptions as reliable link but receiver can authenticate the message's sender

Node failure models:
- arbitrary-fault: node can deviate from its algorithm in arbitrary ways, leading to crashes or unexpected behavior due to bugs or malicious activity
    - out of scope for book
- crash recovery: node doesn't deviate from algorithm, but can crash and restart at any time, losing in-memory state
    - mostly look at these models in this book
- crash-stop, node doesn't deviate from algorithm. but if it crashes it doesn't come back online

Timing models:
- synchronous model: sending a message or executing an operation never takes over a certain amount of time
    - unrealistic
- asynchronous: sending message/executing operation can take infiinite time
    - many problems can't be solved under this assumption so not useful
- partially synchronous: both of the above. behaves synchronously most of the time, but can become asynchronous.

### Chapter 7: Failure Detection

a process shouldn't need to wait until sending a message to find out a destination is unavailable

you can try to maintain a list of available processes by using pings or heartbeats

ping: periodic request that a process sends to another to check if it's still available

heartbeat: a message that a process periodically sends to another to inform that it is still up

pings and heartbeats are used when processes communicate frequently with each other. if not, failure detection at communication time is OK

### Chapter 8: Time

- time plays an important role in figuring out the flow of execution
- in a distributed system, there is no global shared clock that all processes agree on
- learn about logical clocks which measure passage of times in terms of operations

#### 8.2 Logical Clocks

- a logical clock measures the passing of time in terms of logical operations

**Lamport Clock**
- every process has its own local logical clock with a numerical counter
- counter is initialized at 0
- process increments its counter before executing an operation
- when the process sends a message, it increments its counter and sends a copy of it in the message
- when the process receives a message, its counter is updated to 1 plus the maximum of its current counter and the message's counter
- rules guarantee that if operation A happened before operation B, then the logical timestamp of A is less than B
    - the reverse doesn't apply

#### 8.3 Vector clocks

- a logical clock that guarantees that if two operations can be ordered by their logical timestamps, then one must have happened before the other
- implemented with a dictionary of counters, one key-value pair for each process in the system
- each process has its own local copy of the clock
- rules are very similar to lamport clock, just that each process updates its own counter in the dictionary
- if timestamps can't be ordered, then the operations are considered to be concurrent

Important takeaway: can't use physical clocks to derive order of events on different processes

### Chapter 9: Leader Election

Sometimes a process needs to have higher privileges like being able to have write access to resources or being able to delegate work to others. For this to happen, we need the system to be able to elect leaders and be able to elect new ones if the leader becomes unavailable.

A leader election algorithm needs to guarantee that there is at most one leader at any given time and that an election eventually completes.
- the two properties are called safety and liveness

#### 9.1 Raft Leader Election

- in this algorithm, a process can be in one of three states:
    - follower state, in which a process recognizes another as a leader
    - candidate state, process starts a new election proposing itself as a leader
    - leader state, in which process is the leader

- time is divided into ***election terms*** of arbitrary lengths represented with a logical clock
- election terms begin with a new election
- election is triggered when a follower fails to receive a periodic heartbeat from the leader containing the election term the leader was elected in
    - some predefined timeout period
- follower starts a new election by incrementing the election term and transitioning to the candidate state
- follower votes for itself and sends a request with the current election term to all processes in the system to vote for it
- other processes in the follower state will respond to requests on a first-come-first-serve basis
- election ends if a candidate gets a majority of the votes
- a process will remain in the candidate state until it wins, loses or the election times out (i.e a tie)
    - in case of a tie, another election will start

#### 9.2 Practical Considerations

- Raft is one modern take on the leader election algorithm, but you will never need to implement from scratch as there are projects that abstract away the implementation such as etcd and ZooKeeper

### Chapter 10: Replication

- replication is an important part of distributed systems
- replication enables availability, scalability and higher performance
    - data can be stored on more than one node -> availability
    - if data is on more than one node, then each node can provide access concurrency -> scalability + performance
- challenge of replication is consistency
- based on a technique called state machine replication where a single process, the leader, broadcasts operations that asks its followers to change its state, which will then make the followers state consistent with the leader
    - however with network failures, and process failures we need fault tolerance

#### 10.1 State Machine Replication

After a leader is elected with Raft's leader election algorithm, we have a process that is able to make exclusive changes to the state.

- leader will keep track of a log that clients ask of the system. the leader does not alter its local state yet.
    - log contains the operation to be applied to the state, the index of the entry and the term number
- leader will send messages to its followers with the contents of the log entries
- when a follower receives new log entries, it appends the new entries to its local log and sends a message to acknowledge the change in state
- when leader hears back from a majority of followers, it considers the entry to be committed and executes the operation in its local state

We can see from the above algorithm that it is possible that in the event of a leader failure that there are processes with out of date state. To prevent these processes from becoming leaders, only candidates with all committed entries may win.
- in the election process, term and (if necessary) log indexes will be compared to determine if a candidate is valid

#### 10.2 Consensus

Consensus is a problem in distributed systems where a set of processes agree on a value such that:
- every non-faulty process descides some value
- every non-faulty process eventually agrees on a value
- final decision of every non-faulty process is the same everywhere

#### 10.3 Consistency Models

- since only the leader can make changes to the state, any operation that modifies state needs to go through the leader, but what about reads?
- reads can be served by leader, follower or any combination
- since followers are not necessarily consistent with the leader, two clients may have different views of the system's state if they query different processes

**Strong Consistency**

- also known as linearizability, is one of the strongest single-object consistency model and implies that every operation appears to take place atomically in an order consistent with the real time ordering of operations
- reads and writes will go exclusively to the leader, leader needs to check with the followers to make sure it is still the leader before responding to a request
    - increases time to serve a read

**Sequential Consistency**

- model in which operations appear to take place in some order which is consistent with the order of operations on each individual process
- followers can lag behind the leader, but it will always receive updates in the same order as the leader
- have to pin clients to followers

**Eventual Consistency**

- model in which the client is only guaranteed that the followers will converge to a final state if writes stop

**CAP Theorem**

- theory that says that you choose two of three of: strong consistency, availability and partition tolerance
- in reality, network faults are a given so the choice is between strong consistency and availability
- an alternative PACELC theorem states that in the case of a network partition (P) in a distributed computer system, you choose between availability (A) and consistency (C), else when the system is running normally without partitions, you have to choose between latency (L) and consistency (C)
    - the stronger the consistency, the higher the latency of individual operations

### Chapter 11: Transactions

Transactions allow a group of operations to appear uniform and have exclusive access to modify some data. The operations will all complete successfully or none will complete.

#### 11.1 ACID

In a traditional relational database, a transaction is a group of operations for which the database guarantees a set of properties, known as ACID

- Atomicity (A) guarantees that transactions are all or nothing
- Consistency (C) guarantees that application/database level constraints like a column can't be null is always true
    - different from the consistency we talked about before
- Isolation (I) guarantees that concurrent execution of transactions doesn't cause any race conditions
- Durability (D) guarantees that once the data store commits the transaction, the changes are persisted on durable storage
    - a write-ahead log (WAL) is used to ensure durability

#### 11.2 Isolation

Concurrent transations that access the same data can run into all sorts of race conditions:
- dirty write: when a transaction overwrites a value written by another transaction that hasn't been committed yet
- dirty read: happens when a transaction observes a write from a transaction that hasn't completed yet
- fuzzy read: happens when a transaction reads an object's value twice, but sees a different value in each read because a committed transaction updated the value between the two reads
- phantom read: when a transaction reads a set of objects matching a specific condition, while another transaction writes to it - causes the read to be wrong after commit

To protect against race conditions, transactions need to be isolated from others
- isolation levels protect against race conditions and allows us to reason about concurrency
- the stronger the isolation the less performant

Examples of isolation levels:
- Read uncommitted: protects against dirty writes
- Read committed: protects against dirty reads
- Serializable: Forbids all four of the listed race conditions
    - guarantees that the side effects of a set of transactions appear to be the same as if they were executed sequentially
    - doesn't say anything about the order

**Implementing Serializability**

- can be achieved with a pessimistic or an optimistic concurrency control mechanism

Pressimistic Concurrency Control
- pessimistic concurrency control uses locks to block other transactions from accessing a data item
    - most popular protocol is two-phase locking (2PL).
    - 2PL has two types of locks, one for reads and one for writes
    - read lock can be shared by multiple transactions that access data in read-only, but it blocks transactions from acquiring a write lock
    - write lock can only be held by a single transaction and blocks anyone else from acquiring read/write lock on a data item
    - as name implies, 2PL has two phases: expanding and shrinking
        - expanding: transaction allowed only to acquire locks
        - shrinking: transaction allowed only to release locks
        - if rules obeyes protocol guarantees serializability

Optimisic Concurrency Control
- no blocking, only checks for conflicts at the end of a transaction
- if conflict detected, transaction is aborted or restarted
- makes sense to use if you have read-heavy workloads as you don't want to be retrying the same transactions for performance reasons

#### 11.3 Atomicity

- guarantee that either all operations succeed or all fail

**Two-phase commit (2PC)**

- protocol used to implement atomic transaction commits across multiple processes
- split into two phases: prepare and commit
- assumes a process acts as coordinator and orchestrates other processes called participants
    - usually client application that initiates transaction acts as the coordinator
- when coordinator wants to commit a transaction to its participants, it sends a prepare request to the participants, if all participants reply that they are ready, the coordinator sends out a commit message
    - if any process replies that it is not ready, coordinator sends an abort request to all participants
- since this is a synchronous blocking protocol, if any of the participants isn't available the transaction can't make any progress

#### 11.4 Asynchronous transactions

- some transactions may take hours to execute, in which case blocking behaviour would be quite detrimental. Are there asynchronous non-blocking solutions that provide atomicity?
- with a message log we can solve this issue
- a log is an append only, totally ordered sequence of messages which consumers read in order
- say we have two services that both need to update their state atomically. the services will both consume messages from the log and update their state
- messages should be idempotent so that they can be re-read

## Part 3: Scalability

Introduction to 3 aspects of scalability:
- functional decomposition
    - taking an application and breaking it down into individual parts
- partitioning
    - splitting things up in multiple nodes
- duplication
 - creating more instances

### Chapter 12: Functional Decomposition

#### 12.1 Microservices

- as a monolith grows, its components become more coupled over time and makes it harder for teams to modify the codebase, decreasing productivity
- one way to mitigate this is by splitting up the monolith into independent services that communicate via API, called microservices

Pros:
- each service can be developed and operated by a single small team
- a single team can increase velocity:
    - smaller team can communicate more effectively
    - codebase is smaller and easier to digest
    - boundaries between services are stronger
    - each service can be scaled independently

Costs:
- testing the integration of all the microservices can be challenging
- debugging becomes challenging as code is executed on many machines

From a practical perspective, good to start as a monolith then split into microservices as needed.

#### 12.2 API gateway

- a service that exposes the public API and acts as a layer for redirection is called the API gateway
- API gateway provide features liek routing, composition and translation
    - composition: query multiple services and compose their responses to a single one and return to client

#### 12.4 Messaging

- a form of indirect communication, meaning that the services do not have to be available for an immediate response
- producer writes a message to a channel that delivers the message to a consumer on the other end
- allows client to execute an operation on a service asynchronously
    - useful for operations that can take a long time to execute, like processing video
- can load balance and smooth out load by only allowing consumers to read messages at a specific pace

Two different types of channels:

1. point-to-point: specific message is delivered to exactly one consumer
2. publish-subscribe: copy of same message is delivered to all consumers

Communication styles:
- one-way messaging: producer writes a message to a point-to-point channel with expectation that a consumer will eventually read and process it
- request-response messaging: similar to regular request response except it goes through a point to point channel
- broadcast messaging: producer writes a message to a publish-subscribe channel to broadcast it to all consumers
    - generally used to notify services of events

Tradeoffs:
- order guarantees: since a message broker needs to scale, its implementation is also distributed and coordination is required, so many messsage brokers will forgo order for simplicity
- delivery guarantees: at-most-once versus at-least-once
- message durability
- latency
- message size

Failures:
- if a message continuously fails, send it to a dead letter channel, for a person to manually inspect.
    - cant delete as you would have data loss

Fault isolation:
- a specific producer can emit bad messages that can degrade the system
- have messages contain identifier so we can filter the bad producer to a low priority channel
