# Notes on Budget App Challenge

This challenge was the first in the series to introduce Python classes. The
challenge was pretty straight forward to complete, but I did run into a couple
of things to note. 

Using a list as a class attribute caused several tests to fail. It seemed like
conrete implementations of classes each shared the same attribute object. The
tests were each creating a new Category class but all of the test data was
shared across all the tests. When I instantiated the attribute in the
constructor this problem went away and test Categories were populated with the
expected data. 

String formatting was heavily featured again in this challenge. Mostly the
requiremnt where reasonable but getting whitespace exactly right is difficult. 


