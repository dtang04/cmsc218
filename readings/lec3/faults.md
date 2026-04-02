# Faults and Partial Failures

- Single Computer - either fails fully function or entirely broke
- Distributed system - no longer idealized system model
  - one dimension of system → partial failures
- If the system can continue operating under failed nodes, it can be easier to maintain and upgrade the system

## Unreliable Networks

- Shared-nothing system: Machines connected only by network

- Most networks in datacenters are asynchronous packet networks. Under this network, there is no guarantee of when a message from one node to another will arrive, or even arrives at all.
  - The only thing the sender knows is whether a response has been received from a server.
  - If the sender doesn't receive the response - impossible to tell why

## Detecting Faults

- Many systems need to detect faulty nodes.

- If a TCP connection is established between Client and node but there is no listening process, OS will refuse TCP connection by sending a FIN packet.

- If a node process crashed, can alert other nodes about the crash

- Commonly, the solution is just to retry sending messages, and timeout if no response.

But, determining the length of time waiting before timeout is also not trivial.
- Asynchronous networks have unbounded delays
- Network congestion / log queue can all lead to slow server processing of incoming requests

## Synchronous vs. Asynchronous Networks

Synchronous Network:
- No queuing of packets
- Maximum end-to-end latency is fixed.
- Telephone calls are an example of a synchronous network.
  - Direct circuit established between sender and receiver, no queue.
- The key constraint in the synchronous network is that a bandwidth allocation must be determined in advance.
- However, requests sent over the internet can be of any size. Thus, TCP dynamically adapts the rate of data to the capacity needed. This requires an asynchronous network with queuing.

## Node Failure Detection

- Typically a node is declared unresponsive by a quorum, or an (absolute) majority of more than half the nodes.

- Using quorums to make decisions rather than single nodes can make the system resilient to individual node failures.

- However, many operations (such as DB writes) require one node (the leader) to commit the action. If multiple nodes had concurrent writes, it could lead to DB corruption.
  - Incorrect Synchronization (such as leader node continues to hold on to a lock after lease expires), can lead to simultaneous writes to DB, causing corruption.

- One way to resolve a node that falsely believes it is leader is called fencing.
  - Every time a lock is granted, a fencing token is produced. To write to DB, a node must not only believe that it is leader, but also have the fencing token as well. If a node writes to DB without the fencing token, the write is rejected.

```
TIME --->

1. Client 1 requests lock
   Client 1  -----> Lock Service
                    "get lease"

2. Lock Service grants lease with token 33
   Client 1 <----- Lock Service
                   "ok, token: 33"

3. Client 1 enters GC pause (unaware of time passing)
   |                                          |
   |  Client 1: [stop-the-world GC pause...]  |
   |                                          |

4. Lease expires; Client 2 requests and gets lock with token 34
   Client 2 -----> Lock Service
                   "get lease"
   Client 2 <----- Lock Service
                   "ok, token: 34"

5. Client 2 writes to storage with token 34
   Client 2 -----> Storage
                   "write, token: 34"
   Client 2 <----- Storage
                   "ok"

6. Client 1 wakes from GC, tries to write with stale token 33
   Client 1 -----> Storage
                   "write, token: 33"
   Client 1 <----- Storage
                   "REJECTED: old token"
```

- The above diagram shows that because of stop-the-world garbage collection, client 1 was unable to get the alert from the lock that its lease has expired. However, because its fencing token has outdated, the write to DB has rejected.

## Byzantine Faults

- The fencing token scheme works under the assumption that all nodes behave like they're supposed to.
  - What if a node deliberately tries to subvert the system? → node can easily generate a fake fencing token

- A system is Byzantine fault tolerant if some nodes can malfunction and not obeying the protocol.
  - Implementing Byzantine fault tolerant systems are expensive and difficult
  - Most applications take node requests as granted, because the server can parse client requests and invalidate requests that don't follow protocol.
  - But, Byzantine faults are applicable to peer-to-peer networks, where there isn't a centralized server processing requests from nodes

Simple mechanisms to correct corrupted data include:
- Checksums - simple functions like outputs change when incoming packets are corrupted
- Sanitization of incoming requests
- Multiple Servers - Client sends same request to multiple servers. If one server returns a response not like the others, that server is considered unreliable and excluded from synchronization.

## System Models

- Synchronous models assume an upper bound on network delay, process pauses, and clock drift.
  - Impractical in reality

- Partial Synchronous model: The upper bound set by synchronous model is respected most of the time, but sometimes exceed the upper bound.
  - Often the benchmark for most systems

- Asynchronous model: Client cannot make any timing assumptions about server
  - Very restrictive

## Types of Faults

- Crash-stop fault - system has to handle cases where nodes stop responding, typically from crashing. After a node fails, it never comes back.

- Crash-recovery fault - System assumes that nodes may crash at any moment, but may begin responding again after some unknown time (typically used in systems)

- Byzantine fault - System assumes that nodes may do absolutely anything

## Safety vs. Liveness

- Safety - guarantees that the algorithm must satisfy even with system faults.
  - Once property of safety is violated, cannot be undone
  - Ex. Even if all nodes crash, the algorithm must ensure that a wrong result is not returned to the client.

- Liveness - an algorithm property may not hold at some point in time, but there is hope that the property can be satisfied in the future.
  - Ex. An algorithm needs only to respond to client request if a majority of the system's nodes are up.
