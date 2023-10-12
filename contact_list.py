class ContactList:
    
    def __init__(self, list_name, friend_list):
        self._name = list_name
        self._friend_list = friend_list

    @property
    def name(self):
        return self._name()
    
    @name.setter
    def set_name(self, new_name):
        self._name = new_name

    @property
    def contacts(self):
        return self._friend_list
    
    @contacts.setter
    def set_contacts(self, new_contact_list):
        self._friend_list = new_contact_list

    def add_contact(self, new_contact):
        current_contacts = self.get_contacts
        current_contacts.append(new_contact)
        self.set_contacts = sorted(current_contacts, key=lambda sort_by: sort_by['name'])

    def remove_contact(self, name):
        contacts = [c for c in self.contacts if c['name'] != name]
        self.set_contacts(contacts)
        
    def find_shared_contacts(self, contact_list_obj):
        shared_contacts = []
        for number in self.get_contacts:
            if number in contact_list_obj.contacts:
                shared_contacts.append(number)
        return shared_contacts


#add new contact_object to ContactList.contacts[contact_object]
#     `add_contact({})` should add a new contact to the list, while keeping the list sorted
# - `remove_contact('Alice')` should remove a contact from the list by name.
# - `find_shared_contacts(ContactList)` should accept another contact list as an argument, 
# and then return a new list of dictionaries to indicate all the contacts that appear in both lists (exact same name and phone number).

if __name__ == '__main__':
    friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
    work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

    my_friends_list = ContactList('My Friends', friends)
    my_work_buddies = ContactList('Work Buddies', work_buddies)

    # friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
    # friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]