#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const string FILE_NAME = "profile_v1.txt";
class Profile 
{
    public:
    string name, state, city, email;
    int age, pin;
    string mobile;

    public:
    bool isAlpha(const string& str) 
    {
        for (char c : str) 
        {
            if (!isalpha(c) && c != ' ') 
            {
                return false;
            }
        }
        return true;
    }

    string getValidInput() 
    {
        string input;
        getline(cin, input);
        return input;
    }

    void setName(const string& n)
    {
        if (isAlpha(n)) 
        {
            name = n;
        }
        else 
        {
            cout << "Invalid name format! Please enter alphabetic characters only." << endl;
            cout << "Enter name again: ";
            setName(getValidInput());
        }
    }

    void setAge(int a) 
    {
        if (a > 0) 
        {
            age = a;
        }
        else 
        {
            cout << "Invalid age! Please enter a positive numeric value: ";
            cin >> a;
            setAge(a);
        }
    }

    void setMobile(string& m) 
   {
    ifstream file(FILE_NAME);
    string line;
    bool isUnique = true;
    int count = 0;

    while (getline(file, line) && count < 100) 
    {
        getline(file, line); 
        getline(file, line); 
        if (line == m) 
        {
            isUnique = false;
            break;
        }
        for (int i = 0; i < 4; ++i) 
        {
            getline(file, line); 
        }
        ++count;
    }
    file.close();

        while (m.length() != 10 || m.find_first_not_of("0123456789") != string::npos || !isUnique) 
        {
            if (!isUnique) 
            {
                cout << "Phone number already exists! Please enter a unique 10-digit number: ";
            }
            else 
            {
                cout << "Invalid mobile number format! \nPlease enter a 10-digit number: ";
            }
            cin >> m;

            ifstream checkFile(FILE_NAME);
            isUnique = true;
            while (getline(checkFile, line)) 
            {
                getline(checkFile, line); 
                getline(checkFile, line); 
                if (line == m) {
                    isUnique = false;
                    break;
                }
                for (int i = 0; i < 4; ++i) 
                {
                    getline(checkFile, line);
                }
            }
            checkFile.close();
        }

        mobile = m;
    }


    void setState(const string& s) 
    {
        if (isAlpha(s)) 
        {
            state = s;
        }
        else 
        {
            cout << "Invalid state format! Please enter alphabetic characters only." << endl;
            cout << "Enter state again: ";
            setState(getValidInput());
        }
    }

    void setCity(const string& c) 
    {
        if (isAlpha(c)) 
        {
            city = c;
        }
        else 
        {
            cout << "Invalid city format! Please enter alphabetic characters only." << endl;
            cout << "Enter city again: ";
            setCity(getValidInput());
        }
    }

    void setPin(int p) 
    {
        string input;
        while (to_string(p).length() != 6) 
        {
            cout << "Invalid pin code format! \nPlease enter a 6-digit number: ";
            cin >> input;

            try
            {
                p = stoi(input);
            }
            catch (const std::exception& e) 
            {
                p = -1;
            }
        }
        pin = p;
    }

    void setEmail(string& e) 
    {
        while (e.find('@') == string::npos || e.find(".com") == string::npos) 
        {
            cout << "Invalid email format! \nPlease enter a valid email containing '@' and '.com': ";
            cin >> e;
        }
        email = e;
    }

void addContact(ofstream& f) 
{
    if (!mobile.empty() && pin != 0) 
    {
        f << name << endl
          << age << endl
          << mobile << endl
          << state << endl
          << city << endl
          << pin << endl
          << email << endl
          << "-------------------------" << endl; 
        cout << "Contact added successfully." << endl;
    } 
    else 
    {
        cout << "Contact not added due to invalid data." << endl;
    }
}

};

