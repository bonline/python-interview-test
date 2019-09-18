# bOnline Django Interview Test
## The data
The file sales.json contains a list of dictionaries, each dictionary contains
these keys:
- date
- amount (pennies)
- agent

## The task
Using django create a website which has:
- A `Sales` model
- A page where you can upload the provided JSON file of sales, to be stored in the `Sales` table
- A page which displays a table showing the total value of each agent's sales per month like this:

|Agent   | Jan Sales | Jan Total | Feb Sales | Feb Total | Mar Sales | Mar Total |
|--------|----------:|----------:|----------:|----------:|----------:|----------:|
|Andy    |      30   |  4,100.00 |        25 |  5,199.25 |        32 |    250.32 |
|Belinda |      50   | 10,125.33 |        15 |    100.00 |        27 |  1.250.67 |


### REST API extension task
- Use django-rest-framework to provide a REST endpoint for the `Sales` model
