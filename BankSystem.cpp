#include <iostream>

using namespace std;
Fun(int Ac1, int Ac2, int acc1, int acc2,int & Ac1B,int & Ac2B) {
    int am1;
    cout << "Enter The Account Number You Want To Withdraw Money From " << endl;
    cin >> acc1;
    if (acc1 != Ac1 && acc1 != Ac2) { cout << "Invalid Account Number " << endl; }
    cout << "Enter The Account Number You Want To Add Money To " << endl;
    cin >> acc2;
    if (acc2 != Ac1 && acc2 != Ac2) { cout << "Invalid Account Number " << endl; }
    cout << "Enter The Amount Of Money  " << endl;
    cin >> am1;
    if (acc1 == Ac1) {
            Ac2B += am1;
            Ac1B -= am1;
    }
    if (acc1 == Ac2) {
            Ac1B += am1;
            Ac2B -= am1;
    }
}
int main()
{
    int Ac1, Ac2 ,acc1 ,acc2;
    double Ac1B ,Ac2B,am1 ;
    char option ;
    cout<< "Enter The Number Of First Account" <<endl ; 
    cin >> Ac1 ;
    cout<< "Enter The Number Of Second Account" <<endl ; 
    cin >> Ac2 ;
    cout<< "Enter The Balance Of First Account" <<endl ; 
    cin >> Ac1B ;
    cout<< "Enter The Balance Of Second Account" <<endl ; 
    cin >> Ac2B ;
    
    cout << " *************************************** " << endl ;
    cout << " Please select (character) Of These Option :  "<< endl; 
    cout<< " a- Add Money "<<endl ; 
    cout<< " b- Withdraw Money "<<endl ; 
    cout<< " c- Transfere Money From One Account To Another "<<endl ; 
    cin >> option ;
    switch (option) { 
    case 'A' :    cout<< "Enter The Number Of The Account You Want To Add Money To It" <<endl ; 
                  cin >> acc1 ;
                  if (acc1 != Ac1 && acc1 != Ac2){cout << " Invalid Account Number " <<endl ; break ;}
                  cout<< "Enter The Amount Of Money You Want To add Them " <<endl ; 
                  cin >> am1 ;
                  if (acc1 == Ac1){Ac1B += am1;}
                  else Ac2B +=am1;
                  
                  break ; 
    case 'B' : cout<< "Enter The Number Of The Account You Want To Withdraw Money From " <<endl ;
                cin >> acc1 ; 
                if (acc1 != Ac1 && acc1 != Ac2){cout << " Invalid Account Number " <<endl ; break ;}
                cout<< "Enter The Amount Of Money You Want To Withdraw Them " <<endl ; 
                  cin >> am1 ;
                  if (acc1 == Ac1){Ac1B -=am1;}
                  else Ac2B -=am1;
                break ;
    case 'C' :  
        Fun(Ac1, Ac2, acc1, acc2, am1);
                break ;
    default : cout << "error !"<<endl;  break ;
        
    }
    cout << "*************************************** " << endl ;
    cout << "******** Summsry ******** "<<endl ;
    cout << "Account #      Balance "<<endl ; 
    cout << Ac1 ;
    cout << "                " ;
    cout << Ac1B << endl ;
    cout << Ac2  ;
    cout << "                " ;
    cout << Ac2B << endl;
    cout << "Thank You For Using Our Banking Services "<<endl ; 
    
    return 0 ;
}
