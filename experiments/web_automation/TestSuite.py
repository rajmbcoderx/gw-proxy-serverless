import unittest
from FormSubmissionGlassWallSolutions import TestClass
from ApplicationLinkVerification import LinkVerificationTest
from SolutionsChildLinks import SolutionLinkVerificationTest
from ResourcesChildLinks import ResourcesLinkVerificationTest

# get all tests from TestClass and LinkVerificationTest class
form_submission_test = unittest.TestLoader().loadTestsFromTestCase(TestClass)
link_verification_test = unittest.TestLoader().loadTestsFromTestCase(LinkVerificationTest)
solutions_link_verification_test = unittest.TestLoader().loadTestsFromTestCase(SolutionLinkVerificationTest)
resources_link_verification_test = unittest.TestLoader().loadTestsFromTestCase(ResourcesLinkVerificationTest)

# create a test suite combining form_submission_test and link_verification_test
test_suite = unittest.TestSuite([form_submission_test, link_verification_test, solutions_link_verification_test,
                                 resources_link_verification_test])

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)