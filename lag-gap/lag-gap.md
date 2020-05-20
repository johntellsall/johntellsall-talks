## Rapid Development means minimizing LAG and GAP

Theme: minimize Lag (time to get feedback) and Gap (difference between output and expected result).
- Know what Goal you're trying to achieve!
- Humans are great at exploratory testing (easy to measure Gap in different use cases), but are slow (large Lag)
    - Consequence: add interactive interface early, but focus on test automation

## Example: Roman Numeral Calculator

1. Roman func. Only callable via debugger
2. CLI - expand audience - min GAP by allowing exploratory testing 
3. Test with PTW - min LAG, a test cycle goes from seconds to milliseconds, and can start automatically!
4. add code, add happy test - min GAP, add Quality (automatically test the happy path)
5. add Coverage -> min GAP between test and desired coverage percentage
6. user: use exploratory testing to find bugs -> find GAPs from User perspective
   1. you've probably been yelling at the screen for the last 5 steps :)
7. boundary tests -> translate user GAPs (LAG of seconds) to test automation GAPs (min LAG, test automatically)
   1. parameterize - reduce complexity by moving from Code to Configuration


## Also

### dev can get lost, go in circles

* Challenge: unclear how to add value: add web UI (increase Audience) or flesh out func (increase quality, measure Gap with different test cases)
* Answer: 1) allow exploratory testing / increase Audience, 2) add tests next (higher level code = shorter + simpler, allows measurement of Gap/quality), 3) add code last.
* Consequences
    * Can quit at any time and User (large Audience) can see the effect of all the code
    * Failing test is documentation of quality
    * Simple code + UI allows Business to make decisions, vs better code
