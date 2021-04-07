# Test Driven Design (TDD)

```javascript
assertEquals(count, 5);
```

**Perks of Unit testing**

- Specification
  * Know what the problem domain is
  * Enough information to know if we have solved it
- Feedback
  * Run this test and see if the code succeeds
- Regression
  * Knowing that it will continue to work
- Granularity
  * Give information when the test fails

Programmers decided we needed smaller tests in order to show the path of
the code.

This can lead to breaking tests due to customer needs and decisions. This is why
we have behavioural testing

TDD tends to focus too much on unit testing and coverage.

To implement TDD correctly is to write tests before writing the code that  the tests
are testing.

# Behaviour Driven Design (BDD)

```javascript
$(count).should_be(5);
```

BDD was originally a way to teach people to use TDD correctly.

Related Ideas to TDD
- Domain Driven Design
- Ubiquitous Language

Goals of BDD:
- Separate what from how
- say nothing about how the system works
- concentrate only on what the system does

By eliminating technical details we make our testing more durable

## Testing should:

- Minimize programmer waiting.
- Run reliably.
- Predict deployability.
- Respond to behavior changes.
- Not respond to structure changes.
- Be cheap to write.
- Be cheap to read.
- Be cheap to change.
