Feature: Left operand should be string with first pattern 

    Scenario Outline: left operand should be text 
        Given initial value pattern is "<pattern>" 
        And left is "<left>" 
        And operand is "<operator>" 
        And right is "<right>"  
        When I want get left operand
        Then I will see "<expected>" 

    Examples:
        |pattern|left|operator|right|expected|
        |1      |1   |1       |1    |one     |
        |1      |2   |1       |1    |two     |
