# mini-practicum

This is the basis of an interview question where candidates are asked to make constructive criticism of a pull request.

*Note: the code is intentionally horrible. Avert your eyes!*


## Problems with the code

- [ ] No good commit message
- [ ] Multiple imports on the same line
- [ ] `full_name` is nullable but code assumes it's populated
- [ ] `get_first_name` can fail with names w/o a space, or other i18n names
- [ ] User model should change to have separate first and last name fields
- [ ] `create` is a staticmethod, should be a classmethod
- [ ] passwords are stored in plain text
- [ ] no tests for the new view
- [ ] `create` should take an optional full name parameter
- [ ] `view_reset_all` is a poor name, maybe use `reset_all_passwords`
- [ ] Creating a list of all user objects on memory could use too much RAM
- [ ] Eight characters is not enough for a password
- [ ] Should use more character classes than just ascii for the password
- [ ] Potential unicode error in the `Hello` string formatting
- [ ] Sending a user-supplied message into an HTML email unescaped
- [ ] Not returning a HTTP status code for the view
- [ ] View does not handle errors well, bombs out of the entire loop
- [ ] Entire view body should be in an asynchronous task
- [ ] The constant `8` should be named something like `DEFAULT_PASSWORD_LEN`
- [ ] 'Hello, {}' is not internationalized
- [ ] The email does not have a plain text multipart

TODO:
- [ ] change first_name to get_first_name
- [ ] send password in email
