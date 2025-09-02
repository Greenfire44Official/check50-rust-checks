Due to the way this problem works I have to parse the output to check the validity of it. due to this the output must adhere to the following restrictions:
- Each person in the family tree must be printed in a separate line.
- The program must output 3 generations in total. I encourage people to write their program in a way that you can generate families of different number of generations, as is the case in the original problem. But this checker will only expect an output of 3 generations.
- Each generation will have the following names (Case sensitive):
  + Child (Generation 0)
  + Parent (Generation 1)
  + Grandparent (Generation 2)
  What's important is the name itself, the generation number is not checked.
- When printing a person the first word printed shall be the generation name, and the last word shall be the alleles of that person.
  Examples: 
   + `Child (Generation 0): blood type AA`
   + `Parent with blood type AB`
   + `Grandparent OB`
   + `Child {you can print whatever text you desire in here, as long as it's all printed in one line} OA`
   These are all valid.
- The family should be printed with the following structure:
  ```
  Child ... [Alleles]
      Parent ... [Alleles]
          Grandparent ... [Alleles]
          Grandparent ... [Alleles]
      Parent ... [Alleles]
          Grandparent ... [Alleles]
          Grandparent ... [Alleles]
  ```

## Example
Example of a valid formatting of the output:
```
Child (Generation 0): blood type OB
    Parent (Generation 1): blood type OA
      Grandparent (Generation 2): blood type OA
      Grandparent (Generation 2): blood type AO
    Parent (Generation 1): blood type OB
      Grandparent (Generation 2): blood type AO 
      Grandparent (Generation 2): blood type BB
```