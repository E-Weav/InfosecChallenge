# InfosecChallenge

After downloading the file from repository, make sure that the file location in the top (setUp) case is correctly set.  Once the file location is set, all you will need to do is change the email of the new account being added.  
Before running the test, you will have to increment the value in the email (ex. tester1@gmail.com needs to be tester2@gmail.com)

Besides for the setUp and tearDown which get executed for each test case, the others were chosen for a few reasons.  
Test 1: Signin_nav.  This tests to make sure that clicking the sign in button actually brings a user to the new page so they can create and account or sign into an existing one.
Test 2: Existing_account.  This was just to validate that a user would be able to sign into an account that already exists in the system.
Test 3: Error_message.  This test was to validate that duplicate emails are not allowed to be used when creating a new account.
Test 4: New_account.  The largest of the tests doesn't go into any specifics of fields, but rather just validates that a user can go top to bottom in the form to create a new account, hitting only the required fields.

Reasoning for these tests:  I felt that creating these tests does a quick outline of what would need to be necessary at the very least in order for confidence that the site was working appropriately with people putting in rather basic information.  I would add more extensive tests in the future such as checks to each of the required fields, not only validating the inputs into the fields, but also making sure that a user wouldn't be able to continue unless they in-fact populated the fields.

There are quite a few tests that can be added, but I wouldn't list them as critical to the functionality of the system.

Side Note:  I would create some way to get the email to be able to be incremented on it's own in order to be just press "run" and not have to worry about any manual aspects to these tests.
