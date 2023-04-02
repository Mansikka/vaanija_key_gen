import time
import os
from itertools import permutations



"""Primary discs"""


class VaanijaGeyKen:

  english_words = []
   
  discs = [
    ['u', 'a', 'o', 'c', 'i', 'q', 'y', 'd', 'j', 'p'],
    ['n', 'a', 'o', 'a', 'g', 'm', 's', 'y', 'b', 'h'],
    ['u', 'a', 'o', 'c', 'i', 'q', 'y', 'd', 'j', 'p'],
    ['u', 'a', 'o', 'c', 'i', 'q', 'y', 'd', 'j', 'p'],
    ['u', 'a', 'o', 'c', 'i', 'q', 'y', 'd', 'j', 'p']
  ]
   
  disc_order = [0,1,2,3,4]

  spinner = ['|', '/', '-', '\\', '|', '/', '-', '\\']
  spinner_frame = 0

   
  def __init__(self, source_file:str) -> None:
    try:
      f = open(source_file, 'r')
      self.english_words = f.readlines()
      f.close()
    except:
      print('Could not read', source_file)
      exit()
  
  def get_spinner(self) -> str:
    self.spinner_frame += 1
    if self.spinner_frame < 0 or self.spinner_frame >= len(self.spinner):
      self.spinner_frame= 0
    return self.spinner[self.spinner_frame]

  def get_disc_content(self, disc_number:int):
    if disc_number < 0 or disc_number > 4:
        print('INCORRECT DISC')
        return
    disc:list = self.discs[disc_number]
    return ' '.join([key.upper() for key in disc])

  def print_main_menu(self, show_disc):
    os.system('cls')
    print('Vaanija keygen 1.0 by Tommi Mansikka')  
    print('MAIN MENU')
    print('Current disc order:', ' '.join(str(x+1) for x in self.disc_order))
    if show_disc:
      index = 1
      for disc in self.disc_order:
        print('Disk', index, self.get_disc_content(disc))
        index += 1
    print()
    print('Select option')
    print('1: Select disc order')
    print('2: Show/Hide disc content')
    print('3: Generate keywords')
    print('4: Generate all permutations')
    print('5: Exit')

  def main_menu(self):
    """Main menu fuction"""
    new_state = 'EXIT'
    print_disc = False
    while True:
      self.print_main_menu(print_disc)
      selection = input()
      if selection == '1':
        new_state = 'DISC'
      elif selection == '2':
        print_disc = not print_disc
        continue
      elif selection == '3':
        new_state = 'GENERATE'
      elif selection == '4':
        new_state = 'GENERATEALL'
      elif selection == '5':
        new_state = 'EXIT'
      else:
        print('Invalid selection')
        continue
      break
    return new_state

  def print_disc_menu(self, active_order:list[int], options:list[int]):
    os.system('cls')
    print('Vaanija keygen 1.0 by Tommi Mansikka')  
    print('DISC MENU')
    print('Current disc order:', ' '.join([str(disc+1) for disc in active_order]))
    print()
    print('Choose next disc in order:')
    for disc in options:
      print('Disc', (disc+1), self.get_disc_content(disc))

  def disc_menu(self):
    """Disc menu fuction"""
    active_order = []
    options = [0, 1, 2, 3, 4]
    self.print_disc_menu(active_order, options)
    while True:     
      selection = input('Select disc: ')
      if not selection.isnumeric():
        print('Invalid selection')
        continue
      selection = int(selection) - 1 
      if selection not in options:
        print('Invalid selection')
        continue    
      active_order.append(selection)
      options.remove(selection)    
      if len(options) <= 0:
        self.disc_order = active_order
        break
      else:       
        self.print_disc_menu(active_order, options)
    return 'MAIN'
  
  def get_disc_keys(self, disc:int) -> list[str]:
    return self.discs[disc]

  def print_generation(self, disc_position, possibilities):    
    os.system('cls')
    print('Vaanija keygen 1.1 by Tommi Mansikka')  
    print('GENERATING WORDS')
    print('Currently searching position:', disc_position)
    print('Current plausible words:')
    print()
    index = 0
    for position in possibilities:
      if index == 0:
        print('Starting count', len(position))
      else:
        print('Disc position 1', len(position))
      index += 1    

  def generate_list(self):
    """Generates list of options"""
    disc_position = 0
    possibilities = [self.english_words, [], [], [], [], []]
    for disc in self.disc_order:
      disc_keys:list[str] = self.get_disc_keys(disc)
      self.print_generation(disc_position, possibilities)
      print(self.get_spinner())
      time.sleep(1)
      for word in possibilities[disc_position]:
        if word[disc_position].lower() in disc_keys:
          possibilities[disc_position+1].append(word)
      disc_position += 1
    self.print_generation(disc_position, possibilities)
    final = possibilities[5] 
    print()
    print('Final results: ', len(final))
    print('Storing results in results.txt')
    filepath = os.path.join(os.getcwd(), 'results.txt')
    f = open(filepath,'w')
    for word in final:
      print(word, file=f)
    f.close()
    print('Done, file located at', filepath)
    input('Press enter to return to main menu...')
    return 'MAIN'
  
  def print_all_top(self, current:int, max_results:int):    
    os.system('cls')
    print('Vaanija keygen 1.1 by Tommi Mansikka')  
    print('GENERATING ALL PERMUTATIONS')
    print('Generating permutation', current, '/', max_results)
  
  def generate_disc_result(self, disc_order) -> list[str]:
    disc_position = 0
    possibilities = [self.english_words, [], [], [], [], []]
    for disc in disc_order:
      disc_keys:list[str] = self.get_disc_keys(disc)
      for word in possibilities[disc_position]:
        if word[disc_position].lower() in disc_keys:
          possibilities[disc_position+1].append(word)
      disc_position += 1
    return possibilities[5]

  def generate_all_permutations(self):
    order_set = list(permutations([0,1,2,3,4]))
    current = 1
    max_results = len(order_set)
    filepath = os.path.join(os.getcwd(), 'all_permutations.txt')
    f = open(filepath,'w')
    for disc_order in order_set:
      self.print_all_top(current, max_results)
      print(self.get_spinner())
      words = self.generate_disc_result(disc_order)
      for word in words:
        print(word, file=f)
      current += 1
      time.sleep(0.2)
    f.close()    
    self.print_all_top(current, max_results)
    print('COMPLETE')
    print('Results stored in', filepath)
    input('Press enter to return to main menu...')
    return 'MAIN'

  
  def close_program(self):
    print('Exiting...')
    exit(0)

  def main(self):
    print('Please wait, intializing...')
    state = 'MAIN'
    while True:
        if state == 'MAIN':
            state = self.main_menu()
        elif state == 'DISC':
            state = self.disc_menu()
        elif state == 'GENERATE':
            state = self.generate_list()
        elif state == 'GENERATEALL':
            state = self.generate_all_permutations()
        else:
            self.close_program()

keyGen = VaanijaGeyKen('english_words.txt')
keyGen.main()



    

