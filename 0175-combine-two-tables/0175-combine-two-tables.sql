# The ON clause is used specifically with JOIN operations to specify the join condition
# WHERE is used to filter

SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address
ON Person.personId = Address.personId