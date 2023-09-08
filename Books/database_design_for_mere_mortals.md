# Database Design For Mere Mortals

## Chapter 1:

q: "items such as photos, read-only data for web apps, graph data, geospatial data, analytics data" don't quite fit into relational model

## Chapter 2: Design Objectives

- implementing a good design will yield more accurate information, store data more efficiently and effectively and be easier to manage and maintain

## Chapter 3: Terminology

- data: values you store in database
- information: value you retrieve from database
    - people get meaningful information out of the data in the database, i.e information is data processed in some meaningful way

- tables: data is stored in tables which are comprised of records with one or more fields
- field: smallest structure in database, and stores the actual data
    - each field in a properly designed database contains one and only one value. it's name should identify the type of value it holds
    - examples of bad types of fields:
        - multipart field: contains two or more distinct items within it
        - multivalued field: contains multiple instances of the same type of value
        - calculated field: contains a concatenated text value or result of a math expression
- view: virtual table composed of fields from one or more tables in the database
- keys: special fields that play specific roles within a table
    - primary key: uniquely identifies record within a table
        - primary key value identifies a specific record throughout the entire database
        - primary key field identifies a given table throughout the entire database
    - when making a relationship between two tables, you take a copy of the primary key from one table and incorporate it to the second table as a "foreign key"
- index: structures that optimize data processing
- relationships:
    - exist between two tables when you can associate the record of the first table with those of the second
    - every relationship can be characterized in three ways: type of relationship that exists between the tables, the manner in which each table participates, and degree to which each table participates
- types of relationships:
    - one-to-one: a pair of tables has a one-to-one relationship when a single record in the first table is related to zero or one and only one record in the second table and vice versa
        - one relationship where both tables can share the same primary key
        - example: employees table and compensation table can share same employee ID key. every employee will have their associated compensation (in this situation, HR has a lot of work to do managing everyone's separate compensation)
    - one-to-many: a pair of tables has a one-to-many relationship when a single record in the first table can be related to zero, one or many records in the second table, but a single record in the second table can be related to only one record in the first table
    - many-to-many: pair of tables has a many-to-many relationship when both tablles have records that can be related to zero, one, or many records in the other table
        - use a linking table to establish this relationship
        - define linking table by taking copies of the primary key of each table in the relationship -> the two primary keys become the composite primary key of the linking table
- participation:
    - a table's participation within a relationship can be either mandatory or optional
        - e.g a relationship exists between TABLE_A and TABLE_B. TABLE_A's participation is mandatory if at least one record must be entered in TABLE_A before records in TABLE_B can be entered
- degree of participation: minimum number of records that a given table must have associated with a single record in the related table and maximum number of records that a given table is allowed, written as two numbers separated by a comma e.g 1,8
- data integrity: the validity, consistency, and accuracy of the data in a database
    - four types of data integrity:
        - table level integrity: ensures that no duplicate records exist within the table and the field that identifies each record is unique and never Null
        - field level integrity: ensures structure of every field is sound, values in each field are valid, consistent and accurate and fields of the same type are consistently defined throughout the database
        - relationship-levle integrity: ensures relationship between a pair of tables is sound and that the records in the tables are synchronized whenever they are changed
        - business rules: impose restrictions or limitations on certain aspects of a database based on organizational use of data

## Chapter 4: Conceptual Overview

design process:
1. define mission statement and objectives
2. analyze current database (if possible)
3. create the tables
4. determine and create table relationships
5. determine and define business rules
6. determine and establish views
7. review data integrity

## Chapter 5: Starting the Process

- has section on interviewing and writing mission statements that I skipped, but may be useful in the future

## Chapter 6: Analyzing the Current Database

- has more info on interviewing, skipped

## Chapter 7: Establishing Table Structures

table names:
- create a unique, descriptive name that is meaningful to the entire organization
- the name should accurately, clearly and unambiguously identify the subject of the table
- no acronyms or abbreviations
- no proper names
- no name that implicitly/explicitly identifies more than one subject, e.g names with / or &
- use plural form of names

ideal field:
- represents a distinct characteristic of the subject of the table
- contains only a single value
- cannot be deconstructed into smaller components
- does not contain a calculated or concatenated value

## Chapter 8: Keys

keys
- ensure each record in a table is precisely identified
- establish and enforce various types of integrity
- serve to establish table relationships

types of keys:
- candidate keys: field or set of fields that uniquely identifies a single instance. eventually choose one of the candidate keys as the primary key
    - cannot be a multipart field
    - must contain unique values
    - cannot contain Nulls
    - should not cause security issues (i.e dont make a password a candidate key)
    - its value is not optional in whole or in part
    - comprises a minimum number of fields necessary to define uniqueness
    - values must uniquely and exclusively identify each record in the table
    - '' the value of each field within a given record
    - value can be modified only in rare or extreme cases
    - if a candidate key cannot be identified, then create an artificial one
- primary key:
    - identifies the table throughout the database structure and helps establish relationships with other tables
    - uniquely identifies a given record within a table and exclusively represents that record throughout the entire database
- alternate keys:
    - the remaining candidate keys that weren't selected to become a primary key (what's the point of this definition???)


