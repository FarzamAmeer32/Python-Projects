class ToDoList:
  def __init__(self):
    self.task=[]
    self.status={}

  def add_task(self): # add task fucntion
    while True:
        try:
          action=input('enter the task you want to Enter in the list\t')
          if action!='' and len(action)>2:
            self.task.append(action)
            self.status[action]=False
            self.view_task()
          else:
            print('invalid input')
            continue
        except Exception as e:
          return f'Error {e}'

        try:
          choice=int(input('Do you want to enter more Task (1 for YES/ 2 for NO)?\t'))
          if choice==2:
            return self.task,self.status
        except Exception as e:
          return(f'Error {e}')

  def remove_task(self):  # remove task function
    if len(self.task) > 0:
        while True:

            self.view_task()

            action = input('Enter the task you want to remove: ')

            if action !="" and len(action) > 2 and (action in self.task):
                self.task.remove(action)
                self.status.pop(action,None)
                print('List after removing task:')
                self.view_task()
            else:
                print('Invalid input/List is Empty')
                continue

            try:
                if len(self.task) == 0:
                    print('List is empty')
                    break
                choice = int(input('Remove more? (1 = YES / 2 = NO): '))
                if choice == 2:
                    return self.task
            except Exception as e:
                print(f'Error {e}')
    else:
        print('Your To-Do list is empty')


  def view_task(self): # view task function
    if len(self.status)>0:
      print('Your To-Do list is:')
      for task,status in self.status.items():
        if status==False:
          print(f'{task} is pending' )
        else:
          print(f'{task} has been completed')

    else:
      print('To Do list is empty')

  def mark_task_complete(self):
    if len(self.task)>0:


      while True:
        self.view_task()
        inp=input('Enter the task you have completed: ')
        if inp in self.status:
          if self.status[inp]==True:
            print('Task Already Completed')
          else:
            self.status[inp]=True
            self.view_task()
        ch=input('Have you completed more Task?(YES/No)')
        if ch.lower()=='no':
          return self.status
    else:
      print('Your To Do list is empty')


  def completed_task(self):

    if len(self.status)>0:
      print('Your Completed Task are:')
      for task,status in self.status.items():
        if status==True:
          print(task)

    else:
      print('Your To Do list is empty')

  def incomplete_task(self):

    if len(self.status)>0:
      print('Your InCompleted Task are:')
      for task,status in self.status.items():
        if status==False:
          print(task)

    else:
      print('Your To Do list is empty')





  def Dashboard(self): # simple dashboard
    print('Welcome to the TO-D0-List App')
    while True:
      print('What Task Do yo need to perform?')
      try:
        tk=int(input('Enter 1 To Add a Task\nEnter 2 to Remove a Task\nEnter 3 to view Task\nEnter 4 to mark task as completed\nEnter 5 to view completed Task\nEnter 6 to view incomplete Task\t'))
      except ValueError:
        print('Invalid Input')
        continue
      if tk==1:
        self.add_task()
      elif tk==2:
        self.remove_task()
      elif tk==3:
        self.view_task()
      elif tk==4:
        self.mark_task_complete()
      elif tk==5:
        self.completed_task()
      elif tk==6:
        self.incomplete_task()

      else:
        print('No such Task are avaialabe')

      ch=input('Do want to perform Other Task (YES/NO)?')
      if ch.lower()=='no':
        print('Thankyou')
        break






