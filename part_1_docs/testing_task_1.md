### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #should be ==
      return True
    else #no colon after else statement
      return False
   

  #miss spelling of the def keyword
  #no indentation on function content
  dif highest_card(self, card1 card2): #no comma between card parameters
  if card1.value > card2.value:
    return card #should be 'card1'
  else:
    return card2
  

#should be indented into the class
def cards_total(self, cards):
  total #must define a starting value for total
  for card in cards:
    total += card.value
    return "You have a total of" + total #line should be unindented & total needs to be of type str, not int
  
```
