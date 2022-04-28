# Is MapReduce becoming obsolete or is Spark replacing it?

## ABSTRACT

In the world of advancements in every field and every study, the section of Big Data and its frameworks are also evolving based on the requirements of the users and to make sure that they are maintained to be user friendly. Choosing the right one from the multiple frameworks available is always a crucial decision that needs to be made by the user. We are going to compare two big frameworks in big data, that are MapReduce and Apache Spark. We will evaluate the major features of each cluster computing framework based on similar situations and understand the reasons why one of these is being replaced by the other one. Further in this paper we will look at the architecture of the frameworks, their advantages, disadvantages, and application in the real-time world of big data and analyze the importance of both programming languages. In addition, the word MapReduce being obsolete will also be answered based on various short-term and long-term scenarios and transitions.
<br />
<br />

## Table of contents

**I. Introduction**
     
     1.1 What is Big Data and its significance in the current world
     1.2 Big Data analytics tools
     1.3 History of MapReduce
     1.4 History of Apache Spark

**II. Architecture**
     
     2.1 Framework of MapReduce
     2.2 Framework of Apache Spark


**III. MapReduce Vs Spark**
     
     3.1 Comparison between MapReduce and Spark
     3.2 Genre of comparison
     3.3 Sparks' major use cases over MapReduce

**IV. Is MapReduce Obsolete?**
    
     4.1 MapReduce then and now
     4.2 Application of MapReduce in short term and long term
     4.3 Challenges faced or to be faced by the users
     4.4 Road map for the transition 

**V. Conclusion**

**VI. Sources** 

<br />
<br />
<br />
<br />
<br />
<br />
<br />

## **I. INTRODUCTION:**

### *1.1 Big Data and its significance in the current world*

In this age of the modern era, big data plays a major role in the data management system and helps us perform day-to-day activities. This is an open-source software where java frames work is used to store, transfer, and calculate the data. Big data refers to vast and voluminous data sets that may be structured or unstructured and involve the process of examining large data sets to underline insights and patterns. This has been a revolution in the field of Information Technology. Big data analytics leads to intense competition and increased demand for big data professionals in the current world. They have a significant impact on various areas of work. Big Data has seen rapid growth in the market and it's getting a lot easier to automate procedures and decision making. 
<br />
<br />
<br />

### *1.2 Big Data analytics tools*

The availability of huge and scattered file systems makes it difficult to analyze and process the data. Hence several tools and techniques are used to analyze such big and scattered data namely, Apache Hadoop, MapReduce, Spark, Storm, MongoDB, NoSQL, HPCC, KNIME, OpenRefine, etc. These tools help businesses in saving time and money and also in gaining insights to make data-driven decisions. Each of these tools is differently built which bring cost-saving benefits to business when they have to store large amounts of data. These also help in understanding the market conditions such as behavioral analysis that helps companies go ahead of their competitors.
<br />
<br />
<br />

### *1.3 History of MapReduce*

MapReduce was first popularized as a programming model in 2004 by Jeffrey Dean and Sanjay Ghemawat. MR allows for the distributed processing of the map and reduction operations. Initially, Apache, the open-source organization, began using MapReduce in the "Nutch" project, which is an open-source web search engine that is still active today. This performs filtering and sorting and a reduce method which performs a summary operation. This model is a specialization of the split-apply-combine strategy for data analysis. The libraries have been written in many programming languages, with different levels of optimization. In the eCommerce industry, several major players use Map Reduce for high-volume data processing. 

<br />
<br />
<br />

### *1.4 History of Apache Spark*

According to Databrick’s definition “Apache Spark is a lightning-fast unified analytics engine for big data and machine learning. It was originally developed at UC Berkeley in 2009.” Apache Spark is one of the largest open-source projects for data processing, it has a fast and in-memory data processing engine. Spark was initially started in 2009 in UC Berkley R&D lab, known as AMPLab. This is considered a unified analytics engine for large-scale data processing.
<br />
<br />

