# Write an assert statement that triggers an AssertionError if the variables eggs and bacon
# contain strings that are the same as each other, even if their cases are different.
# (That is, 'hello' and 'hello' are considered the same, as are 'goodbye' and 'GOODbye'.)
eggs = 'toodles'
bacon = 'Toodles'
assert eggs.lower() != bacon.lower()