Profile input() 
{
    Profile newContact;
    string temp;
    int age, pin;
    cout << "Enter name: ";
    cin.ignore();
    getline(cin, temp);
    newContact.setName(temp);
    cout << "Enter age: ";
    cin >> age;
    newContact.setAge(age);
    cout << "Enter phone no.: ";
    cin >> temp;
    newContact.setMobile(temp);
    cout << "Enter state: ";
    cin.ignore();
    getline(cin, temp);
    newContact.setState(temp);
    cout << "Enter city: ";
    getline(cin, temp);
    newContact.setCity(temp);
    cout << "Enter pincode: ";
    cin >> pin;
    newContact.setPin(pin);
    cout << "Enter email: ";
    cin >> temp;
    newContact.setEmail(temp);

    return newContact;
}

void viewContacts() {
    ifstream f(FILE_NAME);
    if (f.is_open()) 
    {
        Profile contact;
        bool contactFound = false;
        string line;
        while (getline(f, line)) 
        {
            contact.setName(line);
            f >> contact.age;
            f.ignore();
            getline(f, contact.mobile);
            getline(f, contact.state);
            getline(f, contact.city);
            f >> contact.pin;
            f.ignore(); 
            getline(f, contact.email);
            getline(f, line);

            cout << "\nDetails:\n";
            cout << "Name: " << contact.name << endl;
            cout << "Age: " << contact.age << endl;
            cout << "Phone No.: " << contact.mobile << endl;
            cout << "State: " << contact.state << endl;
            cout << "City: " << contact.city << endl;
            cout << "Pincode: " << contact.pin << endl;
            cout << "Email: " << contact.email << endl;
            cout << "--------------------" << endl;

            contactFound = true;
        }

        f.close();

        if (!contactFound) 
        {
            cout << "No contacts found." << endl;
        }
    } 
    else 
    {
        cout << "Error opening file!" << endl;
    }
}

void searchContact(const string& key) 
{
    ifstream f(FILE_NAME);
    if (f.is_open()) 
    {
        string line;
        bool found = false;
        Profile contact;
        while (getline(f, line)) 
        {
            if (line.find(key) != string::npos) 
            {
                contact.setName(line);
                f >> contact.age >> contact.mobile >> contact.state >> contact.city >> contact.pin >> contact.email;

                cout << "\nDetails:\n";
                cout << "Name: " << contact.name << endl;
                cout << "Age: " << contact.age << endl;
                cout << "Phone No.: " << contact.mobile << endl;
                cout << "State: " << contact.state << endl;
                cout << "City: " << contact.city << endl;
                cout << "Pincode: " << contact.pin << endl;
                cout << "Email: " << contact.email << endl;

                found = true;
                break;
            }
        }
        f.close();
        if (!found) 
        {
            cout << "Contact not found." << endl;
        }
    } 
    else 
    {
        cout << "Error opening file!" << endl;
    }
}


void fileCopy() 
{
    string destination;
    cout<<"Enter destination file name: ";
    cin>>destination;
    ifstream sFile(FILE_NAME, ios::binary);
    ofstream dFile(destination, ios::binary);
    if (!sFile || !dFile) 
    {
        cerr <<"Error opening files!\n";
    }
    dFile<<sFile.rdbuf();
    cout<<"File copied successfully!\n";
    sFile.close();
    dFile.close();
}


int main() 
{
    Profile newContact;
    ofstream outFile(FILE_NAME, ios::app);
    ifstream inFile(FILE_NAME);
    if (!outFile.is_open() || !inFile.is_open()) 
    {
        cerr << "Error opening file!" << endl;
        return 1;
    }

    int ans = 1;
    int choice;
    while (ans == 1) 
    {
        cout << "\nMenu: \n";
        cout << "1. Add a Profile\n";
        cout << "2. Display Profiles\n";
        cout << "3. Search Profile\n";
        cout << "4. Copy data\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) 
        {
            case 1: {newContact = input();
                    newContact.addContact(outFile);}
                    break;
            case 2: viewContacts();
                    break;
            case 3: cout << "Enter Name to Search: ";
                    cin.ignore();
                    getline(cin, newContact.name);
                    searchContact(newContact.name);
                    break;
            case 4: fileCopy();
                    break;
            default:cout << "Invalid choice!\n";
                    break;
        }

        cout << "Do you want to continue?\nType 1 to continue or type 0 to exit.\nEnter: ";
        cin >> ans;
    }
    outFile.close();
    inFile.close();
    return 0;
}