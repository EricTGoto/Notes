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