<img src="https://d2o2utebsixu4k.cloudfront.net/tutorials/topics/images/1576839932046-Apache-Spark---Module-3---Text-tutorial--Nithin-[Kh-Copy]_.jpg" width="600"/>

<br />
<br />
<br />
<br />
<br />

## **II. ARCHITECTURE:**

### *2.1 Framework of MapReduce*

MapReduce is a software framework that enables writing applications that process a vast amount of data. The framework sorts the output of the maps, which are inputted to the reduced tasks, having both the input and output of the job stored in a file system. This takes care of scheduling tasks, monitors them, and re-executes the failed tasks. This framework has a Master-slave architecture that integrates with HDFS to provide the same benefits for parallel data processing. This has phases that include mapping, shuffling, sorting, and reducing. This helps in enabling you to work on large clusters of commodity hardware, in a reliable and fault-tolerate manner.  The code in MapReduce can be written in Java, C, and scripting languages. In MR programs are automatically parallelized and executed on a runtime system that manages to partition the input data, schedule execution, and manage communication, including recovery from machine failures.
<br />
<br />

<img src="https://cdn.thegeekdiary.com/wp-content/uploads/2018/09/mapreduce-framework-phases-sort-shuffle-and-reduce.png" width="300"/>
<br />
<br />
<br />

### *2.2 Framework of Apache Spark*

Apache is a framework that supports in-memory processing to boost the performance of applications that analyze big data. This involves extracting, Transforming, and Loading steps in processing the data. ETL is the process of collecting data from one or multiple sources, modifying the data, and moving the data to the new data store. This includes several ways such as filtering, sorting, joining, cleaning, validating, etc. Spark supports various languages including Scala, Python, Java, SQL, R, and .NET languages. The architecture of Spark includes three main components: the driver, executors, and cluster manager. The applications of Spark run as independent sets of processes on a cluster, coordinated by the driver program.
<br />
<br />

<img src="https://docs.microsoft.com/en-us/dotnet/spark/media/spark-architecture.png" width="300"/>
<br />
<br />
<br />
<br />
<br />

## **III. MAPREDUCE Vs SPARK:**

### *3.1 Comparison between MapReduce and Spark*

The differences between MR and Spark can be explained in 5 categories. These categories help us to decide or make a better choice choosing one of them for data processing tasks. Spark was invented after MR, it was designed to be faster than MapReduce and sometimes Spark can be 100 times faster than MR based on real-time examples. Concerning Performance, Spark uses RAM to process the data and stores intermediate data in memory which reduces the amount of reading and write cycles on the disk, however, MR reads and writes data directly from the disk. Spark's capabilities in performance can suffer if the data sources are too large to fit entirely in the memory and on the other hand, MR kills its processes immediately after completing them. Referring to Operability, Spark is easier to program than MR, as MapReduce is often said to be very difficult to program and the framework is written in Java and it does not have an interactive mode for users to run commands and get immediate feedback. Spark also includes interactive tools that MapReduce cannot offer users. Data Processing can be effectively done by both, Spark has a loaded ML library which helps it do more than just process plain data. MR is good at batch processing, however, to process graph or real-time data processing MR will need an additional platform to support it. MapReduce could be the best batch processing tool ever created, but not as agile as Spark when it comes to being able to perform a wide variety of data processing skills. Discussing the differences based on Failure recovery, as MR relies on hard drives instead of RAM, it is better suited for recovery after failure than Spark and MR can hold its place if it crashes in the middle of a task. The Security of data and its processing is of the highest priority, the tools used in Spark could potentially leave you and your data vulnerable to attacks, hence Spark is less secure than MR.
<br />
<br />