## Chapter 10: Table Relationships

Why relationships are important
- establishes a connection between a pair of tables that are logically related to each other
- helps to refine table structures and minimize redundant data
- lets you draw data from multiple tables simltaneously

self-referencing relationships
- not a relationship formed between tables but inside a table
- a record is related to another record within the same table
- can be one-to-one, one-to-many, many-to-many

identifying existing relationships
- one technique you can use after you've figured out what tables you will need is to use a matrix with the table names written out
- ask two types of questions:
    - Associative: can a single record in one table be associated with one or more records in a second table?
    - Contextual: can a single instance of a subject(table) own, have, be, part of, or contain an instance from a different subject(table)
        - i.e can a student be a part of a class?
    - Contextual: can a subject perform an action on another subject? e.g. make, visit, place, attend, etc
- once you figure out the type of relationship from the questions above, right in the appropriate box 1:1, 1:N (1 to many), M:M (many to many)

establishing relationships:

One-To-One and One-To-Many relationships
- use a primary key and a foreign key to establish the connection between tables participating in a one-to-one or one-to-many relationship
- One-to-One:
    - one table serves as a parent table and the other serves as a child table
    - primary key from parent table becomes a foreign key in the child table
    - a record must exist in the parent table before you can enter a related record in the child table
- One-To-Many relationship
    - take primary key from "one" side of the relationship and put it into the "many" side as a foreign key
- Many-To-Many
    - established with a linking table
        - define linking table by taking copies of the primary key from each table in the relationship and using those keys to form the structure of the table
        - the individual primary keys inserted into the linking table form the linking table's composite primary key
        - can name the linking table something that represents the nature of the relationship between the two tables
        - if there are fields that are no longer appropriate in either table, they could be moved to the linking table

elements of the ideal table:
- represents a single subject - can be an object or event
- has a primary key
- does not contain multipart or multivalued fields
- does not contain calculated fields
- does not contain unnecessary duplicate fields
- contains only an absolute minimum amount of redundant data

Elements of a foreign key:
- same name as the primary key from which it was copied
- draws its value from the primary key to which it refers

Establishing Relationship Characteristics

- can define characteristics like what will happen when you delete a record, type of participation and the degree of participation

Deletion Rules for relationships:
1. Deny: RDBMS will not delete the record in the parent table, but will keep the record and designate it as "inactive"
2. Restrict: RDBMS will not delete the record in the parent table if related records exist in the child table. Must first delete all the related records in the child table before you can delete the record in the parent table
3. Cascade: RDBMS will delete the record in the parent table and automatically delete all related records in the child table
4. Nullify: RDBMS will delete the record in the parent table and update the foreign key values of related records in the child table to Null
5. Set Default: RDBMS will delete the record in the parent table and update the foreign key values of related records in the child table to a default value that has been set

Identifying the type of participation for each table:
- Two types:
    - Mandatory: at least one record must exist in the table before you can enter any records into the related table
    - Optional: no requirement for any records to exist in the table before you can enter records into the related table

Identifying Degree of Participation for each table:

- degree of participation indicates the minimum number of records that a given table must have associated with a single record in the related table and the max number of records that the table is allowed to have associated with a single record in the related table
- indicated by two numbers separated by a comma. e.g 1,5

## Chapter 11: Business Rules

- a business rule is a statement that imposes a constraint on a specific aspect of the database
    - the rules is based on how the organization(business) uses its data
