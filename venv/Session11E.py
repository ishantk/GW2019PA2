cppCode="""
#include<iostream>
using namespace std;
int main(){
    cout<<"Hello World";
    return 0;
}
"""

print(cppCode)
file = open("/Users/ishantkumar/Downloads/MyApp.cpp", "w")
file.write(cppCode)
file.close()
print(">> Data Written")

# HW : Write a Program where you ask from user which programming language you would choose
#      1. Java 2. Python 3. C 4.C++, 5. Scala 6. Go, 7. Ruby, 8. Dart, 9. Kotlin, 10. JS