Spark is a complete data analytics engine and is the undisputed choice for data science use cases, however, Spark needs a lot of memory and if the memory is not enough for the data to fit in, it might lead to major degradation in performance. MapReduce is used for dealing with the data when it is not possible to fit into memory. This explains that Spark provides lesser latency than that MR. Because of the interaction with a hard disk, MR is less tolerant to failure and might not require a full restart in case of any disruption to the process, but Spark can cause disruption to the process as its operations occur in memory and it needs to be started from the initial point if failed in between.
<br />
<br />
<img src="https://k21academy.com/wp-content/uploads/2018/10/Capture-1.png" width="350"/>

<br />
<br />

### *3.2 Genre of comparison*
Comparing both tools using a specific category to better understand the importance and implication of each one of them depending upon our data sets and expected outcomes.
<br />
<br />

>Category of Product: MR is majorly a data processing engine, whereas Spark drives complete analytical solutions and hence can be considered as a data analytics engine.
<br />

>Framework's Performance: In MapReduce reading and writing operations are performed from and to a disk, leading to slowness in the processing speed, however, in Spark, these are minimized along with the data-in-memory allowing it to be 10 times faster but this may suffer degradation if data doesn't fit in memory.
<br />

>Latency: Due to lesser performance than Spark, MR has higher latency in computing, whereas Spark being faster, enables developers with low latency computing.
<br />

>Real-time Analysis: MapReduce was built mainly for batch processing and therefore fails when used in real-time analysis cases. In the case of Spark data from the real-time live streams can be managed and processed efficiently.
<br />

>Interactive Mode: Spark has the possibility of processing the data interactively, whereas MR does not provide an interactive mode.
<br/>

>Tolerance of Failure: In case of any crash, the MapReduce process is capable of starting from the place where it was left off earlier as it relies on hard disks, whereas Spark should start the processing from the beginning and hence becomes less fault-tolerant than MR as it relies on RAM.

<br />

### *3.3 Sparks' major use cases over MapReduce*

Spark has few advancements in its procedure of processing the data. This was invented to overcome the drawbacks of MR over the period and to improvise the procedure of data analysis. One of the major use cases Spark has over MR is the implementation of iterative algorithms in Machine Learning. Unlike MR, Spark also has interactive data mining and processing. This helps the users to understand and work on the data more effectively and with ease. As Spark is a fully Apache Hive-compatible data warehousing system, that can run 100 times faster than that MapReduce. Spark is capable of stream processing, which helps in fraud detection and log processing in live streams for analysis, aggregates, and alerts while streaming. In the case of data being fetched and combined from multiple sources, an in-memory dataset is helpful as they are easy and fast to a process called Sensor data processing. Spark outshines engines when it deals with column-oriented efficient and compressed storage format. Most importantly 100lines of code needed in MR can be replaced with 10 lines using Spark representing the efficiency and ease of the code in Spark.

<br />
<br />
<br />
<br />
<br />

## **IV. IS MAPREDUCE OBSOLETE?:**

### *4.1 MapReduce then and now*
Though we see many drawbacks or limitations concerning MapReduce in the current world of big data processing, we can overcome old pain points and reap the full benefits by incorporating new capabilities into this tried-and-true framework. This framework which was introduced in 2004 had many transitions and improvisations since then. Many systems like Hadoop, CouchBase, and MongoDB used MR as a query engine in the 2000s. MapReduce is not essentially outdated, but instead, the problems that it solves are situations we now try to avoid in our daily course of business. However, getting the data in and out of clusters is difficult. Since the traditional "MR" is a batch processing framework and hence that is not what we work on these days. As we are working on data beyond just batch processing the adoption of MR in real-time cases is reduced over the period. However, it still exhibits higher flexibility and fault-tolerance capacity than Spark
<br />
<br />

