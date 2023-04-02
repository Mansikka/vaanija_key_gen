import time
import os




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

   
  def __init__(self, source_file:str) -> None:
    try:
      f = open(source_file, 'r')
      self.english_words = f.readlines()
      f.close()
    except:
      print('Could not read', source_file)
      exit()
    

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
    print('2: Generate keywords')
    print('3: Show/Hide disc content')
    print('4: Exit')

  def main_menu(self):
    """Main menu fuction"""
    new_state = 'EXIT'
    print_disc = False
    while True:
      self.print_main_menu(print_disc)
      selection = input()
      if selection not in ['1', '2', '3', '4']:
        print('Invalid selection')
      else:
        if selection == '1':
          new_state = 'DISC'
          break
        elif selection == '2':
          new_state = 'GENERATE'
          break
        elif selection == '3':
          print_disc = not print_disc
        else:
          new_state = 'EXIT'
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
    print('Vaanija keygen 1.0 by Tommi Mansikka')  
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
      time.sleep(1)
      for word in possibilities[disc_position]:
        if word[disc_position].lower() in disc_keys:
          possibilities[disc_position+1].append(word)
      disc_position += 1
    final = possibilities[5]    
    self.print_generation(disc_position, possibilities)
    print()
    print('Final results: ', len(final))
    print('Storing results in results.txt')
    with open('results.txt','w') as fp:
      for word in final:
          # write each item on a new line
          fp.write("%s\n" % word)
    print('Done')
    input('Press enter to return to main menu')
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
        else:
            self.close_program()

keyGen = VaanijaGeyKen('english_words.txt')
keyGen.main()



    

