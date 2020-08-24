<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Database Design Assessment - Game Distribution](#database-design-assessment---game-distribution)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Database Design Assessment - Game Distribution

*Student: Jordan Pyott \
ID: 87433186*

During the construction of the game distribution Extended Entity Relationship Model,
there were many assumptions made about the information provided to map this model.

When mapping the `CUSTOMER_ACCOUNT` and its ability to `ACCEPT_FRIEND`, the assumption
made was that a customer could only accept a single member at a time, rather than being able to select
multiple to accept or deny, because of this I gave the recursive relationship a (1, 1)
relationship.

Another assumption made was that the *Sales Report* should be implemented as a procedure
or script rather than implemented into the database in some way. This is because the content
of a report on the statistics is not really suitable to be implemented in an EER Diagram.

Another assumption made was that we could only use a single credit card to purchase `LICENSCE(S)`
at a single time, that there was no split-payment method of paying as this is less commonly
found in an online site.

Licences for games is assumed that a user can `LEND` or `GIFT` multiple licences at a single
time. 

Lastly we assumed that the user interface only allows for accepting a single `USER` at a time, 
and that we cannot group many friends at a single time.
