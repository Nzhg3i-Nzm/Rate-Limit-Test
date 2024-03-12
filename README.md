# Rate-Limit-Test
Tests a login page for rate limiting

The standard to test for "lack of rate limiting" is 300 requests in under one minute.
This tool attempts to login to an account using an invalid password for however many requests you state,
then attempts to login using the real password. The tool prints the response data at the last request so
you can see weather or not you were successful in logging in after all of the other requests.


CWE-770 - "Allocation of Resources Without Limits or Throttling"


---------------------
THIS TOOL IS INTENDED FOR ETHICAL HACKING ONLY!
Please only test this using accounts that you own, and with permission from the site owner!