### *4.2 Application of MapReduce in short term and long term*
Considering the advantages and limitations of MR, there are 2 reasons to justify that it will not be obsolete in short term. The companies using MR have already made huge investments in developing the applications used by MR and this will not motivate them to destroy the entire setup and opt for new execution engines. We still see many companies that use legacy applications as the users are comfortable working on them. The other reason is that MR is still the best tool for maturity and throughput for non-iterative batch processing. However, considering the long-term applicability of MR, it is anticipated to be minimal by various industry ruling companies. MR will continue to decline in favor of other frameworks and platforms. As Spark is better at utilizing memory from clusters which promotes better real-time performance, it is evident and expected that Spark will replace MR in long run. 
<br />
<br />

### *4.3 Challenges faced or to be faced by the users*
Users working on MapReduce face a few challenges in the current situation, these include difficulty in writing the code as it takes many command lines to process the data which is comparatively higher than that of Spark and other frameworks. Data storage and support capabilities are also a major pullback for the users, application deployment support is very difficult. Managing multiple application integrations on a production scale is difficult in MR. The trend of the current world, Machine Learning algorithms, is difficult to scale in MR and also there are statistical and computational charges
<br />
<br />


### *4.4 Road map for the transition*
Considering the above-discussed limitations and complexities of MapReduce, if we decide to phase out completely or partially from the cluster, the road map is not as hard as most people think. Many companies provide a smooth transition from MR to Spark with zero downtime supported by real client experiences. They implement this transition by considering the inventory's existing code, configurations, and other components. The reusability of components is provided such as java libraries which can be used directly in spark without any changes. MR can replace with cycles of automated testing and bug fixes. Hence if anyone prefers to shift, they have resources and services that help in the easy transition.

<br />
<br />
<br />

## **V. CONCLUSION:**
Understanding all the differences between MapReduce and Spark, though they have many differences, they do have a few similarities too. Deciding on the question of whether the MR is outdated, yes to an extent it is because of much flexible support Apache Spark provides to its users. We also see many companies like Google which had MR as their primary data processing model in 2014 are transitioning from MR to Spark. This states that in long run we may see Spark completely taking over MapReduce. Although MR follows a restricted programming framework, it will have greater applicability if new potential features are added to it. MapReduce is for now obsolete based on the requirements of the users and the market but may have future implementations if it is upgraded to meet the requirements.

<br />
<br />
<br />

## **VI. SOURCES:**
<br/>

6.1 [Is MapReduce Dead by JADE GLOBAL,2017](https://www.jadeglobal.com/blog/mapreduce-dead)

6.2 [Why MapReduce is making a comeback by PHIL FRIED,2021](https://www.estuary.dev/why-mapreduce-is-making-a-comeback/#:~:text=That%E2%80%99s%20not%20because%20MapReduce%20itself%20is%20outdated%2C%20but,big%20cluster%2C%20and%20the%20data%20is%20already%20there.)

6.3 [Spark Vs MapReduce:Key Differences by Jonathan Tarud,2021](https://www.koombea.com/blog/spark-vs-mapreduce-key-differences/)

6.4 [MapReduce Vs Spark by EDUCBA](https://www.educba.com/mapreduce-vs-spark/)

6.5 [Spark & MapReduce: Introduction, Differences & Use Case by Surbhi Sharma,2018](https://k21academy.com/big-data-hadoop-dev/spark-vs-mapreduce/)

6.6 [Mapreduce in BigData](https://hkrtrainings.com/mapreduce-in-big-data)
 
 6.8 [Is MapReduce outdated? by Ibis Solution, 2021](ibis-solutions.rs/en/insights/is-mapreduce-outdated/)

 6.9 [Map Reduce is Dead, Long Live Map Reduce by Jeffrey Aven,2019](https://www.linkedin.com/pulse/map-reduce-dead-long-live-jeffrey-aven/)

6.10 [Overview of Apache Spark](https://www.geeksforgeeks.org/overview-of-apache-spark/)

 6.11 [Understanding the Hadoop MapReduce framework](https://www.thegeekdiary.com/understanding-the-hadoop-mapreduce-framework/)


